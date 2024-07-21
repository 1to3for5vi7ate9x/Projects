# from telegram import Update
# from telegram.ext import Application, CommandHandler, ContextTypes

# # Define your bot token
# TOKEN = "7108076179:AAGZzcta6XXVMO6hob6bKaUebjywgsUkH9k"

# # Define the command handlers
# async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     await update.message.reply_text("Hello! Welcome to GoldieCoin Community")

# async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     await update.message.reply_text(
#     """
#     /start -> Welcome to the GoldieCoin
#     /help -> You can reach out our support for help
#     /website -> About the GoldieCoin
#     """
#     )

# async def website(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     await update.message.reply_text("goldiecoin.ai")

# async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     await update.message.reply_text("Contact to @ShibaPlat for any help")

# # Create the Application and pass it your bot's token
# application = Application.builder().token(TOKEN).build()

# # Add the command handlers to the application
# application.add_handler(CommandHandler("start", start))
# application.add_handler(CommandHandler("help", help))
# application.add_handler(CommandHandler("website", website))

# # Run the bot
# application.run_polling()

# from telegram import Update, ChatPermissions
# from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
# import random
# import asyncio

# # Define your bot token
# TOKEN = "7108076179:AAGZzcta6XXVMO6hob6bKaUebjywgsUkH9k"

# # Define the verification answer globally
# VERIFICATION_ANSWER = None

# # Define the command handlers
# async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     await update.message.reply_text("Hello! Welcome to GoldieCoin Community")

# async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     await update.message.reply_text(
#         """
#         /start -> Welcome to the GoldieCoin
#         /help -> You can reach out our support for help
#         /website -> About the GoldieCoin
#         """
#     )

# async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     await update.message.reply_text("Contact @ShibaPlat for any help")

# async def website(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     await update.message.reply_text("goldiecoin.ai")

# verification_status = {}

# async def new_user(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     global VERIFICATION_ANSWER
#     for member in update.message.new_chat_members:
#         if member.id not in verification_status:
#             # Generate a new verification answer for the user
#             verification_status[member.id] = {
#                 "answer": random.randint(10000, 99999),
#                 "failed_attempts": 0
#             }
#             await update.message.reply_text(
#                 f"Welcome {member.full_name}! Please answer this question to verify you're human:\n\n"
#                 f"Please type the following number to be verified: {verification_status[member.id]['answer']}"
#             )

# # Define a function to verify the user's answer
# async def verify(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     global VERIFICATION_ANSWER
#     user_id = update.message.from_user.id
#     if user_id in verification_status:
#         if update.message.text == str(verification_status[user_id]["answer"]):
#             await update.effective_chat.restrict_member(
#                 user_id,
#                 permissions=ChatPermissions(can_send_messages=True)
#             )
#             await update.message.reply_text("You have been verified! Welcome to the GoldieCoin Community!")
#         else:
#             verification_status[user_id]["failed_attempts"] += 1
#             if verification_status[user_id]["failed_attempts"] >= 3:  # Maximum failed attempts
#                 await update.message.reply_text("You have exceeded the maximum number of failed attempts. Please try again later.")
#             else:
#                 await update.message.reply_text("Incorrect answer. Please try again in 30 minutes.")
#                 # Restrict the user's permissions
#                 await update.effective_chat.restrict_member(
#                     user_id,
#                     permissions=ChatPermissions(can_send_messages=False)
#                 )
#                 # Schedule a task to remove the restrictions after 30 minutes
#                 await asyncio.sleep(10)  # 30 minutes in seconds
#                 await update.effective_chat.restrict_member(
#                     user_id,
#                     permissions=ChatPermissions(can_send_messages=True)
#                 )
#                 await update.message.reply_text("Your restrictions have been lifted. Please try again.")
#     else:
#         await update.message.reply_text("You haven't been prompted for verification. Please wait for the next prompt.")

# # Reset verification status for a user
# async def reset_verification_status(user_id):
#     if user_id in verification_status:
#         del verification_status[user_id]


# # # Define a function to handle new users
# # async def new_user(update: Update, context: ContextTypes.DEFAULT_TYPE):
# #     global VERIFICATION_ANSWER
# #     for member in update.message.new_chat_members:
# #         VERIFICATION_ANSWER = random.randint(10000, 99999)  # Generate a new verification answer
# #         await update.message.reply_text(
# #             f"Welcome {member.full_name}! Please answer this question to verify you're human:\n\n"
# #             f"Please type the following number to be verified: {VERIFICATION_ANSWER}"
# #         )

# # # Define a function to verify the user's answer
# # async def verify(update: Update, context: ContextTypes.DEFAULT_TYPE):
# #     global VERIFICATION_ANSWER
# #     if update.message.text == str(VERIFICATION_ANSWER):
# #         await update.effective_chat.restrict_member(
# #             update.message.from_user.id,
# #             permissions=ChatPermissions(can_send_messages=True)
# #         )
# #         await update.message.reply_text("You have been verified! Welcome to the GoldieCoin Community!")
# #     else:
# #         await update.message.reply_text("Incorrect answer. Please try again.")
# #         await update.effective_chat.restrict_member(
# #             update.message.from_user.id,
# #             permissions=ChatPermissions(can_send_messages=False)
# #         )

# # Create the Application and pass it your bot's token
# application = Application.builder().token(TOKEN).build()

# # Add the command handlers to the application
# application.add_handler(CommandHandler("start", start))
# application.add_handler(CommandHandler("menu", menu))
# application.add_handler(CommandHandler("help", help))
# application.add_handler(CommandHandler("website", website))

# application.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, new_user))
# application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, verify))

# # Run the bot
# application.run_polling()

# from telegram import Update, ChatPermissions
# from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
# import random
# import asyncio

# # Define your bot token
# TOKEN = "7108076179:AAGZzcta6XXVMO6hob6bKaUebjywgsUkH9k"

# # Define the verification answer globally
# verification_status = {}

# # Define the command handlers
# async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     await update.message.reply_text("Hello! Welcome to GoldieCoin Community")

# async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     await update.message.reply_text(
#         """
#         /start -> Welcome to the GoldieCoin
#         /help -> You can reach out our support for help
#         /website -> About the GoldieCoin
#         """
#     )

# async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     await update.message.reply_text("Contact @ShibaPlat for any help")

# async def website(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     await update.message.reply_text("goldiecoin.ai")

# # Define a function to handle new users
# async def new_user(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     for member in update.message.new_chat_members:
#         if member.id not in verification_status:
#             await update.message.reply_text(
#                 f"Welcome {member.full_name}! Please start a private chat with me first and type anything to begin the verification process."
#             )

# # Define a function to handle messages in the private chat and initiate the verification process
# async def start_verification(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     user_id = update.message.from_user.id
#     if user_id in verification_status:
#         chat_id = verification_status[user_id]["chat_id"]
#         if chat_id is not None:
#             await context.bot.restrict_chat_member(
#                 chat_id,
#                 user_id,
#                 permissions=ChatPermissions(can_send_messages=True)
#             )
#             await context.bot.send_message(
#                 chat_id,
#                 "You have been verified! Welcome to the GoldieCoin Community!"
#             )
#             del verification_status[user_id]

# # Define a function to verify the user's answer
# async def verify(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     user_id = update.message.from_user.id
#     if user_id in verification_status:
#         if update.message.text == str(verification_status[user_id]["answer"]):
#             # Allow the user to send messages in the group
#             await context.bot.restrict_chat_member(
#                 update.message.chat.id,
#                 user_id,
#                 permissions=ChatPermissions(can_send_messages=True)
#             )
#             await update.message.reply_text("You have been verified! Welcome to the GoldieCoin Community!")
#             # Remove verification status for the user
#             del verification_status[user_id]
#         else:
#             verification_status[user_id]["failed_attempts"] += 1
#             if verification_status[user_id]["failed_attempts"] >= 3:  # Maximum failed attempts
#                 await update.message.reply_text("You have exceeded the maximum number of failed attempts. Please try again later.")
#             else:
#                 await update.message.reply_text("Incorrect answer. Please try again in 30 minutes.")
#     else:
#         await update.message.reply_text("You haven't been prompted for verification. Please wait for the next prompt.")

# # Create the Application and pass it your bot's token
# application = Application.builder().token(TOKEN).build()

# # Add the command handlers to the application
# application.add_handler(CommandHandler("start", start))
# application.add_handler(CommandHandler("menu", menu))
# application.add_handler(CommandHandler("help", help))
# application.add_handler(CommandHandler("website", website))

# application.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, new_user))
# application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, verify))
# application.add_handler(MessageHandler(filters.Text and (filters.ChatType.PRIVATE | filters.ChatType.CHANNEL), start_verification))


# #application.add_handler(MessageHandler(filters.Text & filters.ChatType.PRIVATE, start_verification))  # Add this line

# # Run the bot
# application.run_polling()

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, ChatPermissions
from telegram.ext import Application, CommandHandler, MessageHandler, CallbackQueryHandler, filters, ContextTypes
import asyncio

# Define your bot token
TOKEN = "7108076179:AAGZzcta6XXVMO6hob6bKaUebjywgsUkH9k"

# Define the verification status globally
verification_status = {}

# Define the command handlers
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! Welcome to GoldieCoin Community")

async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        """
        /start -> Welcome to the GoldieCoin
        /help -> You can reach out our support for help
        /website -> About the GoldieCoin
        """
    )

async def join_group(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Check if the user provided an invite link
    if len(context.args) == 0:
        await update.message.reply_text("Please provide an invite link.")
        return
    
    invite_link = context.args[0]
    
    try:
        # Try to join the group using the invite link
        chat = await context.bot.join_chat(invite_link)
        await update.message.reply_text(f"Successfully joined the group {chat.title}.")
    except Exception as e:
        await update.message.reply_text(f"Failed to join the group: {str(e)}")


async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Contact @ShibaPlat for any help")

async def website(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("goldiecoin.ai")

# Define a function to handle new users and start verification
async def new_user(update: Update, context: ContextTypes.DEFAULT_TYPE):
    for member in update.message.new_chat_members:
        await update.effective_chat.restrict_member(
             update.message.from_user.id,
             permissions=ChatPermissions(can_send_messages=False)
         )
        if member.id not in verification_status:
            verification_status[member.id] = {"chat_id": update.message.chat.id}
            keyboard = [[InlineKeyboardButton("Click to Verify", callback_data="verify")]]
            reply_markup = InlineKeyboardMarkup(keyboard)
            await context.bot.send_message(
                update.message.chat.id,
                f"Welcome {member.full_name}! To verify that you are human, please click the button below:",
                reply_markup=reply_markup
            )

# Define a function to handle the verification button click
async def verify_button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    user_id = query.from_user.id
    if user_id in verification_status:
        permissions = ChatPermissions(can_send_messages=True)
        await context.bot.restrict_chat_member(
            verification_status[user_id]["chat_id"],
            user_id,
            permissions=permissions
        )
        await query.answer("You have been verified! Welcome to the GoldieCoin Community!")
        await query.message.delete()
        #del verification_status[user_id]
    del verification_status[user_id]
# Create the Application and pass it your bot's token
application = Application.builder().token(TOKEN).build()

# Add the command handlers to the application
application.add_handler(CommandHandler("start", start))
application.add_handler(CommandHandler("menu", menu))
application.add_handler(CommandHandler("help", help))
application.add_handler(CommandHandler("website", website))
application.add_handler(CommandHandler("join", join_group))
application.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, new_user))
application.add_handler(CallbackQueryHandler(verify_button))

# Run the bot
application.run_polling()





