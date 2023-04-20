
# Discord Rasa AI Bot

This Chatbot is developed to be used within the Twin Cities Engineering Discord Community. All foundational
code has been developed by Cybercube21. His GitHub repository is provided with the link. https://github.com/Cybercube21/Rasa-discord-bot.git
The program uses Python to develop Rasa, an open-source AI development platform to communicate with the Discord API.
A chatbot can be connected to a discord bot following the steps.


##Creating a Discord Bot

Visit https://discord.com/developers/applications to create a new application. Here you will create your discord bot.
Follow online tutorials to adding your bot to your respective discord server.


##Discord Bot Token

Generate a discord bot token. This token will be private and should be stored in a private space.

## Downloading GitHub Repository

Following my own process, I used Pycharm Community Edition. When making a new project, clone this repository to gain
access to all files.

Next step is to create a new file in the project folder called ".env". Make sure to include the period in the title of the
file.

Make sure the .env file is a text file.

in the .env file input the discord token you made when you created your discord bot as follows

TOKEN = ADD_Discord_TOKEN_HERE

## Dependencies

To download dependencies I used anaconda to create an environment and download respective dependencies.
First download Anaconda nucleus to get anaconda.
Next learn to create an anaconda environment and use the environment in Pycharm. When your environments fully created use
the following commands in the terminal to install rasa, discord, and dotenv needed to run the project.

```sh
$ pip3 install rasa 
$ pip3 install discord.py python_dotenv pytz requests
```

## How to Use

Make sure the bot has joined the discord server with proper permissions to communicate. 
```sh
# If running for the first time, use "python -m rasa train" to train a new Rasa model

$ python3 chatbot.py # To start the Bot

# Then open a new Terminal and go in the model/ Folder
# To go into the model folder in terminal use the command "cd model".

#Execute this command in terminal to begin running the rasa server
$ rasa run --enable-api --credentials credentials.yml --cors "*" # To Start the Rasa Server
```
If both the chatbot.py file is running and rasa server is up as mentioned in terminal then your discord bot should
be online. You can chat to him and he will respond by extracting an intent from the users message triggering an
action which responds to the user. 

Rules, and text prompts can be edited in rules.yml, and domain.yml. Editing nlu.yml can improve the bots capability to 
respond to new user requests. Creating stories can improve communication if content evolves.
