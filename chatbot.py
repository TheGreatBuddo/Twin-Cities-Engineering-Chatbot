import os

import discord
import firebase_admin
from discord import app_commands
from dotenv import load_dotenv
from firebase_admin import credentials
from firebase_admin import db

from rasa_connection import curl_request

# Load Discord Bot Token and Firebase key
load_dotenv()
token = os.getenv('TOKEN')
cred = credentials.Certificate('firebasekey.json')
databaseApp = firebase_admin.initialize_app(cred, os.getenv('firebaseurl'))

# Set Discord default intents required for class definition
intents = discord.Intents.default()
intents.message_content = True


class MyClient(discord.Client):

    def __init__(self):
        super().__init__(intents=intents)
        self.synced = False

    async def on_ready(self):
        await tree.sync(guild=discord.Object(id=806384251539947530))
        self.synced = True
        print("Bot is Online")

    async def on_message(self, message):
        if message.author != self.user:
            # Use curl_request Function (located in rasa_connection.py)
            answers = curl_request(message.content, str(message.author))

            # Insert all Response into one String, so we can return it into the Discord Channel
            end_response = " \n ".join((answers))

            # Return the message in a Discord Channel
            return await message.channel.send(f'{message.author.mention} ' + end_response)


client = MyClient()
tree = app_commands.CommandTree(client)


# Ping Pong slash command
@tree.command(name="ping", description="Pings the user", guild=discord.Object(id=806384251539947530))
async def self(interaction: discord.Interaction):
    await interaction.response.send_message(f"Pong")


client.run(token)
