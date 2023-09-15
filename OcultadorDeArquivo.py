import ctypes

pasta = input('Digite o caminho da pasta a ser ocultado ex (C:/pasta): ')

atributo_ocultar = 0x02

retorno = ctypes.windll.kernell32.SetFileAttributesW('ocultar.txt', atributo_ocultar)

if retorno:
    print('Arquivo foi ocultado')
else:
    print('Arquivo nao foi ocultado')
