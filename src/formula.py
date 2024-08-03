def convert_to_A1(col, row):
    # Convert column number to A1 notation
    col_str = ""
    while col > 0:
        col, remainder = divmod(col - 1, 26)
        col_str = chr(65 + remainder) + col_str
    return f"{col_str}{row}"


def formula(sheet, col):
    for i in range(5, 58):
        cellRange = convert_to_A1(col - 2, i)
        sheet.update_cell(i, col-1, f'=PERCENTIF(C{i}:{cellRange}; "")')
