TOKEN = 'MTA3MTc4NzE0ODQxNzcxMjIwOQ.GfjoZ7.5xerRLMbKuNgJjo_BmDCVZg1IY_O8jtBqiAF1E'
GUILD = "TheGreatBuddo's server"

import discord


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

client.run(TOKEN)