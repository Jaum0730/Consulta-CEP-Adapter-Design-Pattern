import requests

def Adaptercep(cep):
    if len(cep) == 8 or not cep.isdecimal:
        consumo_api = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
        cep_data = consumo_api.json()

        if 'erro' not in cep_data.keys():
            print(f'\033[46mCEP consultado:\033[m \033[36m{cep_data["cep"]}\033[m')

            print(f'\033[43mEndereço:      \033[m \033[33m{cep_data["logradouro"]} {cep_data["complemento"]}\033[m')

            print(f'\033[42mLocalidade/UF: \033[m \033[32m{cep_data["localidade"]}-{cep_data["uf"]}\033[m')

        else:  # 01001000
            print(f'\033[31mCEP {cep} inválido ou inexistente!\033[m')
    else:
        print(f'\033[31mCEP {cep} inválido!\033[m')
        quit()


