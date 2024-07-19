import gspread
import time
import random

def update_sheet_with_exponential_backoff(sheet: gspread.worksheet , request):
    for n in range(0, 5):  # Retry up to 5 times
        try:
            sheet.batch_update(request)
            break  # Exit the loop if the request is successful
        except gspread.exceptions.APIError as e:
            if e.response.status_code == 429:
                time.sleep((2 ** n) + random.randint(0, 1000) / 1000)  # Exponential backoff
            else:
                raise  # Reraise the exception if it's not a rate limit error

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
            updateBatch(sheet,coluna, data)
            break  # Exit the loop if the request is successful
        except gspread.exceptions.APIError as e:
            if e.response.status_code == 429:
                time.sleep((2 ** n) + random.randint(0, 1000) / 1000)  # Exponential backoff
                print('Error 429 Quota limit exceeded')
                print('Retrying')
                n -= 1
            else:
                raise  # Reraise the exception if it's not a rate limit error

def col_num_to_letter(col_num):
    """Convert a column number (1-indexed) to a column letter."""
    letter = ''
    while col_num > 0:
        col_num, remainder = divmod(col_num - 1, 26)
        letter = chr(65 + remainder) + letter
    return letter 

def updateBatch(worksheet, col_num, data_list):
    # Convert column number to letter
    col_letter = col_num_to_letter(col_num)
    # Prepare the range string for the specified column
    range_string = f"{col_letter}1:{col_letter}{len(data_list)}"
    # Prepare the data for batch update
    values = [[item] for item in data_list]  # Each item in its own row
    # Correctly structured request for batch_update
    value_ranges = [
        {
            "range": range_string,
            "values": values
        }
    ]
    # Use the worksheet's batch_update method
    worksheet.batch_update(value_ranges, value_input_option='RAW')