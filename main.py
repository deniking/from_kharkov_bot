# bot
import telebot
import random

bot = telebot.TeleBot('5507838809:AAHtBfJfWZ1AvNqG5X7ua2Fw-0XriEaHvqg')


@bot.message_handler(content_types=['text'])
def handle_text(message):
    msg=message.text
    msg=msg.lower()
    if (u'привет' in msg):
        privet = ["Привет лапух", "Приветик", "Че хотел?", "Ну и дальше что?", "Привед-ВЕДМЕД 😂"]
        bot.send_message(message.chat.id, random.choice(privet))
    elif (u'как дела' in msg):
        privet = ["Дела у прокурора", "Дела делишки", "Че хотел то?", "Денег не дам", "Зашибись😂"]
        bot.send_message(message.chat.id, random.choice(privet))
    elif (u'что делаешь' in msg):
        privet = ["сухари сушу", "Дела делаю", "Бухаю😂?", "НИХ@Я", "читаю что тут пишут"]
        bot.send_message(message.chat.id, random.choice(privet))
    elif (u'прилет' in msg):
        privet = ["ТСССС....🤨", "ох уж эти орки", "про место молчим!", "бух-бах", "Бля, достали 😒"]
        bot.send_message(message.chat.id, random.choice(privet))
    elif (u'доброе утро' in msg):
        privet = ["утро добрым не бывает 😂", "добрее видали ", "и вам не хворать", "✌️", "че не спишь?"]
        bot.send_message(message.chat.id, random.choice(privet))
    elif (u'как обстановка' in msg):
        privet = ["В Багдаде все спокойно", "Бегут орки - бегут", "по-прежнему не понятно", "та такое", "а у вас как?"]
        bot.send_message(message.chat.id, random.choice(privet))
    elif (u'здоров' in msg):
        privet = ["Здоровее видали😂", "Здоров без всяких докторов", "как ваше ничего?😂", "хаюшки-бабаюшки", "прЮвет😂"]
        bot.send_message(message.chat.id, random.choice(privet))
    elif(u'да' in msg):
        privet = ["БОЛДА😂", "да-да", "да-туда😂", "караганДА"]
        bot.send_message(message.chat.id, random.choice(privet))

bot.polling()
