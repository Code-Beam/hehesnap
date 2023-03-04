import pyautogui as pag
import webbrowser
import time
import keyboard

def clear():
    pag.click(1236,463)
    pag.keyDown('ctrl')
    pag.keyDown('a')
    pag.keyUp('a')
    pag.keyUp('ctrl')
    pag.hotkey('backspace')

def run(times):
    webbrowser.open("https://web.snapchat.com/")
    time.sleep(5)
    for i in range(times):
        #pag.displayMousePosition()
        if keyboard.is_pressed('alt+s'):
            break
        pag.click(1310,997)
        pag.click(1455,1024)
        pag.click(1236,463)
        """
        pag.typewrite("sasi",interval=0.01)
        pag.click(1466,550)
        clear()
        """
        pag.typewrite("alex")
        pag.click(1466,550)
        """
        pag.typewrite("dhanvin",interval=0.01)
        pag.click(1466,550)
        clear()
        pag.typewrite("snapscore",interval=0.01)
        pag.click(1466,550)
        clear()
        pag.typewrite("harry",interval=0.01)
        pag.click(1466,550)
        clear()
        pag.typewrite("alex",interval=0.01)
        pag.click(1466,550)
        """
        pag.click(1310,1031)

runtimes = int(input("Enter Times To Run: "))

run(runtimes)