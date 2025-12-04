from Database import df,Data_Penjualan
import pandas as pd


# Fitur Tambah produk
def tambah_produk ():
    global df
    print('Daftar barang sekarang')
    print(df)

    nama_produk = input('Masukan nama produk: ')
    harga       = int(input('Masukan harga produk: '))
    Kode        = int(input('Masukan kode produk: '))
    stok        = int(input('Masukan stok produk: '))

    if Kode in df['Kode'].values:
        print('Kode sudah ada, Pakai Kode yang lain')
        return
    
    # Tambahkan data
    df.loc[len(df)] = [nama_produk,harga,Kode,stok]
    print('Produk berhasil ditambahkan')
    print(df)

    #simpan ke csv
    df.to_csv("database_stok.csv", index=False)


# fitur hapus produk
def hapus_produk():
    global df
    print('Daftar Produk')
    print(df)

    user = int(input('Masukan kode produk yang ingin dihilangkan: '))
    konfirmasi = input("Yakin ingin menghapus produk ini? (y/n)")
    if konfirmasi.lower() != 'y':
        print('Dibatalkan')
        return

    if user in df['Kode'].values:
        df = df[df['Kode'] != user].reset_index(drop=True)
        print("Produk berhasil dihapus")
        print(df)
    else:
        print('ERROR Kode tidak ada')

    #simpan ke csv
    df.to_csv("database_stok.csv", index=False)

#Fitur update Stok
def Update_stok():
    global df
    print('Stok produk Saat ini') 
    print(df)

    user = int(input('Masukan Kode Produk yang ingin di update: '))
    
    # Cek Kode Produk dan update
    if user in df['Kode'].values:
        print('Check kode berhasil')
        option = input("Mau update apa (Stok/Harga)")

        #Update Stok
        if option.lower() == 'stok':
            user1 = int(input('Tuliskan stok yang baru: ')) 

            #Konfirmasi
            konfirmasi = input("Yakin ingin Update produk ini? (y/n)")
            if konfirmasi.lower() != 'y':
                print('Dibatalkan')
                return
            
            df.loc[df['Kode'] == user,'Stok'] = user1
            print('Data Stok telah diperbarui')

        #Update Harga
        elif option.lower() == 'harga':
            user2 = int(input("Masukan harga yang baru"))

            #Konfirmasi
            konfirmasi = input("Yakin ingin menghapus produk ini? (y/n)")
            if konfirmasi.lower() != 'y':
                print('Dibatalkan')
                return

            df.loc[df['Kode'] == user, 'Harga'] = user2
            print('Data Harga telah diperbarui')
        else:
            print('Pilihan tidak ditemukan')

    else:
        print("Kode tidak ditemukan")

    #simpan ke csv
    df.to_csv("database_stok.csv", index=False)

    
def Laporan_bulanan():
    global Data_Penjualan

    
    if len(Data_Penjualan) == 0:
        print("Belum ada data penjualan, laporan bulanan tidak bisa dibuat.")
        return

    df = pd.DataFrame(Data_Penjualan)
    user = input('masukan tahun dan bulan (YYYY-MM) : ')


    #filter berdasarkan bulan dan tahun
    df['tanggal'] = pd.to_datetime(df['tanggal'])
    bulan = pd.Period(user,freq='M')
    df_filter = df[df['tanggal'].dt.to_period('M') == bulan]
    


    #Filter data
    if len(df_filter) > 0 :
        print(f'Bulan = {user}')
        print("========= Total Penjualan Bulan Ini =========")
        print(f"Total transakasi = {df_filter['total'].sum()}")
        print(f'Jumlah transaksi = {len(df_filter)}')
        print(f"Rata-rata transaksi = {df_filter['total'].mean():.2f}")
       
    else:
        print("belum ada transaksi bulan ini")
        return
    
    user1 = input('Apakah mau ke file bulanan (y/n):')
    if user1.lower() == 'y':
        file = open("Laporan_Penjualan_Bulanan.txt",'w')

        file.write("========= Total Penjualan Bulan Ini =========\n")
        file.write(f"Total transakasi = {df_filter['total'].sum()}\n")
        file.write(f'Jumlah transaksi = {len(df_filter)}\n')
        file.write(f"Rata-rata transaksi = {df_filter['total'].mean():.2f}\n")
        file.close()
        print("File Berhasil disimpan")




