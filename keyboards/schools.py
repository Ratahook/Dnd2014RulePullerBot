from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

def gen_markup():
    # Создаём кнопки для 8 стандартных школ магии
    button_1 = InlineKeyboardButton(text="Abjuration 🛡️", callback_data="abjuration")
    button_2 = InlineKeyboardButton(text="Conjuration ✨", callback_data="conjuration")
    button_3 = InlineKeyboardButton(text="Divination 🔮", callback_data="divination")
    button_4 = InlineKeyboardButton(text="Enchantment 💫", callback_data="enchantment")
    button_5 = InlineKeyboardButton(text="Evocation 🔥", callback_data="evocation")
    button_6 = InlineKeyboardButton(text="Illusion 🎭", callback_data="illusion")
    button_7 = InlineKeyboardButton(text="Necromancy ☠️", callback_data="necromancy")
    button_8 = InlineKeyboardButton(text="Transmutation ⚗️", callback_data="transmutation")

    keyboard = InlineKeyboardMarkup()
    keyboard.add(
        button_1, button_2,
        button_3, button_4,
        button_5, button_6,
        button_7, button_8
    )
    return keyboard