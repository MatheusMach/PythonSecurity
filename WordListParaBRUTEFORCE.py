import itertools

string = input("String a ser permutada: ")

resultado = itertools.permutations(string, len(string))
#quem fara a permutação dos caracteres no wordlist
#basicmaente é uma lista pra bruteforce
for i in resultado: #para cada caractere no resultado
    print("".join(i)) #imprimir esse caractere e juntar esse caractere com o proximo, gerando um aleatorio
