# KONSTRUKSI DASAR PYTHON
# SEQUENTIAL : EKSEKUSI BERURUTAN
print("Hello World!")
print("by Richki")
print("Tanggal 16 Juni 2020")
print("-" * 10)


#PERCABANGAN
ingin_cepat = False
if ingin_cepat:
    print('jalan lurus aja ya!')
else:
    print('muter muter aja dulu')


#PERCABANGAN PILIHAN LEBIH DARI 2
jumlah_anak = 10

for index_anak in range (1, jumlah_anak+1):
    print(f'halo anak {index_anak}')