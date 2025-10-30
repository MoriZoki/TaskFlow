import flet as ft

def get_navbar(colors, on_add, on_home, on_completed, on_theme_toggle):
    return ft.Container(
        alignment=ft.alignment.bottom_center,
        content=ft.Container(
            bgcolor=colors["navbar"],
            border_radius=14,
            padding=8,
            content=ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_AROUND,
                controls=[
                    ft.IconButton(icon=ft.Icons.LIST, icon_color=colors["text"], tooltip="تسک‌ها", on_click=on_home),
                    ft.FloatingActionButton(icon=ft.Icons.ADD, bgcolor=colors["button"], tooltip="افزودن کار", on_click=on_add),
                    ft.IconButton(icon=ft.Icons.TASK_ALT, icon_color=colors["text"], tooltip="انجام‌شده", on_click=on_completed),
                ],
            ),
        ),
    )


def get_top_bar(colors, on_theme_toggle):
    return ft.Row(
        alignment=ft.MainAxisAlignment.END,
        controls=[
            ft.IconButton(icon=ft.Icons.BRIGHTNESS_6, icon_color=colors["text"], tooltip="تغییر تم", on_click=on_theme_toggle)
        ],
    )


def get_back_button(colors, page):
    return ft.Row(
        alignment=ft.MainAxisAlignment.START,
        controls=[
            ft.IconButton(icon=ft.Icons.ARROW_BACK, icon_color=colors["text"], on_click=lambda e: page.go("/"))
        ],
    )
