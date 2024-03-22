import json
import platform
import time

import discord
from colorama import Back, Fore, Style
from discord import app_commands
from discord.ext import commands
from discord.ui import Button, View
from sqlalchemy import insert
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os
import random

from db.db import engine


class Client(commands.Bot):
    """Client class which is an extension of Bot"""

    def __init__(self):
        super().__init__(
            command_prefix="!",  # commands.when_mentioned_or("!"),
            intents=discord.Intents().all(),
        )
        # self.cogslist = ["cogs.cog1"]
        # self.Session = sessionmaker(bind=engine)

    async def setup_hook(self):
        # for ext in self.cogslist:
        #     await self.load_extension(ext)
        print("hello")

    async def on_ready(self):
        prfx = (
            Back.BLACK
            + Fore.GREEN
            + time.strftime("%H:%M:%S EST", time.gmtime())
            + Back.RESET
            + Fore.WHITE
            + Style.BRIGHT
        )
        print(prfx + " Logged in as " + Fore.YELLOW + self.user.name)
        print(prfx + " Bot ID " + Fore.YELLOW + str(self.user.id))
        print(prfx + " Discord Version " + Fore.YELLOW + discord.__version__)
        print(prfx + " Python Version " + Fore.YELLOW + str(platform.python_version()))

        synced = await self.tree.sync()

        print(prfx + " Bot ID " + Fore.YELLOW + str(len(synced)) + " Commands")

    async def on_message(self, message: discord.Message):
        print(message.author.id)
        print(message.author.name)
        print(message.author.display_name)
        if message.author.name == "deetisaac":
            await message.channel.send("hi")

    async def hello(self, ctx):
        button1 = Button(label="Click me!", style=discord.ButtonStyle.green, emoji="👏")

        async def button_callback(interaction):
            await interaction.response.send_message("hi")

        button2 = Button(label="Danger!", style=discord.ButtonStyle.red, emoji="😢")
        view = View()
        view.add_item(button1)
        await ctx.send("Hello")


# with open('config.json', 'r') as f:
#     data = json.load(f)
#     TOKEN = data['TOKEN']
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
print(TOKEN)
bot = Client()


@bot.command(name="99")
async def nine_nine(ctx):
    brooklyn_99_quotes = [
        "I'm the human form of the 💯 emoji.",
        "Bingpot!",
        (
            "Cool. Cool cool cool cool cool cool cool, "
            "no doubt no doubt no doubt no doubt."
        ),
    ]

    response = random.choice(brooklyn_99_quotes)
    await ctx.send(response)


bot.run(TOKEN)
