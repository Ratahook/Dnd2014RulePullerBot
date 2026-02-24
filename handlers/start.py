from telebot.types import Message
from loader import bot


@bot.message_handler(commands=["start", "help"])
def bot_start(message: Message):
    bot.reply_to(message, f"Привет, {message.from_user.full_name}!\nСейчас реализованы следующие команды:\nПоиск по названию: /name [Часть или полное название заклинания]\nПоиск по кругу заклинания: /lvl [Цифра круга]\nПоиск по школе магии: /school\nПоиск по классу днд 2014: /class")
