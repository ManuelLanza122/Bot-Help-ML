import os
import json
from dotenv import load_dotenv
from telegram.ext import CommandHandler, Filters

GBAN_FILE = 'gban.json'

def register(dispatcher, api_id, api_hash):
    dispatcher.add_handler(CommandHandler('gban', gban, Filters.user(username="@username") | Filters.user(id=123456789)))

def gban(update, context):
    user_id = update.effective_user.id

    if is_sudo_or_owner(user_id):
        add_to_gban_list(user_id)
        context.bot.send_message(chat_id=update.effective_chat.id, text="Usuario baneado a nivel global.")
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text="No tienes permisos para realizar un ban global.")

def is_sudo_or_owner(user_id):
    owner_id = int(os.getenv('OWNER_ID'))
    sudo_ids = [int(id) for id in os.getenv('SUDO_IDS').split(',')]

    return user_id == owner_id or user_id in sudo_ids

def add_to_gban_list(user_id):
    if not os.path.exists(GBAN_FILE):
        gban_list = []
    else:
        with open(GBAN_FILE, 'r') as file:
            gban_list = json.load(file)

    if user_id not in gban_list:
        gban_list.append(user_id)

    with open(GBAN_FILE, 'w') as file:
        json.dump(gban_list, file)

load_dotenv()
api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')

# Crea el Updater y el Dispatcher