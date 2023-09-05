import socket
import sys

def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as e:
        print("a conexão falhou")
        print("Erro: {}".format(e))
        sys.exit()
    print("Socket criado com sucesso")

    HostAlvo = input("Digite o host ou ip a ser conectado: ")
    PortaAlvo = input("Digite a porta a ser conectada: ")

    try:
        s.connect((HostAlvo, int(PortaAlvo)))
        print("Cliente TCP conectado com sucesso no Host: " + HostAlvo + " e na Porta: " + PortaAlvo )
        s.shutdown(2)
    except socket.error as e:
        print("Não foi possivel conectar no Host: " + HostAlvo + " = Porta: " + PortaAlvo)
        print("Erro: {}".format(e))
        sys.exit()

if __name__ == "__main__":
    main()
