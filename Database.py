import pandas as pd
import os

# Database utama
df = pd.DataFrame({
    'Produk': ['Nasi goreng', 'Ayam bakar', 'Ayam goreng', 'Soto', 'Bakso', 'Es teh'],
    'Harga' : [15000,20000,20000,15000,5000,5000],
    'Kode'  : [222,114,212,220,120,555],
    'Stok'  : [20,33,12,5,10,12]
})

#fitur save data
if os.path.exists("database_stok.csv"):
    df = pd.read_csv("database_stok.csv")
else:
    df.to_csv("database_stok.csv", index=False)



#Fitur mencari produk
def cari_produk(kode):
       data = df[df['Kode'] == kode]
       if data.empty :
            return None
       return data.iloc[0]

# Fitur Total penjualan
Data_Penjualan = []
def laporan_penjualan ():

    if len (Data_Penjualan) == 0:
        print('Belum ada transaksi')
        return 
    else:
        print("\n===== LAPORAN PENJUALAN HARI INI =====")
        total_semua = sum(Data_Penjualan)
        jumlah_transaksi = len(Data_Penjualan)
        rata_rata = total_semua/jumlah_transaksi
        print(f'total semua penjualan hari ini adalaha = {total_semua}')
        print(f'jumlah transaksi hari ini adalah = {jumlah_transaksi}')
        print(f'rata-rata transaksi hari ini adalah = {rata_rata}')
        for i, trx in enumerate(Data_Penjualan,start=1):
            print(f'{i}.Rp {trx}')

        user = input('Apakah anda ingin laporan ini di export ke file.txt (y/n): ')
        if user.lower() == 'y':
            export_laporan()
            return

#fitur export laporan            
def export_laporan():
    file = open('Laporan_penjualan.txt','w')
    file.write("\n===== LAPORAN PENJUALAN HARI INI =====")
    total_semua = sum(Data_Penjualan)
    jumlah_transaksi = len(Data_Penjualan)
    rata_rata = total_semua/jumlah_transaksi
    file.write(f'total semua penjualan hari ini adalah = {total_semua}\n')
    file.write(f'jumlah transaksi hari ini adalah = {jumlah_transaksi}\n')
    file.write(f'rata-rata transaksi hari ini adalah = {rata_rata}\n')
    for i, trx in enumerate(Data_Penjualan,start=1):
        file.write(f'{i}.Rp {trx}\n')
    file.close()
    print('File berhasil di Exspor ke laporan_penjualan.txt')
       

#Fitur pemilihan barang
def barang ():
    global df

    print(df)
    user = int(input('Tuliskan barang yang ingin anda beli dg kode produk: '))
    jumlah = int(input('Tuliskan berapa jumlah barang yang ingin anda beli: '))
    uang = int(input('Masukan jumlah uang anda: '))
    item = cari_produk(user)


    if item is None:
          print('Kode tidak valid')
          return
    
    #Pengecekan stok
    stok = df[df['Kode'] == user].iloc[0]['Stok']
    if jumlah > stok:
      print('Stok tidak cukup')
      return
    
    total = item['Harga'] * jumlah
    kembalian = uang - total
    
    #pengecekan uang
    if kembalian < 0:
        print("Uang anad kurang, transaksi dibatalkan")
        return

    #pengurangan stok
    cari_barang = df[df['Kode'] == user].index[0]
    stok_Lama =  df.loc[cari_barang,'Stok']


    #kurangi stok
    stok_Baru = stok_Lama - jumlah
    df.loc[cari_barang,'Stok'] = stok_Baru




    print(f'Anda memilih {item["Produk"]}, jumlah {jumlah}')
    print(f'Total yang harus dibayar = Rp {total}')

    if kembalian > 0:
        print(f'Kembalian anda adalah {kembalian}')
    else:
         print('uang anda kurang')
    
    #simpan ke data penjualan
    Data_Penjualan.append(total)

    #simpan ke csv
    df.to_csv("database_stok.csv", index=False)


      



# fitur cart 
def cart():
    global df
    cart = []
    print(df)

    while True:
        user = int(input('Tuliskan Kode barang ke keranjang : '))
        jumlah = int(input('Tuliskan jumlah barang yang ingin anda beli: '))
        item = cari_produk(user)

        if item is None:
            print('Kode tidak valid')
            continue

        # cek stok
        stok = df[df['Kode'] == user].iloc[0]['Stok']
        if jumlah > stok:
            print("Stok tidak cukup")
            continue

        cart.append({
            'produk': item['Produk'],
            'Kode'  : user,
            'jumlah': jumlah,
            'harga' : item['Harga'],
            'total' : jumlah * item['Harga']
        })

        selesai = input('Sudah selesai belanja? (y/n): ')
        if selesai.lower() == 'y':
            break

    # hitung total belanja
    total_semua = sum(x['total'] for x in cart)
    print("Total semua belanja =", total_semua)

    # pembayaran
    uang = int(input("Masukan jumlah uang anda: "))
    kembalian = uang - total_semua
    if kembalian < 0:
        print('Uang anda kurang')
        return

    print(f'kembalian anda adalah = {kembalian}')

    # Simpan ke data penjualan
    Data_Penjualan.append(total_semua)

    # pengurangan stok setelah bayar
    for barang in cart:
        kode = barang['Kode']
        jumlah = barang['jumlah']
        baris_df = df[df['Kode'] == kode].index[0]
        df.loc[baris_df, 'Stok'] = df.loc[baris_df, 'Stok'] - jumlah

    # tampilkan keranjang
    print("\n===== Keranjang Belanja =====")
    for data in cart:
        print(data)

    #simpan ke csv
    df.to_csv("database_stok.csv", index=False)


        
#fitur menu
def lihat_data ():
     global df
     df=pd.read_csv('database_stok.csv')
     print(df)
