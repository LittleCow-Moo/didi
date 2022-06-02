import discord # v2
from discord.ext import commands

# dispatch events

client = commands.Bot("test", intents=discord.Intents.default())

@client.event
async def on_interaction(ctx):
  client.dispatch("test", ctx)
  
@client.event
async def on_test(ctx):
  print(f"I recieved an event!\nData: {ctx.data}")
  
client.run(...)
