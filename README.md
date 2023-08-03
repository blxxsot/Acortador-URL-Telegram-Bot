# Acortador-URL-Telegram-Bot
Este proyecto es una demostración de un Bot de Telegram que tiene la capacidad de acortar URLs. Cuando envías una URL al bot, él te proporciona una versión más corta del enlace.

# Requisitos
Para ejecutar el bot, necesitarás instalar algunas bibliotecas adicionales:

Python Telegram Bot: Usada para interactuar con los bots de Telegram.
Pyshorteners: Usada para el proceso de acortamiento de URLs.

Puedes instalar estas bibliotecas utilizando el siguiente comando:

pip install python-telegram-bot pyshorteners

# Funciones del Bot
Comando /start: Al utilizar este comando, el bot te dará la bienvenida y te indicará que puedes enviar una URL para que sea acortada.
Comando /help: Al usar este comando, el bot te proporcionará información sobre cómo acortar URLs.
Acortar URL: El bot procesará cualquier mensaje que contenga una URL válida. Si encuentra una URL válida, la acortará y te responderá con la versión más corta.

# Cómo ejecutar el Bot
Para poner en funcionamiento el bot, sigue estos pasos:

Crea un nuevo bot en Telegram:
Inicia una conversación con @BotFather en Telegram.
Escribe el comando /newbot y sigue las instrucciones para crear tu propio bot.
Obtén el token del bot proporcionado por @BotFather y reemplázalo por "TOKEN_DE_TU_BOT" en el archivo main.py.
Ejecuta el bot:
Abre una terminal o línea de comandos en el directorio donde se encuentra el archivo main.py.
Ejecuta el siguiente comando:
python main.py
El bot se activará y estará listo para recibir y acortar URLs.

# Contribuir
Siéntete libre de contribuir y mejorar el bot. Cualquier mejora o corrección que puedas ofrecer será bienvenida y revisada con gusto.
