from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()

#abre um endereço no navegador
#get equivale a digitar uma url na barra de pesquisa
browser.get('https://www.google.com')

#procura na pagina um elemento que possui o ID 
campo_pesquisa = browser.find_element(by=By.ID, value="APjFqb")

#digita no elemento selecionado
campo_pesquisa.send_keys("aiai")

#campo_pesquisa.send_keys(Keys.ENTER)

#procura o botao estou com sorte, seu nome é btnI
btn_estouComSorte = browser.find_elements(By.NAME,"btnI")

#enviar um codigo js para ser executado no navegador
#titulo = browser.execute_script('return document.title;')
#print("o titulo dessa página é : ",titulo)

#btn_estouComSorte[1].click()

browser.execute_script('arguments[0].style.backgroundColor = "red";', btn_estouComSorte[1])

input("Digite algo para fechar")