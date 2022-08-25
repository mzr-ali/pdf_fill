import os

import gspread
from google.oauth2.service_account import Credentials


class GoogleSheetItemExporter():
    def __init__(self, spread_sheet_key, **kwargs):
        super(GoogleSheetItemExporter, self).__init__(**kwargs)
        scopes = [
            'https://www.googleapis.com/auth/spreadsheets',
            'https://www.googleapis.com/auth/drive'
        ]
        folder_path =os.path.join(os.getcwd(), 'APP')
        crentials = Credentials.from_service_account_file(os.path.join(folder_path, 'credss.json'), scopes=scopes)

        gc = gspread.authorize(crentials)
        self.spreadsheet = gc.open_by_key(spread_sheet_key)

    def get_record(self, sheet):
        sheet = self.spreadsheet.worksheet(sheet)
        records = sheet.get_all_records()
        return records

