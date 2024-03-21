from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from mistral import mistral_chat
from mistral import mistral_large
from image_generator import ImageGen
from gemini_chat import GeminiChat


TOKEN: Final = '7007534399:AAG2fHNVOIw8TtqOWQ7XlsAtvYcrqETxQic'
BOT_USERNAME: Final = '@aple_aple_bot'


# Commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello, I am BotSon. How can I help you?')


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('I am BotSon, Please type something so I can respond.')


async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('This is a custom command.')


# Responses
def handle_response(text: str) -> str:
    processed: str = text.lower()

    # return mistral_chat(processed)
    # return mistral_large(processed)

    gc.get_chat_history()
    return gc.message(processed)


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    username_single = update.message.chat.username
    # username_grp = update.message.chat.username
    # user_id = update.message.chat.id

    def getUsername():
        # if message_type == 'private':
            return username_single
        # elif message_type == 'group' or message_type == 'supergroup':
        #     return username_grp

    print(f'\nUser ({getUsername()}) in {message_type}: "{text}"')

    if 'waiting_for_img_prompt' in context.user_data and context.user_data['waiting_for_img_prompt']:
        # This text will be treated as image prompt
        image_prompt = update.message.text
        # Generate the image based on the prompt
        img_gen = ImageGen()
        await update.message.reply_text("Please wait while your image is being generated...")
        img_gen.generate_image(image_prompt)
        # Reset the waiting_for_img_prompt flag
        context.user_data['waiting_for_img_prompt'] = False
        await context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('image.png', 'rb'))
        return

    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, "").strip()
            response: str = handle_response(new_text)
        else:
            return 
    else:
        response: str = handle_response(text)

    print('BotSon:', response)
    await update.message.reply_text(response)


async def gen_img(update: Update, context):
    await update.message.reply_text("Enter your image prompt")

    # Set the waiting_for_img_prompt flag to True
    context.user_data['waiting_for_img_prompt'] = True


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')


if __name__ == '__main__':
    print('Starting bot...')
    app = Application.builder().token(TOKEN).build()

    gc = GeminiChat()

    # Commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('generate_image', gen_img))

    # Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Errors
    app.add_error_handler(error)

    # Polls the bot 
    print('Polling...')
    app.run_polling()