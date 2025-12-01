from Database import df


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
        df.loc[df['Kode'] != user].reset_index(drop=True)
        print("Produk berhasil dihapus")
        print(df)
    else:
        print('ERROR Kode tidak ada')

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

    

