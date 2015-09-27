
from project.fuzzy.data_frame import PandaDataFrame
from project.fuzzy.settings import COLUMNS_FOR_CRM_RECORD, MAXIMUM_FILES_TO_SEND_PER_REQUEST, DESTINATION_FOLDER, CRM_API_URL
import requests
import pprint


class FuzzyAPI:
	def __init__(self, filename, tag, score, country):
		print ("INSIDE FUZZZZZZZZY APIIIIIIIIIIII")
		self.filename = filename
		self.score = score
		self.tag=tag
		self.country = country
		self.df_cls = PandaDataFrame(filename, COLUMNS_FOR_CRM_RECORD, DESTINATION_FOLDER)

	def load_file(self):

		companies = []

		for extracted_row in self.df_cls.extract_row_generator(self.df_cls.df):
			index, row =  extracted_row

			if row["Match Status"] < self.score:
				if len(companies) <= MAXIMUM_FILES_TO_SEND_PER_REQUEST:
					companies.append(parse(row))
				else:
					# companies, self.tag, type: record
					data = {
						'companies'  : companies,
						'tag' : self.tag,
						'type' : "record",
						'country' : self.country
						}
					data = json.dumps(data)
					self.post_to_crm(data)
					companies = []

		return 1



	def send_to_crm(self):
		return self.load_file()

	def parse(self, row):
		return row


	def post_to_crm(self, data):
		print ("**************** POST *******************")
		pprint.pprint(data)
		
		r = requests.post(CRM_API_URL, data=data)
		return (r.status_code,r.text)
	


	


		








