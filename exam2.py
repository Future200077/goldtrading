# import logging
# from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
# from telegram.ext import (
#     Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters, ContextTypes, ConversationHandler
# )

# # Enable logging
# logging.basicConfig(
#     format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
#     level=logging.INFO,
# )
# logger = logging.getLogger(__name__)

# # Define conversation states
# STATE_AI = 1

# # Replace this with your bot token
# TOKEN = "8154482680:AAEAo6NTkwPwGM_8uc77Hdr_HoTw-yrevE4"

# # Function to start the bot
# async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     """Sends a welcome message with an AI Chat button."""
#     keyboard = [[InlineKeyboardButton("🤖 AI Chat", callback_data="ai_chat")]]
#     reply_markup = InlineKeyboardMarkup(keyboard)

#     await update.message.reply_text(
#         "Welcome! Click the button below to start AI Chat Mode:",
#         reply_markup=reply_markup
#     )

# # Function to handle AI Chat button click
# async def ai_chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     """Handle AI chat button callback."""
#     query = update.callback_query
#     await query.answer()  # Acknowledge the callback

#     # Edit message to ask user for a query
#     await query.edit_message_text(
#         "🤖 AI Analysis Mode\n\n"
#         "Enter your query (e.g., 'What is the current gold price trend?'):"
#     )

#     return STATE_AI  # Set conversation state

# # Function to handle user messages in AI Mode
# async def ai_response(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     """Handles the user's AI query input."""
#     user_query = update.message.text  # Get user's input

#     # Simulated AI response (replace this with real AI logic)
#     ai_reply = f"AI Response: I received your query - '{user_query}'"

#     await update.message.reply_text(ai_reply)

#     return ConversationHandler.END  # End conversation

# # Function to handle unknown messages
# async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     """Handle unknown commands/messages."""
#     await update.message.reply_text("Sorry, I didn't understand that command.")

# # Main function to set up the bot
# def main():
#     """Start the bot and register handlers."""
#     app = Application.builder().token(TOKEN).build()

#     # Conversation handler for AI chat
#     conv_handler = ConversationHandler(
#         entry_points=[CallbackQueryHandler(ai_chat, pattern="^ai_chat$")],
#         states={STATE_AI: [MessageHandler(filters.TEXT & ~filters.COMMAND, ai_response)]},
#         fallbacks=[]
#     )

#     # Register handlers
#     app.add_handler(CommandHandler("start", start))
#     app.add_handler(conv_handler)
#     app.add_handler(MessageHandler(filters.COMMAND, unknown))  # Handle unknown commands

#     # Start the bot
#     app.run_polling()

# # Run the bot
# if __name__ == "__main__":
#     main()





# import logging
# import openai
# from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
# from telegram.ext import (
#     Application, CommandHandler, CallbackQueryHandler, MessageHandler,
#     filters, ContextTypes, ConversationHandler
# )

# # Enable logging
# logging.basicConfig(
#     format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
#     level=logging.INFO,
# )
# logger = logging.getLogger(__name__)

# # Define conversation states
# STATE_AI = 1

# # Replace with your bot token and OpenAI API key
# TELEGRAM_BOT_TOKEN = "8154482680:AAEAo6NTkwPwGM_8uc77Hdr_HoTw-yrevE4"
# OPENAI_API_KEY = "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"

# # Set OpenAI API key
# openai.api_key = OPENAI_API_KEY

# # Function to start the bot
# async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     """Sends a welcome message with an AI Chat button."""
#     keyboard = [[InlineKeyboardButton("🤖 AI Chat", callback_data="ai_chat")]]
#     reply_markup = InlineKeyboardMarkup(keyboard)

#     await update.message.reply_text(
#         "Welcome! Click the button below to start AI Chat Mode:",
#         reply_markup=reply_markup
#     )

# # Function to handle AI Chat button click
# async def ai_chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     """Handles AI chat button callback."""
#     query = update.callback_query
#     await query.answer()  # Acknowledge the callback

#     # Inform the user about AI Chat Mode
#     await query.edit_message_text(
#         "🤖 AI Analysis Mode\n\n"
#         "You can now chat with AI. Type your message below.\n"
#         "Type 'end' to exit AI Mode."
#     )

#     return STATE_AI  # Set conversation state

# # Function to handle user messages in AI Mode
# async def ai_response(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     """Handles continuous AI chat until user sends 'end'."""
#     user_query = update.message.text.strip()  # Get user's input

#     # If user types 'end', exit AI chat
#     if user_query.lower() == "end":
#         await update.message.reply_text("AI chat ended. Type /start to restart.")
#         return ConversationHandler.END  # Exit conversation

#     try:
#         # Call OpenAI API
#         response = openai.ChatCompletion.create(
#             model="gpt-3.5-turbo",
#             messages=[{"role": "user", "content": user_query}]
#         )
        
#         ai_reply = response["choices"][0]["message"]["content"]

#     except Exception as e:
#         ai_reply = "Sorry, I encountered an error. Please try again later."
#         logger.error(f"OpenAI API Error: {e}")

#     await update.message.reply_text(ai_reply)
#     return STATE_AI  # Keep conversation going

# # Function to handle unknown messages
# async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     """Handle unknown commands/messages."""
#     await update.message.reply_text("Sorry, I didn't understand that command.")

# # Main function to set up the bot
# def main():
#     """Start the bot and register handlers."""
#     app = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

#     # Conversation handler for AI chat
#     conv_handler = ConversationHandler(
#         entry_points=[CallbackQueryHandler(ai_chat, pattern="^ai_chat$")],
#         states={STATE_AI: [MessageHandler(filters.TEXT & ~filters.COMMAND, ai_response)]},
#         fallbacks=[]
#     )

#     # Register handlers
#     app.add_handler(CommandHandler("start", start))
#     app.add_handler(conv_handler)
#     app.add_handler(MessageHandler(filters.COMMAND, unknown))  # Handle unknown commands

#     # Start the bot
#     app.run_polling()

# # Run the bot
# if __name__ == "__main__":
#     main()







import logging
import g4f  # Free GPT API library
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application, CommandHandler, CallbackQueryHandler, MessageHandler,
    filters, ContextTypes, ConversationHandler
)

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

# Define conversation states
STATE_AI = 1

# Replace with your bot token
TELEGRAM_BOT_TOKEN = "8154482680:AAEAo6NTkwPwGM_8uc77Hdr_HoTw-yrevE4"

# Function to start the bot
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Sends a welcome message with an AI Chat button."""
    keyboard = [[InlineKeyboardButton("🤖 AI Chat", callback_data="ai_chat")]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "Welcome! Click the button below to start AI Chat Mode:",
        reply_markup=reply_markup
    )

# Function to handle AI Chat button click
async def ai_chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handles AI chat button callback."""
    query = update.callback_query
    await query.answer()  # Acknowledge the callback

    # Inform the user about AI Chat Mode
    await query.edit_message_text(
        "🤖 AI Analysis Mode\n\n"
        "You can now chat with AI. Type your message below.\n"
        "Type 'end' to exit AI Mode."
    )

    return STATE_AI  # Set conversation state

# Function to handle user messages in AI Mode
async def ai_response(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handles continuous AI chat until user sends 'end'."""
    user_query = update.message.text.strip()  # Get user's input

    # If user types 'end', exit AI chat
    if user_query.lower() == "end":
        await update.message.reply_text("AI chat ended. Type /start to restart.")
        return ConversationHandler.END  # Exit conversation

    try:
        # Call g4f Free API
        ai_reply = g4f.ChatCompletion.create(
            model=g4f.models.default,  # Use a free available model
            messages=[{"role": "user", "content": user_query}]
        )

    except Exception as e:
        ai_reply = "Sorry, I encountered an error. Please try again later."
        logger.error(f"Free AI API Error: {e}")

    await update.message.reply_text(ai_reply)
    return STATE_AI  # Keep conversation going

# Function to handle unknown messages
async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle unknown commands/messages."""
    await update.message.reply_text("Sorry, I didn't understand that command.")

# Main function to set up the bot
def main():
    """Start the bot and register handlers."""
    app = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

    # Conversation handler for AI chat
    conv_handler = ConversationHandler(
        entry_points=[CallbackQueryHandler(ai_chat, pattern="^ai_chat$")],
        states={STATE_AI: [MessageHandler(filters.TEXT & ~filters.COMMAND, ai_response)]},
        fallbacks=[]
    )

    # Register handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(conv_handler)
    app.add_handler(MessageHandler(filters.COMMAND, unknown))  # Handle unknown commands

    # Start the bot
    app.run_polling()

# Run the bot
if __name__ == "__main__":
    main()

