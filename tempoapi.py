import requests

city = (input('Digite a cidade desejada: '))

url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=xxxxxxx&units=metric&lang=pt_br'


try: 
    response = requests.post(url)
    data = response.json()

    if response.status_code == 200:
        temperature = data['main']['temp']
        weather_description = data['weather'][0]['description']
        humidity = data['main']['humidity']

        print(f'Temperatura: {temperature}°C')
        print(f'Clima: {weather_description.capitalize()}')
        print(f'Umidade {humidity}%')
    else:
        print('Falha na solicitação à API')

except Exception as e:
    print(f'Erro: {str(e)}')
