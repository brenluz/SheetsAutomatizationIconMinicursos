from update import writeToCol 

#Updates the sheet to the right formatting
def Formatsheet(sheet1, sheet2): 
    coluna1 = sheet1.col_values(1)
    coluna2 = sheet1.col_values(2)
    writeToCol(sheet2, 1, coluna1)
    writeToCol(sheet2, 2, coluna2)
