from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from google.oauth2 import service_account

import os
from dotenv import load_dotenv

load_dotenv()

# Autenticación
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SPREADSHEET_ID = os.getenv('DOC_ID')
CREDS = 'credentials.json'

creds = service_account.Credentials.from_service_account_file(CREDS, scopes=SCOPES)

# Extraer información de una celda

def read_sheet(range_name):
    service = build('sheets', 'v4', credentials=creds)
    result = service.spreadsheets().values().get(
        spreadsheetId=SPREADSHEET_ID, range=range_name).execute()
    return result.get('values', [])

def write_sheet(range_name, values):
    service = build('sheets', 'v4', credentials=creds)
    body = {'values': values}
    result = service.spreadsheets().values().update(
        spreadsheetId=SPREADSHEET_ID, range=range_name,
        valueInputOption='USER_ENTERED', body=body).execute()
    return result

# Ejemplo de uso
data = read_sheet('Hoja 1!A1:A2')
print("Datos:", data)

write_sheet('Hoja 1!A11', [['SUMA', '=SUMA(A1:A5)']])
print("Escritura completada.")