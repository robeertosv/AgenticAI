from tools.spreadsheet import SpreadSheet
import os
from dotenv import load_dotenv

load_dotenv()


sheet = SpreadSheet(os.getenv('DOC_ID'))
