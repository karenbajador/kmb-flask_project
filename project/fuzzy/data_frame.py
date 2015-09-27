import pandas as pd
from project.fuzzy.helpers.decorator import CreateDirectory
from project.fuzzy.settings import DESTINATION_FOLDER, PATH
import os

class PandaDataFrame():

    def __init__(self, pd_file, columns, folder):
        
        class myIOError(Exception): pass
        print ("Loading Data...")

        

        try:
            #xls = pd.ExcelFile('files/' + pd_file)
            data = pd.read_csv(os.path.join(PATH, folder+"/"+pd_file))
        except IOError as e:
                raise myIOError('Caching error: %s' % e)  

        #data = xls.parse(xls.sheet_names[0])
        self._pd_file = pd_file
        
        print ("Loaded Data!")

        #Generate DataFrame including relevant columns
        df = pd.DataFrame(data, columns=columns)

        self._new_df = df

    def add_columns(self):
        self._new_df["Match Status"] = ""
        self._new_df["CRM Company Name"] = ""
        self._new_df["CRM Group ID"] = ""
        self._new_df["CRM Company ID"] = ""



    @property
    def df(self):
    	return self._new_df

    def extract_row_generator(self,df):
        for index, row in df.iterrows():
            yield (index,row)


    def update_df(self,index, best_match, best_score):
        if best_score >= 75:
            match_status = 'high'
            ## Add best match columns
        elif best_score >= 70:
            match_status = 'medium'
            ## Add best match columns            
        elif best_score > 0:
            match_status = 'low'
            ## Add best match columns                        
        else:
            match_status = 'not matched'

        #self._new_df['Match Status'][int(index)]=match_status+"="+str(best_score)
        self._new_df['Match Status'][int(index)]=str(best_score)
        self._new_df['CRM Company Name'][int(index)]=best_match.crm_company_name
        self._new_df['CRM Group ID'][int(index)]=best_match.crm_group_id
        self._new_df['CRM Company ID'][int(index)]=best_match.crm_company_id

        self.save()


    
    @CreateDirectory(os.path.join(PATH, DESTINATION_FOLDER))
    def save(self):
        # writer_orig = pd.ExcelWriter('processed_files/'+self._pd_file, engine='xlsxwriter')
        # self._new_df.to_excel(writer_orig, index=False, sheet_name='report')
        #writer_orig = pd.ExcelWriter('processed_files/'+self._pd_file, engine='xlsxwriter')
        self._new_df.to_csv(os.path.join(PATH, DESTINATION_FOLDER+"/"+self._pd_file), index=False)



        #writer_orig.save()




 


    
