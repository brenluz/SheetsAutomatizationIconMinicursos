import gspread
import re

global gui

chooseMessages = []


def lookFor(curso, sheet):
    cell = sheet.find(curso)
    return cell


def cursosDisponiveis(sheet: gspread.worksheet):
    coluna = lookFor('Escolha os minicursos nos quais voce mais tem interesse', sheet)
    cursosDisponivel = sheet.col_values(coluna.col)

    cur_str = ','.join(cursosDisponivel)
    x = cur_str.split(',')
    x = [curso.strip() for curso in x]
    cursosDisponivel = x
    cursos = []

    for i in range(len(cursosDisponivel)):
        if cursosDisponivel[i] not in cursos:
            cursos.append(cursosDisponivel[i])
    cursos.pop(0)
    return cursos


def choose(options):
    for i in range(len(options)):
        print(f'{i + 1} - {options[i]}')
    choice = int(input('Digite o número correspondente ao curso escolhido: '))
    return options[choice - 1]


def getMembers(cursoEscolhido, sheet):
    try:
        chooseMessages.append('Buscando inscritos no curso')
        regex = re.compile(cursoEscolhido)
        cells = sheet.findall(regex)
        participantes = []
        for cell in cells:
            if cell is not None:
                participantes.append(sheet.cell(cell.row, cell.col - 1).value)
        chooseMessages.append('Inscritos encontrados')
        return participantes, chooseMessages
    except:
        chooseMessages.append('Erro ao buscar inscritos')
        return None, chooseMessages
