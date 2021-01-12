
#Tipe data dictionary sekedar menghubungkan antara KEY dan Value
# KVP = Key Value Pair
# dictionaRY = KAMUS

kamus = {}
kamus['anak'] = 'son'
kamus['istri'] = 'wife'
kamus['suami'] = 'husband'

print(kamus)
print(kamus['anak'])

print('\nData ini dikirimkan oleh server Gojek, utk memberikan info driver di sekitar user')

data_dari_server_gojek = {
    'tanggal' : '2021-01-01',
    'driver_list' : [
        {'nama':'eko','jarak':10},
        {'nama':'dwi','jarak':30},
        {'nama': 'tri','jarak': 50},
        {'nama': 'panca','jarak': 100}
    ]
}

print(data_dari_server_gojek )
print(f"Driver di sekitar sini : {data_dari_server_gojek['driver_list']}")
print(f"Driver pertama :{data_dari_server_gojek['driver_list'][0]}")
print(f"driver terjauh anda {data_dari_server_gojek['driver_list'][3]['jarak']}")