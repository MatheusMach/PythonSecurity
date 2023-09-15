from bs4 import BeautifulSoup

import requests

site = input('Digite o nome do site aqui(tente dar o maximo de detalhes possivel')

site = requests.get('https://'+site+'/').content
#objeto está recebendo o conteudo da requisição http
soup = BeautifulSoup(site, 'html.parser')
#objeto soup(sopa de letrinhas)  está baixando do site
print(soup.prettify())
#transforma em string e mostra todo codigo html do site
