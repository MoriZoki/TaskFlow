import flet as ft
from components.navbar import get_navbar, get_top_bar, get_back_button
from components.task_card import create_task_card

def completed_view(page, colors, tasks, on_add, on_home, on_edit, on_theme_toggle):
    done = [t for t in tasks if t["completed"]]
    body = ft.Column(
        controls=[
            create_task_card(t, colors, lambda x: None, on_edit, lambda x: None)
            for t in done
        ] if done else [ft.Text("هیچ تسک انجام‌شده‌ای نیست.", color=colors["text"])],
        spacing=10,
    )

    return ft.View(
        "/completed",
        bgcolor=colors["bg"],
        scroll=ft.ScrollMode.AUTO,
        controls=[
            get_top_bar(colors, on_theme_toggle),
            get_back_button(colors, page),
            ft.Text("تسک‌های انجام‌شده", size=20, weight=ft.FontWeight.BOLD, color=colors["text"], text_align=ft.TextAlign.CENTER),
            ft.Divider(),
            body,
            get_navbar(colors, on_add, on_home, lambda e: None, on_theme_toggle),
        ],
    )
