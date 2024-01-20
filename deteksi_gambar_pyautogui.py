import pyautogui

# Path gambar
image_path = "C:/Users/user/Desktop/gambar.png"

while 1:
    # Menentukan tingkat kemungkinan (confidence)
    confidence_level = 0.8

    # Mencari posisi gambar pada layar
    location = pyautogui.locateOnScreen(image_path, confidence=confidence_level)

    if location:
        print(f"Gambar ditemukan di posisi {location}")
    else:
        print("Gambar tidak ditemukan.")
