print('praktikum-b5')

nim=[2,3,1,0,3,1,0,4,0]
print(nim)
#akses item
print('item indeks 0:',nim[0])
print('item indeks 3:',nim[3])
print('item indeks terakhir:',nim[len(nim)-1])
#akses indeks negatif
print('item indeks terakhir:',nim[len(nim)-1])
print('item indeks pertama:',nim[-len(nim)])
print('itm indeks 3:[-6]',nim[-6])
print('itm indeks 5:[-4]',nim[-4])
print('itm indeks -7:[2]',nim[2])
print('itm indeks 2:[-7]',nim[-7])                 
#akses indeks Batas
print(f'item indeks 1,2....:{nim[1:]}')
print(f'item indeks 3,4....:{nim[3:]}')
print(f'item indeks 0,1,2,3:{nim[:4]}')
print(f'item indeks 0:{nim[:1]}')
print(f'item indeks semua:{nim[:]}')
print(f'item indeks[:8]:{nim[:-1]}')
print(f'item indeks[:4]:{nim[:-5]}')
#pengirisan
print(f'item indeks 1,2 {nim[1:3]}')
print(f'item indeks[]:{nim[3:3]}')
print(f'item indeks 2,3,4 {nim[2:5]}')
print(f'item indeks [1:8]]: {nim[1:-1]}')
print(f'item indeks [2:7]]: {nim[2:-2]}')
#nested list
kelas=[('cinta',2),
       ('kalkulus',3)]
kelas.append(('pti',2))
kelas.append(('pancasila',3))
kelas.append(('islam',3))
#tambahan matkul 4 dan 5 dan sks nya
print('tugas 1')
#mata kuliah 1:matkul 1 dengan 2 sks
print(f'mata kuliah 1: {kelas[0][0]} dengan {kelas[0][1]} sks')
#mata kuliah 2:matkul 2 dengan 3 sks
print(f'mata kuliah 2: {kelas[1][0]} dengan {kelas[1][1]} sks')
#mata kuliah 3:matkul 3 dengan 2 sks
print(f'mata kuliah 3: {kelas[2][0]} dengan {kelas[2][1]} sks')
#mata kuliah 4:matkul 4 dengan 3 sks
print(f'mata kuliah 4: {kelas[3][0]} dengan {kelas[3][1]} sks')
#mata kuliah 5:matkul 5 dengan 3 sks
print(f'mata kuliah 5: {kelas[4][0]} dengan {kelas[4][1]} sks')

print()
print('tugas 2')
data=[('awal',2023,'aktif'),
      (76,98,89,97,99),
      [2,3,2,3,3],
      ('s1-reguler','sistem informasi B','ganjil')]

#nama mahasiswa:awal
print(f'nama mahasiswa : {data[0][0]}')
#inisial awal:a
print(f'inisial awal : {data[0][0][0]}')
#nim awal:231031040
nim_int=int(''.join(map(str, nim)))
print(f'nim {data[0][0]} : {nim_int}')
#program awal :s1-reguler sistem informasi B
print(f'program {data[0][0]} : {data[3][0]} {data[3][1]}')
#angkatan awal:ganjil-2023
print(f'angkatan {data[0][0]} : {data[3][2]}-{data[0][1]}')
#total sks awal adalah:5
print(f'total sks {data[0][0]} adalah : {sum(data[2])}')
#jumlah nilai awal:5
print(f'jumlah nilai {data[0][0]} adalah : {len(data[2])}')
#nilai tertinggi awal:99
print(f'nilai tertinggi {data[0][0]} adalah : {max(data[1])}')
#nilai terendah awal:76
print(f'nilai terendah {data[0][0]} adalah : {min(data[1])}')
#rata-rata nilai awal:91.8
rata=sum(data[1]) / len(data[1])
print(f'rata rata nilai {data[0][0]} adalah : {rata}')      
