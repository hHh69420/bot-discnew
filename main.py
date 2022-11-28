import os
import random

import discord
from discord import client
from discord.ext import commands
from dotenv import load_dotenv


def get_response(message: str) -> str:
    p_message = message.lower()


DISCORD_TOKEN = ''

load_dotenv()
TOKEN = os.getenv(DISCORD_TOKEN)

intents = discord.Intents.default()
intents.members = True
intents.message_content = True


bot = commands.Bot(command_prefix='.', intents=intents)


@bot.command(name='hello', help='Hello')
async def hello(ctx):
    hello = 'Sup nerds! Im Homo erectus, a work-in progress primate bot'
    await ctx.send(hello)



@bot.command(name='chat_revival', help='Chat revival ping')
async def revive(ctx):
    c_revive = '@everyone **REVIVE THE FUCKING CHAT RIGHT NOW**'
    await ctx.send(c_revive)


@bot.command(name='gays', help='Lists gay people')
async def gays(ctx):
    gay_list = [
        'Aarav', 'That one fat kid', 'Yeezu', 'Padia', 'Miss wilma', 'Miss hema', 'Sycon', '@Gabe Itch 2', 'Obama',
        'Kim Jong un', 'Ur mom', 'Modi\'s mom', 'HenryRan'

    ]

    response = random.choice(gay_list)
    await ctx.send(response)


@bot.command(name='percent', help='Gives a random precentage')
async def percent(ctx):
    response_p = str(random.randrange(1, 100))
    await ctx.send(response_p + '%')


@bot.command(name='dice_r', help='Dice roll')
async def dice(ctx):
    rr = str(random.randint(1, 6))
    await ctx.send(rr)


@bot.command(name='nh', help='Says no homo for you')
async def nh(ctx):
    nh = 'The person above me says no homo'
    await ctx.send(nh)


@bot.command(name='piss', help='Says how many liters someone has pissed today')
async def piss(ctx, h_piss):
    l_piss = str(random.randrange(1, 100))
    await ctx.send(h_piss + ' pissed ' + l_piss + ' liters today')


@bot.command(name='for_aarav', help='Websites for Aarav')
async def dreams_d(ctx):
    dreamsd = 'https://dreamsd.com', 'https://piss.com', 'https://shit.com', 'https://eshaan.net', 'https://prawnhub.com', 'sex.com'
    response = random.choice(dreamsd)
    await ctx.send(response)


@bot.command(name='shat', help='Says how many times someone shat today')
async def shat_h(ctx, shat_p):
    shat_pe = str(random.randrange(1, 100))
    await ctx.send(shat_p + ' shat ' + shat_pe + ' times today')


@bot.command(name='haram', help='Says how haram someone is')
async def shat_h(ctx, haram_p):
    haram_perc = str(random.randrange(1, 100))
    await ctx.send(haram_p + ' is ' + haram_perc + '% haram')


@bot.command(name='erect', help='Says how erect someone is')
async def erect_us(ctx, erect_p):
    erect_perc = str(random.randrange(1, 100))
    await ctx.send(erect_p + ' is ' + erect_perc + '% erect')


@bot.command(name='egg', help="Says how egg someone's head is")
async def shat_h(ctx, egg_p):
    egg_perc = str(random.randrange(1, 100))
    await ctx.send(egg_p + ' is ' + egg_perc + '% egg')


@bot.command(name='spam', help="Spams whatever you say")
async def spam_say(ctx, spam_w):
    await ctx.send(spam_w)
    await ctx.send(spam_w)
    await ctx.send(spam_w)
    await ctx.send(spam_w)
    await ctx.send(spam_w)
    await ctx.send(spam_w)
    await ctx.send(spam_w)
    await ctx.send(spam_w)
    await ctx.send(spam_w)
    await ctx.send(spam_w)
    await ctx.send(spam_w)
    await ctx.send(spam_w)


@bot.command(name='yn', help='Says yes or no for you')
async def y_n(ctx, y_no):
    ye_no = ['Yes', 'No']
    resp_ye = random.choice(ye_no)
    await ctx.send('`' + y_no + '`' + ' '+resp_ye)

bot.run(DISCORD_TOKEN)
