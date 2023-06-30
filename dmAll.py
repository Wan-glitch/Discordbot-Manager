import discord
from discord.ext import tasks, commands
import asyncio
import datetime
import sqlite3
from time import sleep
import time
import json
import logging
from discord.ext import commands

class DmAllCog(commands.Cog, name="DmAll"):
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    @commands.has_any_role("Owner", "Senior Manager")
    async def dmall(self, ctx, id:int, *, message):
        role = ctx.guild.get_role(id)
        if role is None:
            await ctx.send("Role not found")
            return

        edit = await ctx.send(f"Dmming {len(role.members)} members")
        success = 0
        fails = 0
        for member in role.members:
            try:
                await member.send(message)
            except:
                fails += 1
            else:
                success += 1

        await edit.edit(content=f"Messaged {success} members with {fails} fials")

    @commands.command()
    @commands.has_any_role("Owner","Manager")
    async def dm(self, ctx, member: discord.Member, *, message):
        if member is None:
            await ctx.send("Please mention the user or put their id")
            return

        edit = await ctx.send(f"Direct messaged {member} member with message: ```{message}```")
   #     success = 0
  #      fails = 0
        
        await member.send(message)
#        await member.send(image)
  #      await channel.send(file=discord.File('logo.jpg'))


def setup(bot):
    bot.add_cog(DmAllCog(bot))
    print("DmAll is loaded")


 
