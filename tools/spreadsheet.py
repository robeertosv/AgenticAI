from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from google.oauth2 import service_account
# import pygsheets as ps # Future support for Charts & Cell customization


class SpreadSheet:

    def __init__(self, sheet_id: str):
        # self.client = ps.authorize()
        # self.psheet = self.client.open_by_key(sheet_id)
        #self.wks = None
        self.wks = 'Hoja 1'
        self.SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
        self.SPREADSHEET_ID = sheet_id
        self.CREDS = 'credentials.json'
        self.creds = service_account.Credentials.from_service_account_file(self.CREDS, scopes=self.SCOPES)
        
    def check_wks(self):
        if self.wks == None:
            self.wks = input("Introduce la hoja: ")

    def update_cell(self, range: str, values: list):
        self.check_wks()
        service = build('sheets', 'v4', credentials=self.creds)
        body = {'values': values}
        range = f'{self.wks}!{range}'

        result = service.spreadsheets().values().update(
            spreadsheetId=self.SPREADSHEET_ID, range=range,
            valueInputOption='USER_ENTERED', body=body).execute()

        return result
    
    def delete_cell(self, range:str):
        self.update_cell(range, [['']])
    
    def read_cell(self, range:str):
        self.check_wks()
        service = build('sheets', 'v4', credentials=self.creds)
        
        result = service.spreadsheets().values().get(
        spreadsheetId=self.SPREADSHEET_ID, range=range).execute()
        
        return result.get('values', [])
        