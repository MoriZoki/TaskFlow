import flet as ft, threading

def create_toast(page):
    def show(msg, color=ft.Colors.GREEN):
        box = ft.Container(
            bgcolor=color,
            content=ft.Text(msg, color="white", size=15, text_align=ft.TextAlign.CENTER),
            border_radius=10,
            padding=10,
            alignment=ft.alignment.center,
        )
        page.overlay.append(box)
        page.update()

        def remove():
            page.overlay.remove(box)
            page.update()

        threading.Timer(1.5, remove).start()

    return show
