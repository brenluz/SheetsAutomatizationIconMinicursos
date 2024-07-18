import gspread

def lookFor(curso,sheet):
    cell = sheet.find(curso)
    return cell

def cursosDisponiveis(sheet: gspread.worksheet):
    coluna = lookFor('Escolha os minicursos nos quais voce mais tem interesse', sheet)
    cursosDisponiveis = sheet.col_values(coluna.col) 

    cur_str = ','.join(cursosDisponiveis)
    x = cur_str.split(',')
    x = [curso.strip() for curso in x]
    cursosDisponiveis = x
    cursos = []

    for i in range(len(cursosDisponiveis)):
        if cursosDisponiveis[i] not in cursos:
            cursos.append(cursosDisponiveis[i])
    cursos.pop(0)
    return cursos

def choose(options):
    print('Escolha um dos cursos disponíveis:')
    for i in range(len(options)):
        print(f'{i+1} - {options[i]}')
    choice = int(input('Digite o número correspondente ao curso escolhido: '))
    return options[choice-1]