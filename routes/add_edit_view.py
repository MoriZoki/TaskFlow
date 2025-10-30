import flet as ft
from uuid import uuid4
from datetime import datetime
from components.navbar import get_back_button

def add_edit_view(page, colors, tasks, save_tasks, toast, categories, color_set, existing=None):
    sel_color = existing["color"] if existing else color_set[5]
    title = ft.TextField(label="عنوان", value=existing["title"] if existing else "", text_align=ft.TextAlign.RIGHT)
    desc = ft.TextField(label="توضیحات", value=existing["desc"] if existing else "", multiline=True, text_align=ft.TextAlign.RIGHT)
    cats = ft.Dropdown(label="دسته", options=[ft.dropdown.Option(c) for c in categories], value=existing["category"] if existing else categories[0])

    def pick(e):
        nonlocal sel_color
        sel_color = e.control.data
        for c in color_row.controls:
            c.border = ft.border.all(2, ft.Colors.TRANSPARENT)
        e.control.border = ft.border.all(3, ft.Colors.BLUE)
        page.update()

    color_row = ft.Row(
        wrap=True,
        spacing=6,
        controls=[ft.Container(width=28, height=28, bgcolor=c, border_radius=30, data=c, on_click=pick) for c in color_set],
    )

    def save(_):
        if not title.value.strip():
            title.error_text = "عنوان الزامی است!"
            page.update()
            return
        t = {
            "id": existing["id"] if existing else str(uuid4()),
            "title": title.value.strip(),
            "desc": desc.value.strip(),
            "category": cats.value,
            "color": sel_color,
            "completed": existing["completed"] if existing else False,
            "created": existing["created"] if existing else str(datetime.now()),
        }
        if existing:
            for i, x in enumerate(tasks):
                if x["id"] == existing["id"]:
                    tasks[i] = t
                    break
            toast("ویرایش شد", ft.Colors.BLUE)
        else:
            tasks.append(t)
            toast("افزوده شد", ft.Colors.GREEN)
        save_tasks()
        page.go("/")

    return ft.View(
        "/edit" if existing else "/add",
        bgcolor=colors["bg"],
        scroll=ft.ScrollMode.AUTO,
        controls=[
            get_back_button(colors, page),
            ft.Text("ویرایش تسک" if existing else "افزودن تسک", size=20, weight=ft.FontWeight.BOLD, color=colors["text"]),
            title, desc, cats, ft.Text("رنگ:", color=colors["text"]),
            color_row,
            ft.Row([
                ft.ElevatedButton("ذخیره", bgcolor=colors["button"], color=ft.Colors.WHITE, on_click=save),
            ], alignment=ft.MainAxisAlignment.END),
        ],
    )