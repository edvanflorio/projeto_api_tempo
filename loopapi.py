import requests
import logging

logging.basicConfig(filename='weather.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

with open('resultados.txt', 'w') as arquivo_resultados:

    cidades = [
        'macapa',
        'santana',
        'fazendinha',
        'mazagão',
        'mazagão velho',
        'porto grande',
        'pedra branca',
        'amapa',
        'lourenço',
        'oiapoque',
        'itaubal'
    ]

    api_key = 'xxxxxxx'
    base_url = 'https://api.openweathermap.org/data/2.5/weather'

    for cidade in cidades:
        params = {
            'q': cidade,
            'appid': api_key,
            'units': 'metric',
            'lang': 'pt_br'
        }

        try:
            response = requests.post(base_url, params=params)
            data = response.json()

            if response.status_code == 200:
                temperature = data['main']['temp']
                weather_description = data['weather'][0]['description']
                humidity = data['main']['humidity']

                arquivo_resultados.write(f'informações meteorologicas para {cidade}:\n')
                arquivo_resultados.write(f'Temperatura: {temperature}°C\n')
                arquivo_resultados.write(f'Clima: {weather_description.capitalize()}\n')
                arquivo_resultados.write(f'Umidade: {humidity}\n')
                arquivo_resultados.write('\n')
                
                logging.info(f'Falha na solicitação a API {cidade}')
            else:
                print(f'Falha na solicitação a API para {cidade}')

        except Exception as e:

            logging.error(f'Erro ao obter informações meteorologicas para {cidade}: {str(e)}')
            print(f'Erro ao obter informações meteorologicas para {cidade}: {str(e)}')
print('Resultados salvos em resultados.txt')
