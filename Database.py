import pandas as pd


# Database utama
df = pd.DataFrame({
    'Produk': ['Nasi goreng', 'Ayam bakar', 'Ayam goreng', 'Soto', 'Bakso', 'Es teh'],
    'Harga' : [15000,20000,20000,15000,5000,5000],
    'Kode'  : [222,114,212,220,120,555],
    'Stok'  : [20,33,12,5,10,12]
})



#Fitur mencari produk
def cari_produk(kode):
       data = df[df['Kode'] == kode]
       if data.empty :
            return None
       return data.iloc[0]





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
    
    total = item['Harga'] * jumlah
    kembalian = uang - total


    #pengurangan stok
    cari_barang = df[df['Kode'] == user].index[0]
    stok_Lama =  df.loc[cari_barang,'Stok']

    #Pengecekan stok
    if jumlah > stok_Lama:
      print('Stok tidak cukup')

    stok_Baru = stok_Lama - jumlah
    df.loc[cari_barang,'Stok'] = stok_Baru




    print(f'Anda memilih {item["Produk"]}, jumlah {jumlah}')
    print(f'Total yang harus dibayar = Rp {total}')

    if kembalian > 0:
        print(f'Kembalian anda adalah {kembalian}')
    else:
         print('uang anda kurang')

      



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

        
#fitur menu
def lihat_data ():
     print(df)
