# import random
# import telebot
# import webbrowser
# from telebot import types 

# bot = telebot.TeleBot('6816795501:AAGVvdEFpWF4rieRiDdY2KgYipom_jm4NeA')

# #Варианты ответов пользователю, если тот ввел непонятное боту сообщение
# answers = ['Я не понял, что хочешь сказать.', 'Извини, я тебя не понимаю.', 'Я не знаю такой команды']

# #Обработка команды /start
# @bot.message_handler(commands=['start'])
# def welcome(message):
#     #Добавляем кнопки, которые будут появляться после выхода команды /start
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     button1 = types.KeyboardButton('Еда')
#     button2 = types.KeyboardButton('Настройки')
#     button3 = types.KeyboardButton('Справка')
#     #Разделяю кнопки по строкам так, чтобы товары были отдельно от остальных кнопок 
#     markup.row(button1)
#     markup.row(button2,button3)

#     if message.text == '/start':
#         #Отправляю привественный текст
#         bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}!\nУ меня ты сможешь купить некоторые пиццы! \nКонтакт моего разработчика: https://t.me/edzen24', reply_markup=markup)

#     else:
#         bot.send_message(message.chat.id, 'Перекинул тебя в главном меню! Выбирай!', reply_markup=markup)


# #Обработка обычных текстовых команд, описанных в кнопках
# @bot.message_handler()
# def info(message):
#     if message.text == 'Еда':
#         goodsChapter(message)
#     elif message.text == 'Настройки':
#         settingsChapter(message)
#     elif message.text == 'Справка':
#         infoChapter(message)

# #Функция, отвечающая за раздел еды
# def goodsChapter(message):
#     #Кнопки для еды
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     button1 = types.KeyboardButton(' Пеперони - 340с')        
#     button2 = types.KeyboardButton(' Маргарита - 290с')        
#     button3 = types.KeyboardButton(' Охотничий - 410с')        
#     button4 = types.KeyboardButton(' Миксовый - 550с')        
#     button5 = types.KeyboardButton(' Назад в меню')        
#     markup.row(button1,button2)
#     markup.row(button3,button4)
#     markup.row(button5)
#     #Отправляем сообщение с прикрепленными к нему кнопками товаров 
#     bot.send_message(message.chat.id, 'Вот все блюда, которые сейчас находятся в продаже:', reply_markup=markup)

# def settingsChapter(message):
#     pass

# def infoChapter():
#     pass








# #Строчка, чтобы программа не останавливалась
# bot.polling(none_stop=True)        



 