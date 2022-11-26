from telegram.ext import Updater, CommandHandler


def start(update, context):
    update.message.reply_text('Hello')


def help():
    pass


def run_bot():
    TOKEN = ""

    # create the updater, that will automatically create also a dispatcher and a queue to make them dialog
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # add handlers for start and help commands
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help))

    # start your shiny new bot
    updater.start_polling()

    # run the bot until Ctrl-C
    updater.idle()