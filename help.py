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

class HelpCog(commands.Cog, name="Help"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_role("Verified")
    async def help(self, ctx):
    #    embed1 = discord.Embed(title="»Feedback« | Moderation", color=0x009401)
    #    embed1.add_field(name="**!giveFeedback [rating (positive/negative)] [user] <comment>**", value="Give a user some feedback!", inline=False)
    #    embed1.add_field(name="**!showFeedback <user>**", value="Get the profile of another member in the community.", inline=False)
    #    embed1.add_field(name="**!leaderboard**", value="Get a list of the top 5 members!", inline=False)
        
        embed1 = discord.Embed(title="HCH Feedback Help | Commands", color=0x009401)
        embed1.add_field(name="**!giveFeedback [rating (positive/negative)] [user] <comment>**", value="Give a user some feedback!", inline=False)
        embed1.add_field(name="**!view <user>**", value="Get the profile of another member in the community.", inline=False)
        embed1.add_field(name="**!invite**", value="Bot will generate invite link which valid for 5mins and 1 user.", inline=False)
        embed1.add_field(name="**!leaderboard**", value="Get a list of the top 5 members!", inline=False)
        embed1.add_field(name="**!help**", value="Get a list of commands!", inline=False)
        
    #    embed2 = discord.Embed(title="Give Feedback | »Moderation«", color=0x009401)
    #    embed2.add_field(name="**!resetuser [user]**", value=f"Reset a user")
    #    embed2.add_field(name="**!resetall**", value=f"Reset all users", inline=False)


        embeds = (embed1)#, embed2)
        temp = 0

        message = await ctx.send(embed = embed1)

     #   await message.add_reaction("⏪")
        await message.add_reaction("🗑️")
     #   await message.add_reaction("⏩")

        def check(reaction, user):
            return user == ctx.author and reaction.message.id == message.id and not user.bot

        while True:
            try:
                reaction, user = await self.bot.wait_for('reaction_add', timeout=300.0, check=check)
            except asyncio.TimeoutError:
                break
            else:
                if str(reaction) == "⏪":
                    temp -= 1
                elif str(reaction) == "⏩":
                    temp += 1
                elif str(reaction) == "🗑️":
                #   if str(reaction) == "🗑️":
                    await message.delete()
                    break
                indx = temp % len(embeds)
                await message.edit(embed=embeds[indx])
                await message.remove_reaction(reaction, user)

#################################################################################################

    @commands.command()
    @commands.has_any_role("Owner","Senior Manager","Manager","Senior Moderator","Moderator","Trial Moderator")
    async def cmd(self, ctx):
    #    embed1 = discord.Embed(title="»Feedback« | Moderation", color=0x009401)
    #    embed1.add_field(name="**!giveFeedback [rating (positive/negative)] [user] <comment>**", value="Give a user some feedback!", inline=False)
    #    embed1.add_field(name="**!showFeedback <user>**", value="Get the profile of another member in the community.", inline=False)
    #    embed1.add_field(name="**!leaderboard**", value="Get a list of the top 5 members!", inline=False)
        
        embed2 = discord.Embed(title="HCH Feedback MOD | MOD Commands", color=0x009401)
        embed2.add_field(name="**!userinfo [User]**", value="Find member's info!", inline=False)
        embed2.add_field(name="**!find [Habbo username]**", value="Find Habbo username that has been registered to HCH!", inline=False)
        embed2.add_field(name="**!bl [Habbo username]**", value="Blacklist Habbo username from entering HCH!", inline=False)
        embed2.add_field(name="**!deletebl [Habbo username] **", value="Delete blacklisted Habbo username", inline=False)
        embed2.add_field(name="**!kick [User]**", value="Kick a member out of HCH!", inline=False)
        embed2.add_field(name="**!delname [Habbo username]**", value="Delete habbo username from HCH Database!", inline=False)
        embed2.add_field(name="**!delverify [Discord ID]**", value="Delete habbo username through ID from HCH Database!", inline=False)
        
        
    #    embed2 = discord.Embed(title="Give Feedback | »Moderation«", color=0x009401)
    #    embed2.add_field(name="**!resetuser [user]**", value=f"Reset a user")
    #    embed2.add_field(name="**!resetall**", value=f"Reset all users", inline=False)


        embeds = (embed2)#, embed2)
        temp = 0

        message = await ctx.send(embed = embed2)

     #   await message.add_reaction("⏪")
        await message.add_reaction("🗑️")
     #   await message.add_reaction("⏩")

        def check(reaction, user):
            return user == ctx.author and reaction.message.id == message.id and not user.bot

        while True:
            try:
                reaction, user = await self.bot.wait_for('reaction_add', timeout=300.0, check=check)
            except asyncio.TimeoutError:
                break
            else:
                if str(reaction) == "⏪":
                    temp -= 1
                elif str(reaction) == "⏩":
                    temp += 1
                elif str(reaction) == "🗑️":
                #   if str(reaction) == "🗑️":
                    await message.delete()
                    break
                indx = temp % len(embeds)
                await message.edit(embed=embeds[indx])
                await message.remove_reaction(reaction, user)

                
def setup(bot):
    bot.add_cog(HelpCog(bot))
    print("Help is loaded")
