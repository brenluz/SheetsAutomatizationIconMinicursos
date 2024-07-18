from update import writeToCol 

#Updates the sheet to the right formatting
def Formatsheet(sheet1, sheet2): 
    coluna1 = sheet1.col_values(1)
    coluna2 = sheet1.col_values(2)
    if isEmpty(coluna1):
        writeToCol(sheet2, 1, coluna1)
    if isEmpty(coluna2):
        writeToCol(sheet2, 2, coluna2)

def isEmpty(array):
    string = array
    i = 0
    while string[0] == '':
        string.pop(0)
        i += 1
    if len(string) == 0:
        return True
    else:
        print('coluna ja existe pulando')
        return False
