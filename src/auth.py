import os
import gspread
import sys

from gspread.exceptions import APIError, SpreadsheetNotFound, NoValidUrlKeyFound

authMessages = []


def authenticate(auth):
    try:
        googleService = gspread.service_account(filename=auth)
        return googleService
    except APIError as e:
        authMessages.append('Erro ao autenticar com o Google Sheets')
        authMessages.append(e)
    except FileNotFoundError as e:
        authMessages.append('Arquivo de credenciais não encontrado')
        authMessages.append(e)
    except Exception as e:
        authMessages.append('Erro desconhecido')
        authMessages.append(e)


# noinspection PyProtectedMember
def getPath():
    try:
        if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
            # If so, use the bundle's directory
            base_path = sys._MEIPASS
        else:
            # Otherwise, use the directory of the script (or executable)
            base_path = os.path.dirname(__file__)
    except OSError as e:
        base_path = os.getcwd()
        authMessages.append('Erro do sistema ao pegar o caminho do arquivo:')
        authMessages.append(e)
    except Exception as e:
        base_path = os.getcwd()
        authMessages.append('Erro desconhecido ao pegar o caminho do arquivo')
        authMessages.append(e)
    return base_path


def getSheet(planilha):
    getPath()
    jsonFilePath = '../credentials.json'
    # jsonFilePath = os.path.join(basePath, 'credentials.json')
    googleService = authenticate(jsonFilePath)
    try:
        sheet = googleService.open_by_url(planilha)
    except SpreadsheetNotFound as e:
        authMessages.append('Planilha não encontrada')
        authMessages.append(e)
        return None, authMessages
    except APIError as e:
        authMessages.append('Erro ao abrir a planilha')
        authMessages.append(e)
        return None, authMessages
    except NoValidUrlKeyFound as e:
        authMessages.append('Url inválida')
        authMessages.append(e)
        print("eu tentei")
        return None, authMessages

    return sheet, authMessages
