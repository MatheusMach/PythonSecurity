import os #Importando o módulo/biblioteca os, que integra os programas de recursos do sistema operacional
import time #importa o modulo/biblioteca do tempo

with open('hosts.txt') as file: 
    dump = file.read() #Lê todo o conteúdo do arquivo e armazena em 'dump'
    dump = dump.splitlines() #Divide o conteúdo do arquivo em uma lista de strings, uma por linha

    for ip in dump:  #Itera sobre cada linha da lista 'dump', que contém endereços IP
        print('verificando o ip: ', ip) 
        os.system('ping -n 2{}'.format(ip)) # Executa o comando 'ping' no sistema operacional com o IP atual
        # A opção '-n 2' especifica que devem ser enviados 2 pacotes ICMP de ping
        time.sleep(5) #espera 5 segundos para execução do proximo programa

