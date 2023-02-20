import PySimpleGUI as sg 
#import system_operations as so

def crypt_page():
    sg.theme("Darkblue 14")
    layout = [
        [sg.Text("Criptografar arquivos")],
        [sg.Input(), sg.FileBrowse("Browse")]
    ]
    
    return sg.Window("crypt", layout, finalize=True)
