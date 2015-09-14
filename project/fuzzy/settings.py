
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

TEST_FOLDER = "files"
TEST_FILE = "sample.csv"
