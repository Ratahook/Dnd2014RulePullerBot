from telebot.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from loader import bot
from api.dndapi import getspellbyclass
from keyboards.dnd_classes import gen_markup

@bot.message_handler(commands=["class"])
def lvl_choice(message: Message):
    bot.reply_to(message, f"Выберите класс заклинаний ниже: ",
        reply_markup=gen_markup(),
    )

@bot.callback_query_handler(func=lambda callback_query: callback_query.data in [
    "barbarian", "bard", "cleric", "druid", "fighter", "monk",
    "paladin", "ranger", "rogue", "sorcerer", "warlock", "wizard"
])
def school_answer(callback_query):
    bot.edit_message_reply_markup(
        callback_query.from_user.id, callback_query.message.message_id
    )
    spell_list = '\n\n'.join(getspellbyclass(callback_query.data))
    bot.send_message(callback_query.from_user.id, f"Вот совпадения из списка заклинаний:\n\n{spell_list}",)