The script uses the pynput library, which allows monitoring and controlling input devices like keyboards and mice in Python.
It defines two functions, on_press() and on_release(), which will be called when a key is pressed and released, respectively.
In the on_press() function, it logs the pressed key to a file named "keylog.txt". If the key is a special key (like Enter, Backspace, etc.), it logs the name of the key instead of its character representation.
The on_release() function is triggered when the Escape key (Key.esc) is released, terminating the keylogging process.
The Listener object is created with the defined callback functions (on_press and on_release), and it starts capturing keyboard events.
The script runs indefinitely until the Escape key is pressed.
