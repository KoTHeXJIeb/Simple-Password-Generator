
import PySimpleGUI as psg
import time

try:
    psg.theme('DarkBlack')   

    layout = [  [psg.Text('Please enter here word, which according to something, you cannot forget:')],
                [psg.Text('', size=(15, 1)), psg.InputText()],
                [psg.Submit()]
            ]


    window = psg.Window('Simple Password Generator - Create password you cannot forget!', icon='C:/Users/V10/Downloads/check_circle_done_accept_icon_175538.ico', size=(480, 120)).Layout(layout)
    event, values = window.read() 
    window.close() 

    print(event, values[0])

    passWord = values[0]
    passWord = passWord.lower()

    if len(passWord) >= 8:
        for i in passWord:
            if i == 'i':
                passWord = passWord.replace(i, '!')
            elif i == 'o':
                passWord = passWord.replace(i, '0')
            elif i == "l":
                passWord = passWord.replace(i, '1')
            elif i == 'e':
                passWord = passWord.replace(i, '3')
            elif i == 'і':
                passWord = passWord.replace(i, '1')
            elif i == 'е':
                passWord = passWord.replace(i, '3')
        psg.Popup(passWord)
    else:
        psg.Popup('Password needs to be longer than 8 symbols!', keep_on_top=True)

except:
    time.sleep(3)
