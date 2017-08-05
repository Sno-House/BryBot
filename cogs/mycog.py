import discord
import cassiopeia as cass
import random
import os
from discord.ext import commands

class Mycog:
    """My custom cog that does stuff!"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def test(self):
        """This does stuff!"""

        summoner = cass.get_summoner(name="BubblyBryan")
        await self.bot.say("{name} is a level {level} summoner on the {region} server.".format(name=summoner.name, level=summoner.level, region=summoner.region))

        champions = cass.get_champions()
        random_champion = random.choice(champions)
        await self.bot.say("He enjoys playing champions such as {name}.".format(name=random_champion.name))

        challenger_league = cass.get_challenger()
        best_na = challenger_league[0].summoner
        await self.bot.say("He's not as good {name} at League, but probably a better python programmer!".format(name=best_na.name))

def setup(bot):
    bot.add_cog(Mycog(bot))




