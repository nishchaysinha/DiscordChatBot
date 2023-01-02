import discord
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create a new chat bot
bot = ChatBot("My Chat Bot")

# Create a trainer for the bot
trainer = ChatterBotCorpusTrainer(bot)

# Train the bot on a selection of English language corpora
trainer.train("chatterbot.corpus.english.greetings",
              "chatterbot.corpus.english.conversations")

# Initialize the Discord client
client = discord.Client()

@client.event
async def on_message(message):
    # If the message was sent by the bot, ignore it
    if message.author == client.user:
        return

    # Get the response from the chat bot
    response = bot.get_response(message.content)

    # Send the response to the channel
    await message.channel.send(response)

# Run the Discord client
client.run("YOUR_DISCORD_BOT_TOKEN")
