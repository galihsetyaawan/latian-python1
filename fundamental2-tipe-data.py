
#tipe data skalar -> tipe data sederhana
anak1 = 'Eko'
anak2 = 'Dwi'
anak3 = 'Tri'
anak4 = 'Catur'

print(anak1)
print(anak2)
print(anak3)
print(anak4)

#tipe data list/array
anak = ['Eko','Dwi','Tri','Catur']
print(anak)
anak.append('Panca')
print(anak)

print('\nsapa anak kedua')
print(f'Hai {anak[1]}!')

print('\nsapa semuanya')

for d in anak:
    print(f'Hai {d}!')

print('\nsapa semuanya : cara ribet')

for a in range  (0,len(anak)):
    print(f'{a+1}.hai {anak[a]}')