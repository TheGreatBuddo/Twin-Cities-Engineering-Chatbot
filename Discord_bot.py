import discord
import os
from dotenv import load_dotenv

from rasa_connection import curl_request
import requests
import json

# Credentials
load_dotenv('.env')


class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content.startswith('$hello'):
            await message.channel.send('Hello World!')

        if message.author != self.user:
            # Use curl_request Function (located in rasa_connection.py)
            answers = curl_request(message.content, str(message.author))

            # Insert all Respons into one String so we can return it into the Discord Channel
            end_response = " \n ".join((answers))

            # Return the message in a Discord Channel
            return await message.channel.send(f'{message.author.mention} ' + end_response)


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)

client.run(os.getenv('TOKEN'))
