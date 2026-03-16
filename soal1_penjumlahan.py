print("=== Program Penjumlahan Dua Angka ===\n")

try:
    angka1 = float(input("Masukkan angka pertama : "))
    angka2 = float(input("Masukkan angka kedua   : "))
    hasil = angka1 + angka2
    print(f"\nHasil: {angka1} + {angka2} = {hasil}")

except ValueError:
    print("\nOops! Input tidak valid. Pastikan Anda memasukkan angka, bukan teks.")
