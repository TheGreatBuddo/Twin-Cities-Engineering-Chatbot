
import discord
import os
from dotenv import load_dotenv

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

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)

client.run(os.getenv('TOKEN'))