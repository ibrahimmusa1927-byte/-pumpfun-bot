import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Get from environment variables (set in Render dashboard)
BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('🚀 Pump.fun Bot is active!')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Use /start to begin')

def main():
    if not BOT_TOKEN:
        logger.error("No TELE
