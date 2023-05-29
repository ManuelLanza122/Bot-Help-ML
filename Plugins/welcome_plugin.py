from telegram.ext import CommandHandler
from telegram import PhotoSize

def register(dispatcher, api_id, api_hash):
    # Define la función de inicio
    def start(update, context):
        # Envía una imagen de bienvenida
        photo_url = 'https://example.com/bienvenida.jpg'  # URL de la imagen de bienvenida
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=photo_url, caption="¡Bienvenido! 🎉")

        # Envía un mensaje épico
        epic_message = "¡Saludos, aventurero! Soy un bot épico creado para brindarte asistencia en tus travesías. ¡Prepárate para embarcarte en una experiencia increíble! 💪🔥"
        context.bot.send_message(chat_id=update.effective_chat.id, text=epic_message)

    # Registra el comando "/start" con la función de inicio
    dispatcher.add_handler(CommandHandler('start', start))
