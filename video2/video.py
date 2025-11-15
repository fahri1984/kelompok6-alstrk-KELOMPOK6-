print("=== KALKULATOR SEDERHANA ===")
print("1. Penjumlahan (+)")
print("2. Pengurangan (-)")
print("3. Perkalian (*)")
print("4. Pembagian (/)")

pilihan = input("Pilih operasi (1/2/3/4): ")

angka1 = float(input("Masukkan angka pertama: "))
angka2 = float(input("Masukkan angka kedua: "))

if pilihan == '1':
    hasil = angka1 + angka2
    print("Hasil penjumlahan:", hasil)

elif pilihan == '2':
    hasil = angka1 - angka2
    print("Hasil pengurangan:", hasil)

elif pilihan == '3':
    hasil = angka1 * angka2
    print("Hasil perkalian:", hasil)

elif pilihan == '4':
    if angka2 != 0:
        hasil = angka1 / angka2
        print("Hasil pembagian:", hasil)
    else:
        print("Error: Tidak bisa membagi dengan nol!")
else:
    print("Pilihan tidak valid!")
