# bot
import telebot
import random
import anekdot

bot = telebot.TeleBot('5507838809:AAHtBfJfWZ1AvNqG5X7ua2Fw-0XriEaHvqg')


@bot.message_handler(content_types=['text'])
def handle_text(message):
    msg=message.text
    msg=msg.lower()
    if (msg== 'доброе утро' or msg== 'доброго ранку'):
        #privet = ["Привет лапух", "Приветик", "Че хотел?", "Ну здравствуй 😁", "Привед-ВЕДМЕД 😂"]
        bot.reply_to(message, "Доброго ранку ми з Ураїни 🇺🇦 \nСЛУШАЙ от меня АНЕКДОТ 😂")
        bot.send_message(message.chat.id, anekdot.list[0])
        del anekdot.list[0]
        stick = ["CAACAgIAAxkBAAEFYlli4CL47Pv3Xu7uk2FW_i6Kb_kLxAACjwEAAladvQqTBL2ODiSRxikE",
                 "CAACAgIAAxkBAAEFb51i6AKSo3pZRT9xPrWkj8jWE0-NtwACAQADwDZPExguczCrPy1RKQQ",
                 "CAACAgIAAxkBAAEFb8Ji6Az_iEhlyG_J5t1TAQqnpt1sCAACWAADUomRI32OzA4HOEuGKQQ",
                 "CAACAgIAAxkBAAEFb8xi6A1biEPLVN2HFsJZurwAAVHfC4wAAucaAAK4hBhIJjH83tMgCW4pBA",
                 "CAACAgIAAxkBAAEFb_Vi6BHGUmvAjJMU-rscfwGnU8NvjAACRBkAAgjh2UlSqev16oISqCkE"]
        bot.send_sticker(message.chat.id, random.choice(stick))
        #bot.send_animation(message.chat.id, 'https://media0.giphy.com/media/QLKSt3wQqlj7a/giphy.gif?cid=790b7611bb1c81a8ea8b7c50f16c0ed742c879d39378f1ba&rid=giphy.gif&ct=g')

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
    elif (u'привет' in msg):
        #privet = ["утро добрым не бывает 😂", "добрее видали ", "и вам не хворать", "✌️", "че не спишь?"]
        animation = ['https://media0.giphy.com/media/QLKSt3wQqlj7a/giphy.gif?cid=790b7611bb1c81a8ea8b7c50f16c0ed742c879d39378f1ba&rid=giphy.gif&ct=g',
                     'https://media0.giphy.com/media/G3Hu8RMcnHZA2JK6x1/giphy.gif?cid=ecf05e47cfkbpa0jmmwo01ibr3qc7hv8nsjl2wkyi9um65a1&rid=giphy.gif&ct=g',
                     'https://media3.giphy.com/media/3PAL5bChWnak0WJ32x/giphy.gif?cid=ecf05e47gh72mldgqjilnuzm90ilqcao2wtyozobfk5t5s5v&rid=giphy.gif&ct=g',
                     'https://media3.giphy.com/media/tpwdIZZ20RQKQ/giphy.gif?cid=ecf05e47vcoppyqgofmu5b1oyva83iugsx4vu1n09ysy7doi&rid=giphy.gif&ct=g',
                     'https://media2.giphy.com/media/xUySTQZfdpSkIIg88M/giphy.gif?cid=ecf05e47vcoppyqgofmu5b1oyva83iugsx4vu1n09ysy7doi&rid=giphy.gif&ct=g',
                     'https://media2.giphy.com/media/W3keANaGsQLC5Ri8DM/giphy.gif?cid=790b76118329259cfe6bed5f00f6ce2182712f13e8c520a2&rid=giphy.gif&ct=g',
                     'https://media0.giphy.com/media/dzaUX7CAG0Ihi/giphy.gif?cid=ecf05e47f0stkvs6efhuch84jcl18w3xcy0jcufnhc8ki40c&rid=giphy.gif&ct=g',
                     'https://media4.giphy.com/media/brsEO1JayBVja/giphy.gif?cid=ecf05e47edwp7ili69d248gy8mwzxgjg8op3mqha4zv7rqkn&rid=giphy.gif&ct=g',
                     'https://media1.giphy.com/media/o7fpdwx8e46c/giphy.gif?cid=790b76111a55bb6408681ab68302488e8799d4ed87e8c6bd&rid=giphy.gif&ct=g',
                     'https://media2.giphy.com/media/Q0LdqbADEDDmE/giphy.gif?cid=ecf05e47tpercp2hvwy0gcenb2i4etz6607z8s2iuvpoy7iv&rid=giphy.gif&ct=g']
        bot.send_animation(message.chat.id, random.choice(animation))

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
