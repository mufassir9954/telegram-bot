import telebot

# আপনার Bot Token
TOKEN = "8483713597:AAHtWTtsaLcyWP2aErQNtC9spFd_MFqH"

bot = telebot.TeleBot(TOKEN)

# Start কমান্ড
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "👋 হ্যালো! আমি Free Earning Bot 🚀")

# Help কমান্ড
@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "📝 সাহায্য লাগলে Admin এর সাথে যোগাযোগ করুন।")

# সাধারণ মেসেজ রিপ্লাই
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"আপনি লিখেছেন: {message.text}")

print("✅ Bot চলছে...")

bot.polling()
