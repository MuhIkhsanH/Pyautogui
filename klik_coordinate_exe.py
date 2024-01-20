import win32gui
import win32api
import win32con
import time
import pyautogui

def get_window_rect(window_handle):
    return win32gui.GetWindowRect(window_handle)

def click_at_position_in_window(window_handle, x, y):
    client_rect = win32gui.GetClientRect(window_handle)
    win_rect = get_window_rect(window_handle)
    adjusted_x = int(x * (win_rect[2] - win_rect[0]) / client_rect[2])
    adjusted_y = int(y * (win_rect[3] - win_rect[1]) / client_rect[3])
    
    # Transformasi koordinat dari koordinat jendela ke koordinat layar
    screen_x = win_rect[0] + adjusted_x
    screen_y = win_rect[1] + adjusted_y

    # Melakukan klik di layar menggunakan pyautogui
    pyautogui.click(x=screen_x, y=screen_y)

# Contoh penggunaan
calculator_handle = win32gui.FindWindow(None, "Calculator")
if calculator_handle:
    print(f"Window dengan judul 'Calculator' ditemukan.")
    while True:
        click_at_position_in_window(calculator_handle, 221, 437)
        print("Melakukan klik pada koordinat (221, 437) di dalam jendela Calculator.")
        time.sleep(5)  # Melakukan klik setiap 5 detik

else:
    print("Calculator tidak ditemukan.")
