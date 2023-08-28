# Задача 3. Добавьте в telegram-бота игру «Угадай числа». Бот загадывает число от 1 до 1000. 
# Когда игрок угадывает его, бот выводит количество сделанных ходов.
import telebot
import requests
import time
import random
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

bot = telebot.TeleBot("6510425737:AAEZUhNTIqnQ0oGzdwPndzHwqdwTW73J_Uc")

bot.current_number = None

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")
        
@bot.message_handler(commands=['play'])
def send_welcome(message):
    min = 1
    max = 5
    bot.reply_to(message, f"Привет! Я загадал число от {min} до {max}. Попробуй угадать его!")

    # Загадываем число
    bot.current_number = random.randint(min, max)
    bot.num_guesses = 0

def check_number(message):
    if bot.current_number is None:
        return False
    return True

@bot.message_handler(func=check_number)
def guess_number(message):
    if bot.current_number is None:
        return
    try:
        guess = int(message.text)
    except ValueError:
        bot.reply_to(message, "Пожалуйста, введите число.")
        return

    bot.num_guesses += 1

    if guess < bot.current_number:
        bot.reply_to(message, "Загаданное число больше.")
    elif guess > bot.current_number:
        bot.reply_to(message, "Загаданное число меньше.")
    else:
        bot.reply_to(message, f"Поздравляю, вы угадали число за {bot.num_guesses} попыток!")
        bot.current_number = None
        bot.num_guesses = 0
	
def get_weather():
    session = requests.Session()
    url = 'https://www.gismeteo.com/weather-belgorod-5039/now/'
    ua = UserAgent()
    headers = {
                'User-Agent': ua.random,
                'DNT': '1',
                'Connection': 'keep-alive',
                'Sec-Fetch-Dest': 'document',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-Site': 'none',
                'Sec-Fetch-User': '?1',
                'Cache-Control': 'max-age=0',
                'TE': 'trailers'
            }
    request = session.get(url, headers=headers)
    soup = BeautifulSoup(request.content, 'html.parser')

    temp = 'Температура: ' + soup.find('span', class_='unit unit_temperature_c').text + '°C'
    feel_temp = 'Ощущается как: ' + soup.find('div', class_='now-feel').find('span', class_='unit unit_temperature_c').text + '°C'

    sunrise = 'Рассвет: ' + soup.find('div', class_='now-astro-sunrise').find('div', class_='time').text
    sunset = 'Закат: ' + soup.find('div', class_='now-astro-sunset').find('div', class_='time').text

    str_wind = soup.find('div', class_='unit unit_wind_m_s').text
    wind = ''
    for i in range(len(str_wind)):
        if str_wind[i].isdigit():
            wind = 'Ветер: ' + str_wind[:i + 1] + ' м/с'
    darii = soup.find('div', class_='unit unit_wind_m_s').find('div', class_='item-measure').find_all('div')[1].text

    str_pressure = soup.find('div', class_='unit unit_pressure_mm_hg_atm').text
    pressure = ''
    for i in range(len(str_pressure)):
        if str_pressure[i].isdigit():
            pressure = 'Давление: ' + str_pressure[:i + 1] + ' мм рт. ст.'

    humidity = 'Влажность: ' + soup.find('div', class_='now-info-item humidity').find('div', class_='item-value').text + '%'

    gm = 'Геомагнитная активность: ' + soup.find('div', class_='now-info-item gm').find('div', class_='item-value').text + '/9'

    water = 'Температура воды: ' + soup.find('div', class_='now-info-item water').find('div', class_='item-value').find('span', class_='unit unit_temperature_c').text + '°C'

    result = temp + '\n' + feel_temp + '\n' + sunrise + '\n' + sunset + '\n' + wind + ' ' + darii + '\n' + pressure + '\n' + humidity + '\n' + gm + '\n' + water
    
    return result

@bot.message_handler(content_types=['text'])
def greetings(message):
    # print(message)
    text = message.text
    if 'привет' in text:
        bot.reply_to(message, f'Привет, {message.from_user.first_name}')
    elif 'погода'in text:
        bot.reply_to(message, get_weather())
    elif text == 'котик':
        req = requests.get(f'https://cataas.com/cat?{time.time()}')
        bot.send_photo(message.chat.id, req.content)


bot.polling()


