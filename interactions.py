import discord
from discord import app_commands
from discord.ext import commands
import os
from dotenv import load_dotenv

# Load Discord Bot Token
load_dotenv()
token = os.getenv('TOKEN')

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)
client = discord.Client()


@bot.event
async def on_ready():
    print("Bot is Up and Ready!")
    # Sync slash commands to bot on ready
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(f"Error syncing commands: {e}")

    server = client.get_server("server id")
    await bot.send_message(server.get_channel("channel id"), "Message content")


@bot.command(pass_context=True)
async def poke(ctx, member: discord.Member):
    await bot.send_message(member, 'boop')


bot.tree.command(name="hello")


async def hello(interaction: discord.Interaction):
    await interaction.response.send_message(f"Hey {interaction.user.mention}! This is a slash command.", ephemeral=True)


bot.run(token)
