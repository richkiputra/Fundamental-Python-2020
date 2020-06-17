"""
 Tipe data dictionary sekedar menghubungkan antara KEY dan VALUE
 KVP = Key Value Pair
 Dictionary = kamus
"""

kamus = {'anak': 'son', 'istri': 'wife', 'ayah': 'father', 'ibu': 'mother'}

print(kamus)
print(kamus['ayah'])

print('Data ini dikirimkan oleh server gojek untuk memberikan info driver di sekitar user')
data_dari_server_gojek = {
    'tanggal': '2020-06-10',
    'driver_list': [{'nama': 'Richki', 'jarak': 10},
                    {'nama': 'Tachi', 'jarak': 15},
                    {'nama': 'Jojo', 'jarak': 22},
                    {'nama': 'Jeje', 'jarak': 30}
    ]

}

print(data_dari_server_gojek)
print(f"Driver disekitas sini {data_dari_server_gojek['driver_list']}")
print(f"Driver #1 disekitas sini {data_dari_server_gojek['driver_list'][0]}")
