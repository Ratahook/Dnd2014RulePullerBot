from telebot.types import Message
from loader import bot
from api.dndapi import getspellbyschool
from keyboards.schools import gen_markup




@bot.message_handler(commands=["school"])
def lvl_choice(message: Message):
    bot.reply_to(message, f"Выберите школу заклинаний ниже: ",
        reply_markup=gen_markup(),
    )

@bot.callback_query_handler(func=lambda callback_query: callback_query.data in [
    "abjuration", "conjuration", "divination", "enchantment",
    "evocation", "illusion", "necromancy", "transmutation"
])
def school_answer(callback_query):
    bot.edit_message_reply_markup(
        callback_query.from_user.id, callback_query.message.message_id
    )
    spell_list = '\n\n'.join(getspellbyschool(callback_query.data))
    bot.send_message(callback_query.from_user.id, f"Вот совпадения из списка заклинаний:\n\n{spell_list}",)