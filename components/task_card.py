import flet as ft

def create_task_card(task, colors, on_detail, on_edit, on_complete):
    border_color = task["color"]
    title = ft.Text(task["title"], size=15, weight=ft.FontWeight.BOLD, color=colors["text"])
    desc = ft.Text(task["desc"], size=12, color=colors["text"], max_lines=2, overflow=ft.TextOverflow.ELLIPSIS)

    def confirm_complete(e):
        dlg = ft.AlertDialog(
            modal=True,
            content=ft.Text("این تسک را انجام‌شده علامت بزنم؟", color=colors["text"]),
        )

        def close_dialog(result):
            dlg.open = False
            e.page.update()
            if result:
                on_complete(task)

        dlg.actions = [
            ft.TextButton("خیر", on_click=lambda x: close_dialog(False)),
            ft.TextButton("بله", on_click=lambda x: close_dialog(True)),
        ]

        e.page.dialog = dlg
        dlg.open = True
        e.page.update()

    row = ft.Row(
        alignment=ft.MainAxisAlignment.END,
        controls=[
            ft.IconButton(icon=ft.Icons.INFO, tooltip="جزئیات", on_click=lambda e: on_detail(task)),
            ft.IconButton(icon=ft.Icons.EDIT, tooltip="ویرایش", on_click=lambda e: on_edit(task)),
            ft.IconButton(icon=ft.Icons.CHECK_CIRCLE, icon_color=border_color, tooltip="تکمیل", on_click=confirm_complete),
        ],
    )

    return ft.Container(
        bgcolor=colors["card"],
        border=ft.border.all(2, border_color),
        border_radius=12,
        padding=10,
        margin=ft.margin.only(bottom=6),
        content=ft.Column(spacing=4, controls=[title, desc, row]),
    )
