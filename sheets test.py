import gspread
import pprint
from oauth2client.service_account import ServiceAccountCredentials
#API Authentication Stuff
scope = ["https://spreadsheets.google.com/feeds"]
creds = ServiceAccountCredentials.from_json_keyfile_name("sheets test.json", scope)
client = gspread.authorize(creds)
#Open and get sheet
sheet = client.open_by_url('https://docs.google.com/spreadsheets/d/1I9U5DGPxlhLopXS6Oo2HRuNJHQqnfxw60kmpKBEXJ7U/')
worksheet = sheet.get_worksheet(0)
data = worksheet.get_all_values()

pp = pprint.PrettyPrinter()
pp.pprint(data)
print(data[1][0])
