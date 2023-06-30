import discord
from discord.ext import commands
import asyncio
import datetime
import sqlite3
from time import sleep
import json
import random
import requests
from bs4 import BeautifulSoup

class MessageCog(commands.Cog, name="Message"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_any_role("Owner","Senior Manager","Manager","Senior Moderator","Moderator","Trial Moderator")
 #   @commands.has_role(""Moderator")
    async def motto(self, ctx, user:discord.Member):
        message = await ctx.send("Sending...")
        await message.edit(content="Sent.")
        channel = ctx.guild.get_channel(712687767787929729)
        await channel.send(f"{user.mention}, unable to verify. Please put `HCHVerify` on your motto and re-send your Habbo username. ✨ ")
        
    @commands.command()
    @commands.has_any_role("Owner","Senior Manager","Manager","Senior Moderator","Moderator","Trial Moderator")
    async def howto(self, ctx, user:discord.Member):
        message = await ctx.send("Sending...")
        await message.edit(content="Sent.")
        channel = ctx.guild.get_channel(712687767787929729)
        await channel.send(f"Haiyo {user.mention}, Please refer to <#716591141998559262> on the requirements ~! ✨ ")


    @commands.command()
    @commands.has_any_role("Owner","Senior Manager","Manager","Senior Moderator","Moderator","Trial Moderator")
    async def alt(self, ctx, user:discord.Member):
        message = await ctx.send("Sending...")
        await message.edit(content="Sent.")
        channel = ctx.guild.get_channel(712687767787929729)
        await channel.send(f"{user.mention}, unable to verify. Suspected alternative account ✨ ")
    
        
    @commands.command()
    @commands.has_any_role("Owner","Senior Manager","Manager","Senior Moderator","Moderator","Trial Moderator")
    async def name(self, ctx, user:discord.Member):
        message = await ctx.send("Sending...")
        await message.edit(content="Sent.")
        channel = ctx.guild.get_channel(712687767787929729)
        await channel.send(f"Haiyo {user.mention}, we can't find your Habbo username. Please re-send them again. Do check out <#716591141998559262>")

    @commands.command()
    @commands.has_any_role("Owner")
    async def faq121(self, ctx):
        message = await ctx.send("Sending...")
        await message.edit(content="Sent.")
        channel = ctx.guild.get_channel(730431481826115676)
        await channel.send(file=discord.File('logo.jpg'))
   #     await send_file(area, r"C:\Users\devzo\Downloads\Screenshot_7.png")
        await channel.send(f"\nHow do I get <@&712687767276093505>?\n**Answer:** To get <@&712687767276093505> role, you will need at least +70 Positive feedback on the server or a Moderator+ in casino or have a highly trading background.\n *Please note that we do not transfer other server's trusted role.* \n \n How to become <@&712687767276093506>? \n**Answer:** To become <@&712687767276093506> on the server, you need at least +100 Positive feedback on server and being vouched by Manager(s). \n \n How to get <@&730672358020612117> and what is the benefits? \n**Answer:** To get <@&730672358020612117>, you must have at least have +50 positive feedback on the server. There are some benefits once they receive this role. \n \n How to get <@&715081559853629500> role? \n**Answer:** Habbo Chill Hub reward our active users with free VIP. Please go to this link for more info on how to get VIP role: https://discordapp.com/channels/712687767276093501/712687767640997930/723602640298049588 \n \n VIP perks includes; \n Coloured name \n Change your name at any time \n Higher up on the rankings on the sidebar \n Access to the VIP channels \n (Some special perks will be added soon)\n \n*If you prefer to buy VIP role, the price is 1gb (Monthly subscription), please message any of the <@&712687767276093508>*\n ")

    @commands.command()
    @commands.has_any_role("Owner","Senior Manager","Manager","Senior Moderator","Moderator","Trial Moderator")
    async def deny(self, ctx, user:discord.Member):
        message = await ctx.send("Sending...")
        await message.edit(content="Sent.")
        channel = ctx.guild.get_channel(712687767787929729)
        await channel.send(f"Haiyo {user.mention}, We can't accept your membership request. Do check out <#716591141998559262>")
        
    @commands.command()
    async def rig(self, ctx, user:discord.Member):
        await ctx.message.delete()
        await ctx.send(f"Oit oit, {user.mention} dont rig this!")
        
    @commands.command()
    @commands.has_any_role("Owner","Senior Manager","Manager")
    async def updatefeedback(self, ctx):
        message = await ctx.send("Sending...")
        await message.edit(content="Sent.")
        channel = ctx.guild.get_channel(715201575085146112)
        await channel.send(f"Haiyo, IM BACK! ALIVE! Also previous feedback has been updated. Thank you for waiting! RAWR!")
        
    @commands.command()
    @commands.has_any_role("Owner")
    async def updated(self, ctx):
        message = await ctx.send("Sending...")
        await message.edit(content="Sent.")
        channel = ctx.guild.get_channel(716591141998559262)
        await channel.send(f"To view and access Habbo Chill Hub, you must pass our verification process first. Simply fill out the form below and send it into <#712687767787929729> \n\n``[Habbo username]: Put your habbo username`` \n \nKindly put [HCHVerify] into your HABBO [COM] motto for us to verify your account. \n \n``HCHVerify``\n \nAlso to join, you must at least have:- \n1. Minimum : 1700 Achievement Score \n2. Minimum Creation date: January 2020 ( 01 / 2021 ) \n\nYour account creation date must not exceed January 2020 \n~Do read the <#716642551360389173> \n<@&715056792953946142>")

    @commands.command()
    @commands.has_any_role("Verified")
    async def invite(self, ctx):
        invitelink = await ctx.channel.create_invite(max_age = 300, max_uses=1, unique=True)
        await ctx.author.send(f"Please note this invite link is valid for 5 minutes and 1 invite.")
        await ctx.author.send(invitelink)
        await ctx.send(f"Invite link sent to dm. Requested by {ctx.author.mention}.")



def setup(bot):
    bot.add_cog(MessageCog(bot))
    print("Message is loaded")

    