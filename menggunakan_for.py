# inisialisasi nilai
n = int(input('Masukkan nilai n: '))
faktorial = 1

# melakukan perulangan
for i in range(1, n + 1):
  faktorial *= i

# melakukan cetak hasil faktorial
print(f'{n}! = {faktorial}')