import flet as ft


def main(page: ft.Page):
    buttonstyle = ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10))
    page.title = "RadioMD"

    def init():
        if page.client_storage.get("theme") == None:
            page.client_storage.set("theme", "Comfort Blue")
            page.theme = ft.Theme(color_scheme_seed='blue')
        if page.client_storage.get("theme") == "Comfort Blue":
            page.theme = ft.Theme(color_scheme_seed='blue')
        elif page.client_storage.get("theme") == "Dark Green":
            page.theme = ft.Theme(color_scheme_seed='green')
        elif page.client_storage.get("theme") == "Angry Red":
            page.theme = ft.Theme(color_scheme_seed='red')

    def settingsClicked(e):
        page.open(settings)
        page.update()

    def dropdownChanged(e):
        if settings.content.value == "Comfort Blue":
            page.theme = ft.Theme(color_scheme_seed='blue')
            page.client_storage.set("theme", "Comfort Blue")
        elif settings.content.value == "Dark Green":
            page.theme = ft.Theme(color_scheme_seed='green')
            page.client_storage.set("theme", "Dark Green")
        if settings.content.value == "Angry Red":
            page.theme = ft.Theme(color_scheme_seed='red')
            page.client_storage.set("theme", "Angry Red")

        page.update()

    settings = ft.AlertDialog(title=ft.Text("Settings"), content=ft.Dropdown(label="Theme", on_change=dropdownChanged, options=[ft.dropdown.Option("Comfort Blue"), ft.dropdown.Option("Dark Green"), ft.dropdown.Option("Angry Red")]))

    label = ft.Container(
        content = ft.Row([ft.Text("RadioMD", size=24), ft.IconButton(icon=ft.icons.SETTINGS_SHARP, icon_size=32, on_click=settingsClicked)], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
        margin = 16,
        alignment = ft.alignment.center
    )

    txtfld = ft.Container(
        content = ft.TextField(label="Frequency", hint_text="87,5 - 108 MHz"),
        margin = 16,
        alignment = ft.alignment.center
    )

    button = ft.Container(
        content = ft.FilledButton(text="Find", style=buttonstyle),
        margin = 16,
        alignment = ft.alignment.center
    )

    content = ft.Column([
    label,
    txtfld,
    button
    ])

    init()
    page.add(content)

ft.app(main)