import flet as ft
import os
import gspread
from dotenv import load_dotenv

from choose import cursosDisponiveis, getMembers
from auth import getSheet
from horarios import getHorarios

load_dotenv()


def create_form():
    return ft.TextField(
        label="Insert Url",
        text_align=ft.TextAlign.CENTER
    )


def create_loading_page():
    return ft.Column([
        ft.Card(
            ft.Text("Loading"),
        ),
        ft.ProgressRing(
            width=16,
            height=16
        )
    ])


class ConsoleApp:
    def __init__(self, page):
        self.page = page
        self.log = []
        self.console = self.create_console()
        self.loading_page = create_loading_page()
        self.form = create_form()
        self.cursos = self.create_url_page(
            "Insira o url da planilha na qual o programa ira procurar os cursos",
            self.insert_url(nextpage=self.create_options_page)

        )
        self.current = self.cursos
        self.sheet: gspread.Spreadsheet or None = None
        self.selectedOption = None

    def create_console(self):
        return ft.Card(
            ft.SafeArea(
                ft.Column(
                    [
                        ft.Text("Console"),
                        ft.Column(
                            self.log,
                            alignment=ft.MainAxisAlignment.START,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            width=300,
                            height=300,
                            scroll=ft.ScrollMode.ADAPTIVE
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.START,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,

                ),
            ),
            color=ft.colors.BLACK
        )

    def create_url_page(self, text: str, onclick):
        return ft.Column([
            ft.Text(text),
            ft.Card(
                self.form,
                width=300
            ),
            ft.ElevatedButton(
                text="Submit",
                on_click=onclick
            )],
        )

    def insert_url(self, nextpage):
        self.change_page(self.loading_page)
        self.update_log(["Buscando planilha"])
        url = self.form.value
        self.sheet, authMessages = getSheet(url)
        self.update_log(authMessages)
        if self.sheet:
            self.update_log(["Planilha encontrada"])
            self.change_page(nextpage)

    def create_options_page(self):
        opcoes = cursosDisponiveis(self.sheet.sheet1)
        buttons = ft.RadioGroup(
            content=ft.Column(
                [ft.Radio(value=opcao, label=opcao) for opcao in opcoes],
            ),
            on_change=self.on_change_option
        )
        return ft.Column([
            ft.Text("Escolha uma opção"),
            ft.Column(
                [
                    buttons,
                    ft.OutlinedButton("Submit", on_click=self.choose)],
                alignment=ft.MainAxisAlignment.START,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ),

        ])

    def on_change_option(self, e):
        self.selectedOption = e.control.value

    def choose(self, e):
        self.change_page(self.loading_page)
        e.control.parent.parent.clean()
        e.control.parent.parent.update()
        participantes, memberMessages = getMembers(self.selectedOption, self.sheet.sheet1)
        self.update_log(memberMessages)
        urlHorarios = os.getenv('HORARIOS')
        self.sheet, sheetMessages = getSheet(urlHorarios)
        self.update_log(sheetMessages)
        horarios, horariosMessages = getHorarios(self.sheet.sheet1, participantes)
        self.update_log(horariosMessages)

    def update_log(self, messages):
        for message in messages:
            self.log.append(ft.Text(message))
        self.console.update()

    def view_table(self):
        self.change_page(
            self.create_url_page(
                "Insira o url da planilha na qual deseja escrever os dados",
                self.insert_url(nextpage=self.create_table)
            )
        )

    def create_table(self):
        values = self.sheet.sheet1.get_all_values()
    def change_page(self, page):
        self.current = page
        self.page.clean()
        self.build()

    def build(self):
        self.page.vertical_alignment = ft.MainAxisAlignment.CENTER
        self.page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.page.add(
            ft.Row(
                [self.console, self.current],
                spacing=100
            ),
        )


def gui(page: ft.page):
    app = ConsoleApp(page)
    app.build()
    return app


ft.app(target=gui)

# async def gui(page: ft.page):
#     def button_clicked(e):
#         url = form.value
#         sheet = getSheet(url)
#         if sheet is None:
#             log.append(ft.Text("Invalid Url"))
#             return
#         current.clean()
#         return sheet
#
#     page.vertical_alignment = ft.MainAxisAlignment.CENTER
#     page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
#     log = [ft.Text("Console")]
#     console = ft.Card(
#         ft.Column(
#             log,
#             alignment=ft.MainAxisAlignment.START,
#             horizontal_alignment=ft.CrossAxisAlignment.CENTER,
#             width=300
#         ),
#         color=ft.colors.BLACK
#     )
#     form = ft.TextField(
#         label="Insert Url",
#         text_align=ft.TextAlign.CENTER
#     )
#     cursos = ft.Column([
#             ft.Text("Insira a planilha na qual o programa ira procurar os cursos"),
#             ft.Card(
#                 form,
#                 width=300
#             ),
#             ft.ElevatedButton(
#                 text="Submit",
#                 on_click=button_clicked
#             )]
#     )
#
#     current = cursos
#     page.add(
#         ft.Row(
#             [console],
#             alignment=ft.MainAxisAlignment.START
#         ),
#         current
#     )
