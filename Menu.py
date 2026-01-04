from Database import barang,cart,lihat_data,laporan_penjualan
from New_fitur import tambah_produk,hapus_produk,Update_stok,Laporan_bulanan,Grafik_penjualan

def main_menu_admin():
    while True:
        print("""
        ==== KASIR MINI | ADMIN ====
        1. Lihat menu
        2. Pilih menu
        3. Keranjang Menu
        4. Tambah Produk
        5. Hapus Produk
        6. Update Stok/Harga
        7. Laporan penjualan harian
        8. Laporan penjualan Bulanan
        9. Grafik penjualan Harian/Bulanan
        10. Exit
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

        elif user == '7':
            laporan_penjualan()

        elif user == '8':
            Laporan_bulanan()

        elif user == '9':
            Grafik_penjualan()
        
        elif user == '10':
            break

def menu_kasir():
    while True:
        print("""
        ==== KASIR MINI | KASIR ====
        1. Lihat Menu
        2. Pilih Menu
        3. Keranjang Menu
        0. logout
        """)

        user = input('pilih menu = ')

        if user == '1':
            lihat_data()
        elif user == '2':
            barang()
        elif user == '3':
            cart()
        elif user == '0':
            break

#Validasi input
def input_angka (pesan):
    #Menerima input angka integer
    while True:
        nilai = input(pesan)
        try:
            return int(nilai)
        except ValueError:
            print("Input harus berupa angka!")


def input_yn (pesan):
    #Menerima input Y / N (case insensitive).
    while True:
        jawab = input(pesan).lower()
        if jawab in ['y','n']:
            return jawab
        print('Pilihan harus (y/n)!')

def input_menu(jumlah_menu, pesan="Pilih menu: "):
     #"""Validasi input menu berdasarkan jumlah pilihan."""
        while True:
            nilai = input(pesan)
            if nilai.isdigit():
                nilai = int(nilai)
                if 1 <= nilai <= jumlah_menu:
                    return nilai
            print(f"Pilihan menu harus angka antara 1 - {jumlah_menu}")