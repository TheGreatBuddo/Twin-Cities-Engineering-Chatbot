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
firebaseurl = {'databaseURL': os.getenv('firebaseurl')}
databaseApp = firebase_admin.initialize_app(cred, firebaseurl)

# Set Discord default intents required for class definition
intents = discord.Intents.default()
intents.message_content = True
discord_guild_id = 806384251539947530


class MyClient(discord.Client):

    def __init__(self):
        super().__init__(intents=intents)
        self.synced = False

    async def on_ready(self):
        await tree.sync(guild=discord.Object(id=discord_guild_id))
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


# # Ping Pong slash command
# @tree.command(name="ping", description="Pings the user", guild=discord.Object(id=discord_guild_id))
# async def self(interaction: discord.Interaction):
#     await interaction.response.send_message(f"Pong")
#
#
# @tree.command(name="goal", description="User defined goal", guild=discord.Object(id=discord_guild_id))
# async def self(interaction: discord.Interaction, goal: str):
#     user = interaction.user.name
#     # refer beginning at start of firebase db at forward slash (/)
#     ref = db.reference(f"/")
#     # Update the database with user defined goal
#     ref.push({
#         user: {"Goal": goal}
#     })
#     await interaction.response.send_message(f"Your goal \"{goal}\" has been stored in firebase ")
#
# # inform the user the bot will check in with them for their status
# # Allow user to check off the goal
#
# # To_do list
# # Allow user to type deadline
# # allow bot to remind user in response to deadline
# # allow user to retype deadline after answering a storyline prompt through rasa explaining the ins and outs.
#
# @tree.command(name="complete", description="User to erase a goal", guild=discord.Object(id=discord_guild_id))
# async def self(interaction: discord.Interaction):
#     user = interaction.user.name
#     # refer beginning at start of firebase db at forward slash (/)
#     ref = db.reference(f"/{user}/Goal")
#     #Fetch goal from database
#     goal = ref.get()
#
#     # Update the database with user defined goal
#     #ref.child(goal).delete()
#     #await interaction.response.send_message(f"Your goal \"{goal}\" has been stored in firebase ")


client.run(token)
