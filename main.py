import logging
import re
import pyshorteners
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

def start(update: Update, context: CallbackContext) -> None:
    name = update.message.from_user.first_name
    update.message.reply_text(f'Hola, {name}! \n Soy un bot que acorta URLs. Envíame una URL y la acortaré para ti. \n\n Owner: @ry_sukuna')

def help_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Envíame una URL y la acortaré para ti.')

def shorten_url(update: Update, context: CallbackContext) -> None:
    url = re.findall(r'http[s]?://\S+', update.message.text)

    if url:
        url = url[0]
        s = pyshorteners.Shortener()
        shortened_url = s.tinyurl.short(url)
        update.message.reply_text(f'URL acortada: {shortened_url}')
        print(update.message.from_user.first_name, 'acortó la siguiente URL:', url)
    else:
        update.message.reply_text('Por favor, envía una URL válida.')

def main() -> None:
    updater = Updater("TOKEN_DE_TU_BOT")  # Reemplaza con el token real de tu bot de Telegram

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))

    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, shorten_url))
    
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
