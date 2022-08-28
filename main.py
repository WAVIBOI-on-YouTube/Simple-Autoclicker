import time
import threading
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode

print("Hello! Press ` on your keyboard to the Autoclicker on or off. You can close this app by clicking K.")
print("Note: Only use in games which allow Autoclicker or singleplayer games.")
print("Made by W A V I B O I.")

delay = 0.00000000000001
button = Button.left
start_stop_key = KeyCode(char='`')
exit_key = KeyCode(char='k')


class ClickMouse(threading.Thread):
    def __init__(self, delay, button):
        super(ClickMouse, self).__init__()
        self.delay = delay
        self.button = button
        self.running = False
        self.program_run = True

    def start_clicking(self):
        self.running = True

    def stop_clicking(self):
        self.running = False

    def exit(self):
        self.stop_clicking()
        self.program_run = False

    def run(self):
        while self.program_run:
            while self.running:
                mouse.click(self.button)
                time.sleep(self.delay)
            time.sleep(1)


mouse = Controller()
thread = ClickMouse(delay, button)
thread.start()


def on_press(key):
    if key == start_stop_key:
        if thread.running:
            thread.stop_clicking()
        else:
            thread.start_clicking()
    elif key == exit_key:
        thread.exit()
        listener.stop()


with Listener(on_press=on_press) as listener:
    listener.join()
