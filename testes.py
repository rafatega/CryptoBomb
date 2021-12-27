import time
import pyautogui

n = int(input( 'Numero: '))

n = n * 2

j = 0

for i in range(n):
    if i%2 == 0:
        print('Entrou na soma: ', i)
        j += i
    else:
        pass

print('Resultado das somas: ', j)