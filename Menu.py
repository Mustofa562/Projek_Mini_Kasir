from Database import barang,cart,lihat_data
from New_fitur import tambah_produk,hapus_produk,Update_stok

while True:
    print("""
    Kasir mini
    1. Lihat menu
    2. Pilih menu
    3. Keranjang Menu
    4. Tambah Produk
    5. Hapus Produk
    6. Update Stok/Harga
    """)

    user = input('Pilih salah satu menu : ')

    if user == '1':
        lihat_data()

    elif user == '2':
        barang()

    elif user == '3':
        cart()

    elif user == '4':
        tambah_produk()

    elif user == '5':
        hapus_produk()

    elif user == '6':
        Update_stok()
