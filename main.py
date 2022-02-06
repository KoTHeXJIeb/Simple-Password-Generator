
from hashlib import md5
import PySimpleGUI as psg
import pyperclip as pc
import langdetect
import transliterate
import xlwt
import hashlib

import config
import generate

themes = psg.theme_list()

layout = [
            [psg.Text('Current version of app is:'), psg.Text(config.version)],
            [psg.Text('Please enter here word, which according to something, you cannot forget:')],
            [psg.Text(size=(16, 1))],
            [psg.InputText()],
            [psg.Button('Generate Random Password')],
            [psg.Submit('Generate')]
]

window = psg.Window('Simple Password Generator - Create password you cannot forget!', size=(480, 240)).Layout(layout)
event, values = window.read() 
window.close() 

psg.theme(config.theme_name)

wb = xlwt.Workbook()
sheet = wb.add_sheet('First Sheet')

def main():
    if event == "Generate Random Password":
        randpass = generate.generateRandomPassword()
        psg.Popup('Password saved to a Excel file!')
        sheet.write(1, 0, 'Password')
        sheet.write(1, 1, randpass)
        sheet.write(2, 0, 'Hash')
        sheet.write(2, 1, 'MD5')
        sheet.write(2, 2, hashlib.md5(randpass.encode(encoding = 'UTF-8', errors = 'strict')).hexdigest())
        sheet.write(3, 1, 'SHA256')
        sheet.write(3, 2, hashlib.sha256(randpass.encode(encoding = 'UTF-8', errors = 'strict')).hexdigest())
        wb.save('password_generator.xls')
    elif event == 'Generate':
        passWord = values[0].lower()
        if langdetect.detect(passWord) != 'en':
            passWord = transliterate.translit(passWord, reversed=True)
        if len(passWord) >= 8:
            final = generate.generatePassword(password = passWord)
            psg.Popup(final)
            psg.Popup('Password saved to a Excel file!')
            sheet.write(1, 0, 'Password')
            sheet.write(1, 1, passWord)
            sheet.write(2, 0, 'Hash')
            sheet.write(2, 1, 'MD5')
            sheet.write(2, 2, hashlib.md5(passWord.encode(encoding = 'UTF-8', errors = 'strict')).hexdigest())
            sheet.write(3, 1, 'SHA256')
            sheet.write(3, 2, hashlib.sha256(passWord.encode(encoding = 'UTF-8', errors = 'strict')).hexdigest())
            wb.save('password_generator.xls')
        elif len(passWord) < 8:
            psg.PopupError('Password needs to be longer than 8 symbols!')
main()
