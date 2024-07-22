# This only works with:
# pip install openai==0.28

import asyncio
import discord
import requests
import os
import openai

TOKEN = 'DISCORD TOKEN'
openai.api_key = "OPENAI API KEY"


intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    text = message.content
    text = text.lower()
    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": text}])
    await message.channel.send(completion.choices[0].message.content)
    return




client.run(TOKEN)
