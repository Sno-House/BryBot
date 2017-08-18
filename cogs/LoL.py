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

    @commands.command()
    async def getChamps(self, champ):
        # annie = Champion(name="Annie", region="NA")
        champion = Champion(name=champ)
        await self.bot.say(champion.name)
        await self.bot.say(champion.title)
        for spell in champion.spells:
            await self.bot.say(spell.name)
            await self.bot.say(spell.keywords)

        await self.bot.say(champion.info.difficulty)
        await self.bot.say(champion.passive.name)
        await self.bot.say({item.name: count for item, count in champion.recommended_itemsets[0].item_sets[0].items.items()})
        await self.bot.say(champion._Ghost__all_loaded)
        await self.bot.say(champion)
        await self.bot.say("Thank you, come again!")


def setup(bot):
    bot.add_cog(Mycog(bot))




