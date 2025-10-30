# core/settings.py
import json
import os

SETTINGS_FILE = os.path.join("data", "settings.json")

def save_theme_settings(theme_mode):
    os.makedirs("data", exist_ok=True)
    settings = load_settings()
    settings["theme_mode"] = theme_mode.value
    with open(SETTINGS_FILE, "w") as f:
        json.dump(settings, f)

def load_settings():
    if not os.path.exists(SETTINGS_FILE):
        return {"theme_mode": "light"}
    with open(SETTINGS_FILE) as f:
        return json.load(f)