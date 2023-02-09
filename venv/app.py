import telebot
from config import keys, TOKEN
from extensions import ConvertionException, CryptoConverter
bot = telebot.TeleBot(TOKEN)



@bot.message_handler(commands=['start','help'])
def help(message: telebot.types.Message):
    text = 'для начала работы введите: название валюты, в какую валюту перевести, количество переводимой валюты'
    bot.reply_to(message, text)


@bot.message_handler(commands=['values'])
def values(message:telebot.types.Message):
    text = 'Доступные валюты для перевода'
    for key in keys.keys():
        text = '\n'.join((text, key, ))
    bot.reply_to(message,text)


@bot.message_handler(content_types = ['text', ])
def convert(message: telebot.types.Message):
    try:
        values = message.text.split(' ')

        if len(values) != 3:
            raise ConvertionException('не верное количество значений, пожалуйста введите три значения')

        quote, base, amount = values
        total_base = CryptoConverter.convert(quote, base, amount)
    except ConvertionException as e:
        bot.reply_to(message, f'ошибка полльзователя.\n {e}')

    except Exception as e:
        bot.reply_to(message, f'не удалось обработать команду \n {e}')
    else:
        k = float(total_base)* float(amount)
        text = f'цена {amount} {quote} в {base} - {k}'
        bot.send_message(message.chat.id, text)


bot.polling(none_stop=True)

