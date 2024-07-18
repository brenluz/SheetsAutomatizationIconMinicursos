from auth import getSheet
from members import getMembers
from choose import cursosDisponiveis, choose
from horarios import getHorarios
from formatting import Formatsheet
from update import createMember

# Abre a planilha com os cursos, pega todas as opcoes e as demonstra ao usuario
planilhaCursos = getSheet('Cursos').sheet1 
opcoes = cursosDisponiveis(planilhaCursos)
cursoEscolhido = choose(opcoes)

# Pega os participantes do curso escolhido e os horarios disponiveis
participantes = getMembers(cursoEscolhido, planilhaCursos) 
planilhaHorarios = getSheet('Horarios').sheet1
horarios = getHorarios(planilhaHorarios, participantes)

planilhaFinal = getSheet('Planejamento')
ws_titles = [ws.title for ws in planilhaFinal.worksheets()] # Pega todas as planilhas do planejamento dos cursos

 # Pega todas as planilhas do planejamento
print('Abrindo planilha para escrever os dados')
if cursoEscolhido not in ws_titles: # Verifica se o curso escolhido ja está na planilha de planejamento
    planilhaFinal.add_worksheet(title= cursoEscolhido, rows= 100, cols= 30)# Adiciona uma nova planilha para o curso escolhido
planilhaFinal = planilhaFinal.worksheet(cursoEscolhido)
Formatsheet(planilhaHorarios, planilhaFinal) # Formata a planilha de horarios para a planilha final

print('Escrevendo horarios dos inscritos na planilha')
for i in range(len(participantes)):
    planilhaFinal.update_cell(1, i+2, participantes[i]) # Adiciona os participantes na planilha final   
    createMember(planilhaFinal, participantes[i], horarios[i])
print('Programa finalizado')
