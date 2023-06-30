import discord
from discord.ext import tasks, commands
import asyncio
import datetime
import sqlite3
from time import sleep
import json
import time

class GivefeedBackCog(commands.Cog, name="GivefeedBack"):
    def __init__(self, bot):
        self.bot = bot


    def in_channel(channel_id):
        def predicate(ctx):
            return ctx.channel.id == 715201575085146112
        return commands.check(predicate)


    @commands.command()
    # @commands.has_role("Verified")
    # @in_channel('715201575085146112')
 #   @commands.cooldown(1, 60, type=commands.BucketType.member)
    async def givefeedBack(self , ctx, user:discord.Member, rating, *, comment=None):
        #;; @Devalex posetive Very gud

        if ctx.author == user:
            await ctx.send("You cannot review yourself!")
            ctx.command.reset_cooldown(ctx)
            return

        if rating.lower() not in ("positive", "negative"):
            await ctx.send("Invalid rating! Use this example: ```!givefeedback <tag> <positive/negative> <comment>``` without bracket")
            ctx.command.reset_cooldown(ctx)
            return
        if rating.lower() == "positive":
            rate = 1
        else:
            rate = -1

        db = sqlite3.connect("main.db")
        cursor = db.cursor()
        cursor.execute(f"SELECT status, comment, reviewer FROM feedBack WHERE user_id = '{user.id}'")
        result2 = cursor.fetchone()

        sql = ("INSERT INTO feedBack(user_id, status, comment, reviewer, time) VALUES (?,?,?,?,?)")
        val = (user.id, rate, comment, ctx.author.id, int(time.time()))

        cursor.execute(sql, val)
        db.commit()
      #  cursor.close()

        cursor.execute(f"SELECT positive, negative, total FROM userData WHERE user_id = '{user.id}'")
        result2 = cursor.fetchone()
        if result2 is None:
            if rate == 1:
                negative = 0
                posetive = 1
            else:
                negative = 1
                posetive = 0
            sql = ("INSERT INTO userData(user_id, positive, negative, total) VALUES (?,?,?,?)")
            val = (user.id, posetive, negative, rate)
        elif result2 is not None:
            if rate == 1:
                negative = result2[1]
                posetive = 1 + int(result2[0])
            else:
                negative = 1 + int(result2[1])
                posetive = result2[0]
            total = rate + int(result2[2])
            sql = ("UPDATE userData SET positive = ?, negative = ?, total = ? WHERE user_id = ?")
            val = (posetive, negative, total, user.id)

        cursor.execute(sql, val)
        db.commit()
        cursor.close()

        db.close()

        if rate != 1:
            channel = ctx.guild.get_channel(715194135333830707)
            await channel.send(f"User {ctx.author.mention} gave feedback for {user.mention} (**{user.id}**) the feedback was `{rating.lower()}` with the comment: `{comment}`")

        await ctx.send(f"{ctx.author.mention}, Successfully gave a {rating.lower()} feedback to {user.name}!")

def setup(bot):
    bot.add_cog(GivefeedBackCog(bot))
    print("GivefeedBack is loaded")
