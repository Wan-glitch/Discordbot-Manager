import discord
from discord.ext import tasks, commands
import asyncio
import datetime
import sqlite3
from time import sleep
import json

class Relay1Cog(commands.Cog, name="Relay1"):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        guild = message.guild
        if guild is None:
            serverGuild = self.bot.get_guild(712687767276093501)
            channel = serverGuild.get_channel(730733201538154516)
            await channel.send(f"{message.author.mention} says: ```{message.content}```")


def setup(bot):
    bot.add_cog(Relay1Cog(bot))
    print("Relay1 is loaded")
