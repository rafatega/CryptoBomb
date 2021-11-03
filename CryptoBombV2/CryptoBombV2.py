import pyautogui
import time
import random
from datetime import datetime

# pip install opencv-python

# Personagens e suas devidas carteiras
personagens = 12

numRandom_longo = random.random() * 120
numRandom_curto = random.random() * 3

move_before_scroll_x = 784
move_before_scroll_y = 512

move_after_scroll_x = 815
move_after_scroll_y = 120

work_x = 895
work_y = 753

# Tempo para que o script comece a atuar
time.sleep(5)

# Validação para que o script fiquei em loop infinito
validacao = True


def reconnect():
    # LOG
    print(datetime.timestamp(datetime.now()), '| RECCONECT()')

    pyautogui.press('f5')
    time.sleep(3.2)

    # Clica em Connect Wallet
    temporizador = 0

    while temporizador < 20:
        UM_connect_wallet = pyautogui.locateOnScreen('1_connect_wallet.png', confidence=0.9)
        print(UM_connect_wallet)
        if UM_connect_wallet is not None:
            time.sleep(0.2)
            pyautogui.click(UM_connect_wallet)
            temporizador = 500
        else:
            temporizador += 2
            time.sleep(2)
    if temporizador == 20:
        full_entrance()

    # Clica em MetaMask
    temporizador = 0

    while temporizador < 20:
        DOIS_meta_mask = pyautogui.locateOnScreen('2_meta_mask.png', confidence=0.9)

        if DOIS_meta_mask is not None:
            time.sleep(0.2)
            pyautogui.click(DOIS_meta_mask)
            temporizador = 500
            print(datetime.timestamp(datetime.now()), '| RELOAD() - COMPLETE')
        else:
            temporizador += 2
            time.sleep(2)
    if temporizador == 20:
        full_entrance()
        print(datetime.timestamp(datetime.now()), '| RELOAD() - FAIL')

    # Clica em Assinar
    temporizador = 0

    while temporizador < 20:
        TRES_assinar = pyautogui.locateOnScreen('3_assinar.png', confidence=0.9)

        if TRES_assinar is not None:
            time.sleep(0.2)
            pyautogui.click(TRES_assinar)
            temporizador = 500
        else:
            temporizador += 2
            time.sleep(2)
    if temporizador == 20:
        full_entrance()


# Coloca os personagens para trabalhar e clica para jogar.
def lets_work():
    print(datetime.timestamp(datetime.now()), '| LETS_WORK()')

    # Clica em Heroes
    temporizador = 0

    while temporizador < 20:
        QUATRO_heroes = pyautogui.locateOnScreen('4_heroes.png', confidence=0.9)

        if QUATRO_heroes is not None:
            time.sleep(0.2)
            pyautogui.click(QUATRO_heroes)
            temporizador = 500
        else:
            temporizador += 2
            time.sleep(2)
    if temporizador == 20:
        full_entrance()

    # Scroll na página dos HEROES
    for j in range(2):
        scroll = True
        while scroll:
            time.sleep(2)
            pyautogui.moveTo(move_before_scroll_x, move_before_scroll_y)
            time.sleep(0.2)
            pyautogui.mouseDown(button='left')
            pyautogui.moveTo(move_after_scroll_x, move_after_scroll_y, duration=0.2)
            pyautogui.click()
            time.sleep(0.3)
            scroll = False

    # Clica em todos os HEROES
    for i in range(personagens):
        pyautogui.click(work_x, work_y)
        time.sleep(1)

    # Clica em fechar aba HEROES
    temporizador = 0

    while temporizador < 20:
        CINCO_close_heroes = pyautogui.locateOnScreen('5_close_heroes.png', confidence=0.9)
        print(CINCO_close_heroes)
        if CINCO_close_heroes is not None:
            time.sleep(0.2)
            pyautogui.click(CINCO_close_heroes)
            temporizador = 500
        else:
            temporizador += 2
            time.sleep(2)
    if temporizador == 20:
        full_entrance()
        print(datetime.timestamp(datetime.now()), '| LETS_WORK() - FAIL')

def treasure_hunter():
    print(datetime.timestamp(datetime.now()), '| TREASURE_HUNTER()')

    temporizador = 0

    while temporizador < 20:
        SEIS_treasure_hunter = pyautogui.locateOnScreen('6_treasure_hunter.png', confidence=0.9)

        if SEIS_treasure_hunter is not None:
            time.sleep(0.2)
            pyautogui.click(SEIS_treasure_hunter)
            temporizador = 500
            print(datetime.timestamp(datetime.now()), '| TREASURE_HUNTER() - COMPLETE')
        else:
            temporizador += 2
            time.sleep(2)
    if temporizador == 20:
        full_entrance()
        print(datetime.timestamp(datetime.now()), '| TREASURE_HUNTER() - FAIL')

def new_map():
    print(datetime.timestamp(datetime.now()), '| NEW MAP')

    temporizador = 0

    while temporizador < 20:
        SETE_new_map = pyautogui.locateOnScreen('7_new_map.png', confidence=0.9)

        if SETE_new_map is not None:
            pyautogui.click(SETE_new_map)
            temporizador = 500

            print(datetime.timestamp(datetime.now()), '| NEW MAP - COMPLETE')

        else:
            temporizador += 2
            time.sleep(2)
    if temporizador == 20:
        print(datetime.timestamp(datetime.now()), '| NEW MAP - FAIL')
        full_entrance()

# ENTRADA NO GAME APÓS UM ERRO
def error():
    print(datetime.timestamp(datetime.now()), '| ERROR')

    reconnect()
    treasure_hunter()

    print(datetime.timestamp(datetime.now()), '| ERROR - COMPLETE')


#  ENTRADA COMPLETA NO GAME
def full_entrance():

    print(datetime.timestamp(datetime.now()), '| ENTRADA COMPLETA')

    reconnect()
    lets_work()
    treasure_hunter()

    print(datetime.timestamp(datetime.now()), '| ENTRADA COMPLETA - COMPLETE')

# MAIN

ativador = True

while ativador:

    full_entrance()

    maps = 1
    errors = 0
    timer = 0

    while timer <= 4200:
        print('Tempo pausa (s): ', timer)
        SETE_new_map = pyautogui.locateOnScreen('7_new_map.png', confidence=0.9)
        OITO_error = pyautogui.locateOnScreen('8_error.png', confidence=0.9)

        if SETE_new_map is not None:
            time.sleep(0.2)
            pyautogui.click(SETE_new_map)
            time.sleep(4.8)
            timer += 5
            maps += 1
            print('*MAPS*: ', maps)

        elif OITO_error is not None:
            time.sleep(0.2)
            error()
            timer += 25
            errors += 1
            print('*ERROS*: ', errors)

        else:
            time.sleep(5)
            timer += 5