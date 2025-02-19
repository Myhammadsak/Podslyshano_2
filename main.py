import telebot

API_TOKEN = '7669890753:AAGRThheKHp9tf15UB9m67q10YUywT2jVsI'

bot = telebot.TeleBot(API_TOKEN)
anime = 0


@bot.message_handler(commands=['start'])
def send_welcome(message):
      bot.send_message(message.chat.id, "Привет, я бот 'Подслушано 2' для предложки постов!\n/post - предложить пост")

@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.send_message(message.chat.id, '/start - Начальная кманда\n/post - Команда для предложки поста')

@bot.message_handler(commands=['post'])
def send_welcome(message):
    global anime
    send = bot.send_message(message.chat.id, 'Отправь сюда пост'.format(message.from_user))
    anime = 1
    bot.register_next_step_handler(send, admin_message)

@bot.message_handler(func=lambda message: True)
def admin_message(message):
    global anime
    if anime == 1:
        bot.reply_to(message, 'Пост отправлен на рассмотрение!')
        bot.forward_message(1420386760, message.chat.id, message.message_id)
        bot.forward_message(1068456643, message.chat.id, message.message_id)
        bot.copy_message(6460908058, message.chat.id, message.message_id)
        anime = 0


bot.infinity_polling(timeout=10, long_polling_timeout = 5)