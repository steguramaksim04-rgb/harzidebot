import telebot
from telebot import types

TOKEN = "8607586432:AAFqkMh2OWQ0WJJlkkWDKG92gF-5lS3kUYU"

ADMIN_IDS = [
    1419642101,
    7294463917,
    7289108353,
    5189626835
]

PHOTO_ID = "AgACAgIAAxkBAAM0ahlv-NJ0QtWBZI3uaimsx_HtTHcAAkUfaxvmudBIH5VoaEq_LGgBAAMCAAN5AAM7BA"

ANKETA_PHOTO_ID = "AgACAgIAAxkBAAOEahmNOiT_YyFOokPB-tiqljS6fEwAAvIfaxvmudBIllcCBxQDxq8BAAMCAAN5AAM7BA"

THANKS_PHOTO_ID = "AgACAgIAAxkBAAOeahmXXy6PxKEgcd2Ek1LKS5DkSYYAAiogaxvmudBI_kWMzcECvpABAAMCAAN5AAM7BA"

bot = telebot.TeleBot(TOKEN)

users_waiting = []

@bot.message_handler(commands=['start'])
def start(message):

    text = """
〘🎰〙<b>CLAN | HARZIDE</b> відкриває масовий набір

〘⁉️〙 Давно шукав сильний та масштабний клан,
який залітає на різні проєкти та не стоїть на місці.

<blockquote>
➜ Тоді тобі до нас! Місце, де кожен допоможе,
підтримає та піде до кінця разом із тобою.

➯ Активний склад
➯ Постійний розвиток
➯ Адекватне керівництво
➯ Дружня атмосфера
➯ Гарно оформлений TG чат клана
</blockquote>

〘📁〙 Щоб приєднатися до нас —
натисни кнопку нижче та заповни анкету.
"""

    markup = types.InlineKeyboardMarkup()

    btn1 = types.InlineKeyboardButton(
        "📋 Подати заявку",
        callback_data="zayavka"
    )

    markup.add(btn1)

    bot.send_photo(
        message.chat.id,
        PHOTO_ID,
        caption=text,
        parse_mode="HTML",
        reply_markup=markup
    )

@bot.callback_query_handler(func=lambda call: call.data == "zayavka")
def zayavka(call):

    users_waiting.append(call.message.chat.id)

    text = """
〘📁〙<b>Щоб подати заявку —</b>
нажміть на шаблон нижче та заповніть його.

••••••••••••••••••••••••••••••<code>
➯ Ваш вік:
➯ Ваш нік-нейм:
➯ На яких проектах грали:
➯ В яких сім'ях/кланах були:
➯ Ваші досягнення в сфері проектів:
</code>••••••••••••••••••••••••••••••

〘⚠️〙Надішліть заповнену анкету
одним повідомленням.
"""

    bot.send_photo(
        call.message.chat.id,
        ANKETA_PHOTO_ID,
        caption=text,
        parse_mode="HTML"
    )

@bot.message_handler(func=lambda message: message.chat.id in users_waiting)
def anketa(message):

    users_waiting.remove(message.chat.id)

    zayavka_text = f"""
🚨 <b>НОВА ЗАЯВКА!</b> 🚨

@Off1orenzo @offArimaa @Capitandf

━━━━━━━━━━━━━━━━━━

👤 USERNAME: @{message.from_user.username}

🆔 ID ДЛЯ ВІДПОВІДІ:

<code>{message.from_user.id}</code>

━━━━━━━━━━━━━━━━━━

{message.text}
"""

    for admin in ADMIN_IDS:

        bot.send_message(
            admin,
            zayavka_text,
            parse_mode="HTML"
        )

    thanks = """
〘❤️〙 <b>ДЯКУЄМО ЗА ЗАЯВКУ!</b>

<blockquote>
➯ Ваша анкета успішно подана
та передана на розгляд керівництву.

➯ По питанням писати до:
@Off1orenzo
@offArimaa
@Capitandf

➯ Очікуйте відповіді
найближчим часом.
</blockquote>

〘🗽〙<b>З повагою CLAN | HARZIDE</b>
"""

    bot.send_photo(
        message.chat.id,
        THANKS_PHOTO_ID,
        caption=thanks,
        parse_mode="HTML"
    )

@bot.message_handler(commands=['r'])
def reply_user(message):

    if message.from_user.id not in ADMIN_IDS:
        return

    try:

        data = message.text.split(maxsplit=2)

        user_id = int(data[1])

        text = data[2]

        bot.send_message(
            user_id,
            f"📨 <b>ВІДПОВІДЬ ВІД CLAN | HARZIDE</b>\n\n{text}",
            parse_mode="HTML"
        )

        bot.send_message(
            message.chat.id,
            "✅ Повідомлення відправлено."
        )

    except:

        bot.send_message(
            message.chat.id,
            "❌ Використання:\n/r ID текст"
        )

@bot.message_handler(content_types=['photo'])
def get_photo(message):

    file_id = message.photo[-1].file_id

    bot.send_message(message.chat.id, file_id)

bot.infinity_polling()
