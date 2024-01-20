import win32gui
import win32api

def get_cursor_position_in_window(window_handle):
    win_rect = win32gui.GetWindowRect(window_handle)
    x, y = win32gui.GetCursorPos()
    return x - win_rect[0], y - win_rect[1]

# Contoh penggunaan
notepad_handle = win32gui.FindWindow(None, "Calculator")
if notepad_handle:
    print(f"Window dengan judul 'Untitled - Notepad' ditemukan.")
    while True:
        cursor_x, cursor_y = get_cursor_position_in_window(notepad_handle)
        print(f"Kursor di dalam jendela Notepad. Koordinat: x={cursor_x}, y={cursor_y}")
        #print(f"Kursor di dalam jendela Notepad. Koordinat: x={cursor_x-50}, y={cursor_y-100}")
else:
    print("Notepad tidak ditemukan.")
