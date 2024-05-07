import pyautogui
pyautogui.PAUSE = 0.5
import time
#aperta uma tecla
pyautogui.press("win")
#escreve no teclado
pyautogui.write("google")
pyautogui.press("enter")


#entrar no sistema site
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
#pausa onde voce quer que espere
time.sleep(2)
#fazer o login
pyautogui.click(x=817, y=471)
pyautogui.write("kamilysimeao@gmail.com")
pyautogui.press("tab")
pyautogui.write("kamily2005")
pyautogui.press("tab")
pyautogui.press("enter")

import pandas

tabela = pandas.read_csv("produtos.csv")

print(tabela)

for linha in tabela.index:
    

    pyautogui.click(x=1052, y=328)
    pyautogui.write(str(tabela.loc[linha, "codigo"]))

    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "marca"]))

    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))

    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))

    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))

    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))

    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "obs"]))

    pyautogui.press("tab")
    pyautogui.press("enter")
    
    pyautogui.scroll(5000)

