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

class VerifyCog(commands.Cog, name="Verify"):
    def __init__(self, bot):
        self.bot = bot


    def in_channel(channel_id):
        def predicate(ctx):
            return ctx.channel.id == 715067852566036500
        return commands.check(predicate)

    @commands.command()
    @commands.has_any_role("Owner","Senior Manager","Manager","Senior Moderator","Moderator","Trial Moderator")
    # @in_channel('715067852566036500')
    async def verify(self, ctx, user:discord.Member, name):
        db = sqlite3.connect("main.db")
        cursor = db.cursor()
        cursor.execute(f"SELECT name FROM Blacklist")
        results = cursor.fetchall()

        results = [result[0].lower() for result in results]

        if name.lower() in results:
            await ctx.send("This user has been blacklisted. You have permission to ban!```?ban <tag>/<id> <reason>``` Only <@&712687767276093509> & <@&712687767276093508> can use `!fverify` to force verify them.")
            return
            
            
        cursor = db.cursor()
        cursor.execute(f"SELECT name FROM verify")
        result3 = cursor.fetchall()

        result3 = [result[0].lower() for result in result3]

        if name.lower() in result3:
  #          await ctx.send("This user already verified. Please notify the <@&712687767276093508> if there's any error.")
            embed=discord.Embed(title="Verified user", description=f"This user already verified. Please notify the <@&712687767276093508> if there's any error.", color=0xec6565)
            await ctx.send(embed=embed)   
            return


        #;;verify @Devalex1
        message = await ctx.send("Verifying...")
        responce = requests.get(f"https://www.habbo.com/api/public/users?name={name}").json()
        try:
            if responce["error"] == "not-found":
                embed = discord.Embed(title="Oh no! An error has occured.", color=0xb20000, description=f"Uh oh, what do i do now?\nWell first make sure you spelled everything correctly. If you sill need help and the error is persistent you can contact <@402125535968362496>\nError:```py\n404 user not found or has been banned from Habbo.```")
                await ctx.send(embed=embed)
                return
        except KeyError:
            pass
        url=f"https://www.habbo.com/habbo-imaging/avatarimage?direction=4&head_direction=3&action=wav&gesture=sml&size=m&user={name}"

        db = sqlite3.connect("main.db")
        cursor = db.cursor()
        cursor.execute(f"SELECT name, url FROM verify WHERE user_id = '{user.id}'")
        result2 = cursor.fetchone()
            
        if result2 is None:
            sql = ("INSERT INTO verify(user_id, name, url) VALUES (?,?,?)")
            val = (user.id, name, url)
        elif result2 is not None:
            sql = ("UPDATE verify SET name = ?, url = ? WHERE user_id = ?")
            val = (name, url, user.id)

        cursor.execute(sql, val)
        db.commit()
        cursor.close()
        db.close()
        await message.edit(content=f"{user.mention} Verification Successful.")

        channel = ctx.guild.get_channel(715621195361419345)
        await channel.send(f"User {ctx.author.mention} verified {user.mention} ({user.id}) as **{name}** in Habbo data!")
        channel = ctx.guild.get_channel(712687767787929729)
        await channel.send(f"{user.mention} - Verification successful")
        #verified
        #Message
        await user.send(f"Hiya! You've been verified on Habbo Chill Hub. Do check out our channel now <#716595773873061898>. Thank you for joining and don't forget to invite your friends! ❤️" )
        role = ctx.guild.get_role(712687767276093502)
        await user.add_roles(role)
        await asyncio.sleep(2)
        #Unverified
        role = ctx.guild.get_role(715056792953946142)
        await user.remove_roles(role)
        
 #      role = ctx.guild.get_role(712687767276093502)
   #     await asyncio.sleep(5)
  #      await user.add_roles(role)
   #     role = get(ctx.message.server.roles, name='Unverified')
   #     role = ctx.guild.get_role(715056792953946142)
  #      await user.remove_roles(role)
   #     await user.send(f"Hiya! You've been verified on Habbo Chill Hub. Do check out our channel now <#716595773873061898>. Thank you for joining and don't forget to invite your friends! ❤️" )
   #     await asyncio.sleep(2)



##############################""" FORCE VERIFICATION """#########################################################

    @commands.command()
    @commands.has_any_role("Owner","Senior Manager", "Manager", "Senior Moderator")
    @in_channel('715067852566036500')
    async def fverify(self, ctx, user:discord.Member, name):
        #;;verify @Devalex1
        message = await ctx.send("Verifying...")
        responce = requests.get(f"https://www.habbo.com/api/public/users?name={name}").json()
        try:
            if responce["error"] == "not-found":
                embed = discord.Embed(title="Oh no! An error has occured.", color=0xb20000, description=f"Uh oh, what do i do now?\nWell first make sure you spelled everything correctly. If you sill need help and the error is persistent you can contact <@402125535968362496>\nError:```py\n404 user not found or has been banned from Habbo.```")
                await ctx.send(embed=embed)
                return
        except KeyError:
            pass
        url=f"https://www.habbo.com/habbo-imaging/avatarimage?direction=4&head_direction=3&action=wav&gesture=sml&size=m&user={name}"

        db = sqlite3.connect("main.db")
        cursor = db.cursor()
        cursor.execute(f"SELECT name, url FROM verify WHERE user_id = '{user.id}'")
        result2 = cursor.fetchone()
        if result2 is None:
            sql = ("INSERT INTO verify(user_id, name, url) VALUES (?,?,?)")
            val = (user.id, name, url)
        elif result2 is not None:
            sql = ("UPDATE verify SET name = ?, url = ? WHERE user_id = ?")
            val = (name, url, user.id)

        cursor.execute(sql, val)
        db.commit()
        cursor.close()
        db.close()
       
       
        await message.edit(content=f"{user.mention} Verification Successful.")

        channel = ctx.guild.get_channel(715621195361419345)
        await channel.send(f"User {ctx.author.mention} **force** verified {user.mention} ({user.id}) as **{name}** in Habbo data!")
        channel = ctx.guild.get_channel(712687767787929729)
        await channel.send(f"{user.mention} - Verification successful")
        role = ctx.guild.get_role(712687767276093502)
        await asyncio.sleep(2)
        await user.add_roles(role)
   #     role = get(ctx.message.server.roles, name='Unverified')
        role = ctx.guild.get_role(715056792953946142)
        await user.remove_roles(role)
        await user.send(f"Hiya! You've been verified on Habbo Chill Hub. Do check out our channel now <#716595773873061898>. Thank you for joining and don't forget to invite your friends! ❤️" )
        await asyncio.sleep(2)
        role = ctx.guild.get_role(715061196809699370)
        await asyncio.sleep(1)
        await user.add_roles(role)
        await message.edit(content=f"{user.mention} ~ Given <@&715061196809699370>.")

        ##RECHECK THE ROLE
        role = ctx.guild.get_role(712687767276093502)
        await asyncio.sleep(2)
        await user.add_roles(role)
   #     role = get(ctx.message.server.roles, name='Unverified')
        role = ctx.guild.get_role(715056792953946142)
        await user.remove_roles(role)
        await user.send(f"Hiya! You've been verified on Habbo Chill Hub. Do check out our channel now <#716595773873061898>. Thank you for joining and don't forget to invite your friends! ❤️" )
        await asyncio.sleep(2)
        role = ctx.guild.get_role(715061196809699370)
        await asyncio.sleep(1)
        await user.add_roles(role)
        await message.edit(content=f"{user.mention} ~ Given <@&715061196809699370>.")
  
    def is_any_user(Plax):
        def predicate(ctx):
            return ctx.message.author.id == 402125535968362496
        return commands.check(predicate)
        
    @is_any_user('402125535968362496')
    @commands.command()
    async def hverify(self, ctx, user:discord.Member, name):
        channel = ctx.guild.get_channel(717428995867803799)
        await channel.send(f"Verified!")
        channel = ctx.guild.get_channel(715621195361419345)
        await channel.send(f"User {ctx.author.mention} verified {user.mention} ({user.id}) as **{name}** in Habbo data!")
        channel = ctx.guild.get_channel(712687767787929729)
        await channel.send(f"{user.mention} - Verification successful")
        #verified
        #Message
        await user.send(f"Hiya! You've been verified on Habbo Chill Hub. Do check out our channel now <#716595773873061898>. Thank you for joining and don't forget to invite your friends! ❤️" )
        role = ctx.guild.get_role(712687767276093502)
        await user.add_roles(role)
        await asyncio.sleep(2)
        #Unverified
        role = ctx.guild.get_role(715056792953946142)
        await user.remove_roles(role)

    @hverify.error
    async def hverify_error(ctx, error):
        if isinstance(error, commands.CheckFailure):
            pass

def setup(bot):
    bot.add_cog(VerifyCog(bot))
    print("Verify is loaded")

