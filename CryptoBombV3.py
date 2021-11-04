import pyautogui
import time
import random
from datetime import datetime

# Dicas pessoais:
# Rodei o Pyinstaller no CMD do Windows

# Infos para que outros PCs rodem sem problemas:
# Tela deve ser fullhd, com o zoom em 100%
# Coloquei atalhos de tecla nas metamasks dos navegadores, ALT+P. Para tratar um possível erro ao assinar.
# Reload da página é feito com o F5, portanto, nada pode estar bindado em paralelo com está tecla.

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
Wallet_0 = Wallet(15)
Wallet_1 = Wallet(15)
Wallet_2 = Wallet(15)

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
            print(date_time(), '#2 - METAMASK - OK')
        else:
            temporizador += 2
            time.sleep(2)
    if temporizador == 20:
        full_entrance()
        print('Temporizador: ', temporizador)
        print(date_time(), '#2 - METAMASK - FAIL')

    # Clica em Assinar
    temporizador = 0
    meta_mask_error_handling = 0

    while temporizador < 20:
        TRES_assinar = pyautogui.locateOnScreen('3_assinar.png', confidence=0.9)

        if TRES_assinar is not None:
            time.sleep(0.2)
            pyautogui.click(TRES_assinar)
            temporizador = 500
            TRES_assinar = None
            print(date_time(), '#3 - ASSINAR - OK')
        else:
            temporizador += 2
            time.sleep(2)
            meta_mask_error_handling += 2

            if meta_mask_error_handling == 8:

                print(date_time(), '#3 - ASSINAR - METAMASK ERROR HANDLING - OK')
                pyautogui.keyDown('alt')
                time.sleep(0.2)
                pyautogui.press('p')
                time.sleep(0.2)
                pyautogui.keyUp('alt')
            else:
                pass

    if temporizador == 20:
        print('Temporizador: ', temporizador)
        print(date_time(), '#3 - ASSINAR - FAIL')
        full_entrance()


# Coloca os personagens para trabalhar e clica para jogar.
def lets_work():
    print(date_time(), '| LETS_WORK()')

    # Clica em Heroes
    temporizador = 0

    while temporizador < 60:
        QUATRO_heroes = pyautogui.locateOnScreen('4_heroes.png', confidence=0.9)

        if QUATRO_heroes is not None:
            time.sleep(0.2)
            pyautogui.click(QUATRO_heroes)
            temporizador = 500
            QUATRO_heroes = None
            print(date_time(), '#4 - HEROES - OK')
        else:
            temporizador += 2
            time.sleep(2)
    if temporizador == 60:
        print('Temporizador: ', temporizador)
        print(date_time(), '#4 - HEROES - FAIL')
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
        if CINCO_close_heroes is not None:
            pyautogui.moveTo(CINCO_close_heroes)
            time.sleep(0.4)
            pyautogui.click(CINCO_close_heroes)
            temporizador = 500
            CINCO_close_heroes = None
            print(date_time(), '#5 - CLOSE HEROES - OK')
        else:
            temporizador += 2
            time.sleep(2)
    if temporizador == 20:
        print('Temporizador: ', temporizador)
        print(date_time(), '#5 - CLOSE HEROES - FAIL')
        full_entrance()


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
            print(date_time(), '#6 - TREASURE HUNTER - OK')
        else:
            temporizador += 2
            time.sleep(2)
    if temporizador == 20:
        print('Temporizador: ', temporizador)
        print(date_time(), '#6 - TREASURE HUNTER - FAIL')
        error()



def new_map():

    temporizador = 0

    while temporizador < 20:
        SETE_new_map = pyautogui.locateOnScreen('7_new_map.png', confidence=0.9)

        if SETE_new_map is not None:
            pyautogui.click(SETE_new_map)
            temporizador = 500
            SETE_new_map = None
            print(date_time(), '#7 - NEW MAP - COMPLETE')

        else:
            temporizador += 2
            time.sleep(2)
    if temporizador == 20:
        print('Temporizador: ', temporizador)
        print(date_time(), '#7 - NEW MAP - FAIL')
        full_entrance()

# ENTRADA NO GAME APÓS UM ERRO
def error():
    print(date_time(), '############## ERROR #############')
    reconnect()
    treasure_hunter()
    print(date_time(), '############## ERROR COMPLETE #############')


#  ENTRADA COMPLETA NO GAME
def full_entrance():
    print('Temporizador: ', temporizador)
    print(date_time(), '############## FULL ENTRANCE #############')

    reconnect()
    lets_work()
    treasure_hunter()

    print(date_time(), '############## FULL ENTRANCE COMPLETE #############')


def last_validation():

    temporizador = 0

    while temporizador < 20:
        NOVE_validation = pyautogui.locateOnScreen('9_validation.png', confidence=0.9)

        if NOVE_validation is not None:
            pyautogui.click(NOVE_validation)
            temporizador = 500
            NOVE_validation = None
            print(date_time(), '#9 - LAST VALIDATION - COMPLETE')

        else:
            temporizador += 2
            time.sleep(2)
    if temporizador == 20:
        error()

    # ALT TAB
def alt_tab():
    print(date_time(), '############## ALT TAB #############')
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
    last_validation_bool = 0

    for k in range(tab):
        temporizador = 0

        full_entrance()
        alt_tab()

    # 18 Minutos neste loop
    while timer <= 1080:
        start_time = time.time()

        print('Tempo pausa (s): ', timer)
        time.sleep(5)
        SETE_new_map = pyautogui.locateOnScreen('7_new_map.png', confidence=0.9)
        OITO_error = pyautogui.locateOnScreen('8_error.png', confidence=0.9)

        if SETE_new_map is not None:

            time.sleep(0.2)
            pyautogui.click(SETE_new_map)
            time.sleep(2)
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
            print('*ERROS TRATADOS*: ', errors)
            alt_tab()

            execution_time = round((time.time() - start_time), 2)
            timer += execution_time

        # Aos 15 minutos irá sair e entrar na partida para desbugar os herois.
        elif 900 <= timer <= 960 and last_validation_bool == 0:
            for k in range(tab):
                temporizador = 0

                last_validation()
                alt_tab()

            last_validation_bool = 1

            execution_time = round((time.time() - start_time), 2)
            timer += execution_time

        else:
            time.sleep(5)
            alt_tab()

            execution_time = round((time.time() - start_time), 2)
            timer += execution_time


    print(date_time(), '| PAUSA DE DESCANSO - INICIADA')
    start_time = time.time()
    # 62 minutos de parada TOTAL no SCRIPT.
    time.sleep(3720)
    execution_time = round((time.time() - start_time), 2)
    timer += execution_time
    print(date_time(), '| PAUSA DE DESCANSO - COMPLETE')

    # Após completado 1h20m de pausa, o SCRIPT reinicia.

    # ________________________--------------______________________
    # A fazer:
    # Achar alguma maneira de não ficar preso caso o loop de carregamento incial apareça;
    # Verificar se o erro do CACHE lotado foi arrumado. Caso não, achar uma solução.