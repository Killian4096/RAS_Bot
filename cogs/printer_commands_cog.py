import os

import discord
from discord import utils
from discord.ext import commands
import cv2

PRINTER_IMAGE_NAME = "printer_picture.png"
PRINTER_IMAGE_LOCATION = "images"


def save_printer_image():
    cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    ret, frame = cam.read()
    location = PRINTER_IMAGE_LOCATION + "/" + PRINTER_IMAGE_NAME
    cv2.imwrite(location, frame)
    cam.release()
    cv2.destroyAllWindows()
    return location

def get_printer_status():
    return "No printer connected"

class PrinterCommandsCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def printerpicture(self, ctx):
        location = save_printer_image()
        await ctx.channel.send(file=discord.File(location))

    @commands.command()
    async def printpicture(self, ctx):
        await ctx.invoke(self.bot.get_command('printerpicture'))
    
    @commands.command()
    async def printerstatus(self, ctx):
        message = get_printer_status()
        await ctx.channel.send(message)


def setup(bot):
    bot.add_cog(PrinterCommandsCog(bot))
    print("Printer Commands Cog initialized")