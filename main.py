import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def name(ctx):
    await ctx.send(f'Merhaba! Benim ismim tacomaco!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def kodland(ctx):
    await ctx.send(f'Merhaba {bot.user}! hoş gelmediniz!')

bot.run("TOKEN")

