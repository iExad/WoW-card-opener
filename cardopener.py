import win32api
import win32con
import random
import time
import msvcrt

go = True

while True:
    if msvcrt.kbhit():
        print("Pause", go)
        msvcrt.getch()
        go = not go

    if go:
        pong = random.random() * 0.9
        ping = random.randint(1, 1)
        tennis = ping * pong
        print("Card opened...", tennis, 'sec'), time.asctime()
        win32api.keybd_event(win32con.VK_F3, 0, 0, 0)
        win32api.keybd_event(win32con.VK_F3, 0, win32con.KEYEVENTF_KEYUP, 0)
        time.sleep(tennis)
