import discord
from discord.ext import tasks, commands
import asyncio
import datetime
import sqlite3
import requests
from time import sleep
import json
import time
import json
import logging
from bs4 import BeautifulSoup
from discord.utils import get


class ModerationCog(commands.Cog, name="Moderation"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_any_role("Owner","Senior Manager", "Manager", "Senior Moderator", "Moderator")
    async def delname(self, ctx, name):
        #;;reset @Devalex
        db = sqlite3.connect("main.db")
        cursor = db.cursor()
        sql = f"DELETE from verify where name = '{name}'"
        cursor.execute(sql)
        db.commit()
        cursor.close()
        db.close()
        channel = ctx.guild.get_channel(715621195361419345)
        await channel.send(f"User {ctx.author.mention} deleted {name} from verification!")
        await ctx.send(f"Cleared Habbo info: {name}.")


    @commands.command()
    @commands.has_any_role("Owner","Senior Manager", "Manager", "Senior Moderator", "Moderator")
    async def delverify(self, ctx, user:discord.Member):
        #;;reset @Devalex
        db = sqlite3.connect("main.db")
        cursor = db.cursor()
        sql = f"DELETE from verify where user_id = '{user.id}'"
        cursor.execute(sql)
        db.commit()
        cursor.close()
        db.close()
        channel = ctx.guild.get_channel(715621195361419345)
        await channel.send(f"User {ctx.author.mention} cleared {user.mention} verification info!")
        await ctx.send(f"Cleared Habbo info of {user.name} ({name}).")


#################### FEEDBACK RESET ###################################
    @commands.command()
    @commands.has_any_role("Owner","Senior Manager", "Manager")
    async def reset(self, ctx, user:discord.Member):
        #;;reset @Devalex
        db = sqlite3.connect("main.db")
        cursor = db.cursor()
        sql = f"DELETE from userData where user_id = '{user.id}'"
        cursor.execute(sql)
        sql = f"DELETE from feedBack where user_id = '{user.id}'"
        cursor.execute(sql)
        db.commit()
        cursor.close()
        db.close()
        channel = ctx.guild.get_channel(730722681930121227)
        await channel.send(f"User {ctx.author.mention} cleared {user.mention} the feedback info!")
        await ctx.send(f"Cleared all data from {user.name}.")

    @commands.command()
    @commands.has_role("Owner")
    async def resetall(self, ctx):
        #;;reset @Drillenissen
        db = sqlite3.connect("main.db")
        cursor = db.cursor()
        sql = f"DELETE from userData"
        cursor.execute(sql)
        sql = f"DELETE from feedBack"
        cursor.execute(sql)
        db.commit()
        cursor.close()
        db.close()
        channel = ctx.guild.get_channel(730722681930121227)
    #    await channel.send(f"{ctx.author.roles}{ctx.author.mention} reset members feedback info!")
        await channel.send(f"User {ctx.author.mention} reset members feedback info!")
        await ctx.send(f"Cleared all users data.")
        await ctx.send("All data removed successfully.")

########################## BLACKLIST #######################################################
    @commands.command()
    @commands.has_any_role("Owner","Senior Manager", "Manager", "Senior Moderator", "Moderator","Trial Moderator")
    async def blacklist (self, ctx, name):
        db = sqlite3.connect("main.db")
        cursor = db.cursor()
        cursor.execute(f"SELECT name FROM Blacklist WHERE name = '{name}'")
        result = cursor.fetchone()
        if result is not None:
            await ctx.send(f"{name} is already in the blacklist.")
            return

  #      results = [result.lower() for result in results]

  #      if name.lower() in results:
  #          await ctx.send(f"{name} is already in the blacklist.")
 #           return


  #      message = await ctx.send("Adding...")
  #      responce = requests.get(f"https://www.habbo.com/api/public/users?name={name}").json()
  #      try:
  #          if responce["error"] == "not-found":
  ##              embed = discord.Embed(title=f"{name} has been banned from Habbo", color=0xb20000, description=f"Uh oh, what do i do now?\nWell first make sure you spelled everything correctly. If you sill need help and the error is persistent you can contact <@402125535968362496>\nError:```py\n404 user not found or has been banned by Habbo.```")
  #              await ctx.send(embed=embed)
  #              return
  #      except KeyError:
  #          pass
        url=f"https://www.habbo.com/habbo-imaging/avatarimage?direction=4&head_direction=3&action=wav&gesture=sml&size=m&user={name}"

        db = sqlite3.connect("main.db")
        cursor = db.cursor()
        cursor.execute(f"SELECT name, url FROM Blacklist WHERE name = '{name}'")
        result2 = cursor.fetchone()
        if result2 is None:
            sql = ("INSERT INTO Blacklist(name, url) VALUES (?,?)")
            val = (name, url)
        elif result2 is not None:
            sql = ("UPDATE Blacklist SET name = ?, url = ? WHERE name = ?")
            val = (name, url)

        cursor.execute(sql, val)
        db.commit()
        cursor.close()
        db.close()
        await ctx.send(content=f"Habbo: **{name}** is added in Scammer Database!")
        channel = ctx.guild.get_channel(724483342745206814)
        await channel.send(f"User {ctx.author.mention} inserted **{name}** into Scammer Database!")

    @commands.command()
    @commands.has_any_role("Owner","Senior Manager", "Manager", "Senior Moderator", "Moderator","Trial Moderator")
    async def bl (self, ctx, name):
        db = sqlite3.connect("main.db")
        cursor = db.cursor()
        cursor.execute(f"SELECT name FROM Blacklist WHERE name = '{name}'")
        result = cursor.fetchone()
        if result is not None:
            await ctx.send(f"{name} is already in the blacklist.")
            return

  #      results = [result.lower() for result in results]

  #      if name.lower() in results:
  #          await ctx.send(f"{name} is already in the blacklist.")
 #           return


        message = await ctx.send("Adding...")
        responce = requests.get(f"https://www.habbo.com/api/public/users?name={name}").json()
        try:
            if responce["error"] == "not-found":
                embed = discord.Embed(title=f"{name} has been banned from Habbo", color=0xb20000, description=f"Uh oh, what do i do now?\nWell first make sure you spelled everything correctly. If you sill need help and the error is persistent you can contact <@402125535968362496>\nError:```py\n404 user not found or has been banned by Habbo.```")
                await ctx.send(embed=embed)
                return
        except KeyError:
            pass
        url=f"https://www.habbo.com/habbo-imaging/avatarimage?direction=4&head_direction=3&action=wav&gesture=sml&size=m&user={name}"

        db = sqlite3.connect("main.db")
        cursor = db.cursor()
        cursor.execute(f"SELECT name, url FROM Blacklist WHERE name = '{name}'")
        result2 = cursor.fetchone()
        if result2 is None:
            sql = ("INSERT INTO Blacklist(name, url) VALUES (?,?)")
            val = (name, url)
        elif result2 is not None:
            sql = ("UPDATE Blacklist SET name = ?, url = ? WHERE name = ?")
            val = (name, url)

        cursor.execute(sql, val)
        db.commit()
        cursor.close()
        db.close()
        await message.edit(content=f"Habbo: **{name}** is added in Scammer Database!")
        channel = ctx.guild.get_channel(820860114654461972)
        await channel.send(f"User {ctx.author.mention} inserted **{name}** into Scammer Database!")

    @commands.command()
    @commands.has_any_role("Owner","Senior Manager", "Manager", "Senior Moderator")
    async def deletebl (self, ctx, name):
        db = sqlite3.connect("main.db")
        cursor = db.cursor()
        cursor.execute(f"SELECT name FROM Blacklist WHERE name = '{name}'")
        result = cursor.fetchone()
        if result is None:
            await ctx.send(f"{name} is not in the blacklist.")
            return

        message = await ctx.send("Deleting...")
        db = sqlite3.connect("main.db")
        cursor = db.cursor()
        sql = f"DELETE from Blacklist where name = '{name}'"
        cursor.execute(sql)

        cursor.execute(sql)
        db.commit()
        cursor.close()
        db.close()

        await message.edit(content=f"Habbo: **{name}** is deleted from Scammer/Blacklist Database!")
        channel = ctx.guild.get_channel(724483342745206814)
        await channel.send(f"User {ctx.author.mention} deleted **{name}** from Scammer Database!")


############################## MODERATION #####################################################3
    @commands.command()
    @commands.has_any_role("Owner","Senior Manager","Manager","Senior Moderator","Moderator","Trial Moderator")
    async def kick(self, ctx, member: discord.Member, *, reason=None):
   #     Roles = [role for role in member.roles]
        if reason is not None:
            await member.send(f'You have been kicked from Habbo Chill Hub for this reason:```{reason}```')

            await asyncio.sleep(3)
            await member.kick(reason=reason)

        elif reason is None:
            await asyncio.sleep(3)
            await member.kick(reason=reason)

        await ctx.send(f'{member.mention} (**{member.id}**) has been kicked')
        channel = ctx.guild.get_channel(717262151521402902)
        await channel.send(f'{ctx.author.mention} kicked {member.mention} ({member.id})')

    @commands.command()
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        await ctx.send(f"Good try {ctx.author.mention}! You're too __poor__ for this lol!")
        
    @commands.command()
    async def pinn(self, ctx, messageID):    
        msg_to_pin = await message.channel.get_message(int(messageID))
        await msg_to_pin.pin()
'''    @commands.command()
    async def warn(self, ctx, user: discord.Member, *, reason=None):
  #      await ctx.send(f"Good try {ctx.author.mention}! You're too __poor__ for this lol!")

        if ctx.author == user:
            await ctx.send("You cannot warn yourself... btw nice try!")
            ctx.command.reset_cooldown(ctx)
            return

        db = sqlite3.connect("userdata.db")
        cursor = db.cursor()
        cursor.execute(f"SELECT user_id, reason, moderator, time FROM WarningData WHERE user_id = '{user.id}'")
        result3 = cursor.fetchone()

        sql = ("INSERT INTO WarningData(user_id, reason, moderator, time) VALUES (?,?,?,?)")
        val = (user.id, reason, ctx.author.id, int(time.time()))

        cursor.execute(sql, val)
        db.commit()
        cursor.close()

        db.close()  
        
        await ctx.send(f"{user.mention} has been warned")
'''

 #   @commands.command()
#    @commands.has_any_role("Owner","Manager","Moderator")
 #   async def unban(ctx, member: discord.Member, *, reason=None):
 #       banned_users = await ctx.guild.bans()
 #       member_name, member_discriminator = member.split('#')

 #       for ban_entry in banned_users:
 #           user = ban_entry.user

 #           if (user.name, user.discriminator) == (member.name, member_discriminator):
  #              await ctx.guild.unban(user)
  #              await ctx.send(f'{ctx.author.mention} unbanned {user.mention}')
  #              channel = ctx.guild.get_channel(717262151521402902)
   #             await channel.send(f'{ctx.author.mention} unbanned {member.mention}({member.id})')
   #             return

def setup(bot):
    bot.add_cog(ModerationCog(bot))
    print("Moderation is loaded")
