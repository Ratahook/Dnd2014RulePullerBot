from telebot.types import Message
from loader import bot
from api.dndapi import getspellbyname

@bot.message_handler(commands=["name"])
def lvl_searcher(message: Message):
    args = message.text.split()
    if len(args) < 2:
        bot.reply_to(message, "Формат: /lvl_search [Spell name]")
        return
    if len(args) == 2:
        name_arg = args[1]
    if len(args) > 2:
        arg_list = []
        for index, value in enumerate(args):
            if index != 0:
                arg_list.append(value)
        name_arg = ' '.join(arg_list)
        print()
    spell_list = '\n\n'.join(getspellbyname(name_arg))
    bot.reply_to(message, f"Вот совпадения из списка заклинаний:\n\n{spell_list}")