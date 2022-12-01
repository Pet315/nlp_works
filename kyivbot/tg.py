import telebot
import config
# from kyivbot.View import View
from kyivbot.resources import messages

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, messages.greeting)
    # view = View()
    # view.output(messages.main_menu, message)


@bot.message_handler(content_types=['text'])
def input(message):
    pass


# RUN
if __name__ == "__main__":
    bot.polling(none_stop=True)