import pyautogui
import time
import random
import json
from datetime import datetime
from getmac import get_mac_address as gma
import requests
import cv2


# Dicas pessoais:
# Rodei o Pyinstaller no CMD do Windows

# Infos para que outros PCs rodem sem problemas:
# Tela deve ser fullhd, com o zoom em 100%
# Coloquei atalhos de tecla nas metamasks dos navegadores, ALT+P. Para tratar um possível erro ao assinar.
# Reload da página é feito com o F5, portanto, nada pode estar bindado em paralelo com está tecla.
# "cmd.exe" /k ""C:\Users\Tega\Envs\CodigosIndependentes\Scripts\activate.bat""  para entrar na VENV
# pyinstaller --hidden-import getmac --hidden-import opencv-python --hidden-import opencv-python-headless --hidden-import cv2 --onefile CryptoBombV4.py
# pip install opencv-python
# pip install Pillow
# pip install pyautogui
# pip install getmac
# pip install opencv-python-headless


def auth():
    # URL da API
    url = 'https://rafatega.github.io/cbjsonapi/publicapicb.json'

    # Pegando as infos da URL
    response = requests.get(url)

    # Resposta em tipo JSON (confuso de ler)
    packages_json = response.json()

    # Deixando legível.
    packages_str = json.dumps(packages_json, indent=2)

    # Carregando dados do JSON
    loads_json = json.loads(packages_str)

    authentication = False

    while authentication is False:

        username = input('Username: ')
        password = input('Password: ')

        try:
            if loads_json[username]:
                api_password = loads_json[username]['password']
                api_mac = loads_json[username]['mac']
                mac_address = gma()

                # Única maneira de autenticação
                if password == api_password and mac_address == api_mac:
                    authentication = True
                    print('Bem-vindo :D')

                    return authentication

                elif password == api_password and mac_address != api_mac:
                    print('Este computador não tem permissão para executar o BOT.')
                else:
                    print('Credenciais erradas, tente novamente.')

        except:
            print('Credenciais erradas, tente novamente.')


# Tempo para que o script comece a atuar
time.sleep(5)

# Total de abas
tab = api_tab


def f_cinco():
    print(date_time(), '| F5')

    pyautogui.keyDown('ctrl')
    time.sleep(0.2)
    pyautogui.press('f5')
    time.sleep(0.2)
    pyautogui.keyUp('ctrl')

    time.sleep(3.2)


def connect_wallet():

    temporizador = 0

    while temporizador < 20:
        UM_connect_wallet = pyautogui.locateOnScreen('1_connect_wallet.png', confidence=0.9)
        if UM_connect_wallet is not None:
            time.sleep(0.2)
            pyautogui.click(UM_connect_wallet)
            UM_connect_wallet = None
            temporizador = 500
            print(date_time(), '#1 - CONNECT WALLET - OK')
            def_error = 0
            return def_error
        else:
            temporizador += 2
            time.sleep(2)
    if temporizador == 20:
        print('Temporizador: ', temporizador)
        print(date_time(), '#1 - CONNECT WALLET - FAIL')
        def_error = 1
        return def_error


def meta_mask():
    temporizador = 0

    # Clica em MetaMask
    while temporizador < 20:
        DOIS_meta_mask = pyautogui.locateOnScreen('2_meta_mask.png', confidence=0.9)
        if DOIS_meta_mask is not None:
            time.sleep(0.2)
            pyautogui.click(DOIS_meta_mask)
            temporizador = 500
            DOIS_meta_mask = None
            print(date_time(), '#2 - CLICK METAMASK - OK')
            def_error = 0
            return def_error
        else:
            temporizador += 2
            time.sleep(2)
    if temporizador == 20:
        print('Temporizador: ', temporizador)
        print(date_time(), '#2 - CLICK METAMASK - FAIL')
        def_error = 1
        return def_error


def assinar():
    temporizador = 0
    meta_mask_error_handling = 0

    while temporizador < 20:
        TRES_assinar = pyautogui.locateOnScreen('3_assinar.png', confidence=0.9)
        if TRES_assinar is not None:
            time.sleep(0.2)
            pyautogui.click(TRES_assinar)
            temporizador = 500
            TRES_assinar = None
            print(date_time(), '#3 - CLICK ASSINAR - OK')
            def_error = 0
            return def_error
        else:
            temporizador += 2
            meta_mask_error_handling += 2
            time.sleep(2)

            if meta_mask_error_handling == 12:

                pyautogui.keyDown('alt')
                time.sleep(0.2)
                pyautogui.press('p')
                time.sleep(0.2)
                pyautogui.keyUp('alt')

                meta_mask_error_handling = 0

                print(date_time(), '#3 - METAMASK ERROR HANDLING - OK')
            else:
                pass

    if temporizador == 20:
        print('Temporizador: ', temporizador)
        print(date_time(), '#3 - ASSINAR - FAIL')
        def_error = 1
        return def_error


def heroes():
    temporizador = 0

    # Clica em Heroes
    while temporizador < 120:
        QUATRO_heroes = pyautogui.locateOnScreen('4_heroes.png', confidence=0.9)

        if QUATRO_heroes is not None:
            time.sleep(0.8)
            pyautogui.click(QUATRO_heroes)
            temporizador = 500
            QUATRO_heroes = None
            print(date_time(), '#4 - HEROES - OK')
            def_error = 0
            return def_error
        else:
            temporizador += 2
            time.sleep(2)
    if temporizador == 120:
        print('Temporizador: ', temporizador)
        print(date_time(), '#4 - HEROES - FAIL')
        def_error = 1
        return def_error


def scroll():
    temporizador = 0

    while temporizador < 20:
        DOZE_character_scroll_down = pyautogui.locateOnScreen('12_charapter_scroll_down.png', confidence=0.9)
        if DOZE_character_scroll_down is not None:
            pyautogui.moveTo(DOZE_character_scroll_down.left, DOZE_character_scroll_down.top + 150)
            time.sleep(0.2)
            temporizador = 500
            DOZE_character_scroll_down = None
            for s in range(58):
                pyautogui.scroll(-99)
            print(date_time(), '#12 - SCROLL - COMPLETE')
            def_error = 0
            return def_error
        else:
            temporizador += 2
            time.sleep(2)
    if temporizador == 20:
        print('Temporizador: ', temporizador)
        print(date_time(), '#12 - SCROLL - FAIL')
        def_error = 1
        return def_error


def click_heroes():
    # Clica em todos os HEROES
    temporizador = 0

    while temporizador < 20:
        DEZ_work_heroes = pyautogui.locateOnScreen('10_backlog_work.png', confidence=0.99)
        ONZE_work_heroes_complete = pyautogui.locateOnScreen('11_backlog_work_complete.png', confidence=0.99)

        if DEZ_work_heroes is not None:
            while DEZ_work_heroes is not None:
                pyautogui.moveTo(DEZ_work_heroes)
                time.sleep(0.2)
                pyautogui.click(DEZ_work_heroes)
                DEZ_work_heroes = None
                DEZ_work_heroes = pyautogui.locateOnScreen('10_backlog_work.png', confidence=0.99)

            temporizador = 500
            DEZ_work_heroes = None
            def_error = 0
            return def_error

        elif ONZE_work_heroes_complete is not None:
            temporizador = 500
            ONZE_work_heroes_complete = None
            def_error = 0
            return def_error

        else:
            temporizador += 2
            time.sleep(2)
    if temporizador == 20:
        print('Temporizador: ', temporizador)
        print(date_time(), 'WORK - FAIL')
        def_error = 1
        return def_error


def close_heroes():
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
            def_error = 0
            return def_error
        else:
            temporizador += 2
            time.sleep(2)
    if temporizador == 20:
        print('Temporizador: ', temporizador)
        print(date_time(), '#5 - CLOSE HEROES - FAIL')
        def_error = 1
        return def_error


def treasure_hunter():
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
            def_error = 0
            return def_error
        else:
            temporizador += 2
            time.sleep(2)
    if temporizador == 20:
        print('Temporizador: ', temporizador)
        print(date_time(), '#6 - TREASURE HUNTER - FAIL')
        def_error = 1
        return def_error


def new_map():
    temporizador = 0

    while temporizador < 20:
        SETE_new_map = pyautogui.locateOnScreen('7_new_map.png', confidence=0.9)

        if SETE_new_map is not None:
            pyautogui.click(SETE_new_map)
            temporizador = 500
            SETE_new_map = None
            print(date_time(), '#7 - NEW MAP - COMPLETE')
            def_error = 0
            return def_error

        else:
            temporizador += 2
            time.sleep(2)
    if temporizador == 20:
        print('Temporizador: ', temporizador)
        print(date_time(), '#7 - NEW MAP - FAIL')
        def_error = 1
        return def_error


def last_validation():
    temporizador = 0

    while temporizador < 20:
        NOVE_validation = pyautogui.locateOnScreen('9_validation.png', confidence=0.9)

        if NOVE_validation is not None:
            pyautogui.click(NOVE_validation)
            temporizador = 500
            NOVE_validation = None
            print(date_time(), '#9 - LAST VALIDATION - COMPLETE')
            def_error = 0
            return def_error

        else:
            temporizador += 2
            time.sleep(2)
    if temporizador == 20:
        print(date_time(), '#9 - LAST VALIDATION - FAIL')
        def_error = 1
        return def_error


def alt_tab():
    if tab > 1:
        pyautogui.keyDown('alt')
        time.sleep(0.2)
        for h in range(tab - 1):
            pyautogui.press('tab')
            time.sleep(0.2)
        time.sleep(0.2)
        pyautogui.keyUp('alt')
        time.sleep(0.4)
    else:
        pass


def date_time():
    now = datetime.now()  # current date and time

    date_time = now.strftime("%d/%m/%Y, %H:%M:%S")
    return date_time


# Tratamentos
def full_entrance():
    f_cinco()

    if connect_wallet() == 0:
        pass
    else:
        full_entrance()
        return

    if meta_mask() == 0:
        pass
    else:
        full_entrance()
        return

    if assinar() == 0:
        pass
    else:
        full_entrance()
        return

    if heroes() == 0:
        pass
    else:
        full_entrance()
        return

    if scroll() == 0:
        pass
    else:
        full_entrance()
        return

    if click_heroes() == 0:
        pass
    else:
        full_entrance()
        return

    if close_heroes() == 0:
        pass
    else:
        full_entrance()
        return

    if treasure_hunter() == 0:
        # TALVEZ ISSO FAÇA SENTIDO ATÉ DEMAIS
        return
    else:
        full_entrance()
        return


def error():
    f_cinco()

    if connect_wallet() == 0:
        pass
    else:
        error()
        return

    if meta_mask() == 0:
        pass
    else:
        error()
        return

    if assinar() == 0:
        pass
    else:
        error()
        return

    if treasure_hunter() == 0:
        # TALVEZ ISSO FAÇA SENTIDO ATÉ DEMAIS
        return
    else:
        error()
        return


# MAIN

maps = 1
errors = 0
timer = 0
last_validation_bool = 0

ativador = True

while ativador:
    for k in range(tab):
        full_entrance()
        alt_tab()

# 18 Minutos neste loop
    while timer <= 1080: #1080
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
                treasure_hunter()
                alt_tab()

            last_validation_bool = 1

            execution_time = round((time.time() - start_time), 2)
            timer += execution_time

        else:
            #time.sleep(5)
            alt_tab()

            execution_time = round((time.time() - start_time), 2)
            timer += execution_time

    print(date_time(), '| PAUSA DE DESCANSO - INICIADA')
    start_time = time.time()
    # 62 minutos de parada TOTAL no SCRIPT.
    time.sleep(3720) #3720
    execution_time = round((time.time() - start_time), 2)
    timer += execution_time
    print(date_time(), '| PAUSA DE DESCANSO - COMPLETE')
