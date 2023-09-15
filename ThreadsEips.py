from threading import Thread

def carro1(velocidade):
    trajeto = 0 
    while trajeto <= 100:
        print('Carro1: ', trajeto)
        trajeto+=velocidade

def carro2(velocidade):
    trajeto = 0 
    while trajeto <= 100:
        print('Carro2: ', trajeto)
        trajeto+=velocidade

#os dois nao estão andando simultaneamente se for apenas aqui 
#carro1(10)
#carro2(20) 

t_carro1 = Thread(target=carro1, args=[1])
t_carro2 = Thread(target=carro2, args=[1.5])

#target é o alvo que fará parte do componente, e args os argumentos ai no caso a velocidade

t_carro1.start()
t_carro2.start()

#com esse programa é possivel criar um porgrama de solicitação simultanea de serviço de rede por exemplo
