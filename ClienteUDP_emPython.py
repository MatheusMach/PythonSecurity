import socket #UDP contempla o principio de disponibilidade a biblioteca envolta isso

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #criando objeto de conexão; UDP é o protocolo de datagrama do usuario

#ai caso ele for criado com sucesso
print('Cliente Socket Criado com Sucesso!!!')

host = 'localhost' #localhost é uma rede local que é a rede interna da sua maquina, linux>comando para redes
porta = 5433
mensagem = 'Olá servidor firmeza? '

try: #tentar enviar e receber essa mensagem
    print('Cliente: ' +mensagem)
    s.sendto(mensagem.encode(), (host, 5432)) #écomo se tivesse empacotando ela e mandando ao servidor
    #empacotar a mensagem -> enviar ela no local host na porta 5432

    dados, servidor = s.recvfrom(4096) #2 variaveis que vao receber do servidor uma resposta em 4096 bytes
    dados = dados.decode() #vai desempacotar
    print("Cliente: " + dados) #vai printar os dados
finally
    print('Cliente: Fechando a conexão')
    s.close() #fechar para que nao fique em looping
