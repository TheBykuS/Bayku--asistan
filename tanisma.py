# -*- coding: utf-8 -*-


import json
import os

USER_DATA_FILE = "user_data.json"

def save_user_data(user_data):
    with open(USER_DATA_FILE, "w") as f:
        json.dump(user_data, f)

def load_user_data():
    if os.path.exists(USER_DATA_FILE):
        with open(USER_DATA_FILE, "r") as f:
            return json.load(f)
    return {"name": ""}

def meet_user(take_command, speak):
    user_data = load_user_data()
    if not user_data["name"]:
        speak("Merhaba! Ben Acro, sizinle tanışmak için sabırsızlanıyorum. İsminizi öğrenebilir miyim?")
        user_name = take_command()
        user_data["name"] = user_name
        save_user_data(user_data)
        speak(f"Memnun oldum, {user_name}! Size nasıl yardımcı olabilirim?")
    else:
        speak(f"Hoş geldiniz, {user_data['name']}! ")

def change_name(take_command, speak):
    speak("Elbette, isminizi değiştirmek istiyorsanız yeni isminizi söyleyebilirsiniz.")
    user_name = take_command()
    user_data = {"name": user_name}
    save_user_data(user_data)
    speak(f"İsminizi {user_name} olarak değiştirdim. Memnun oldum tekrar, {user_name}!")
