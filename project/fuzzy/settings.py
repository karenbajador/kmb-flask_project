
import os
PATH = os.path.dirname(os.path.abspath(__file__))
#Where cource spreadsheet is located
SOURCE_FOLDER = "file_upload"

#Where processed spread are saved
DESTINATION_FOLDER = "file_download"

#Columns to retrieve from spreadsheet
COLUMNS = ["Company Name", \
            "Key ID", \
            "Address Line 1", \
            "City", \
            "Phone", \
            "URL", \
            "Revenue (As Reported)", \
            "Employees" \
            ]

#Columns to retrieve from spreadsheet
COLUMNS_FOR_CRM_RECORD = ["Company Name", \
            "Address Line 1", \
            "City", \
            "Phone", \
            "URL", \
            "Revenue (As Reported)", \
            "Employees" \
            "Match Status"
            ]  
         
TEST_FOLDER = "files"
TEST_FILE = "sample.csv"

MAXIMUM_FILES_TO_SEND_PER_REQUEST = 100

CRM_API_URL = ''
