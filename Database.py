import pandas as pd


# Database utama
df = pd.DataFrame({
    'Produk': ['Nasi goreng', 'Ayam bakar', 'Ayam goreng', 'Soto', 'Bakso', 'Es teh'],
    'Harga' : [15000,20000,20000,15000,5000,5000],
    'Kode'  : [222,114,212,220,120,555]
})

#Fitur mencari produk
def cari_produk(kode):
       data = df[df['Kode'] == kode]
       if data.empty :
              return None
       return data.iloc[0]

#fitur menu
def lihat_data ():
     print(df)



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

    print(f'Anda memilih {item["Produk"]}, jumlah {jumlah}')
    print(f'Total yang harus dibayar = Rp {total}')

    if kembalian > 0:
        print(f'Kembalian anda adalah {kembalian}')
    else:
         print('uang anda kurang')



# fitur cart 
def cart ():
    global df
    cart = []
    print(df)
    while True:
        user = int(input('Tuliskan Kode barang ke keranjang : '))
        jumlah = int(input('Tuliskan jumlah barang yang ingin anda beli: '))
        item = cari_produk(user)



        if item == None:
              print('Kode tidak valid')
              continue

        cart.append({
                'produk': item['Produk'],
                'jumlah': jumlah,
                'harga' : item['Harga'],
                'total' : jumlah * item['Harga']
        })

        selesai = input('sudah selesai belanja(y/n)')
        if selesai == 'y':
               break

        uang = int(input("Masukan jumlah uang anda: "))
        kembalian = uang - cart['total']
        if kembalian < 0:
             print('Uang anda kurang')

        print("\n===== Keranjang Belanja =====")
    for data in cart:
        print(data)
    print("Total semua:", sum(x['Total'] for x in cart))
    print(f"Kembalian anda adalah = {kembalian} ")
