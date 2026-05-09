import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user}')

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

bot.run("MTQzNDU5MjUxODQwOTgxNDE4MA.GhAiw1.z9MfV3iNQDW9ms94Dzi75JUNvO9FoDDJxZFqps")
