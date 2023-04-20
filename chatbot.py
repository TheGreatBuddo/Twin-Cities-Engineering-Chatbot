import os

import discord
from discord import app_commands
from dotenv import load_dotenv

# Imports to use google firebase if future development wants to user store data
# import firebase_admin
# from firebase_admin import credentials
# from firebase_admin import db

from rasa_connection import curl_request

# Load Discord Bot Token
load_dotenv()
token = os.getenv('TOKEN')

#Currently commented out code to use google firebase as a database.
#Can be used in the future to store information from users.
# cred = credentials.Certificate('firebasekey.json')
# firebaseurl = {'databaseURL': os.getenv('firebaseurl')}
# databaseApp = firebase_admin.initialize_app(cred, firebaseurl)

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
            #debug print
            #print(message.content, message.author)
            # Insert all Responses into one String so we can return it into the Discord Channel
            end_response = " \n ".join((answers))
            print(end_response)
            # Return the message in a Discord Channel
            return await message.channel.send(f'{message.author.mention} ' + end_response)


client = MyClient()
tree = app_commands.CommandTree(client)


client.run(token)

#Example code to create commands in discord

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


# Beginning code to use firebase as a database

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