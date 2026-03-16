print("=== Buku Tamu ===")
print("Ketik 'selesai' untuk berhenti dan menyimpan.\n")

names = []

while True:
    try:
        name = input("Masukkan nama tamu: ")

        if name.lower() == "selesai":
            break

        if not name.strip():
            raise ValueError("Nama tidak boleh kosong.")

        if any(char.isdigit() for char in name):
            raise ValueError("Nama tidak boleh mengandung angka.")

        names.append(name)
        print(f"  -> '{name}' berhasil ditambahkan.\n")

    except ValueError as e:
        print(f"  [!] Input tidak valid: {e} Silakan coba lagi.\n")

if names:
    with open("guest_book.txt", "w") as file:
        for name in names:
            file.write(name + "\n")
    print(f"\n{len(names)} nama berhasil disimpan ke guest_book.txt.")
else:
    print("\nTidak ada nama yang dimasukkan. File tidak dibuat.")
