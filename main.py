# bot
import telebot
import random
import anekdot

bot = telebot.TeleBot('5507838809:AAHtBfJfWZ1AvNqG5X7ua2Fw-0XriEaHvqg')


@bot.message_handler(content_types=['text'])
def handle_text(message):
    msg=message.text
    msg=msg.lower()
    if (u'привет' in msg):
        #privet = ["Привет лапух", "Приветик", "Че хотел?", "Ну здравствуй 😁", "Привед-ВЕДМЕД 😂"]
        bot.reply_to(message, "Привед-ВЕДМЕД 😂 \nСЛУШАЙ от меня АНЕКДОТ 😂")
        bot.send_message(message.chat.id, anekdot.list[0])
        del anekdot.list[0]
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEFYlli4CL47Pv3Xu7uk2FW_i6Kb_kLxAACjwEAAladvQqTBL2ODiSRxikE')
    elif (msg == 'привет из россии' or msg == 'россия'):
        privet = ["Рашка-пидорашка😁", "Биомусор из Рашки", "Оркостан", "Кацапское удобрение 😁", "Рашисты-фашисты"]
        bot.reply_to(message, random.choice(privet))
        stick = ["CAACAgIAAxkBAAEFYJ9i3u-UC0gq3y52QzkojfC30d2OkgAC0wIAAgaRjBe5kRzrUAy8aikE",
                 "CAACAgIAAxkBAAEFYKli3u-6Y_Veb1ayO-e8-Lk_zW_UBAAC8gIAAgaRjBf2OH4xSJqHJikE",
                 "CAACAgIAAxkBAAEFYKti3u_VCbvhay5X-ZbqME1f6yp8LwACOwMAAgaRjBdh3FhOcCqFeykE",
                 "CAACAgIAAxkBAAEFYKNi3u-ZoVgVGAwnrhWidgaHtNqCDgACOwMAAgaRjBdh3FhOcCqFeykE",
                 "CAACAgIAAxkBAAEFYKRi3u-a8kYG-fQDaLp81AnKTfwHrQAClgcAAipVGAKLbGVlcW-KJCkE",
                 "CAACAgIAAxkBAAEFYK1i3vK6X514U62nZuQU_wNpiDaF_AAC6wIAAgaRjBdLVw_io-XDXSkE",
                 "CAACAgIAAxkBAAEFYK9i3vK9QhNu332eYxNSX2Z2DDrOPQAC5wIAAgaRjBdrCXEuHNx8FCkE",
                 "CAACAgIAAxkBAAEFYLFi3vK_BoARXOK3djlttkPAAfBoQAAC3AIAAgaRjBfEX6sjjsH5VikE"]
        bot.send_sticker(message.chat.id, random.choice(stick))

    elif (u'как дела' in msg):
        privet = ["Дела у прокурора", "Дела делишки", "Че хотел то?", "Денег не дам", "Зашибись😂"]
        bot.reply_to(message, random.choice(privet))
    elif (u'что делаешь' in msg):
        privet = ["сухари сушу", "Дела делаю", "Бухаю😂?", "НИХ@Я", "читаю что тут пишут"]
        bot.reply_to(message, random.choice(privet))
    elif (u'прилет' in msg):
        privet = ["ТСССС....🤨", "ох уж эти орки", "про место молчим!", "бух-бах", "Бля, достали 😒"]
        bot.reply_to(message, random.choice(privet))
    elif (u'доброе утро' in msg):
        privet = ["утро добрым не бывает 😂", "добрее видали ", "и вам не хворать", "✌️", "че не спишь?"]
        bot.reply_to(message, random.choice(privet))
    elif (u'как обстановка' in msg):
        privet = ["В Багдаде все спокойно", "Бегут орки - бегут", "по-прежнему не понятно", "та такое", "а у вас как?"]
        bot.reply_to(message, random.choice(privet))
    elif (u'здоров' in msg):
        privet = ["Здоровее видали😂", "Здоров без всяких докторов", "как ваше ничего?😂", "хаюшки-бабаюшки", "прЮвет😂"]
        bot.reply_to(message, random.choice(privet))
    elif(msg == "да" or msg== "да да"):
        privet = ["БАЛДА😂", "да-да", "да-туда😂", "караганДА"]
        bot.reply_to(message, random.choice(privet))
    elif (u'что вы тут' in msg):
        privet = ["мы то тут, а вы там😂", "все отлично!", "а вы что тут?", "а мы тут плюшками балуемся😂", "наблюдаем за всеми😂"]
        bot.reply_to(message, random.choice(privet))
    elif (u'слава украине' in msg):
        privet = ["Героям слава 🇺🇦 ", "русня здохла на полях😂", "смерть врогам!", "Украина сильная страна", "Бренд русского фарша 😂"]
        bot.reply_to(message, random.choice(privet))
    elif (u'слава росии' in msg):
        privet = ["В составе Украины 🇺🇦 ", "Русский биомусор😂", "сдохни падаль!", "твой IP уже записали, жди в гости, мразь", "Сдохла ваша раша"]
        bot.reply_to(message, random.choice(privet))
    elif (u'я спать' in msg):
        privet = ["А я еще нет 🤷‍♂️", "споки-ноки😂", "спят усталые игрушки", "спать не срать - можно подождать 😂 ", "ну и спи 😂"]
        bot.reply_to(message, random.choice(privet))
    elif (u'спокойной ночи' in msg):
        privet = ["не спать 😂", "споки-ноки😂", "спят усталые игрушки", "Спокойной и тихой ночи ", "ну и спи 😂"]
        bot.reply_to(message, random.choice(privet))
    elif (msg== "ем"):
        privet = ["приятного аппетита", "нямка", "вкусняхи лопаешь?", "фото в студию что жрешь 😂", "обжора"]
        bot.reply_to(message, random.choice(privet))
    elif (u'играть' in msg):
        privet = ["сразимся на шпагах?", "я чемпион по подводным шахматам", "GO-В-КС:GO", "давай в покер забацаем?", "принимаю ставки"]
        bot.reply_to(message, random.choice(privet))
    elif (u'где все' in msg):
        privet = ["тута мы, и не уходили", "русню ебашем 😂", "жрут наверно и не признаются", "наверно в подвале", "в полях воробья ловят"]
        bot.reply_to(message, random.choice(privet))
    elif (u'тихо' in msg):
        privet = ["хорошо когда тихо", "тишина и мертвые с косами стоят 😂", "тихо и ладно", "аж странно когда тихо", "тихо потому что русня сдохла вся"]
        bot.reply_to(message, random.choice(privet))
    elif (u'сирена' in msg):
        privet = ["все в укрытие", "правило двух стен помним ?", "от ори проклятые - заебали", "ВАРНИНГ😂", "Лучше спрячусь и я"]
        bot.reply_to(message, random.choice(privet))
    elif (u'ахаха' in msg):
        privet = ["смешно?", "че ты ржёшь?", "хахатушки - ребятушки", "хи-хи😂", "расскажи и мне, вместе поржём 😂"]
        bot.reply_to(message, random.choice(privet))


bot.polling()
