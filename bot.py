import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from googletrans import Translator

# Load environment variables from .env file
load_dotenv()

# Get the bot token from environment variables
TOKEN = os.getenv('DISCORD_TOKEN')

# Set up intents for the bot
intents = discord.Intents.default()
intents.message_content = True

# Create a new bot instance
bot = commands.Bot(command_prefix='!', intents=intents)

# Create a Translator instance
translator = Translator()

# Event: Bot is ready
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

# Command: !translate <text>
@bot.command(name='translate')
async def translate(ctx, *, text: str):
    # Translate text from English to Spanish
    translated = translator.translate(text, src='en', dest='es')
    await ctx.send(translated.text)

# Run the bot with the token
bot.run(TOKEN)
