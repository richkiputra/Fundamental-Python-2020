#tipe data skalar

anak1 = 'Richki'
anak2 = 'Tachi'
anak3 = 'Jojo'
anak4 = 'Jeje'

print(anak1)
print(anak2)
print(anak3)
print(anak4)

# tipe data list/daftar/array

anak = ['Richki', 'Tachi', 'Jojo', 'Jeje']
print(anak)
anak.append('Syerin')
print(anak)

# sapa anak ke -2
print(f'Hai {anak[1]}!')

for a in anak:
    print(f'Hai {a}!')

for a in range(0, len(anak)):
    print(f'\n {a+1} Hai {anak[a]}')
