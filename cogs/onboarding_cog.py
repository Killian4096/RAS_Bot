import discord
from discord import utils
from discord.ext import commands

class OnboardingCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    commands.Cog.listener("on_reaction_add")
    async def give_entrance_role():
        print("It worked")
