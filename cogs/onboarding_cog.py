import discord
from discord import utils
from discord.ext import commands

ONBOARDING_CHANNEL = "onboarding"
ACTIVE_MEMBER_ROLE = "Active Member"
NEW_MEMBER_ROLE = "New Member"

def verify_member(member):
    return

class OnboardingCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    async def verify_member(self, message):
        newrole = discord.utils.get(message.guild.roles, name=NEW_MEMBER_ROLE)
        activerole = discord.utils.get(message.guild.roles, name=ACTIVE_MEMBER_ROLE)
        if newrole == None or activerole == None:
            print(f"Server {message.guild} has not set up their onboarding roles.")
            return
        if discord.utils.get(message.guild.roles, name=NEW_MEMBER_ROLE) in message.author.roles:
            await message.author.remove_roles(newrole)
            await message.author.add_roles(activerole)
    
    @commands.Cog.listener(name='on_message')
    async def give_entrance_role(self, message):
        if message.channel.name == ONBOARDING_CHANNEL:
            await self.verify_member(message)

def setup(bot):
    bot.add_cog(OnboardingCog(bot))
