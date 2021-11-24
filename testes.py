import time
import pyautogui
import random


def teste():
    return random.randint(3, 9)


teste()
print(teste)






'''a = 2

def error():
    pergunta = int(input('Erro? '))
    if pergunta == 0:
        return 0
    else:
        return 1

verdade = True

while verdade is True:
    if error() == 1:
        pass'''







'''def pergunta():
    opa = input('Digite: ')

    if opa == '1':
        val = 1
        return val
    else:
        val = 0
        return val


ativador = True


def main():
    while ativador is True:

        if pergunta() == 1:
            print('Resposta = 1')

        else:
            main()


main()'''









'''time.sleep(5)

def restart():
    pyautogui.press('f5')
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
            def_error = 0
            return def_error
        else:
            temporizador += 2
            time.sleep(2)
    if temporizador == 20:
        print('Temporizador: ', temporizador)
        def_error = 1
        return def_error



# MAIN
restart()

if connect_wallet() == 0:
    print("Return 0")
else:
    print('Return 1')'''
