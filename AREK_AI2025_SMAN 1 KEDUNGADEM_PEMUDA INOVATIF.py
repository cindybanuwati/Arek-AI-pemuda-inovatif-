def hitung_nilai(h, uts, uas):
    return (0.4*h) + (0.3*uts) + (0.3*uas)

print("=== Penilaian Akhir Semester ===")

nilai_h = float(input("Nilai latihan/harian : "))
nilai_tengah = float(input("Nilai UTS: "))
nilai_akhir = float(input("Nilai UAS: "))

skor = hitung_nilai(nilai_h, nilai_tengah, nilai_akhir)

print("\nNilai akhir yang diperoleh =", format(skor, ".2f"))

# Penentuan status
if skor >= 75:
    print("Status kelulusan = LULUS")
    print("Selamat! Anda lulus 🎉")
else:
    print("Status kelulusan = TIDAK LULUS")
    print("Mohon maaf, anda belum lulus. Silakan mengikuti remedial.")