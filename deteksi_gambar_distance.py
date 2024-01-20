import pyautogui
import math

def cari_gambar(template_path):
    try:
        # Mencari koordinat gambar pada layar
        lokasi = pyautogui.locateOnScreen(template_path)

        if lokasi is not None:
            # Mendapatkan pusat koordinat gambar
            pusat_koordinat = pyautogui.center(lokasi)
            x, y = pusat_koordinat
            #print(f"Gambar ditemukan pada koordinat: X={x}, Y={y}")

            # Mendapatkan koordinat kursor saat ini
            kursor_x, kursor_y = pyautogui.position()

            # Menghitung jarak antara kursor dan koordinat gambar
            jarak = math.sqrt((x - kursor_x)**2 + (y - kursor_y)**2)
            if jarak < 20:
                print("Anda berada di target")
            else:
                print(f"Jarak antara kursor dan gambar: {jarak:.0f} piksel")
        else:
            print("Gambar tidak ditemukan di layar.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

if __name__ == "__main__":
    # Gantilah 'path/to/template.png' dengan path gambar yang ingin Anda cari
    template_path = 'Desktop/gambar.png'
    while True:
        cari_gambar(template_path)
