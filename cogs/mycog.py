import discord
from discord.ext import commands

class Mycog:
    """My custom cog that does stuff!"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def add(self, arg1, arg2):
        """This does stuff!""" 

        result = int(arg1) + int(arg2)
        #Your code will go here
        await self.bot.say(result)

def setup(bot):
    bot.add_cog(Mycog(bot))


