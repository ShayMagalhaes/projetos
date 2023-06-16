import PySimpleGUI as sg

sg.theme('darkAmber')

layout = [[sg.Combo(['001','002','003'], default_value=None, k='id'),sg.Text('-- nome do funcionario -- ', k= 'txt')],
          [sg.Button('Bt')]]

windown = sg.Window('Teste', layout)

while True:
    eventos, valores = windown.read(timeout=100)

    if eventos == sg.WIN_CLOSED:
        break
    if valores['id'] == '001':
        windown['txt'].update('Joao')
    if valores['id'] == '002':
        windown['txt'].update('jubisclauto')
    #if eventos == 'Bt':
        #exclui o funcionario com a id no valores['id']

windown.close()
