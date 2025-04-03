import discord
import os
import requests
import json
import random
from replit import db
from keep_alive import keep_alive

intents = discord.Intents.default()
intents.members = True




client = discord.Client()

@client.event
async def on_ready():
    print(f'We have logged in as {client.user} because this bot is now alive')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!boba'):
        await message.channel.send('YES PLS')
    if message.content.startswith('can i have a hug'):
        await message.channel.send('im good')
    if message.content.startswith('!nicotine'):
        await message.channel.send('that is not good for anyone')
    if message.content == "!ping":
      await message.channel.send("Pong!")
    elif message.content.startswith("!roll"):
      try:
        num_dice, num_sides = map(int, message.content[6:].split())
      except ValueError:
        await message.channel.send("Invalid input. Use the format `!roll XdY`, where X is the number of dice and Y is the number of sides on each die.")
      return
      dice = [random.randint(1, num_sides) for _ in range(num_dice)]
      total = sum(dice)
      await message.channel.send(f"You rolled {num_dice} dice with {num_sides} sides each. Results: {dice}. Total: {total}.")
    if message.content == "!khai":
      await message.channel.send("SMART person")
    if message.content == "emily you suck":
      await message.channel.send("yeah she does")
    if message.content == "you suck":
      await message.channel.send("nah im better")
    if message.content == "!ethan":
      await message.channel.send("the dude who made me")
    if message.content == "keyclub":
      await message.channel.send("community service club with a lot of asian people")
    if message.content == "STFU":
      await message.channel.send("you stfu")
    if message.content == "!kiss?":
      await message.channel.send("hell no you crazy")
    if message.content == "!pout":
      await message.channel.send("https://tenor.com/view/nayeon-gioated-drilied-kitye-frown-gif-20444920")
    if message.content == "!be serious":
      await message.channel.send("https://tenor.com/view/yoghurt-bnk48-gaga-bnk48-nopparada-ygnprd-yhurtgo48-gif-25082001")
    if message.content == "!transform":
      await message.channel.send("https://tenor.com/view/titantyra-tiktok-gif-18786091")
    if message.content == "you're so cute":
      await message.channel.send("no")
    if message.content == "ur so cute":
      await message.channel.send("no")
    if message.content == "ft?":
      await message.channel.send("nah you weird")
    if message.content == "!aaron":
      await message.channel.send("someone")
    if message.content == "!tim":
      await message.channel.send("ultimate girl haver")
    if message.content == "does ailily pull":
      await message.channel.send("no")      
    if message.content == "!jugbir":
      await message.channel.send("another guy")








keep_alive()
client.run(os.getenv('TOKEN'))
