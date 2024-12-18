# Fungsi untuk menghitung gaji
def hitung_gaji(jam_kerja, tarif_per_jam):
    if jam_kerja <= 40:
        # Jika jam kerja <= 40, tidak ada lembur
        gaji = jam_kerja * tarif_per_jam
    else:
        # Hitung gaji normal (40 jam pertama)
        gaji_normal = 40 * tarif_per_jam
        
        # Hitung lembur (jam kerja lebih dari 40)
        jam_lembur = jam_kerja - 40
        tarif_lembur = 1.5 * tarif_per_jam
        gaji_lembur = jam_lembur * tarif_lembur
        
        # Total gaji
        gaji = gaji_normal + gaji_lembur
    
    return gaji

# Program utama
try:
    # Input dari pengguna
    jam_kerja = float(input("Masukkan jumlah jam kerja dalam seminggu: "))
    tarif_per_jam = float(input("Masukkan tarif per jam: "))

    # Validasi input
    if jam_kerja < 0 or tarif_per_jam < 0:
        print("Jam kerja dan tarif per jam harus bernilai positif.")
    else:
        # Hitung gaji
        gaji_total = hitung_gaji(jam_kerja, tarif_per_jam)

        # Tampilkan hasil
        print(f"Gaji karyawan untuk {jam_kerja} jam kerja dengan tarif Rp {tarif_per_jam}/jam adalah: Rp {gaji_total:.2f}")
except ValueError:
    print("Harap masukkan angka yang valid untuk jam kerja dan tarif per jam.")
