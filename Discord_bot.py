TOKEN = 'MTA3MTc4NzE0ODQxNzcxMjIwOQ.GlEmoy._t3rCg_2dmmP6P3oazFndjk3tYupdjYYq37-yA'
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

#Intents is a new thinggy.

a = 4
print(a)


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)

client.run(TOKEN)