import discord
from discord.ext import tasks, commands
import asyncio
import datetime
import sqlite3
from time import sleep
import json

class showFeedbackCog(commands.Cog, name="view"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    # @commands.has_role("Verified")
    async def view(self , ctx, user:discord.Member=None):
        #;;view @Drillenissen
        if user == None:
            user = ctx.author

        db = sqlite3.connect("main.db")
        cursor = db.cursor()
        cursor.execute(f"SELECT name, url FROM verify WHERE user_id = '{user.id}'")
        usrData = cursor.fetchone()
        if usrData is not None:
            habbo = usrData[0]
            img = usrData[1]
        else:
            habbo = "Not set"
            img = ""

        cursor.execute(f"SELECT status, comment, reviewer FROM feedBack WHERE user_id = '{user.id}' ORDER BY time DESC")
        result2 = cursor.fetchall()
        if len(result2) == 0:
            embed = discord.Embed(color=0xa00009, description=f"User: {user.mention}\nID: {user.id}")#\nHabbo name: {habbo}")
       #     **{user.id}**)
            embed.set_author(icon_url=user.avatar_url, name=f"Feedback Info for {user.name}")


   #         embed.set_thumbnail(url=img)

            embed.add_field(name="Positive", value=f"```diff\n+ 0```")
            embed.add_field(name="Negative", value=f"```diff\n- 0```")
            embed.add_field(name="Total", value=f"```0```")
            embed.add_field(name=f"Comments [0]", value="‎")
            message = await ctx.send(embed=embed)

            await message.add_reaction("⬅️")
            await message.add_reaction("➡️")

            def check(reaction, user):
                return user == ctx.author and reaction.message.id == message.id and not user.bot

            while True:
                try:
                    reaction, user = await self.bot.wait_for('reaction_add')#, check=check)
      #              reaction, user = await self.bot.wait_for('reaction_add', timeout=300.0, check=check)
                except asyncio.TimeoutError:
                    embed.set_footer(text=f"Habbo Chill Hub")
                    await message.edit(embed=embed)
                    break
     #           else:
     #               await message.remove_reaction(reaction, user)
        else:
            comments = []
            posetive = 0
            negative = 0
            total = 0
            for i in result2:
                if i[0] == "1":
                    posetive += 1
                else:
                    negative += 1
                #COMMENTS
                if i[1] != None:
                    commenter = ctx.guild.get_member(int(i[2]))
                    comments.append((commenter, i[1], i[0]))
                    total += 1

            embed = discord.Embed(color=0xa00009, description=f"User: {user.mention}\nID: {user.id}") #\nHabbo name: {habbo}")
            embed.set_author(icon_url=user.avatar_url, name=f"Feedback for {user.name}")
        #    embed.set_thumbnail(url=img)

            embed.add_field(name="Positive", value=f"```diff\n+ {posetive}```")
            embed.add_field(name="Negative", value=f"```diff\n- {negative}```")
            embed.add_field(name="Total", value=f"```{posetive+negative}```")


            indx = 0

            out = ""
            for usr, comment, rate in comments:
                print(usr)
                if indx == 5:
                    break
                if usr is not None:
                    if rate == "1":
                        rate = "Positive"
                    else:
                        rate = "Negative"
                    out += f"{usr.mention} » {rate.capitalize()} » {comment}\n"
      #              indx2 += 1
                    indx += 1
            if out != "":
                embed.add_field(name=f"Comments [{len(comments)}]", value=out)

            else:
                embed.add_field(name=f"Comments [0]", value="‎")

            message = await ctx.send(embed=embed)

    @commands.command()
    # @commands.has_role("Verified")
    async def viewfeedback(self , ctx, user:discord.Member=None):
        #;;view @Drillenissen
        if user == None:
            user = ctx.author

        db = sqlite3.connect("main.db")
        cursor = db.cursor()
        cursor.execute(f"SELECT name, url FROM verify WHERE user_id = '{user.id}'")
        usrData = cursor.fetchone()
        if usrData is not None:
            habbo = usrData[0]
            img = usrData[1]
        else:
            habbo = "Not set"
            img = ""

        cursor.execute(f"SELECT status, comment, reviewer FROM feedBack WHERE user_id = '{user.id}' ORDER BY time DESC")
        result2 = cursor.fetchall()
        if len(result2) == 0:
            embed = discord.Embed(color=0xa00009, description=f"User: {user.mention}\nID: {user.id}")#\nHabbo name: {habbo}")
       #     **{user.id}**)
            embed.set_author(icon_url=user.avatar_url, name=f"Feedback Info for {user.name}")


   #         embed.set_thumbnail(url=img)

            embed.add_field(name="Positive", value=f"```diff\n+ 0```")
            embed.add_field(name="Negative", value=f"```diff\n- 0```")
            embed.add_field(name="Total", value=f"```0```")
            embed.add_field(name=f"Comments [0]", value="‎")
            message = await ctx.send(embed=embed)

            await message.add_reaction("⬅️")
            await message.add_reaction("➡️")

            def check(reaction, user):
                return user == ctx.author and reaction.message.id == message.id and not user.bot

            while True:
                try:
                    reaction, user = await self.bot.wait_for('reaction_add')#, check=check)
      #              reaction, user = await self.bot.wait_for('reaction_add', timeout=300.0, check=check)
                except asyncio.TimeoutError:
                    embed.set_footer(text=f"Habbo Chill Hub")
                    await message.edit(embed=embed)
                    break
     #           else:
     #               await message.remove_reaction(reaction, user)
        else:
            comments = []
            posetive = 0
            negative = 0
            total = 0
            for i in result2:
                if i[0] == "1":
                    posetive += 1
                else:
                    negative += 1
                #COMMENTS
                if i[1] != None:
                    commenter = ctx.guild.get_member(int(i[2]))
                    comments.append((commenter, i[1], i[0]))
                    total += 1

            embed = discord.Embed(color=0xa00009, description=f"User: {user.mention}\nID: {user.id}") #\nHabbo name: {habbo}")
            embed.set_author(icon_url=user.avatar_url, name=f"Feedback for {user.name}")
        #    embed.set_thumbnail(url=img)

            embed.add_field(name="Positive", value=f"```diff\n+ {posetive}```")
            embed.add_field(name="Negative", value=f"```diff\n- {negative}```")
            embed.add_field(name="Total", value=f"```{posetive+negative}```")


            indx = 0

            out = ""
            for usr, comment, rate in comments:
                print(usr)
                if indx == 5:
                    break
                if usr is not None:
                    if rate == "1":
                        rate = "Positive"
                    else:
                        rate = "Negative"
                    out += f"{usr.mention} » {rate.capitalize()} » {comment}\n"
      #              indx2 += 1
                    indx += 1
            if out != "":
                embed.add_field(name=f"Comments [{len(comments)}]", value=out)

            else:
                embed.add_field(name=f"Comments [0]", value="‎")

            message = await ctx.send(embed=embed)

    @commands.command()
    # @commands.has_role("Verified")
    async def fb(self , ctx, user:discord.Member=None):
        #;;view @Drillenissen
        if user == None:
            user = ctx.author

        db = sqlite3.connect("main.db")
        cursor = db.cursor()
        cursor.execute(f"SELECT name, url FROM verify WHERE user_id = '{user.id}'")
        usrData = cursor.fetchone()
        if usrData is not None:
            habbo = usrData[0]
            img = usrData[1]
        else:
            habbo = "Not set"
            img = ""

        cursor.execute(f"SELECT status, comment, reviewer FROM feedBack WHERE user_id = '{user.id}' ORDER BY time DESC")
        result2 = cursor.fetchall()
        if len(result2) == 0:
            embed = discord.Embed(color=0xa00009, description=f"User: {user.mention}\nID: {user.id}")#\nHabbo name: {habbo}")
       #     **{user.id}**)
            embed.set_author(icon_url=user.avatar_url, name=f"Feedback Info for {user.name}")


   #         embed.set_thumbnail(url=img)

            embed.add_field(name="Positive", value=f"```diff\n+ 0```")
            embed.add_field(name="Negative", value=f"```diff\n- 0```")
            embed.add_field(name="Total", value=f"```0```")
            embed.add_field(name=f"Comments [0]", value="‎")
            message = await ctx.send(embed=embed)

            await message.add_reaction("⬅️")
            await message.add_reaction("➡️")

            def check(reaction, user):
                return user == ctx.author and reaction.message.id == message.id and not user.bot

            while True:
                try:
                    reaction, user = await self.bot.wait_for('reaction_add')#, check=check)
      #              reaction, user = await self.bot.wait_for('reaction_add', timeout=300.0, check=check)
                except asyncio.TimeoutError:
                    embed.set_footer(text=f"Habbo Chill Hub")
                    await message.edit(embed=embed)
                    break
     #           else:
     #               await message.remove_reaction(reaction, user)
        else:
            comments = []
            posetive = 0
            negative = 0
            total = 0
            for i in result2:
                if i[0] == "1":
                    posetive += 1
                else:
                    negative += 1
                #COMMENTS
                if i[1] != None:
                    commenter = ctx.guild.get_member(int(i[2]))
                    comments.append((commenter, i[1], i[0]))
                    total += 1

            embed = discord.Embed(color=0xa00009, description=f"User: {user.mention}\nID: {user.id}") #\nHabbo name: {habbo}")
            embed.set_author(icon_url=user.avatar_url, name=f"Feedback for {user.name}")
        #    embed.set_thumbnail(url=img)

            embed.add_field(name="Positive", value=f"```diff\n+ {posetive}```")
            embed.add_field(name="Negative", value=f"```diff\n- {negative}```")
            embed.add_field(name="Total", value=f"```{posetive+negative}```")


            indx = 0

            out = ""
            for usr, comment, rate in comments:
                print(usr)
                if indx == 5:
                    break
                if usr is not None:
                    if rate == "1":
                        rate = "Positive"
                    else:
                        rate = "Negative"
                    out += f"{usr.mention} » {rate.capitalize()} » {comment}\n"
      #              indx2 += 1
                    indx += 1
            if out != "":
                embed.add_field(name=f"Comments [{len(comments)}]", value=out)

            else:
                embed.add_field(name=f"Comments [0]", value="‎")

            message = await ctx.send(embed=embed)


 
def setup(bot):
    bot.add_cog(showFeedbackCog(bot))
    print("view is loaded")
