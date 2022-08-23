import time
import threading
from pynput.mouse import Controller, Button
from pynput.keyboard import Listener, KeyCode

print("Hello! Press T on your keyboard to the Autoclicker on or off.")
print("Note: Only use in games which allow Autoclicker or singleplayer games.")
print("Made by W A V I B O I.")

TOGGLE_KEY = KeyCode(char="t")

clicking = False
mouse = Controller()


def clicker():
    while True:
        if clicking:
            mouse.click(Button.left, 1)
        time.sleep(0.000001)


def toggle_event(key):
    if key == TOGGLE_KEY:
        global clicking
        clicking = not clicking


click_thread = threading.Thread(target=clicker)
click_thread.start()

with Listener(on_press=toggle_event) as listener:
    listener.join()