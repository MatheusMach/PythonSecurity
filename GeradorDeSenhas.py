import random, string

tamanho = 16

chars = string.ascii_letters + string.digits + '!@#$%&*:()'
rnd = random.SystemRandom() # os.urandom gera números aleatórios com random

# Usando uma lista por compreensão para gerar os caracteres aleatórios e depois convertendo-os em uma string com ''.join()
senha = ''.join(rnd.choice(chars) for i in range(tamanho))

print(senha)
