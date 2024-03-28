import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.messages = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.command()
async def clear(ctx, amount: int):
    if discord.utils.get(ctx.author.roles, ID="1210588217464717392"):
        await ctx.channel.purge(limit=amount + 1)
    else:
        await ctx.send("У Вас нет доступа к этой команде.")

bot.run('MTIyMjkwMTk1MjYzMTgwMzkzNA.GY0A9P.cjsrdTOwvkgi00v8AyQPC-Pw0bdkbJk-0wtmI4')