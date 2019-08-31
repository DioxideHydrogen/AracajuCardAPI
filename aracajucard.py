import requests
import bs4

urlLogin = "https://sistemas.aracajucard.com.br/portaldousuario/Acesso.aspx"
urlSaldo = "http://sistemas.aracajucard.com.br/portaldousuario/ExtratoUtilizacao.aspx"

username = "" # Seu usuário
password = "" # Sua senha

s = requests.Session()
s.auth = (username,password)

login = s.post(urlLogin)


preparaHeaders = login.headers['Set-Cookie']
split1 = preparaHeaders.split(";")
cookieASP = split1[0].split("=")

cookie = {
    'ASP.NET_SessionId': '', # Token capturado no navegador
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

print frase
