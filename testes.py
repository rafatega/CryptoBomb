import time
start_time = time.time()

import pyautogui

def new_map():

    temporizador = 0

    while temporizador < 20:
        ONZE_symbol_meta_mask = pyautogui.locateOnScreen('2_meta_mask.png', confidence=0.9)

        if ONZE_symbol_meta_mask is not None:
            pyautogui.click(ONZE_symbol_meta_mask)
            temporizador = 500
            ONZE_symbol_meta_mask = None
            print(date_time(), '#11 - SIMBOLO META MASK - OK')

        else:
            temporizador += 2
            time.sleep(2)
    if temporizador == 20:
        print('Temporizador: ', temporizador)
        print(date_time(), '#11 - SIMBOLO META MASK - FAIL')
        full_entrance()

new_map()