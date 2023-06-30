import re
import discord
from discord.ext import tasks, commands
import asyncio
import datetime
import sqlite3
from time import sleep
import json

class RelayCog(commands.Cog, name="Relay"):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        # guild = message.guild
        # if guild is None:
        #     serverGuild = self.bot.get_guild(712687767276093501)
        #     channel = serverGuild.get_channel(730733201538154516)
        #     await channel.send(f"{message.author.mention} says: ```{message.content}```")

        x = re.findall("(?:https?://)?discord(?:(?:app)?\.com/invite|\.gg)/?[a-zA-Z0-9]+/?", message.content)
        if len(x) != 0 and not message.author.bot:
            await message.delete()
            context = await self.bot.get_context(message)

            out = f"Member - {message.author.mention} `({message.author.id})`\n**Invite codes:**\n"

            for i in x:
                try:
                    invite_converter = discord.ext.commands.InviteConverter()
                    invite = await invite_converter.convert(context, i)

                    if invite.guild is not None:
                        out += f"`{invite.code}` | {invite.guild.name}\n"
                    else:
                        out += f"`{invite.code}` | DM Invite\n"

                except discord.ext.commands.errors.BadArgument:
                    codeIndx = i[::-1].find("/")
                    code = i[::-1][:codeIndx][::-1]

                    out += f"`{code}` | Invalid Invite\n"


            embed = discord.Embed(color = 0xff4040, title = "Invite code detected", description = out)

            channel = message.guild.get_channel(774619716902715422)
            await channel.send(embed=embed)



def setup(bot):
    bot.add_cog(RelayCog(bot))
    print("Relay is loaded")
