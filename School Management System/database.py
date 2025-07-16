import json
import os

DATA_DIR = "data"
USERS_FILE = os.path.join(DATA_DIR, "users.json")
CLASSES_FILE = os.path.join(DATA_DIR, "classes.json")
GRADES_FILE = os.path.join(DATA_DIR, "grades.json")

def load_data(filepath):
    if not os.path.exists(filepath):
        return {}
    with open(filepath, 'r') as f:
        return json.load(f)

def save_data(filepath, data):
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=4)

def get_all_users():
    return load_data(USERS_FILE)

def save_all_users(users):
    save_data(USERS_FILE, users)

def get_all_classes():
    return load_data(CLASSES_FILE)

def save_all_classes(classes):
    save_data(CLASSES_FILE, classes)

def get_all_grades():
    return load_data(GRADES_FILE)

def save_all_grades(grades):
    save_data(GRADES_FILE, grades)
