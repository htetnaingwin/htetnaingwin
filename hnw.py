from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN: Final='7666608264:AAG5gQVwmcBAbIVCz5eV9jBcRR1h3Db7J78'
BOT_USERNAME: Final='@saturndragonbot'

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
  await update.message.reply_text('Hello! How are you!')
  
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
  await update.message.reply_text('I am Nagar Lay! Please type something so I can respond!')
  
async def hi_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
  await update.message.reply_text('hi, I am Nagar Lay!')
  
def handle_response(text: str):
   processed: str = text.lower()
   
   if 'hello' in processed:
      return 'Hey there!"
      
   if 'how are you' in processed:
      return 'I am good!'
      
   if 'i love python' in processed:
      return 'Remember to subscribe!"
      
  return 'I do not understand what you wrote...'
  
  
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
  message_type: str = update.message.chat.type
  text: str = update.message.text
  
  print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')

 if message _type = 'group':
     if BOT_USERNAME in text:
       new_text: str = text.replace(BOT_USERNAME,'').strip()
       response: str = handle_response(new_text)
     else:
    return
 else:  
    response: str = handle_response(text)
 
  print('Bot:',response)
  await update.message.reply_text(response)
  
async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
   print(f'Update {update} caused error {context.error}')
   
if _name_ = '_main_':
  print('Starting bot...')
    app = Application.builder().token(TOKEN).build()
    
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('hi', hi_command))
    
    app.add_handler(MessageHandler(filters.TEXT, handle_message))
    
    app.add_error_handler(error)
    
    print('Polling...')
    
    app.run_polling(poll_interval=3)
