from telebot.types import Message
from loader import bot
from api.dndapi import getspellbylvl

@bot.message_handler(commands=["lvl"])
def lvl_searcher(message: Message):
    args = message.text.split()
    if len(args) < 2:
        bot.reply_to(message, "Формат: /lvl_search [Spell level]")
        return
    level_arg = int(args[1])
    spell_list = '\n'.join(getspellbylvl(level_arg))
    bot.reply_to(message, f"Вот заклинания {level_arg} круга:\n{spell_list}")