import flet as ft
from components.navbar import get_back_button

def detail_view(page, colors, tasks, save_tasks, toast, tid):
    task = next((t for t in tasks if t["id"] == tid), None)
    if not task:
        return ft.View("/detail", controls=[ft.Text("وظیفه یافت نشد", color=ft.Colors.RED)])

    def toggle(_):
        task["completed"] = not task["completed"]
        save_tasks()
        toast("وضعیت تغییر کرد")
        page.go("/")

    def delete(_):
        tasks.remove(task)
        save_tasks()
        toast("حذف شد", ft.Colors.RED)
        page.go("/")

    box = ft.Container(
        bgcolor=colors["card"],
        border=ft.border.all(2, task["color"]),
        border_radius=10,
        padding=12,
        content=ft.Column([
            ft.Text(task["title"], size=22, weight=ft.FontWeight.BOLD, color=colors["text"]),
            ft.Text(task["desc"], color=colors["text"]),
            ft.Text(task["category"], color=task["color"]),
        ]),
    )

    btns = ft.Row([
        ft.TextButton("ویرایش", on_click=lambda e: page.go(f"/edit/{tid}")),
        ft.ElevatedButton("تغییر وضعیت", bgcolor=ft.Colors.GREEN, color=ft.Colors.WHITE, on_click=toggle),
        ft.OutlinedButton("حذف", style=ft.ButtonStyle(color=ft.Colors.RED), on_click=delete),
    ], alignment=ft.MainAxisAlignment.END)

    return ft.View(
        f"/detail/{tid}",
        bgcolor=colors["bg"],
        scroll=ft.ScrollMode.AUTO,
        controls=[get_back_button(colors, page), box, ft.Divider(), btns],
    )
