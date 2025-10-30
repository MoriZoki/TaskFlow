import flet as ft
from core.theme import get_theme_colors
from core.storage import load_tasks, save_tasks
from components.toast import create_toast
from routes.home_view import home_view
from routes.completed_view import completed_view
from routes.add_edit_view import add_edit_view
from routes.detail_view import detail_view

CATEGORIES = ["کار","خانواده","مطالعه","ملاقات","سفر","خرید","ورزش","پروژه","مالی","آموزش","ترجمه","بازاریابی","چک‌لیست","یادآوری","فنی","تحقیق","هنر","یادگیری","همکاری","دیگر"]

COLORS = ["#F44336","#E91E63","#9C27B0","#673AB7","#3F51B5","#2196F3","#03A9F4","#00BCD4","#009688","#4CAF50","#8BC34A","#CDDC39","#FFEB3B","#FFC107","#FF9800","#FF5722","#795548","#9E9E9E","#607D8B","#000000"]

def main(page: ft.Page):
    page.title = "Task Manager"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.scroll = ft.ScrollMode.AUTO
    page.padding = 20
    tasks = load_tasks()
    toast = create_toast(page)
    colors = get_theme_colors(page.theme_mode)

    def store():
        save_tasks(tasks)

    def toggle_theme(e):
        # تغییر تم
        page.theme_mode = (
            ft.ThemeMode.DARK
            if page.theme_mode == ft.ThemeMode.LIGHT
            else ft.ThemeMode.LIGHT
        )

        # به‌روزرسانی رنگ‌ها طبق تم جدید
        new_colors = get_theme_colors(page.theme_mode)
        for k in colors.keys():
            colors[k] = new_colors[k]

        # خنثی کردن تم داخلی فلت
        page.theme = ft.Theme(
            color_scheme_seed=None,
            visual_density=ft.VisualDensity.ADAPTIVE_PLATFORM_DENSITY,
        )

        # ست مستقیم رنگ پس‌زمینه
        page.bgcolor = colors["bg"]
        page.window.bgcolor = colors["bg"]
        page.window_surface = colors["bg"]

        # پاک کردن ویوها و بازسازی کامل صفحه
        page.views.clear()
        page.update()
        page.go(page.route)
        print("Theme mode:", page.theme_mode, "BG:", colors["bg"])



    def handle_complete(task):
        task["completed"] = True
        save_tasks(tasks)
        toast("تسک تکمیل شد", ft.Colors.GREEN)
        page.go("/")

    def route_change(e):
        page.views.clear()
        r = page.route
        if r == "/":
            page.views.append(
                home_view(page, colors, tasks,
                          on_add=lambda e: page.go("/add"),
                          on_detail=lambda t: page.go(f"/detail/{t['id']}"),
                          on_edit=lambda t: page.go(f"/edit/{t['id']}"),
                          on_completed=lambda e: page.go("/completed"),
                          on_theme_toggle=toggle_theme,
                          on_complete=handle_complete)
            )
        elif r == "/add":
            page.views.append(add_edit_view(page, colors, tasks, store, toast, CATEGORIES, COLORS))
        elif r.startswith("/edit/"):
            tid = r.split("/edit/")[1]
            exist = next((t for t in tasks if t["id"] == tid), None)
            page.views.append(add_edit_view(page, colors, tasks, store, toast, CATEGORIES, COLORS, exist))
        elif r == "/completed":
            page.views.append(completed_view(page, colors, tasks, on_add=lambda e: page.go("/add"), on_home=lambda e: page.go("/"), on_edit=lambda t: page.go(f"/edit/{t['id']}"), on_theme_toggle=toggle_theme))
        elif r.startswith("/detail/"):
            tid = r.split("/detail/")[1]
            page.views.append(detail_view(page, colors, tasks, store, toast, tid))
        page.update()

    def view_pop(e):
        page.views.pop()
        page.update()

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go("/")

ft.app(target=main)
