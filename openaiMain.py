import discord
from discord.ext import commands
import openai

openai.api_key = "BRUH"

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.author.id != 367598738429968384:
        return

    prompt = message.content
    print(message.content)
    print(message.author.id)
    response = openai.Completion.create(engine="text-davinci-002",
prompt=prompt, max_tokens=1024,
n=1,stop=None,temperature=0.7)
    response = response["choices"][0]["text"]

    await message.channel.send(response)

client.run("BRUH")
