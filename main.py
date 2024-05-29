from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, Filters
import time

TOKEN = '6774136454:AAHHwHmCXBe-JWbJeB79SLb-KoyDFjoI450'
TIMEOUT = 60  # Tiempo de espera en segundos

def start(update: Update, context):
    # Cuando un usuario se une al grupo, restringir los permisos de escritura
    context.bot.restrict_chat_member(update.effective_chat.id, update.effective_user.id, can_send_messages=False)

    # Enviar un mensaje privado con las normas del grupo
    rules_message = "Lore ipsum si aemet"
    keyboard = [
        [InlineKeyboardButton("Accept", callback_data='accept'),
         InlineKeyboardButton("Cancel", callback_data='cancel')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.send_message(update.effective_user.id, text=rules_message, reply_markup=reply_markup)

    # Iniciar un temporizador para echar al usuario si no responde
    context.job_queue.run_once(kick_user, TIMEOUT, context=update.effective_user.id)

def button(update: Update, context):
    query = update.callback_query
    query.answer()

    if query.data == 'accept':
        # Si el usuario acepta, dar permisos de escritura
        context.bot.promote_chat_member(update.effective_chat.id, update.effective_user.id, can_send_messages=True)
    else:
        # Si el usuario rechaza, echar al usuario del grupo
        context.bot.kick_chat_member(update.effective_chat.id, update.effective_user.id)

def kick_user(context):
    # Echar al usuario del grupo si no ha respondido en el tiempo establecido
    context.bot.kick_chat_member(update.effective_chat.id, context.job.context)

def main():
    updater = Updater(token=TOKEN, use_context=True)

    dp = updater.dispatcher

    dp.add_handler(MessageHandler(Filters.status_update.new_chat_members, start))
    dp.add_handler(CallbackQueryHandler(button))

    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()
