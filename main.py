from Menu import main_menu_admin, menu_kasir
from Auth import login

def main ():
    role = None
    while role is None:
        role = login()

    if role == 'admin':
        main_menu_admin()
    else:
        menu_kasir()


if __name__ == "__main__":
    main()