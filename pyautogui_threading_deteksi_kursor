import threading
import time
import pyautogui as py

def my_loop():
    global is_running
    while is_running:
        a = py.position()
        print(a)
        

def stop_loop():
    global is_running
    is_running = False

def main():
    # waktunya
    threshold = 4

    global is_running
    is_running = True

    # Membuat thread untuk menjalankan loop
    thread = threading.Thread(target=my_loop)

    # Menjalankan thread loop
    thread.start()

    # Membuat timer untuk menghentikan loop setelah waktu tertentu
    timer = threading.Timer(threshold, stop_loop)
    timer.start()

    # Menunggu thread loop selesai
    thread.join()

if __name__ == '__main__':
    main()
