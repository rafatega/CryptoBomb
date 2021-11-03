import pyautogui
import time
import random
from datetime import datetime

# Rodei o Pyinstaller no CMD do Windows

# pip install opencv-python

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

# Registro das carteiras.
class Wallet:
    def __init__(self, heroes):
        self.heroes = heroes

# Inserção de dados da carteira
Wallet_0 = Wallet(14)
Wallet_1 = Wallet(14)
Wallet_2 = Wallet(14)

# Lista com as carteiras
wallet_list = [Wallet_0, Wallet_1, Wallet_2]

# Total de abas
tab = len(wallet_list)


def reconnect():
    # LOG
    print(date_time(), '| RECCONECT()')

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
            UM_connect_wallet = None
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
            DOIS_meta_mask = None
            print(date_time(), '| RELOAD() - COMPLETE')
        else:
            temporizador += 2
            time.sleep(2)
    if temporizador == 20:
        full_entrance()
        print(date_time(), '| RELOAD() - FAIL')

    # Clica em Assinar
    temporizador = 0

    while temporizador < 20:
        TRES_assinar = pyautogui.locateOnScreen('3_assinar.png', confidence=0.9)

        if TRES_assinar is not None:
            time.sleep(0.2)
            pyautogui.click(TRES_assinar)
            temporizador = 500
            TRES_assinar = None
        else:
            temporizador += 2
            time.sleep(2)
    if temporizador == 20:
        full_entrance()


# Coloca os personagens para trabalhar e clica para jogar.
def lets_work():
    print(date_time(), '| LETS_WORK()')

    # Clica em Heroes
    temporizador = 0

    while temporizador < 20:
        QUATRO_heroes = pyautogui.locateOnScreen('4_heroes.png', confidence=0.9)

        if QUATRO_heroes is not None:
            time.sleep(0.2)
            pyautogui.click(QUATRO_heroes)
            temporizador = 500
            QUATRO_heroes = None
        else:
            temporizador += 2
            time.sleep(2)
    if temporizador == 40:
        full_entrance()

    # Scroll na página dos HEROES
    for j in range(2):
        scroll = True
        while scroll:
            time.sleep(1)
            pyautogui.moveTo(move_before_scroll_x, move_before_scroll_y)
            time.sleep(0.2)
            pyautogui.mouseDown(button='left')
            pyautogui.moveTo(move_after_scroll_x, move_after_scroll_y, duration=0.2)
            pyautogui.click()
            time.sleep(0.3)
            scroll = False

    # Clica em todos os HEROES
    for i in range(wallet_list[k].heroes):
        pyautogui.click(work_x, work_y)
        time.sleep(1.2)

    # Clica em fechar aba HEROES
    temporizador = 0

    while temporizador < 20:
        CINCO_close_heroes = pyautogui.locateOnScreen('5_close_heroes.png', confidence=0.9)
        print(CINCO_close_heroes)
        if CINCO_close_heroes is not None:
            pyautogui.moveTo(CINCO_close_heroes)
            time.sleep(0.4)
            pyautogui.click(CINCO_close_heroes)
            temporizador = 500
            CINCO_close_heroes = None
        else:
            temporizador += 2
            time.sleep(2)
    if temporizador == 20:
        full_entrance()
        print(date_time(), '| LETS_WORK() - FAIL')

def treasure_hunter():
    print(date_time(), '| TREASURE_HUNTER()')

    temporizador = 0

    while temporizador < 20:
        SEIS_treasure_hunter = pyautogui.locateOnScreen('6_treasure_hunter.png', confidence=0.9)

        if SEIS_treasure_hunter is not None:
            time.sleep(0.2)
            pyautogui.click(SEIS_treasure_hunter)
            time.sleep(0.2)
            pyautogui.click(SEIS_treasure_hunter)
            temporizador = 500
            SEIS_treasure_hunter = None
            print(date_time(), '| TREASURE_HUNTER() - COMPLETE')
        else:
            temporizador += 2
            time.sleep(2)
    if temporizador == 20:
        full_entrance()
        print(date_time(), '| TREASURE_HUNTER() - FAIL')


def new_map():
    print(date_time(), '| NEW MAP')

    temporizador = 0

    while temporizador < 20:
        SETE_new_map = pyautogui.locateOnScreen('7_new_map.png', confidence=0.9)

        if SETE_new_map is not None:
            pyautogui.click(SETE_new_map)
            temporizador = 500
            SETE_new_map = None
            print(date_time(), '| NEW MAP - COMPLETE')

        else:
            temporizador += 2
            time.sleep(2)
    if temporizador == 20:
        print(date_time(), '| NEW MAP - FAIL')
        full_entrance()

# ENTRADA NO GAME APÓS UM ERRO
def error():
    print(date_time(), '| ERROR')

    reconnect()
    treasure_hunter()

    print(date_time(), '| ERROR - COMPLETE')


#  ENTRADA COMPLETA NO GAME
def full_entrance():

    print(date_time(), '| ENTRADA COMPLETA')

    reconnect()
    lets_work()
    treasure_hunter()

    print(date_time(), '| ENTRADA COMPLETA - COMPLETE')

    # ALT TAB
def alt_tab():
    print(date_time(), '| ALT + TAB')
    pyautogui.keyDown('alt')
    time.sleep(0.2)
    for h in range(tab - 1):
        pyautogui.press('tab')
        time.sleep(0.2)
    time.sleep(0.2)
    pyautogui.keyUp('alt')
    time.sleep(0.4)

def date_time():
    now = datetime.now()  # current date and time

    date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
    return date_time


# MAIN
ativador = True

while ativador:

    maps = 1
    errors = 0
    timer = 0

    for k in range(tab):
        full_entrance()
        alt_tab()

    # 25 Minutos neste loop
    while timer <= 1500:
        start_time = time.time()

        print('Tempo pausa (s): ', timer)
        time.sleep(5)
        SETE_new_map = pyautogui.locateOnScreen('7_new_map.png', confidence=0.9)
        OITO_error = pyautogui.locateOnScreen('8_error.png', confidence=0.9)

        if SETE_new_map is not None:

            time.sleep(0.2)
            pyautogui.click(SETE_new_map)
            time.sleep(4.8)
            SETE_new_map = None
            maps += 1
            print('*MAPS*: ', maps)
            alt_tab()

            execution_time = round((time.time() - start_time), 2)
            timer += execution_time

        elif OITO_error is not None:

            time.sleep(0.2)
            error()
            errors += 1
            OITO_error = None
            print('*ERROS*: ', errors)
            alt_tab()

            execution_time = round((time.time() - start_time), 2)
            timer += execution_time

        else:
            time.sleep(5)
            alt_tab()

            execution_time = round((time.time() - start_time), 2)
            timer += execution_time

    print(date_time(), '| PAUSA DE DESCANSO - INICIADA')
    start_time = time.time()
    time.sleep(2700)
    execution_time = round((time.time() - start_time), 2)
    timer += execution_time
    print(date_time(), '| PAUSA DE DESCANSO - COMPLETE')