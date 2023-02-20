import PySimpleGUI as sg
import pages.home as home
import pages.crypt as crypt

window1, window2 = home.home_page(), None

while True:
    window, event, values = sg.read_all_windows()

    if window == window1 and event == sg.WIN_CLOSED:
        break

    elif window == window1 and event == "criptografar":
        window2 = crypt.crypt_page()

    elif window == window2 and event == sg.WIN_CLOSED:
        window2.close()