from os import startfile
from pyautogui import click
from keyboard import press
from keyboard import write
from time import sleep


def WhatsappMsg(name, message):
    startfile("C:\\Users\\ketan\\AppData\\Local\\WhatsApp\\Whatsapp.exe")

    sleep(15)

    click(x=147, y=130)

    sleep(1)

    write(name)

    sleep(1)

    click(x=134, y=299) 

    sleep(1)

    click(x=835, y=992)

    write(message)

    press('enter')

def WhatsappCall(name):
    startfile("C:\\Users\\ketan\\AppData\\Local\\WhatsApp\\Whatsapp.exe")

    sleep(10)

    click(x=147, y=130)

    sleep(1)

    write(name)

    sleep(1)

    click(x=134, y=299) 

    sleep(1)

    click(x=1720, y=80)

def WhatsappChat(name):
    startfile("C:\\Users\\ketan\\AppData\\Local\\WhatsApp\\Whatsapp.exe")

    sleep(10)

    click(x=147, y=130)

    sleep(1)

    write(name)

    sleep(1)

    click(x=134, y=299)

def WhatsappVideoCall(name):

    startfile("C:\\Users\\ketan\\AppData\\Local\\WhatsApp\\Whatsapp.exe")

    sleep(10)

    click(x=147, y=130)

    sleep(1)

    write(name)

    sleep(1)

    click(x=134, y=299) 

    sleep(1)

    click(x=1656, y=80)

WhatsappMsg('Manas','Hi' )