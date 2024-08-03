import os

from dotenv import load_dotenv
from auth import getSheet
from choose import getMembers, cursosDisponiveis, choose
from horarios import getHorarios
from update import createMember, addInitialValues
from formatting import formatSheet
from formula import formula

load_dotenv()
# noinspection PyRedeclaration


def main():
    # Abre a planilha com os cursos, pega todas as opcoes e as demonstra ao usuario
    cursosUrl = os.getenv('CURSOS')
    planilhaCursos = getSheet(cursosUrl)[0].sheet1
    opcoes = cursosDisponiveis(planilhaCursos)
    cursoEscolhido = choose(opcoes)

    # Pega os participantes do curso escolhido e os horarios disponiveis
    participantes = getMembers(cursoEscolhido, planilhaCursos)[0]
    horariosUrl = os.getenv('HORARIOS')
    planilhaHorarios = getSheet(horariosUrl)[0].sheet1
    horarios = getHorarios(planilhaHorarios, participantes)[0]

    planilhaFinalUrl = os.getenv('PLANILHAFINAL')
    planilhaFinal = getSheet(planilhaFinalUrl)[0]
    ws_titles = [ws.title for ws in planilhaFinal.worksheets()]  # Pega todas as planilhas do planejamento dos cursos

    # Pega todas as planilhas do planejamento
    print('Abrindo planilha para escrever os dados')
    if cursoEscolhido not in ws_titles:  # Verifica se o curso escolhido ja está na planilha de planejamento
        planilhaFinal.add_worksheet(title=cursoEscolhido, rows=100, cols=30)  # Adiciona uma nova planilha para o
        # curso escolhido
    elif cursoEscolhido in ws_titles:
        entrada = input('Este Curso ja possui uma planilha, tem certeza que deseja continuar? [y/n]')
        entrada.lower()
        if entrada == 'n':
            print('Programa finalizado')
            exit()
    planilhaFinal = planilhaFinal.worksheet(cursoEscolhido)
    addInitialValues(horariosUrl, planilhaHorarios.title, planilhaFinal)
    print('Escrevendo horarios dos inscritos na planilha')
    for i in range(len(participantes)):
        planilhaFinal.update_cell(1, i+3, participantes[i])  # Adiciona os participantes na planilha final
        createMember(planilhaFinal, participantes[i], horarios[i])

    print("adicionando formatacao correta na planilha")
    for i in range(len(participantes)):
        planilhaFinal.update_cell(1, i+3, participantes[i])
        formatSheet(planilhaFinal, planilhaFinal.find(participantes[i]), horarios[i])
        planilhaFinal.update_cell(1, i+3, "")
    colformula = len(participantes) + 4
    formula(planilhaFinal, colformula)
    print('Planilha pronta')
    print('Programa finalizado com sucesso')
    repeat = input("Quer fazer a planilha de outro curso? [y/n]")
    if repeat == 'y':
        main()
    else:
        exit()


main()
