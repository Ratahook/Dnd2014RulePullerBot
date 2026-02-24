from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

def gen_markup():
    # Создаём кнопки для 13 классов D&D
    button_1 = InlineKeyboardButton(text="Barbarian 🪓", callback_data="barbarian")
    button_2 = InlineKeyboardButton(text="Bard 🎵", callback_data="bard")
    button_3 = InlineKeyboardButton(text="Cleric ✝️", callback_data="cleric")
    button_4 = InlineKeyboardButton(text="Druid 🌿", callback_data="druid")
    button_5 = InlineKeyboardButton(text="Fighter ⚔️", callback_data="fighter")
    button_6 = InlineKeyboardButton(text="Monk 🥋", callback_data="monk")
    button_7 = InlineKeyboardButton(text="Paladin 🛡️", callback_data="paladin")
    button_8 = InlineKeyboardButton(text="Ranger 🏹", callback_data="ranger")
    button_9 = InlineKeyboardButton(text="Rogue 🗡️", callback_data="rogue")
    button_10 = InlineKeyboardButton(text="Sorcerer 🔥", callback_data="sorcerer")
    button_11 = InlineKeyboardButton(text="Warlock 👁️", callback_data="warlock")
    button_12 = InlineKeyboardButton(text="Wizard 📖", callback_data="wizard")

    keyboard = InlineKeyboardMarkup()
    keyboard.add(
        button_1, button_2,
        button_3, button_4,
        button_5, button_6,
        button_7, button_8,
        button_9, button_10,
        button_11, button_12,
    )
    return keyboard