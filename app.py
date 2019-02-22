import logging
import os

from telegram.ext import Updater, CommandHandler
from handler import add_command, check_command

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logging.info("started")

updater = Updater(token=os.getenv("BOT_TOKEN"))
dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler("add", add_command, pass_args=True))
dispatcher.add_handler(CommandHandler("check", check_command, pass_args=True))

updater.start_polling()
updater.idle()
