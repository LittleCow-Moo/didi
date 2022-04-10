import os
try:
  import interactions
  import asyncio
  from threading import Thread
  import requests, flask
except:
  os.system("pip install git+https://github.com/interactions-py/library.git requests flask")
  exit("Please restart the program")

try:
  from discord.ext import commands
  from discord_slash import SlashCommand
except:
  os.system("pip install discord-py-slash-command discord")
  exit("Please restart the program")


client = interactions.Client(token=os.environ['InvalidTokenTest'])
app = flask.Flask(__name__)

os.environ['interactions-endpoint'] = "https://"

@app.route("/")
def __():
  return "Hello World"



@client.command(name="suggest", description="填寫回饋表單")
async def _test(ctx):
  modal = interactions.Modal(
        title="回饋與建議",
        custom_id="sug",
        components=[interactions.TextInput(
          style=interactions.TextStyleType.PARAGRAPH,
          label="你的回饋",
          custom_id="sug",
          min_length=10,
          max_length=2048
        )]
    )
  await ctx.popup(modal)
  await ctx.defer()


@client.event
async def on_message(message):
  pass

@client.event
async def on_ready():
  print("ready")

@client.modal("sug")
async def main(ctx, response: str):
  requests.post(f"{os.environ['interactions-endpoint']}", json={
    "content": f"{response}",
    "key": f"{os.environ['none']}",
    "author": f"{ctx.author}",
    "a": f"https://cdn.discordapp.com/avatars/{ctx.author.id}/{ctx.author.avatar}.png?size=1024"
  })
  await ctx.send("謝謝你的回饋! 已將你的想法交給了牛牛團隊!")

def runner():
  app.run(host="0.0.0.0", port=8080)


Thread(target=runner).start()
client.start()
