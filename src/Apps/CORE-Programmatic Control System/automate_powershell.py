import pyautogui
import time

def open_powershell():
    pyautogui.press('winleft')
    pyautogui.write('PowerShell')
    pyautogui.press('enter')
    time.sleep(2)

def type_command(command):
    pyautogui.write(command)
    pyautogui.press('enter')

def run_command(command):
    open_powershell()
    time.sleep(2)
    type_command(command)

if __name__ == "__main__":
    run_command('echo Hello, World!')
