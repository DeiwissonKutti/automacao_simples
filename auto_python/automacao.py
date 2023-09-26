#importando o pyautogui
import pyautogui
# importando o sleep da biblioteca time
from time import sleep


def inicia_automacao():
	link = "https://www.youtube.com"
	tamanho_link = len(link)

	if tamanho_link == 23 and link == "https://www.youtube.com":

		pyautogui.PAUSE = 0.5

		pyautogui.press('winleft')
		pyautogui.write(" Chrome", interval=0.2)
		pyautogui.press('enter')
		sleep(4)
		pyautogui.write("https://www.youtube.com", interval=0.1)
		pyautogui.press('enter')
	else:
		pyautogui.alert("Erro!")
		print("erro")
