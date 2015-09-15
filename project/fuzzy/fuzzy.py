import re
import sys
import collections
from fuzzywuzzy import fuzz
from project.fuzzy.postgres_interface import PostgresInterface
from project.fuzzy.helpers.ignored_words import IgnoreWords
from project.fuzzy.data_frame import PandaDataFrame
from project.fuzzy.settings import SOURCE_FOLDER

import time

# # Specify the Employee namedtuple.
postgres_interface_cls = PostgresInterface()
Match = collections.namedtuple("Match", ["crm_company_id", "crm_company_name", "crm_group_id", "score"])


class Fuzzy:
	def __init__(self, filename, country, territory):
		print ("INSIDE FUZZZZZZZZY")
		self.filename = filename
		self.country=country
		self.territory=territory
		self.ignore_words_cls = IgnoreWords()
		self.df_cls = PandaDataFrame(filename)	
		# self.postgres_interface_cls = PostgresInterface()
	
	def start():
		print("START")
		for extracted_row in extract_row_generator(df_cls.df):
			index, row =  extracted_row

			## Clean company_name
			company_name = self.clean(row["Company Name"]).lower()
			
			## Ignore words
			company_keywords_list = self.ignore_words_cls.return_keyword_lists(company_name)

			print ("*****************")
			print (row["Company Name"])
			print (company_keywords_list)

			## Find matches in DB using keywords , country and territory
			crm_results = postgres_interface_cls.get_record_match(company_name, company_keywords_list, self.country,  self.territory)


			## Fuzzy match 
			best_match = Match(crm_company_id = "",crm_company_name = "",crm_group_id = "", score="")
			best_score = 0

			best_match, best_score = self.call_fuzzy_match_generator(best_match, best_score, row["Company Name"].lower(), crm_results)

			## Test Prints
			# if best_score >= 75: 
			# 	#print ("keword_list: {} + crm_results count: {}".format(company_keywords_list,len(crm_results)))
			# 	print("{} => best_match: {} => '{}'".format(best_score, row["Company Name"], best_match))		
			print("{} => best_match: {}".format(best_score, best_match))
			
			
			### Generate new file
			self.df_cls.update_df(index, best_match, best_score)

	def start_test(self):
		print("START TEST ")
		for extracted_row in self.extract_row_generator(self.df_cls.df):
			index, row =  extracted_row

			## Clean company_name
			company_name = self.clean(row["Company Name"]).lower()
			
			## Ignore words
			company_keywords_list = self.ignore_words_cls.return_keyword_lists(company_name)

			print ("*****************")
			print (row["Company Name"])
			print (company_keywords_list)

		return 1

	
	def save(self):
		print("START TEST ")	
		self.df_cls.save()


	def extract_row_generator(self,df):
		for index, row in df.iterrows():
			yield (index,row)

	def clean(self,company_name):
		## Clean spaces
		company_name = re.sub(r'([^\s\+\&\w\.])|_+', ' ', company_name) 
		return re.sub(' +',' ',company_name).strip()		

	def get_fuzzy_match_generator(self,crm_results, excel_company_name):
		for result in crm_results:
			# yield Match(crm_company_id = result[0],crm_company_name = result[1],crm_group_id = result[2], score=fuzz.weighted_6(excel_company_name, result[1], total_weight =50))
			yield Match(crm_company_id = result[0],crm_company_name = result[1],crm_group_id = result[2], score=fuzz.partial_ratio(excel_company_name, result[1]))


	def call_fuzzy_match_generator(self,best_match, best_score, company_name, crm_results):
		for match in get_fuzzy_match_generator(crm_results, company_name):
			if match.score >= best_score:
				if match.score > best_score:
					best_match = {}
					best_score = match.score
				best_match = match
		return best_match, best_score


		








