import pandas as pd


# Database utama
df = pd.DataFrame({
    'Produk': ['Nasi goreng', 'Ayam bakar', 'Ayam goreng', 'Soto', 'Nasi', 'Es teh'],
    'Harga' : [15000,20000,20000,15000,5000,5000],
    'Kode'  : [222,114,212,220,120,555]
})

cart = {'barang': [],
        'jumlah': []}

#Fitur pemilihan barang
def barang ():
    global df
    while True:
        print(df)
        user = int(input('tuliskan barang yang ingin anda beli dg kode produk: '))
        jumlah = int(input('Tuliskan berapa jumlah barang yang ingin anda beli: '))

        if user == 222:
            print(f'anda memilih produk {df['Produk'][0]}, dengan jumlah : {jumlah}')
            total = df['Harga'][0] * jumlah
            print(f'Total pembayaran anda adalah = {total}')
        

print(barang())