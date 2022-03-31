import discord
import os
from discord.ext import commands
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from io import BytesIO
from config import *
from keep_alive import keep_alive

bot = commands.Bot(command_prefix=os.environ['PREFIX'], case_insensitive=True, intents = discord.Intents.all())

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    ITALIC = '\033[3m'

@bot.event
async def on_ready():
    # Booting info:
    print(
        bcolors.OKCYAN + "[INFO]: " + bcolors.ENDC + bcolors.OKGREEN + bcolors.BOLD + "Successful Login! " + bcolors.ENDC)
    print(
        bcolors.OKCYAN + "[INFO]: " + bcolors.ENDC + "Logged in as: " + bcolors.OKCYAN + bcolors.HEADER + bcolors.ITALIC + "{bot_username}".format(
            bot_username=bot.user.name) + bcolors.ENDC)
    print(
        bcolors.OKCYAN + "[INFO]: " + bcolors.ENDC + "Bot ID: " + bcolors.OKCYAN + bcolors.HEADER + bcolors.ITALIC + "{bot_user_id}".format(
            bot_user_id=bot.user.id) + bcolors.ENDC)
    print(
        bcolors.OKCYAN + "[INFO] Bot Made By" + bcolors.ENDC + bcolors.OKGREEN + bcolors.BOLD + " albert.#1033 " + bcolors.ENDC)
    print(
        bcolors.OKCYAN + "[INFO]: " + bcolors.ENDC + bcolors.OKGREEN + bcolors.BOLD + "Successful Login! " + bcolors.ENDC)
    # Set bot's status
    await bot.change_presence(
        activity=discord.Activity(type=discord.ActivityType.playing, name="Made by albert.!"))
    print(bcolors.FAIL + "[INFO]: " + bcolors.ENDC + bcolors.OKBLUE + "Copyright NoError Studios™" + bcolors.ENDC)
    print('----------------------------------------------------------------------')

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(welcome_channel)
    img = Image.open("infoimgimg.png") #Replace infoimgimg.png with your background image.
    draw = ImageDraw.Draw(img)
    asset=member.avatar_url_as(size=128)
    data=BytesIO(await asset.read())
    pfp=Image.open(data)
    font = ImageFont.truetype("DefconZeroCondensedItalic-aRlJ.otf", 20) #Make sure you insert a valid font from your folder.
    fontbig = ImageFont.truetype("RadioSpaceBoldItalic-13Ge.otf", 80) #Make sure you insert a valid font from your folder.
    #    (x,y)::↓ ↓ ↓ (text)::↓ ↓     (r,g,b)::↓ ↓ ↓
    draw.text((200, 5), "Welcome!", (255, 255, 255), font=fontbig) 
    draw.text((180, 100), f"Username: {member.name}#{member.discriminator}", font = font)
    draw.text((180, 130), image_content, font = font)
    draw.text((500, 260), f"Image was made by albert.#1033", font=font)
    img.paste(pfp, (30, 90))
    img.save('infoimg3.png')
    await channel.send(content = message_content,file = discord.File("infoimg3.png"))

@bot.command()
async def test(ctx):
  channel = bot.get_channel(welcome_channel)
  user = ctx.author
  img = Image.open("infoimgimg.png") #Replace infoimgimg.png with your background image. Recommended size: 833 x 278
  draw = ImageDraw.Draw(img)
  asset=user.avatar_url_as(size=128)
  data=BytesIO(await asset.read())
  pfp=Image.open(data)
  font = ImageFont.truetype("DefconZeroCondensedItalic-aRlJ.otf", 20) #Make sure you insert a valid font from your folder.
  fontbig = ImageFont.truetype("RadioSpaceBoldItalic-13Ge.otf", 80) #Make sure you insert a valid font from your folder.
    #    (x,y)::↓ ↓ ↓ (text)::↓ ↓     (r,g,b)::↓ ↓ ↓
  draw.text((200, 5), "Welcome!", (255, 255, 255), font=fontbig) 
  draw.text((180, 100), f"Username: {user.name}#{user.discriminator}", font = font)
  draw.text((180, 130), image_content, font = font)
  draw.text((500, 260), f"Image was made by albert.#1033", font=font)
  img.paste(pfp, (30, 90))
  img.save('infoimg2.png')
  await channel.send(file = discord.File("infoimg2.png"))
  await ctx.send("Done sending welcome card! Check your welcoming channel")


keep_alive()
bot.run(os.environ['TOKEN'])

