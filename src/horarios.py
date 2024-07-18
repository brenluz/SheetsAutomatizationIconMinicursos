import gspread
import unicodedata
import re

def normalize_string(s):
    """Normalize string by removing accents"""
    return ''.join(c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn')

def getHorarios(sheet: gspread.worksheet, participantes):
    array = []
    # Assuming you're interested in a specific column, e.g., the first column
    # Fetch all values in that column
    print('Buscando horarios dos inscritos')
    try:
        all_values = sheet.row_values(4)  # Adjust the column index as needed
        normalized_values = [normalize_string(value) for value in all_values]

        for participante in participantes:
            normalized_participante = normalize_string(participante.split()[0])
            found = False

            # Iterate through normalized_values to find a match
            for index, value in enumerate(normalized_values):
                if normalized_participante.lower() in value.lower():
                    # print(f"Match found: {all_values[index]} at index {index + 1}")
                    found = True
                    # Fetch the entire row where the match was found
                    array.append(sheet.col_values(index + 1))  # Adjusting for 0-based index
                    break  # Assuming you only need the first match for each participante
            if not found:
                print('Participante não encontrado')
        print('Horarios encontrados')
        return array
    except:
        print('Erro ao buscar horarios')
        return None