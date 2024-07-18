import gspread

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
            print
            sheet.update_cell(i+1, col, data[i])

def createMember(sheet, member, data):
    member = sheet.find(member)
    coluna = member.col
    # coluna = updateMember(sheet, member, data)
    writeToCol(sheet, coluna, data)