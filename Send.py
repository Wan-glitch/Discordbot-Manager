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

class SendCog(commands.Cog, name="Send"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_any_role("Owner")
    async def send(self, ctx):
   # async def send(self, bot) ctx, user:discord.Member):
  #      await channel.send(f"{user.mention}, who knows <3, got this from some server ")
    #    embed1 = discord.Embed(title="»Feedback« | Moderation", color=0x009401)
    #    embed1.add_field(name="**!giveFeedback [rating (positive/negative)] [user] <comment>**", value="Give a user some feedback!", inline=False)
    #    embed1.add_field(name="**!showFeedback <user>**", value="Get the profile of another member in the community.", inline=False)
    #    embed1.add_field(name="**!leaderboard**", value="Get a list of the top 5 members!", inline=False)
        
        embed1 = discord.Embed(title="HCH Scammer Database", color=0xfa0000)
        embed1.add_field(name="Scammer's Habbo:", value="**[kingbruno](https://www.habbowidgets.com/habinfo/hhus-d00ed65179ad4f39a0c6f5641f52fa37)** / [Retract](https://www.habbowidgets.com/habinfo/hhus-269029339fd8c55e6489bf57fd65137c)", inline=False)
        embed1.add_field(name="Scammer:", value=f"**zay#8334**(<@751427461375459340>)", inline = False)
    #    embed1.add_field(name="Suspected accomplice", value=f"**Verifying...**"
  #      embed1.add_field(name="Scammed:", value="**Snova**", inline=False)
   #     embed1.add_field(name="Scammed Amount:", value="**45gbs**", inline=False)
        embed1.add_field(name="Scammer's Email:", value="**cifvevo@gmail.com / cifvevo1@gmail.com**", inline = False)
        embed1.add_field(name="Details:", value=f"**Click [Here](https://discord.com/channels/712687767276093501/712687767787929723/817584477831561226) for details.**", inline=False)
 #       channel = ctx.guild.get_channel(712687767787929722)
        embed1.set_thumbnail(url="https://www.habbo.com/habbo-imaging/avatarimage?direction=4&head_direction=3&action=wav&gesture=sml&size=m&user=Pumpkunss")
   #     embed1.set_thumbnail(url="https://i.imgur.com/VZGZyso.png")
  #      await channel.send(f"https://cdn.discordapp.com/avatars/715973090512994324/e4ec88a09b5b954723cc4f1796c1eb3a.png? ")

     #Discord
    #    embed1.add_field(name="Discord:", value="**cuteasian16#8193 / lovemakesyoublind#2311 **", inline = False)
    
    #RealStuff
    #    embed1.add_field(name="Real Name:", value="**Johann Raph Sor **", inline = False)

    #    embed1.add_field(name="Facebook:", value="**https://www.facebook.com/profile.php?id=100001822387923**", inline = False)
    #    embed1.add_field(name="Instagram:", value="**https://instagram.com/jeongwoolff?igshid=1b9of5m208lrv**", inline = False)
     
     
     
    #    embed2 = discord.Embed(title="Give Feedback | »Moderation«", color=0x009401)
    #    embed2.add_field(name="**!resetuser [user]**", value=f"Reset a user")
    #    embed2.add_field(name="**!resetall**", value=f"Reset all users", inline=False)


        embeds = (embed1)#, embed2)
        temp = 0
        message = await ctx.send(embed = embed1)
                
def setup(bot):
    bot.add_cog(SendCog(bot))
    print("Send is loaded")

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    #    embed1 = discord.Embed(title="»Feedback« | Moderation", color=0x009401)
    #    embed1.add_field(name="**!giveFeedback [rating (positive/negative)] [user] <comment>**", value="Give a user some feedback!", inline=False)
    #    embed1.add_field(name="**!showFeedback <user>**", value="Get the profile of another member in the community.", inline=False)
    #    embed1.add_field(name="**!leaderboard**", value="Get a list of the top 5 members!", inline=False)
        
     #   embed1 = discord.Embed(title="HCH Scammer Database", color=0xfa0000)
    #    embed1.add_field(name="Scammer's Habbo:", value="**antfood**", inline=False)
   #     embed1.add_field(name="Discord:", value="**hadtrio#9776 <708756194797551686> **", inline = False)
     #   embed1.add_field(name="Scammer's Name:", value="**Loh Keng Hoe**", inline=False)
     #   embed1.add_field(name="Tried to Scammed:", value="**Lyall **", inline=False)
    #    embed1.add_field(name="Scammed Amount:", value="** 25gbs **", inline=False)
     #   embed1.add_field(name="Details:", value="**Giveaway Scamm**", inline=False)
     
     #Discord
    #    embed1.add_field(name="Discord:", value="**cuteasian16#8193 / lovemakesyoublind#2311 **", inline = False)
    
    #RealStuff
    #    embed1.add_field(name="Real Name:", value="**Johann Raph Sor **", inline = False)
    #    embed1.add_field(name="Email:", value="**johnnysins123003@gmail.com / sorianojohann19@gmail.com**", inline = False)
    #    embed1.add_field(name="Facebook:", value="**https://www.facebook.com/profile.php?id=100001822387923**", inline = False)
    #    embed1.add_field(name="Instagram:", value="**https://instagram.com/jeongwoolff?igshid=1b9of5m208lrv**", inline = False)
     
     
     
    #    embed2 = discord.Embed(title="Give Feedback | »Moderation«", color=0x009401)
    #    embed2.add_field(name="**!resetuser [user]**", value=f"Reset a user")
    #    embed2.add_field(name="**!resetall**", value=f"Reset all users", inline=False)


 

                
def setup(bot):
    bot.add_cog(SendCog(bot))
    print("Send is loaded")
