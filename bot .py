import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = os.getenv("8499269449:AAGg-0Y0I83YEa0YiD-kI5T1gr3AZaI-oxw")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привет! Это Harizma Mebel 🛋️\n"
        "Я помогу подобрать диван и рассчитать цену.\n\n"
        "Напиши, какой диван тебе нужен (угловой, прямой, размер)."
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()

    # супер-простой “ИИ” логики пока
    if "цена" in text:
        await update.message.reply_text(
            "Цены зависят от модели.\n"
            "Угловые диваны: от 35 000₽\n"
            "Прямые: от 25 000₽\n\n"
            "Напиши, какой стиль тебе нужен — подберу варианты."
        )
    elif "контакт" in text or "телефон" in text:
        await update.message.reply_text(
            "Оставь, пожалуйста, имя и телефон — менеджер свяжется с тобой."
        )
    else:
        await update.message.reply_text(
            "Понял 👍\n"
            "Уточни: тебе нужен угловой или прямой диван?"
        )

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Bot started...")
    app.run_polling()

if __name__ == "__main__":
    main()