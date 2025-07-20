from core.database import read_json, write_json

def load_users(file_path):
    users = read_json(file_path)
    if isinstance(users, dict):
        users = [users]
    return users

def authenticate_user(username, password, file_path):
    users = load_users(file_path)
    for user in users:
        if user['username'] == username and user['password'] == password:
            return True
    return False

def register_user(new_user, file_path):
    users = load_users(file_path)
    users = [user for user in users if isinstance(user, dict) and 'username' in user]
    
    if any(user['username'] == new_user['username'] for user in users):
        return False

    users.append(new_user)
    write_json(file_path, users)
    return True
