#B-Bot by Ferontwix aka B-Nuke

import discord
import youtube_dl
from discord import Game
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
from itertools import cycle
import random

startup_extensions = ["Music"]

BOT_PREFIX = ("/")
bot = commands.Bot(command_prefix=BOT_PREFIX)

status = ['On feature development', 'Prefix: /', 'Do /help for help', 
'Zephyr: Only for Neo Hotel', 'Created by B-Nuke', 'with humans', 'Music', 'Don\'t forget to share the server']

async def change_status():
    await bot.wait_until_ready()
    msg = cycle(status)

    while not bot.is_closed:
        current_status = next(msg)
        await bot.change_presence(game=Game(name=current_status))
        await asyncio.sleep(120)

@bot.event
async def on_ready():
    print ("Bot online.\n")

@bot.event
@commands.has_role("Tester")
async def on_message(message):
    await bot.process_commands(message)

@bot.command()
@commands.has_role("Tester")
async def load(extension):
    """Loads a certain category of commands"""
    try:
        bot.load_extension(extension)
        print('{} loaded'.format(extension))
        await bot.say('{} loaded'.format(extension))
    except Exception as error:
        print('Failed to load extension {}. [{}]'.format(extension, error))

@bot.command()
@commands.has_role("Tester")
async def unload(extension):
    """Unloads a certain category of commands"""
    try:
        bot.unload_extension(extension)
        print('{} unloaded'.format(extension))
        await bot.say('{} unloaded'.format(extension))
    except Exception as error:
        print('Failed to unload extension {}. [{}]'.format(extension, error))

if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as error:
                print('Failed to load extension {}. [{}]'.format(extension, error))

    bot.loop.create_task(change_status())
    bot.run(token)
