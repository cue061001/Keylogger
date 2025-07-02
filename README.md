

# 🕵️‍♂️ Keylogger & System Monitor Tool
> ⚠️ Disclaimer : This tool is for educational and ethical purposes only. Unauthorized monitoring or surveillance is illegal and unethical. Always ensure you have proper authorization before using such tools. 

This Python-based script acts as a multi-functional system monitor , logging keystrokes, clipboard data, screenshots, audio recordings, and basic system information. It's built using various libraries like pynput, PIL, sounddevice, and more.

## 🔧 Features
1. ✅ Keylogging – Logs every key pressed by the user.
2. ✅ Clipboard Monitoring – Captures copied text from the clipboard.
3. ✅ Screenshot Capture – Takes a screenshot of the entire screen.
4. ✅ Audio Recording – Records ambient microphone input (configurable time).
5. ✅ System Info Logging – Gathers system details like IP, OS, Processor, etc.

## 🛠️ How It Works
The script uses the following libraries:

- pynput.keyboard – For capturing keyboard events
- win32clipboard – To access and copy clipboard contents
- PIL.ImageGrab – To take screenshots
- sounddevice + scipy.io.wavfile – For audio recording
- platform, socket, datetime – For system and time-related data
- All output files are saved in a specified directory (file_path) on the local machine.

## ⏱️ Configurable Options
You can tweak these settings at the top of the script:

- microphone_time – Duration of audio recording (in seconds)
- time_iteration – Time between iterations (not used in current version)
- number_of_iterations_end – Total number of runs before exit
- file_path – Directory where logs will be stored
  
## ⚠️ Legal & Ethical Use
This tool should only be used:

- On your own systems for learning and testing
- With full consent from the system owner
- In controlled environments like penetration testing labs or forensics analysis
- Unauthorized use is strictly prohibited and may violate privacy laws.
