from selenium import webdriver
from lxml import html
import requests
import bs4
import sys 

username = sys.argv[1]# Seu usuario

password = sys.argv[2] # Sua senha

print(username+" "+password)
def request(driver):  
                   s = requests.Session()
                   cookies = driver.get_cookies()
                   for cookie in cookies:
                         s.cookies.set(cookie['name'], cookie['value'])
                   return s
def login():
    try:
        driver = webdriver.Firefox()
        requisicao(driver)    
    except:
        try:
            driver = webdriver.Chrome()
            requisicao(driver)
        except:
            try:
                driver = webdriver.Ie()
                requisicao(driver)
            except:
                try:
                    driver = webdriver.Opera()
                    requisicao(driver)
                except:
                    print('Nenhum Browser disponivel')
def requisicao(driver):
    driver.get("https://sistemas.aracajucard.com.br/portaldousuario/Acesso.aspx")
    driver.find_element_by_id('ContentPlaceHolder1_pConteudo_username').send_keys(username)
    driver.find_element_by_id('ContentPlaceHolder1_pConteudo_password').send_keys(password)
    driver.find_element_by_id('ContentPlaceHolder1_pConteudo_btAcessar').click()
      
    # Now move to other pages using requests
    req = request(driver)
    response = req.get("http://sistemas.aracajucard.com.br/portaldousuario/ExtratoUtilizacao.aspx")      
    #    arquivo = open('index.html','w+')
    #    for linha in response:
    #        arquivo.write(str(linha))
    saldoGetContents = response.content
    soup = bs4.BeautifulSoup(saldoGetContents, 'html.parser')
    tr = soup.find('tr',{'bgcolor':'#653052'})
    td = tr.find('td',{'class':'text-right'})
    font = td.find('font',{'color':'#FFFFFF'})
    saldo = font.get_text()[13:].replace(',',' reais e ')
    frase = 'Saldo atual da carteira de transporte e de {} centavos'.format(saldo)
    print(frase)
    driver.quit()
login()
