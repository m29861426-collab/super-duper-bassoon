import telebot
import random

# التوكن الخاص بك
TOKEN = '8359609081:AAErbaNtq2he44FYnBGIIwE699QyEJNJjdM'
bot = telebot.TeleBot(TOKEN)

# قائمة الردود
responses = {
    "هايا": ["عيون هايا", "يا عمري قال اسمي", "سمي يعيني", "اجمل من قال هايا", "ولك فيدتك"],
    "المطور": "مطوري هو المبدع صاحب الحساب @bsm86",
    "السلام عليكم": ["وعليكم السلام يا هلا نورتنا", "وعليكم السلام حياك الله", "وعليكم السلام نورت يعيني"],
    "صلي على النبي": "اللهم صل وسلم على نبينا محمد",
    "بطلع": ["كيف تطلع وانت احسن واحد بالقروب", "مين زعلك يطلع هو"],
    "احلف": "ترى يكذب مافي داعي يحلف",
    "احبك": ["يعمري", "انا ولا شخص تاني؟", "احبك الله في الذي احببتني فيه"]
}

# ردود عشوائية عند مناداة كلمة بوت
bot_calls = [
    "موضوع مهم؟؟",
    "بدعي عليك تصير بوت",
    "لو ناديتني هايا كان جاك رد احلى",
    "ترا بزعل واتعطل",
    "اسمي هايا ولكك",
    "ه ا ي ا وين الصعب",
    "عندي اسم مثل ما سميت"
]

@bot.message_handler(regexp=r'^اضف (.+) : (.+)')
def add_new_response(message):
    try:
        text_parts = message.text.replace("اضف ", "").split(":")
        word = text_parts[0].strip()
        answer = text_parts[1].strip()
        responses[word] = answer
        bot.reply_to(message, f"تم حفظ الرد لو احد قال {word} برد بـ {answer}")
    except:
        bot.reply_to(message, "خطأ اكتبها كذا: اضف الكلمة : الرد")

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.reply_to(message, "اهلن بك في بوت الردود")

@bot.message_handler(func=lambda message: True)
def auto_reply(message):
    user_text = message.text.strip()
    
    # الرد على الكلمات المخزنة
    if user_text in responses:
        res = responses[user_text]
        if isinstance(res, list):
            bot.reply_to(message, random.choice(res))
        else:
            bot.reply_to(message, res)
    
    # الرد عند مناداة بوت
    elif "بوت" in user_text:
        bot.reply_to(message, random.choice(bot_calls))

print("البوت شغال الحين.. جربه في تليجرام")
bot.polling()
