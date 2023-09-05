import os #Importando o módulo/biblioteca os, que integra os programas de recursos do sistema operacional

print("=" * 60)

ip_ou_host = input("Digite o ip ou host a ser verificado: ") # variavel que vai receber o ip ou host e verifica-lo

print("=" * 60)

os.system('ping -n 6 {}'.format(ip_ou_host)) #chamando a biblioteca/modulo para trazer todos os comandos do sistema
print("=" * 60)
