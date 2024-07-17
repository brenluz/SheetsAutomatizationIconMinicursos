from auth import getSheet

def write(sheet, row, col, data): # Função para escrever na planilha recebe a planilha, linha e coluna, e o dado a ser escrito
    sheet.update_cell(row, col, data)

cursoEscolhido = input('Digite para qual curso gostaria de ver a disponibilidade de horários:')

cursos = getSheet('Cursos').sheet1

print(cursos.get_all_values())
horarios = getSheet('Horarios')
plan = getSheet('Planejamento')

ws_titles = [ws.title for ws in plan.worksheets()] # Pega todas as planilhas do planejamento dos cursos

 # Pega todas as planilhas do planejamento
if cursoEscolhido not in ws_titles: # Verifica se o curso escolhido ja está na planilha de planejamento
    plan.add_worksheet(title= cursoEscolhido, rows= 100, cols= 20) # Adiciona uma nova planilha para o curso escolhido