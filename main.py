
import PySimpleGUI as psg
import time
import pyperclip as pc
import random
import config

psg.theme('DarkBlack')   

layout = [  
            [psg.Text('Current version of app is:'), psg.Text(config.version)],
            [psg.Text('Please enter here word, which according to something, you cannot forget:')],
            [psg.Text('', size=(15, 1)), psg.InputText()],
            [psg.Submit('Generate Random Password')],
            [psg.Submit('Generate')]
        ]


window = psg.Window('Simple Password Generator - Create password you cannot forget!', size=(480, 240)).Layout(layout)
event, values = window.read() 
window.close() 


def genPass(password):
    for i in password:
            if i == 'i':
                password = password.replace(i, '!')
            elif i == 'o':
                password = password.replace(i, '0')
            elif i == "l":
                password = password.replace(i, '1')
            elif i == 'e':
                password = password.replace(i, '3')
            elif i == 'і':
                password = password.replace(i, '1')
            elif i == 'е':
                password = password.replace(i, '3')
            elif i == "b":
                password = password.replace(i, '6')
    # Here we need to show the popup, which asks you if u wanna to save a password
    # as a file or just copy it
    pc.copy(password)


def generateRandomPassword():
    randpass = random.choice(config.passWords)
    randpass = randpass.lower()
    genPass(password = randpass)
    psg.Popup('Password successfully generated and copied!')
    pc.copy(password)
    window.close()


def main():
    if event == "Generate Random Password":
        generateRandomPassword()
    elif event == 'Generate':
        passWord = values[0]
        passWord = passWord.lower()
        if len(passWord) >= 8:
            genPass(password = passWord)
        elif len(passWord) < 8:
            psg.PopupError('Password needs to be longer than 8 symbols!', keep_on_top=True)


def saveAs():
    try:
        file = open('password.txt', 'w+')
        file.write(password)
        file.close()
    except e:
        psg.PopupError('Error was discovered while proccessing! Error: ' + e)

main()
