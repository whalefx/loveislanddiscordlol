import discord
import os
from contestants import *

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('hello!')

    if message.content.startswith('!'):
        first_word = message.content[1:].split()[0].lower()
        if first_word in contestants_names:
            find_bio = get_bio(first_word)
            await message.channel.send(file=discord.File(find_bio[0]))
            await message.channel.send(f"{find_bio[1]}")


client.run(os.getenv('token'))