import json

def load_users():
    with open("users.json",'r') as file:
        return json.load(file)
    
def login():
    users = load_users()

    print("\n === Login Kasir ===")
    username = input('Username = ')
    password = input('password = ')

    for user in users:
        if user["username"] == username and user["password"] == password:
            print(f"\n Login berhasil sebagai {user['role'].upper()}")
            return user["role"]
        

    print("\n Login gagal! Username atau Password salah.")
    return None