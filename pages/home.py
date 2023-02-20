import PySimpleGUI as sg

def home_page():

    sg.theme("Darkblue 14")

    layout = [
        [sg.Text("Criptografar e Descriptografar arquivos")],
        [sg.Button("Criptografar",key="criptografar"),sg.Button("Descriptografar",key="descriptografar")]
    ]

    return sg.Window("System", layout, finalize=True)
