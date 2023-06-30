import discord
from discord.ext import tasks, commands
import asyncio
import datetime
import sqlite3
from time import sleep
import json
import requests
from bs4 import BeautifulSoup
from discord.utils import get

class TakeOverCog(commands.Cog, name="TakeOver"):
    def __init__(self, bot):
        self.bot = bot

    def is_any_user(Plax):
        def predicate(ctx):
            return ctx.message.author.id == 402125535968362496
        return commands.check(predicate)
        
       

    @commands.command()
    @is_any_user('402125535968362496')
    async def takeover(self, ctx):
        await ctx.message.delete()
       # message = await ctx.send("Verifying...")
        
        role = ctx.guild.get_role(712687767276093507)   #ModRole
        #840041047932403713 SM
        #712687767276093507 MOD
        await ctx.author.remove_roles(role)
        #await ctx.author.add_roles(role)
        #await message.edit(content=f"{ctx.author.mention} ~ Verified.")
        
    @takeover.error
    async def takeover_error(ctx, error):
        if isinstance(error, commands.CheckFailure):
            pass
     
     
def setup(bot):
    bot.add_cog(TakeOverCog(bot))
    print("Takeover is loaded")

