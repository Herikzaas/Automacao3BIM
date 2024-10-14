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
btn_estouComSorte = browser.find_element(By.NAME,"btnI")
btn_estouComSorte.click()


input("Digite algo para fechar")