import requests
import bs4
import os
from pesquisas import Pesquise

urlLogin = "https://sistemas.aracajucard.com.br/portaldousuario/Acesso.aspx"
urlSaldo = "http://sistemas.aracajucard.com.br/portaldousuario/ExtratoUtilizacao.aspx"

username = "08042911521"
password = "70sergipe"

s = requests.Session()
s.auth = (username,password)

login = s.post(urlLogin)


preparaHeaders = login.headers['Set-Cookie']
split1 = preparaHeaders.split(";")
cookieASP = split1[0].split("=")

cookie = {
    'ASP.NET_SessionId': 'rlrrn4pv33sp3z5bybxvbzyw',
}

saldoGet = s.get(urlSaldo, cookies=cookie)
saldoGetContents = saldoGet.content
soup = bs4.BeautifulSoup(saldoGetContents, 'html.parser')

tr = soup.find('tr',{'bgcolor':'#653052'})
if tr == False:
    exit
td = tr.find('td',{'class':'text-right'})
font = td.find('font',{'color':'#FFFFFF'})
saldo = font.get_text()[13:].replace(',','reais e')

frase = 'Saldo atual da carteira de transporte e de {} centavos'.format(saldo)

a = Pesquise(frase)
a.fala(frase)