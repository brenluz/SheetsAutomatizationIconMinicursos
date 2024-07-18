import gspread
import time
import random

def update_sheet_with_exponential_backoff(sheet, request):
    for n in range(0, 5):  # Retry up to 5 times
        try:
            sheet.batch_update(request)
            break  # Exit the loop if the request is successful
        except gspread.exceptions.APIError as e:
            if e.response.status_code == 429:
                time.sleep((2 ** n) + random.randint(0, 1000) / 1000)  # Exponential backoff
            else:
                raise  # Reraise the exception if it's not a rate limit error

def updateMember(sheet: gspread.worksheet , member, data):
    col = 2
    while(sheet.cell(1, col).value != None):
        col += 1
    sheet.update_cell(1, col, member)
    print("DATA:")
    print(data)
    print("END DATA")
    for i in range(len(data)):
        print(data[i])
        sheet.update_cell(data[i])  
    return col

def writeToCol(sheet: gspread.worksheet, col, data):
    for i in range(len(data)):
        if data[i] != '':
            sheet.update_cell(i+1, col, data[i])

def createMember(sheet, member, data):
     for n in range(0, 5):  # Retry up to 5 times
        try:
            memberCell = sheet.find(member)
            coluna = memberCell.col
            # coluna = updateMember(sheet, member, data)
            writeToCol(sheet, coluna, data)
            break  # Exit the loop if the request is successful
        except gspread.exceptions.APIError as e:
            if e.response.status_code == 429:
                time.sleep((2 ** n) + random.randint(0, 1000) / 1000)  # Exponential backoff
                print('Error 429 Quota limit exceeded')
                print('Retrying')
            else:
                raise  # Reraise the exception if it's not a rate limit error
