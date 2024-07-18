import re

def getMembers(cursoEscolhido,sheet):
    try:
        print('Buscando inscritos no curso')
        regex = re.compile(cursoEscolhido)
        cells = sheet.findall(regex)
        participantes = []  
        for cell in cells:
            if(cell != None):
                participantes.append(sheet.cell(cell.row, cell.col-1).value)
        print('Inscritos encontrados')
        return participantes   
    except:
        print('Erro ao buscar participantes')
        return None