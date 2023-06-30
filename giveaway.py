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
import random
import uuid

class GiveawayCog(commands.Cog, name="Giveaway"):
    def __init__(self, bot):
        self.bot = bot
        self.update.start()

    @commands.command()
    async def roll(self, ctx, id:int, amount:int):
        role = ctx.guild.get_role(722461783398547554)
        channel = ctx.guild.get_channel(722461784178688051)
        
        channel = ctx.channel
        message = await channel.fetch_message(id)

        if len(message.reactions) == 0:
            await ctx.send("No reactions on this message.")
            return

        users = []
        async for user in message.reactions[0].users():
            users.append(user)

        random.shuffle(users)
        indx = 0
        for user in users:
   #     for user in shuffeld:
            if indx != amount:
                await channel.send(f"{user.mention} wont the giveaway!\n{message.jump_url}")
            else:
                return
            indx += 1

  #      channel = ctx.channel
 #          for i in range(amount):
  #          message = await channel.fetch_message(id)

  #          if len(message.reactions) == 0:
  #              await ctx.send("No reactions on this message.")
  #              return

  #          users = []
 #           async for user in message.reactions[0].users():
 #               users.append(user)
 #           print(users)
          #  while True:
 #           while len(users) != 0:
 #               choice = random.choice(users)
  #              if role in choice.roles:
  #                  await channel.send(f"{choice.mention} wont the giveaway!\n{message.jump_url}")
 #                   await message.remove_reaction(message.reactions[0], choice)
 #                   break
  #              users.pop(users.index(choice))

    @commands.command()
    async def rig(self, ctx, id:int, user:discord.Member):
        channel = ctx.guild.get_channel(722461784178688051)
        message = await channel.fetch_message(id)
        await channel.send(f"{user.mention} won the giveaway!\n{message.jump_url}")


    @commands.command()
    async def giveaway(self, ctx, date, time, *, title):
        format = "%d%m%y %H:%M"
        date = f"{date} {time}"
        time = datetime.datetime.strptime(date, format)
        remaning = time - datetime.datetime.now()

        strOut = ""
        if remaning.days != 0:
            strOut = f"{remaning.days} days, "

        embed = discord.Embed(olor=0xb20000, title=title, description=f"Time remaning: **{strOut}{round(remaning.seconds/60/60,2)} hours**\nHosted by: {ctx.author.mention}")
        embed.set_footer(text="Ends at")
        embed.timestamp = time
        channel = ctx.guild.get_channel(722461784178688051) #Giveaway Channel ID
        message = await channel.send(embed=embed)
        await message.add_reaction("🥳")
        

        db = sqlite3.connect("main.db")
        cursor = db.cursor()

        sql = ("INSERT INTO giveaways(message_id) VALUES (?)")
        val = (message.id,)

        cursor.execute(sql, val)
        db.commit()
        cursor.close()
        db.close()


    @tasks.loop(seconds=10)
    async def update(self):
        try:
            guild = self.bot.get_guild(722461783373381662)
            channel = guild.get_channel(722461784178688051)

            db = sqlite3.connect("main.db")
            cursor = db.cursor()
            cursor.execute(f"SELECT message_id FROM giveaways")
            results = cursor.fetchall()

            for result in results:
                id = result[0]
                message = await channel.fetch_message(int(id))
                embed = message.embeds[0]
                desc = embed.description
                author = desc.split("\n")[1]

                time = embed.timestamp
                remaning = time - datetime.datetime.now()
                if remaning.total_seconds() <= 0:
                    cursor.execute(f"DELETE from giveaways WHERE message_id = '{id}'")
                    db.commit()
                    cursor.close()
                    db.close()

                    embed.description = f"Time remaning: **0.00 hours**\n{author}"
                    await message.edit(embed=embed)
                    return

                strOut = ""
                if remaning.days != 0:
                    strOut = f"{remaning.days} days, "

                embed.description = f"Time remaning: **{strOut}{round(remaning.seconds/60/60,2)} hours**\n{author}"
                await message.edit(embed=embed)
        except Exception as e:
            print(e)

def setup(bot):
    bot.add_cog(GiveawayCog(bot))
    print("Giveaway is loaded")
