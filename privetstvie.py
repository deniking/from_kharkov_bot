import datetime
import random
import anekdot
import aforizm
import telebot
import pytz

bot = telebot.TeleBot('5507838809:AAHtBfJfWZ1AvNqG5X7ua2Fw-0XriEaHvqg')




@bot.message_handler(content_types=['text'])
def privetstvie (message):

    time = datetime.datetime.now(pytz.timezone('Europe/Kiev'))
    # time = datetime.datetime.now().time() #print(time.hour)
    time1 = int(time.strftime('%H'))
    time2 = time.strftime('%H:%M:%S')

    msg = message.text
    msg = msg.lower()
# утро
    if time1 >= 6 and time1 <= 11:
        if (u'доброе утро' in msg or u'доброго ранку' in msg):
            bot.reply_to(message, "Доброго ранку ми з Ураїни 🇺🇦 \nСЛУШАЙ от меня АНЕКДОТ 😉")
            bot.send_message(message.chat.id, anekdot.list[0])
            del anekdot.list[0]
            stick = ["CAACAgIAAxkBAAEFYlli4CL47Pv3Xu7uk2FW_i6Kb_kLxAACjwEAAladvQqTBL2ODiSRxikE",
                         "CAACAgIAAxkBAAEFb51i6AKSo3pZRT9xPrWkj8jWE0-NtwACAQADwDZPExguczCrPy1RKQQ",
                        "CAACAgIAAxkBAAEFb8Ji6Az_iEhlyG_J5t1TAQqnpt1sCAACWAADUomRI32OzA4HOEuGKQQ",
                        "CAACAgIAAxkBAAEFb8xi6A1biEPLVN2HFsJZurwAAVHfC4wAAucaAAK4hBhIJjH83tMgCW4pBA",
                        "CAACAgIAAxkBAAEFb_Vi6BHGUmvAjJMU-rscfwGnU8NvjAACRBkAAgjh2UlSqev16oISqCkE"]
            bot.send_sticker(message.chat.id, random.choice(stick))
    else:
        if (u'доброе утро' in msg or u'доброго ранку' in msg):
            utro = ['Ты здурел? какое нафиг утро?, ты время видел?🤔 ',
                    'По ходу ты ВАСЯ попутал 🤨',
                    'Только глаза открыл? Я же предупреждал, меньше надо пить 😝',
                    'Уже не утро, смотри на время 👇',
                    'Утро начинаеться с кофе, а я его давно уже выпил ☕️']
            stick = ["CAACAgIAAxkBAAEFewli7h9UFlTWS_weaeKo_CZiTpO7sAACSgADUomRIyleaTHC6cM1KQQ",
                     "CAACAgIAAxkBAAEFewti7h9hoFGaEVfWh6HSInMGnd4VcQAC-AIAAgaRjBcPcDyQMH4mmCkE",
                     "CAACAgIAAxkBAAEFeypi7jHFFbKiFv_cl1Imt5lSpdm0SAACWwADWbv8JWRSp1P6Y54eKQQ",
                     "CAACAgIAAxkBAAEFey5i7jK2lFG9cIyDPVOf24VDeVi0jQAC6gIAAgaRjBdYifOhxrdujikE",
                     "CAACAgIAAxkBAAEFezBi7jLccMaXh12ajIiYO3j9Nuj3fwACPgADUomRI4x8Q-JPPwtuKQQ",
                     "CAACAgIAAxkBAAEFezJi7jLxj8WqC9ubNIm0J__6pm4XzQACxhoAAlGVWEs1d0W4BAtqSikE"]
            bot.send_message(message.chat.id, random.choice(utro))
            bot.send_message(message.chat.id, time2)
            bot.send_sticker(message.chat.id, random.choice(stick))

#день
    if time1 >= 12 and time1 <= 17:
        if (u'добрый день' in msg or u'доброго дня' in msg):
            bot.reply_to(message, "Доброго дня ми з Ураїни 🇺🇦 \nСЛУШАЙ что я тебе скажу 😉")
            bot.send_message(message.chat.id, aforizm.list[0])
            del aforizm.list[0]
            stick = ["CAACAgIAAxkBAAEFe1xi7kZcMIRprL57dVpZQMOH0WoyeAAC3QIAAvPjvgtmtuXpv_V2eCkE",
                     "CAACAgIAAxkBAAEFe2Ji7kssAAHOg8mp0ebMHb8rEkFAT1gAAqUBAAJWnb0Khivz6UztO2UpBA",
                     "CAACAgIAAxkBAAEFe2Ri7kvdGlD8-NuArtXXzI4zRqHvPwACKAADwZxgDKEyH9MLlol4KQQ",
                     "CAACAgIAAxkBAAEFe2pi7kv9IXLkuEAVDZ0z9dZll50I2gACdBkAAv3EyUkrrD3DFv2fpSkE",
                     "CAACAgIAAxkBAAEFe25i7kw5kXvfC2haZFVnVm1UFBCn-wACMQADr8ZRGnN5cKUC7ZK6KQQ"]
            bot.send_sticker(message.chat.id, random.choice(stick))
    else:
        if (u'добрый день' in msg or u'доброго дня' in msg):
            den = ['Ты здурел? какое нафиг день?, ты время видел?🤔 ',
                    'По ходу ты ВАСЯ попутал 🤨',
                    'Уже не день. Я же предупреждал, меньше надо пить 😝',
                    'Уже не день, смотри на время 👇',
                    'Днем обычно обедают, но что-то я не вижу что бы ты ел борщь 🍲️']
            stick = ["CAACAgIAAxkBAAEFewli7h9UFlTWS_weaeKo_CZiTpO7sAACSgADUomRIyleaTHC6cM1KQQ",
                     "CAACAgIAAxkBAAEFewti7h9hoFGaEVfWh6HSInMGnd4VcQAC-AIAAgaRjBcPcDyQMH4mmCkE",
                     "CAACAgIAAxkBAAEFeypi7jHFFbKiFv_cl1Imt5lSpdm0SAACWwADWbv8JWRSp1P6Y54eKQQ",
                     "CAACAgIAAxkBAAEFey5i7jK2lFG9cIyDPVOf24VDeVi0jQAC6gIAAgaRjBdYifOhxrdujikE",
                     "CAACAgIAAxkBAAEFezBi7jLccMaXh12ajIiYO3j9Nuj3fwACPgADUomRI4x8Q-JPPwtuKQQ",
                     "CAACAgIAAxkBAAEFezJi7jLxj8WqC9ubNIm0J__6pm4XzQACxhoAAlGVWEs1d0W4BAtqSikE"]
            bot.send_message(message.chat.id, random.choice(den))
            bot.send_message(message.chat.id, time2)
            bot.send_sticker(message.chat.id, random.choice(stick))

#вечер
    if time1 >= 18 and time1 <= 24:
        if (u'добрий вечір' in msg or u'доброго вечора' in msg or u'добрый вечер' in msg):
            bot.reply_to(message, "Доброго вечора ми з Ураїни 🇺🇦")
            #bot.send_message(message.chat.id, aforizm.list[0])
            #del aforizm.list[0]
            animation = ["https://www.gifki.org/data/media/908/flag-ukrainy-animatsionnaya-kartinka-0018.gif",
                         "https://media0.giphy.com/media/WmP2WYYdhdztEtovnf/giphy.gif?cid=ecf05e47c0ekh67xncf1ta8efxgdnp7aw8gfdag2tn7291gq&rid=giphy.gif&ct=g",
                         "https://i.gifer.com/71zM.gif",
                         "https://i.gifer.com/FXZn.gif",
                         "https://i.gifer.com/UJX.gif"]
            bot.send_animation(message.chat.id, random.choice(animation))
    else:
        if (u'добрий вечір' in msg or u'доброго вечора' in msg or u'добрый вечер' in msg):
            den = ['Ты здурел? какое нафиг вечер?, ты время видел?🤔 ',
                    'По ходу ты ВАСЯ попутал 🤨',
                    'Уже не вечер. Я же предупреждал, меньше надо пить 😝',
                    'Уже не вечер, смотри на время 👇',
                    'Вечером обычно пьют пиво, но что-то я не вижу что бы ты пил пиво 🍻']
            stick = ["CAACAgIAAxkBAAEFewli7h9UFlTWS_weaeKo_CZiTpO7sAACSgADUomRIyleaTHC6cM1KQQ",
                     "CAACAgIAAxkBAAEFewti7h9hoFGaEVfWh6HSInMGnd4VcQAC-AIAAgaRjBcPcDyQMH4mmCkE",
                     "CAACAgIAAxkBAAEFeypi7jHFFbKiFv_cl1Imt5lSpdm0SAACWwADWbv8JWRSp1P6Y54eKQQ",
                     "CAACAgIAAxkBAAEFey5i7jK2lFG9cIyDPVOf24VDeVi0jQAC6gIAAgaRjBdYifOhxrdujikE",
                     "CAACAgIAAxkBAAEFezBi7jLccMaXh12ajIiYO3j9Nuj3fwACPgADUomRI4x8Q-JPPwtuKQQ",
                     "CAACAgIAAxkBAAEFezJi7jLxj8WqC9ubNIm0J__6pm4XzQACxhoAAlGVWEs1d0W4BAtqSikE"]
            bot.send_message(message.chat.id, random.choice(den))
            bot.send_message(message.chat.id, time2)
            bot.send_sticker(message.chat.id, random.choice(stick))

#ночь
    if time1 >= 0 and time1 <= 5:
        if (u'доброй ночи' in msg or u'доброї ночі' in msg):
            bot.reply_to(message, "Добррої ночі ми з Ураїни 🇺🇦")
            #bot.send_message(message.chat.id, aforizm.list[0])
            #del aforizm.list[0]
            animation = ["https://i.gifer.com/OvZ.gif",
                         "https://i.gifer.com/89vi.gif",
                         "https://i.gifer.com/T3B1.gif",
                         "https://i.gifer.com/Iqt.gif",
                         "https://i.gifer.com/Dhmb.gif"]
            bot.send_animation(message.chat.id, random.choice(animation))
    else:
        if (u'доброй ночи' in msg or u'доброї ночі' in msg):
            den = ['Ты здурел? какая ночь нафиг?, ты время видел?🤔 ',
                    'По ходу ты ВАСЯ попутал 🤨',
                    'Уже не ночь. Я же предупреждал, меньше надо пить 😝',
                    'Уже не ночь, смотри на время 👇',
                    'Ночью обычно спят, но что-то я не вижу что бы ты спал 😴']
            stick = ["CAACAgIAAxkBAAEFewli7h9UFlTWS_weaeKo_CZiTpO7sAACSgADUomRIyleaTHC6cM1KQQ",
                     "CAACAgIAAxkBAAEFewti7h9hoFGaEVfWh6HSInMGnd4VcQAC-AIAAgaRjBcPcDyQMH4mmCkE",
                     "CAACAgIAAxkBAAEFeypi7jHFFbKiFv_cl1Imt5lSpdm0SAACWwADWbv8JWRSp1P6Y54eKQQ",
                     "CAACAgIAAxkBAAEFey5i7jK2lFG9cIyDPVOf24VDeVi0jQAC6gIAAgaRjBdYifOhxrdujikE",
                     "CAACAgIAAxkBAAEFezBi7jLccMaXh12ajIiYO3j9Nuj3fwACPgADUomRI4x8Q-JPPwtuKQQ",
                     "CAACAgIAAxkBAAEFezJi7jLxj8WqC9ubNIm0J__6pm4XzQACxhoAAlGVWEs1d0W4BAtqSikE"]
            bot.send_message(message.chat.id, random.choice(den))
            bot.send_message(message.chat.id, time2)
            bot.send_sticker(message.chat.id, random.choice(stick))