from Database import barang,cart,lihat_data

print("""
Kasir mini
1. Lihat menu
2. Pilih menu
3. Keranjang Menu
""")

user = input('Pilih salah satu menu : ')

if user == '1':
    lihat_data()

if user == '2':
    barang()

if user == '3':
    cart()
