import flet as ft
from auth import getSheet


def create_form():
    return ft.TextField(
        label="Insert Url",
        text_align=ft.TextAlign.CENTER
    )


class ConsoleApp:
    def __init__(self, page):
        self.page = page
        self.log = []
        self.console = self.create_console()
        self.form = create_form()
        self.cursos = self.create_url_page("Insira a planilha na qual o programa ira procurar os cursos")
        self.current = self.cursos

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

    def create_url_page(self, text: str):
        return ft.Column([
            ft.Text(text),
            ft.Card(
                self.form,
                width=300
            ),
            ft.ElevatedButton(
                text="Submit",
                on_click=self.button_clicked
            )],
        )

    def button_clicked(self, e):
        url = self.form.value
        sheet, authMessages = getSheet(url)
        self.update_log(authMessages)
        return sheet

    def update_log(self, messages):
        self.log.clear()
        for message in messages:
            self.log.append(ft.Text(message))
        self.console.update()

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
