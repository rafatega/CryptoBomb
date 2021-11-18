import requests
import json
from getmac import get_mac_address as gma

# pip install getmac
'''
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

authentication = 0

while authentication == 0:

    username = input('Username: ')
    password = input('Password: ')

    try:
        if loads_json[username]:
            api_password = loads_json[username]['password']
            api_mac = loads_json[username]['mac']
            mac_address = gma()

            if password == api_password and mac_address == api_mac:
                print('Entrou com sucesso')

                authentication = 1

            elif password == api_password and mac_address != api_mac:
                print('Este computador não tem permissão para executar o BOT.')
            else:
                print('Credenciais erradas, tente novamente.')

    except:
        print('Credenciais erradas, tente novamente.')


print('Você está dentro do código.')'''


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


auth()
