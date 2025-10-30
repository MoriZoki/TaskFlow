import flet as ft

LIGHT_THEME = {
    "bg": "#FFFFFF",
    "text": "#121212",
    "card": "#F9F9F9",
    "navbar": "#EDEDED",
    "button": "#2196F3",
}

DARK_THEME = {
    "bg": "#121212",
    "text": "#FFFFFF",
    "card": "#1E1E1E",
    "navbar": "#252525",
    "button": "#2196F3",
}


def get_theme_colors(mode: ft.ThemeMode):
    return LIGHT_THEME if mode == ft.ThemeMode.LIGHT else DARK_THEME
