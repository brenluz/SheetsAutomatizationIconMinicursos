import gspread
import gspread_formatting as gf


def to_a1(row, col):
    """Convert row and column numbers to A1 notation."""
    # Convert column number to letter(s)
    col_letter = ''
    while col > 0:
        col, remainder = divmod(col - 1, 26)
        col_letter = chr(65 + remainder) + col_letter
    # Concatenate column letter(s) with row number
    return f"{col_letter}{row}"


def createRule(initialCell, finalCell, sheet: gspread.worksheet, condition):
    rule = gf.ConditionalFormatRule(
        ranges=[gf.GridRange.from_a1_range(initialCell + ':' + finalCell, sheet)],
        booleanRule=gf.BooleanRule(
            condition=gf.BooleanCondition('TEXT_EQ', condition),
            format=gf.CellFormat(backgroundColor=gf.Color(147 / 255, 196 / 255, 125 / 255))
        )
    )
    return rule


def formatSheet(sheet: gspread.worksheet, cell, data):
    try:
        initialcell = [cell.row + 4, cell.col]
        finalcell = [cell.row + len(data), cell.col]
        initialcell = to_a1(initialcell[0], initialcell[1])
        finalcell = to_a1(finalcell[0], finalcell[1])
        current_fmt = gf.get_effective_format(sheet, initialcell)
        if current_fmt.backgroundColor == gf.Color(1, 1, 1):
            bold_border = gf.Border(style='SOLID_MEDIUM', color=gf.Color(0, 0, 0))  # Black, medium (bold) border
            # Apply the bold border to all sides of the cell
            borders = gf.Borders(top=bold_border, bottom=bold_border, left=bold_border, right=bold_border)

            fmt = gf.cellFormat(backgroundColor=gf.Color(224 / 255, 102 / 255, 102 / 255), borders=borders)
            gf.format_cell_range(sheet, initialcell + ':' + finalcell, fmt)

            rule = createRule(initialcell, finalcell, sheet, [""])
            rules = gf.get_conditional_format_rules(sheet)
            rules.append(rule)
            rules.save()
    except Exception as e:
        print(e)
        print('Error formatting cell')
        exit()
