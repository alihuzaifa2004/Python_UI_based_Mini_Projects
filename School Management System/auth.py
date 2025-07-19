import tkinter as tk
from tkinter import messagebox
import database

import database

def login(username, password, role=None):
    users = database.get_all_users()
    user = users.get(username)
    if user and user["password"] == password:
        if role is None or user["role"] == role:
            return user
    return None

def register(username, password, role):
    users = database.get_all_users()
    if username in users:
        return False, "Username already exists!"
    users[username] = {
        "password": password,
        "role": role
    }
    database.save_all_users(users)
    return True, "Registration successful!"
