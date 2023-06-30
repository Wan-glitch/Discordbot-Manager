import discord
from discord.ext import tasks, commands
import asyncio
import datetime
import sqlite3
from time import sleep
import json
import requests
from bs4 import BeautifulSoup
import traceback
import uuid

class ErrorsCog(commands.Cog, name="Errors"):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if hasattr(ctx.command, 'on_error'):
            return

        if isinstance(error, commands.CommandNotFound):
            return
        if isinstance(error, commands.CommandOnCooldown):
            cooldown = error.retry_after
            message = f"Woah, wait!You are on cooldown. Try again in {round(cooldown/60, 2)}m"
        else:
            try:
                ctx.command.reset_cooldown(ctx)
            except:
                pass

        exc = error

        etype = type(exc)
        trace = exc.__traceback__
        verbosity = 4

        lines = traceback.format_exception(etype, exc, trace, verbosity)

        traceback_text = ''.join(lines)

        id = str(uuid.uuid4())

        embed = discord.Embed(title=f"Oh no! An error has occured.", description=f"Uh oh, what do i do now?\n Well first make sure you spelled everything correctly. If you sill need help and the error is persistent you can contact <@402125535968362496> \nError:\n```py\n{error}```")
        embed.set_footer(text=f"Uuid: {id}")
        await ctx.send(embed=embed)

        db = sqlite3.connect("main.db")
        cursor = db.cursor()
        sql = ("INSERT INTO errors(uuid, traceback) VALUES (?,?)")
        val = (id, traceback_text)

        cursor.execute(sql, val)
        db.commit()
        cursor.close()

        db.close()


def setup(bot):
    bot.add_cog(ErrorsCog(bot))
    print("Errors is loaded")
