import time
import pyautogui

time.sleep(5)

WORK = pyautogui.locateOnScreen('backlog_work.png', confidence=0.9)

pyautogui.moveTo(WORK)

print(WORK)


'''temporizador = 0

while temporizador < 20:
    UM_connect_wallet = pyautogui.locateOnScreen('1_connect_wallet.png', confidence=0.9)
    if UM_connect_wallet is not None:
        time.sleep(0.2)
        pyautogui.click(UM_connect_wallet)
        UM_connect_wallet = None
        temporizador = 500
        print(date_time(), '#1 - CONNECT WALLET - OK')
    else:
        temporizador += 2
        time.sleep(2)
if temporizador == 20:
    print('Temporizador: ', temporizador)
    print(date_time(), '#1 - CONNECT WALLET - FAIL')
    full_entrance()'''