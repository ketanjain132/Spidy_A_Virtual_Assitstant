from os import startfile
from pyautogui import click
from keyboard import press
from keyboard import write
from time import sleep

def OffLight():
    startfile("C:\\Users\\ketan\\Desktop\\off_light\\off_light.ino")
    sleep(4)
    click(x=58, y=75)
    
def OnLight():
    startfile("C:\\Users\\ketan\\Desktop\\on_light\\on_light.ino")
    sleep(4)
    click(x=58, y=75)