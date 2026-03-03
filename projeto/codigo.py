import pyautogui
import time
#passo 1 - entrar no sistema
link = "https://dlp.hashtagtreinamentos.com/p"
pyautogui.press("win")
pyautogui.write("Chrome")
pyautogui.press("enter")
time.sleep(10)
pyautogui.write(link)
pyautogui.press("enter")



