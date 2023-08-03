import logging
import pyshorteners
import re

from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

def start(update: Update, _: CallbackContext) -> None:
    update.message.reply_text(f'Hola, {update.message.from_user.first_name} Bienvenido! Soy un bot creado por @azaelclrz')
    update.message.reply_text('Me asignaron el trabajo de hacerte la vida más fácil. Proporcianme una URL y te la acortaré inmediatamente.')


def help_command(update: Update, _: CallbackContext) -> None:
    update.message.reply_text('¡Proporcioname una URL y la acortaré para ti!')


def url_shortener(update: Update, _: CallbackContext) -> None:
    s = pyshorteners.Shortener()
    link = re.findall(r'(\w*\.\w+\.*\w+.*)', update.message.text)
    if link:
        url = s.tinyurl.short(f'https://{link[0]}')
        update.message.reply_text(url)
        print(update.message.from_user.first_name, 'shorted this link:', f'https://{link[0]}')
    else:
        update.message.reply_text('Proporciona una URL válida.')


def main() -> None:
    updater = Updater("6587578305:AAHqtmE9yBjlj1Y1Si9dqPhhnDkyYImwmbQ")

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))

    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, url_shortener))
    
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
