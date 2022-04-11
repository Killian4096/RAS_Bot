import discord
from discord import utils
from discord.ext import commands

ONBOARDING_CHANNEL = "onboarding"

class OnboardingCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener(name='on_message')
    async def give_entrance_role(self, message):
        if message.channel.name == ONBOARDING_CHANNEL:
            print("User verified")

def setup(bot):
    bot.add_cog(OnboardingCog(bot))
