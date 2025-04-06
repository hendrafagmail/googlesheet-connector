try:
    # Membuat kredensial dari file JSON
    creds = Credentials.from_service_account_file(creds_file, scopes=scope)

    # Mengotorisasi gspread dengan kredensial
    gc = gspread.authorize(creds)

    # ID Google Sheet Anda
    spreadsheet_id = '1YPv4cOu2lSOWcMJhU3bw2P08HvEoUAoAc2jVVWlc0II'  # Ganti dengan ID spreadsheet Anda

    # Membuka spreadsheet berdasarkan ID
    spreadsheet = gc.open_by_key(spreadsheet_id)

    # Memilih worksheet (sheet pertama secara default)
    worksheet = spreadsheet.sheet1
    # Atau, jika Anda ingin memilih berdasarkan nama:
    # worksheet = spreadsheet.worksheet('Nama Sheet Anda')

    # --- Contoh: Membaca Data dari Sheet ---
    print("--- Membaca Data ---")
    # Mendapatkan semua nilai dalam bentuk list of lists
    all_data = worksheet.get_all_values()
    if all_data:
        print("Seluruh data:")
        for row in all_data:
            print(row)
    else:
        print("Sheet kosong.")

    # Mendapatkan nilai dari sel tertentu (baris, kolom) - indeks dimulai dari 1
    try:
        cell_value = worksheet.acell('A1').value
        print(f"\nNilai sel A1: {cell_value}")
    except gspread.exceptions.CellNotFound:
        print("\nSel A1 tidak ditemukan.")

    # Mendapatkan nilai dari rentang sel
    try:
        range_values = worksheet.get('A1:B2')
        print(f"\nNilai rentang A1:B2: {range_values}")
    except gspread.exceptions.GSpreadException as e:
        print(f"\nTerjadi kesalahan saat membaca rentang: {e}")

    # --- Contoh: Menulis Data ke Sheet ---
    print("\n--- Menulis Data ---")
    # Menulis satu nilai ke sel tertentu (baris, kolom) - indeks dimulai dari 1
    try:
        worksheet.update_cell(3, 1, 'Data Baru')  # Menulis 'Data Baru' ke baris 3, kolom 1 (A3)
        print("Berhasil menulis 'Data Baru' ke sel A3.")
    except gspread.exceptions.GSpreadException as e:
        print(f"Terjadi kesalahan saat menulis ke sel: {e}")

    # Menulis list ke baris tertentu (akan menimpa data yang ada)
    try:
        new_row_data = ['Nilai 1', 'Nilai 2', 'Nilai 3']
        worksheet.update('A4', [new_row_data])  # Menulis ke baris 4, mulai dari kolom A
        print(f"Berhasil menulis baris baru: {new_row_data} ke baris 4.")
    except gspread.exceptions.GSpreadException as e:
        print(f"Terjadi kesalahan saat menulis baris: {e}")

    # Menambahkan baris baru di akhir sheet
    try:
        another_new_row = ['Data Tambahan 1', 'Data Tambahan 2']
        worksheet.append_row(another_new_row)
        print(f"Berhasil menambahkan baris baru di akhir: {another_new_row}")
    except gspread.exceptions.GSpreadException as e:
        print(f"Terjadi kesalahan saat menambahkan baris: {e}")

    print("\nScript selesai.")

except FileNotFoundError:
    print(f"Error: File kredensial '{creds_file}' tidak ditemukan.")
except Exception as e:
    print(f"Terjadi kesalahan: {e}")
