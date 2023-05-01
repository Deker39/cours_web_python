from telegram.ext import ApplicationBuilder, CommandHandler
from telegram import Update
TOKEN = '6275499245:AAHa-rKHA63hSKNniqmK65NJ8zdVC3wBRyg'


async def start(update: Update, context):
    print(update)
    await update.message.reply_text(f'Welcome! {update.effective_user.first_name}')


app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler('start', start))

app.run_polling()