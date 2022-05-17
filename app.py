
import telebot
from config import keys, TOKEN
from utils import CryptoConverter, ConvertionException

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def echo_test(message: telebot.types.Message):
    text = 'Для начала работы введите сообщение боту в следующем виде:\n<имя валюты> \
<в какую валюту перевести> ' \
           '<количество валюты>\nУвидеть список всех доступных валют: /values'
    bot.reply_to(message, text)


@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for key in keys.keys():
        text = '\n'.join((text, key,))
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):
    try:
        values = message.text.split(' ')

        if len(values) != 3:
          raise ConvertionException('Too many param')
        quote, base, amount = values
        total_base = CryptoConverter.convert(quote, base, amount)
    except ConvertionException as e:
        bot.reply_to(message, f'User exception. \n{e}')
    except Exception as e:
        bot.reply_to(message, f'Failed command\n{e}')
    else:

        text = f'Price {amount} {quote} in {base} - {total_base}'
        bot.send_message(message.chat.id, text)


bot.polling()
