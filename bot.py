import os
import discord
from discord.ext import commands
import asyncio

BOT_TOKEN = ''
GUILD_ID = 1198699628376363048  # Replace with your guild ID

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.members = True
intents.messages = True

bot = commands.Bot(command_prefix='=', intents=intents, help_command=None)

def is_valid_guild():
    def predicate(ctx):
        return ctx.guild.id == GUILD_ID
    return commands.check(predicate)

async def load():
    print("Starting bot....")
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            # cut off the .py from the file name
            await bot.load_extension(f"cogs.{filename[:-3]}")

async def set_status():
    await bot.wait_until_ready()
    activity = discord.Game(name="with commands | !help")
    await bot.change_presence(activity=activity)

async def main():
        await load()
        await bot.start(BOT_TOKEN)
        await set_status()

asyncio.run(main())