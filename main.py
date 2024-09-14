import flet as ft
import json

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

    def findClicked(e):
        listview = ft.ListView(expand=1, spacing=10, padding=20)
        with open("sl.json", "r", encoding='utf-8') as sl:
            streams = json.load(sl)
        for i in streams:
            #if txtfld.content.value in i['name']:
            station = ft.ListTile(leading = ft.Icon(ft.icons.ALBUM), title=ft.Text(f"{i['name']}"), trailing=ft.IconButton(icon=ft.icons.PLAY_CIRCLE_FILL_OUTLINED, data=i["url"], on_click=playClicked))
            listview.controls.append(station)
        page.add(listview)

    def playClicked(e):
        banner = ft.Container(content=ft.Banner(leading=ft.Icon(ft.icons.AUDIOTRACK, color=ft.colors.GREEN_400, size=40), content=ft.Text(value="Station is loaded! Now press play button!"), actions=[ft.TextButton(text="Okay", style=buttonstyle, on_click=lambda _: page.close(banner.content))]), margin=16)
        global audio
        audio = ft.Audio(src=e.control.data, on_loaded=lambda _: page.open(banner.content))
        page.add(audio)
        audio.release()
        audio.play()

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
        content = ft.TextField(label="Station name", hint_text="Enter station name"),
        margin = 16,
        alignment = ft.alignment.center
    )

    findbutton = ft.Container(
        content = ft.FilledButton(text="Find", style=buttonstyle, on_click=findClicked),
        margin = 16,
        alignment = ft.alignment.center
    )

    content = ft.Column([
    label,
    txtfld,
    ft.Row([findbutton, ft.ElevatedButton("Play", on_click=lambda _: audio.play()), ft.ElevatedButton("Stop", on_click=lambda _: audio.release())])
    ])

    init()
    page.add(content)

ft.app(main)