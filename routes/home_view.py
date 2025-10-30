import flet as ft
from components.task_card import create_task_card
from components.navbar import get_navbar, get_top_bar

def home_view(page, colors, tasks, on_add, on_detail, on_edit, on_completed, on_theme_toggle, on_complete):
    # فقط تسک‌های انجام‌نشده
    search = ft.TextField(
        hint_text="جستجو...",
        prefix_icon=ft.Icons.SEARCH,
        bgcolor=colors["card"],
        border_radius=10,
        color=colors["text"],
        text_align=ft.TextAlign.RIGHT,
    )
    results = ft.Column(spacing=8)

    def refresh(_=None):
        q = search.value.lower().strip()
        visible = [
            t for t in tasks if (not t["completed"]) and (q in t["title"].lower() or q in t["desc"].lower() or q in t["category"].lower())
        ] if q else [t for t in tasks if not t["completed"]]
        results.controls = [
            create_task_card(t, colors, on_detail, on_edit, on_complete) for t in visible
        ] if visible else [ft.Text("هیچ تسکی وجود ندارد.", color=colors["text"])]
        page.update()

    search.on_change = refresh
    refresh()

    return ft.View(
        "/",
        bgcolor=colors["bg"],
        scroll=ft.ScrollMode.AUTO,
        controls=[
            get_top_bar(colors, on_theme_toggle),
            ft.Text("مدیریت کارها", size=22, weight=ft.FontWeight.BOLD, color=colors["text"], text_align=ft.TextAlign.CENTER),
            search,
            results,
            ft.Divider(),
            get_navbar(colors, on_add, lambda e: page.go("/"), on_completed, on_theme_toggle),
        ],
    )
