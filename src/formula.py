from update import updateBatch
from formatting import formatSheet
import gspread

def remove_percentage(values):
    result = []
    for value in values:
        if '%' in value:
            value = value.replace('%', '')
            print(value)
            result.append(int(value))
    return result


def convert_to_A1(col, row):
    # Convert column number to A1 notation
    col_str = ""
    while col > 0:
        col, remainder = divmod(col - 1, 26)
        col_str = chr(65 + remainder) + col_str
    return f"{col_str}{row}"


def add_percentage(values):
    result = []
    for value in values:
        result.append(f"{value}%")
    return result


def formula(sheet: gspread.worksheet, col):
    array = ["", "", "", ""]
    for i in range(5, 58):
        cellRange = convert_to_A1(col - 2, i)
        string = '=PERCENTIF(C' + str(i) + ':' + cellRange + '; "")'
        array.append(string)
    sheet.update_cell(4, col, "Porcentagem de Horarios Livres")
    updateBatch(sheet, col, array)
    formatSheet(
        sheet=sheet,
        cell=sheet.cell(4, col),
        data=array[4:],
        condition=["50%"],
        type_of="NUMBER_GREATER",
        color1=[234 / 255, 153 / 255, 153 / 255],
        color2=[183 / 255, 225 / 255, 205 / 255]
    )
