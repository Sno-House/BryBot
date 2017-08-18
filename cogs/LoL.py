import discord
import cassiopeia as cass
from cassiopeia import Champion
import random
import os
from discord.ext import commands

class Mycog:
    """My custom cog that does stuff!"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def title(self, champ):
        """This does stuff!"""

        champion = Champion(name=champ)
        await self.bot.say(champion.title)

    @commands.command()
    async def item(self, champ):
        champion = Champion(name=champ)

        for spell in champion.spells:
            await self.bot.say(spell.name)
            await self.bot.say(spell.keywords)
            await self.bot.say("--------")


def setup(bot):
    bot.add_cog(Mycog(bot))




