import telebot
from functions import *
import creds

password = "123456789"
global is_typing_date
is_typing_date = False
global is_typing_password
is_typing_password = False
global is_typing_homework
is_typing_homework = False
global text_type
bot = telebot.TeleBot(creds.teletoken)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, text="Привет! Я бот для рассылания чего-либо. "
                     "Для того чтобы отправить сообщение, ты должен написать команду /send и ввести пароль. "
                     "Для прочтения записи нужно написать команду /read.")


@bot.message_handler(commands=['read'])
def read(message):
    bot.send_message(message.chat.id, text=rm())


@bot.message_handler(commands=['send'])
def send(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    button1 = telebot.types.InlineKeyboardButton(text="Обычный", callback_data="1")
    button2 = telebot.types.InlineKeyboardButton(text="Повторяющийся", callback_data="2")
    button3 = telebot.types.InlineKeyboardButton(text="Отмена", callback_data="N")
    keyboard.add(button1)
    keyboard.add(button2)
    keyboard.add(button3)
    bot.send_message(message.chat.id, text="Какой тип сообщения вы хотите отправить?", reply_markup=keyboard)

'''@bot.message_handler(commands=['comm'])
def add_comment(message):
    global username
    keyboard = telebot.types.InlineKeyboardMarkup()
    button1 = telebot.types.InlineKeyboardButton(text="Да", callback_data="Y")
    button2 = telebot.types.InlineKeyboardButton(text="Нет", callback_data="N")
    keyboard.add(button1)
    keyboard.add(button2)
    bot.send_message(message.chat.id, text="Вы хотите написать комментарий?", reply_markup=keyboard)
    username = bot.get_chat_member(message.chat.id, message.from_user.id).user.first_name'''


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    global is_typing_password
    global is_typing_date
    global text_type
    if call.message and is_typing_password:
        if call.data == "N":
            is_typing_password = False
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="ввод остановлен...")
    elif call.message:
        if call.data == "1":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="введите пароль")
            is_typing_password = True
            text_type = 'usual'
        if call.data == "2":
            is_typing_date = True
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text='введите дату, до которой будет выводиться повторяющееся сообщение'
                                       '(без пробелов, в формате "ГГГГ-ММ-ДД", использовать только тире')
            is_typing_password = False
            text_type = 'repeating'
        elif call.data == "N":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="ну ладно(")


@bot.message_handler(func=lambda message: True)
def answer(message):
    global is_typing_password
    global is_typing_homework
    global is_typing_date
    global text_type
    if is_typing_password:
        if message.text == password:
            bot.send_message(message.chat.id, text="вводите сообщение")
            is_typing_password = False
            is_typing_homework = True
        else:
            keyboard2 = telebot.types.InlineKeyboardMarkup()
            button1 = telebot.types.InlineKeyboardButton(text="Отмена ввода", callback_data="N")
            keyboard2.add(button1)
            bot.send_message(message.chat.id, text="неправильный пароль.", reply_markup=keyboard2)
    elif is_typing_homework:
        if text_type == 'usual':
            sm(message.text)
            is_typing_homework = False
        else:
            srm(message.text)
            is_typing_homework = False
    elif is_typing_date:
        load_date(message.text)
        bot.send_message(chat_id=message.chat.id, text="введите пароль")
        is_typing_password = True
        is_typing_date = False
    else:
        bot.send_message(message.chat.id, text="пожалуйста, не пиши мне просто так, хорошо?")


bot.polling()
