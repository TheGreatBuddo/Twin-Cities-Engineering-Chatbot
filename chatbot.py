import discord
import requests
import os

from rasa_connection import curl_request
from dotenv import load_dotenv

# Load Discord Bot Token
load_dotenv()
token = os.getenv('TOKEN')

# Set Discord default intents required for class definition
intents = discord.Intents.default()
intents.message_content = True


class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        if message.author != self.user:
            # Use curl_request Function (located in rasa_connection.py)
            answers = curl_request(message.content, str(message.author))

            # Insert all Respons into one String so we can return it into the Discord Channel
            end_response = " \n ".join((answers))

            # Return the message in a Discord Channel
            return await message.channel.send(f'{message.author.mention} ' + end_response)


client = MyClient(intents=intents)
client.run(token)
