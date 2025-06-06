import pyautogui
import time

pyautogui.PAUSE = 0.7

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.click(x=380, y=908)

time.sleep(2)

pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

pyautogui.press("tab")
pyautogui.write("therafaellima@top.com")

pyautogui.press("tab")
pyautogui.write("senha1234567")

pyautogui.press("tab")
pyautogui.press("enter")
