#!/usr/bin/env python3.10
import os

import discord
from discord import utils
from discord.ext import commands
from dotenv import load_dotenv

COMMAND_PREFIX = "!RB "
COGS_LOCATION = "cogs"

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

def loadCogs(bot):
    for file in os.listdir(COGS_LOCATION):
        if file.endswith(".py"):
            cogname, ext = os.path.splitext(file)
            bot.load_extension(COGS_LOCATION + "." + cogname)

bot = commands.Bot(command_prefix=COMMAND_PREFIX)
loadCogs(bot)

@bot.event
async def on_connect():
    print(f'{bot.user} connected')

@bot.event
async def on_disconnect():
    print(f'{bot.user} disconnected')

@bot.event
async def on_ready():
    print(f'{bot.user} ready')

@bot.command()
async def ping(ctx):
    await ctx.channel.send("pong")

bot.run(TOKEN)