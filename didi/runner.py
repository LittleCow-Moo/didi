try:
  import discord, os, datetime
  from discord.ext import commands
  from discord_slash import SlashCommand
  from discord_slash.utils.manage_commands import create_option, create_choice
  from discord_slash.context import MenuContext, SlashContext
  from discord_slash.model import ContextMenuType
  import time
  from discord_slash.utils.manage_components import create_actionrow, create_button, create_select, create_select_option, wait_for_component, ComponentContext
  from discord_slash.model import ButtonStyle
  import asyncio
  from threading import Thread
  import random
  import flask, requests
  from replit import db
  import dishook
except:
  os.system("pip install discord-py-slash-command discord flask replit git+https://github.com/AWeirdScratcher/dishook.git")
  exit("Please restart the program")

client = commands.Bot(commands.when_mentioned_or("didi "))
client.remove_command("help")
slash = SlashCommand(client, sync_commands=True)
app = flask.Flask(__name__)
admin = [
  865814467837558813, # the stupid guy
  766956325480562689,
  847793738578395137
]

try:
  db['ban']
except:
  db['ban'] = []

try:
  db['list']
except:
  db['list'] = []

@app.route("/", methods=['POST'])
def api():
  if flask.request.method == 'POST':
    if flask.request.json['key'] == os.environ['uwu']:
      requests.post(os.environ['UnexpectedIndex'], json={
        "username": "回饋",
      "avatar_url": "https://cdn.discordapp.com/avatars/952110125882167336/cd14b4814b31367c21d8d74c89cf8702.png?size=1024",
      "embeds": [
        {
          "title": "收到回饋表單!",
          "description": f"{flask.request.json['content']}",
          "author": {
            "name": f"{flask.request.json['author']}",
            "icon_url": f"{flask.request.json['a']}"
          },
          "color": 0x2f3136
        }
      ]
    })
    return "Hello World"
  else:
    return "sus"


@app.errorhandler(405)
def ____ohno____(e):
  return """
  You're not allowed to view this page due to this is top secret!
  """



@client.event
async def on_guild_channel_create(ch):
  print("this is for sure")
  guild = None
  if str(ch.type) == "text" and ch.name == "didi-network":
    for guild in client.guilds:
      for channel in guild.channels:
        if channel.id == ch.id:

          guildy = guild.name
    json = {
      "avatar_url": "https://cdn.discordapp.com/avatars/952110125882167336/cd14b4814b31367c21d8d74c89cf8702.png?size=1024",
      "username": "牛弟弟廣播",
      "embeds": [
        {
          "title": "   ",
          "image": {
            "url": "https://file.scratchthings.repl.co/didiNFT.png"
          },
          "color": 0x2f3136
        },
        {
          "title": f":wave: {guildy} 加入了牛弟弟跨群!",
          "color": 0x2f3136,
          "description": "在這裡傳送訊息即可開始聊天!\n輸入 `didi net help` 以取得 Didi Network Bot 的幫助。",
          "footer": {
            "text": "使用 /suggest 以回報問題"
          }
        }
      ]
    }
    for guild in client.guilds:
            for ch in guild.channels:
              if str(ch.type) == "text" and ch.name == "didi-network":
                url = await checkWebhook(ch)
                requests.post(url, json=json)

@client.event
async def on_guild_channel_delete(ch):
  if str(ch.type) == "text" and ch.name == "didi-network":
    print("ran")
    json = {
      "username": "牛弟弟廣播",
      "avatar_url": "https://cdn.discordapp.com/avatars/952110125882167336/cd14b4814b31367c21d8d74c89cf8702.png?size=1024",
      "embeds": [
        {
          "title": "有個伺服器離開了牛弟弟跨群 :(",
          "color": 0x2f3136
        }
      ],

    }
    for guild in client.guilds:
            for ch in guild.channels:
              if str(ch.type) == "text" and ch.name == "didi-network":
                url = await checkWebhook(ch)
                requests.post(url, json=json)


async def checkWebhook(ch):
    all = await ch.webhooks()
    for w in all:
      if w.name == "didiHere" and w.user.id == client.user.id:
        return w.url
    w2 = await ch.create_webhook(name="didiHere", reason="建立Webhook以和他人對話!")
    return w2.url


# didi network
@client.event
async def on_message(message):
  if message.author.bot:
    return

  if f"{message.author} {message.author.id}" in db['list']:
    pass
  else:
    db['list'].append(f"{message.author} {message.author.id}")
  
  if message.author.id in db['ban']:
    return await message.channel.send(":x: 你已被停權")

  
  if message.channel.name == "didi-network":
    await message.delete()
    if "@everyone" in message.content:
      message.content = message.content.replace("@everyone", "everyone")
    if "@here" in message.content:
      message.content = message.content.replace("@here", "here")
    if message.content.startswith("didi net "):
      
      cmd = message.content.replace("didi net ", "", 1)

      if cmd.startswith("lookup "):
        user = cmd.replace("lookup ", "")
        print(user)
        for i in db['list']:
          if i.startswith(user):
            return await message.channel.send(i.replace(user + " ", "", 1))
          else:
            continue


        return await message.channel.send(":x: 找不到使用者")
        
      
      if cmd == "stats" or cmd == "stat":
        i = 0
        for g in client.guilds:
          for channel in g.channels:
            if str(channel.type) == "text" and channel.name == "didi-network":
             i += 1 
        await message.channel.send(f"目前有 **{i}個伺服器** 正在使用 Didi Network!")
        return

      if cmd == ("help"):
        return await message.channel.send(embed=discord.Embed(
          title="如何使用",
          description="""
> `didi net stats` - 顯示目前 Didi Network 的伺服器總數
> `didi net agree` - 表示同意
> `didi net disagree` - 表示反對
> `didi net raise` - 舉手
> `didi net send <訊息>` - 以 CowDidi 的身分傳送訊息
> `didi net poll <標題>` - 舉行一場投票
> `didi net warn <使用者#0000>` - 警告使用者
> `didi net ban <使用者ID>` - 對使用者停權
> `didi net unban <使用者ID>` - 對使用者取消停權
> `didi net lookup <使用者#0000>` - 尋找使用者
""",
          color=0x2f3136
        ))
      
      if cmd.startswith("ban "):
        if not message.author.id in admin:
          return await message.channel.send(":x: 你不是管理員!")
        else:
          db['ban'].append(int(cmd.replace("ban ", "", 1)))
          json = {
          "username": str(message.author),
          "avatar_url": str(message.author.avatar_url),
          "embeds": [
            {
              "title": f"ID {cmd.replace('ban', '', 1)}已被停權。",
              "color": 0xFF0000
            }
          ]
        }
        for guild in client.guilds:
          for ch in guild.channels:
            if str(ch.type) == "text" and ch.name == "didi-network":
              url = await checkWebhook(ch)
              requests.post(url, json=json)
        return

      if cmd.startswith("unban "):
        if not message.author.id in admin:
          return await message.channel.send(":x: 你不是管理員!")
        else:
          db['ban'].remove(int(cmd.replace("unban ", "", 1)))
          await message.channel.send(f"{cmd.replace('unban ', '', 1)} 已被解除停權，但是並不會被公告。")
        return
      
      if cmd.startswith("warn "):
        if not message.author.id in admin:
          return await message.channel.send(":x: 你不是管理員!")
        else:
          json = {
          "username": str(message.author),
          "avatar_url": str(message.author.avatar_url),
          "embeds": [
            {
              "title": f"警告：{cmd.replace('warn', '', 1)}，請注意你的言行舉止!",
              "color": 0xFF0000
            }
          ]
        }
        for guild in client.guilds:
          for ch in guild.channels:
            if str(ch.type) == "text" and ch.name == "didi-network":
              url = await checkWebhook(ch)
              requests.post(url, json=json)
        return

      if cmd.startswith("poll "):
        content11 = cmd.replace("poll ", "", 1)
        btn1 = dishook.Button(
          style=dishook.Style.blurple,
          label="同意",
          custom_id="p:agree"
        )
        btn2 = dishook.Button(
          style=dishook.Style.red,
          label="否決",
          custom_id="p:disagree"
        )
        btn3 = dishook.Button(
          style=dishook.Style.gray,
          label="🖐️",
          custom_id="p:raise"
        )
        for guild in client.guilds:
          for ch in guild.channels:
            if str(ch.type) == "text" and ch.name == "didi-network":
              url = await checkWebhook(ch)
              w = dishook.Webhook(url)
              w.add_button(btn1)
              w.add_button(btn2)
              w.add_button(btn3)
              w.add_embed(
                dishook.Embed(
                  title=f':bar_chart: {content11}',
                  description="",
                  color=0x2f3136
                )
              )
              w.send("", avatar_url=str(message.author.avatar_url), username=str(message.author))
        return
      
      if cmd == "raise" or cmd == "hand" or cmd == "raise hand":
        json = {
          "username": str(message.author),
          "avatar_url": str(message.author.avatar_url),
          "embeds": [
            {
              "title": f":hand_splayed: {str(message.author)} 舉起了手",
              "color": 0x2f3136
            }
          ]
        }
        for guild in client.guilds:
          for ch in guild.channels:
            if str(ch.type) == "text" and ch.name == "didi-network":
              url = await checkWebhook(ch)
              requests.post(url, json=json)
        return
      
      if cmd == "info":
        if message.author.id in admin:
          json = {
            "content": "Hi! 各位若需要了解指令說明，可以使用 `didi net help` 喔!",
            "avatar_url": str(client.user.avatar_url),
            "username": "牛弟弟 [提醒]"
          }
          for guild in client.guilds:
            for ch in guild.channels:
              if str(ch.type) == "text" and ch.name == "didi-network":
                url = await checkWebhook(ch)
                requests.post(url, json=json)
          return
      
      if cmd.startswith("disagree"):
        json = {
          "username": str(message.author),
          "avatar_url": str(message.author.avatar_url),
          "embeds": [
            {
              "title": f":thumbsdown: {str(message.author)} 表示不同意",
              "color": 0x2f3136
            }
          ]
        }
        for guild in client.guilds:
          for ch in guild.channels:
            if str(ch.type) == "text" and ch.name == "didi-network":
              url = await checkWebhook(ch)
              requests.post(url, json=json)
        return
        
      if cmd.startswith("agree"):
        json = {
          "username": str(message.author),
          "avatar_url": str(message.author.avatar_url),
          "embeds": [
            {
              "title": f":thumbsup: {str(message.author)} 表示同意",
              "color": 0x2f3136
            }
          ]
        }
        for guild in client.guilds:
          for ch in guild.channels:
            if str(ch.type) == "text" and ch.name == "didi-network":
              url = await checkWebhook(ch)
              requests.post(url, json=json)
        return
      if cmd.startswith("send "):
        json = {
          "username": "Cow Didi",
          "avatar_url": 'https://cdn.discordapp.com/avatars/952110125882167336/cd14b4814b31367c21d8d74c89cf8702.png?size=1024',
          "content": "_ _",
          "allowed_mentions": False,
          'embeds': [
            {
              "title": "   ",
              "image": {
                "url": "https://cdn.discordapp.com/attachments/858984158620286998/959774538902695956/unknown.png"
              },
              "color": 0x2f3136
            },
            {
              "title": f"{message.author}說:",
              "description": f"{message.content.replace('didi net send ', '', 1)}",
              "color": 0x5865F2
            }
          ]
        }
        for guild in client.guilds:
          for ch in guild.channels:
            if str(ch.type) == "text" and ch.name == "didi-network":
              url = await checkWebhook(ch)
              requests.post(url, json=json)
        return
    att = []
    if message.reference:
      owo = message.reference.message_id
      got = await message.channel.fetch_message(owo)
      author = str(got.author).replace("#0000", "", 1)
      main =  got.content
      if len(got.content) > 30:
        main = got.content[:30] + "..."
        
      embed = {
        "description": main,
        "author": {
          "name": author,
          "icon_url": str(got.author.avatar_url)
        },
        "color": 0x2f3136
      }

    else:
      embed = {}
    
    
    if message.attachments:
      for a in message.attachments:
        att.append(a.url)

    if not embed:
      if not att:
        a = {
          "username": str(message.author),
          "avatar_url": str(message.author.avatar_url),
          "content": message.content,
          "allow_mentions": False,
        }
      else:
        SEND = '\n'.join(att)
        a = {
          "username": str(message.author),
          "avatar_url": str(message.author.avatar_url),
          "content": message.content + f"\n{SEND}",
          "allow_mentions": False,
        }
    else:
      if not att:
        a = {
          "username": str(message.author),
          "avatar_url": str(message.author.avatar_url),
          "content": message.content,
          "embeds": [embed],
          "allowed_mentions": False,
        }
      else:
        SEND = '\n'.join(att)
        a = {
          "username": str(message.author),
          "avatar_url": str(message.author.avatar_url),
          "content": message.content + f"\n{SEND}",
          "embeds": [embed],
          "allowed_mentions": False,
        }
    for guild in client.guilds:
      for ch in guild.channels:
        if str(ch.type) == "text" and ch.name == "didi-network":
          url = await checkWebhook(ch)
          requests.post(url, json=a)


@client.event
async def on_ready():
  print('ready')


async def get_part_of_day(h):
    h = h + 8
    if h > 24:
      h = h - 24
    return (
        "早安"
        if 5 <= h <= 11
        else "午安"
        if 12 <= h <= 17
        else "晚安"
        if 18 <= h <= 22
        else "晚安"
    )

  
@slash.subcommand(base="didi", name="help", description="哞! 需要幫助嗎?")
async def __help__(ctx):
  await ctx.defer()
  await asyncio.sleep(0.8)
  now = datetime.datetime.now()
  embed = discord.Embed(title="  ", description="哞! 我是牛弟弟!", color=0x2f3136)
  embed.set_image(url="https://cdn.discordapp.com/attachments/858984158620286998/959757351521513482/unknown.png")
  res = await get_part_of_day(now.hour)
  para = client.get_emoji(959765608768090142)
  new = client.get_emoji(959835339239870475)
  a = await ctx.send("_ _")
  
  await a.edit(content=res + "，" + str(ctx.author.nick or ctx.author.name), embed=embed, components=[create_actionrow(create_button(style=ButtonStyle.gray, label="繼續", emoji=para, custom_id=f"help:next,{ctx.author.id}"), create_button(
    style=ButtonStyle.blurple,
    label="新增",
    custom_id=f"script:new,{ctx.author.id},{a.id}",
    emoji=new
  ))])




@client.event
async def on_component(ctx):
  id = ctx.component['custom_id']
  if id.startswith("p:"):
    main = id.replace("p:", "", 1)
    await ctx.defer(
      ignore=True
    )
    if main == "agree":
      message = ctx
      json = {
          "username": str(message.author),
          "avatar_url": str(message.author.avatar_url),
          "embeds": [
            {
              "title": f":thumbsup: {str(message.author)} 表示同意",
              "color": 0x2f3136
            }
          ]
        }
    elif main == "disagree":
      message = ctx
      json = {
          "username": str(message.author),
          "avatar_url": str(message.author.avatar_url),
          "embeds": [
            {
              "title": f":thumbsdown: {str(message.author)} 表示不同意",
              "color": 0x2f3136
            }
          ]
        }
    else:
      message = ctx
      json = {
          "username": str(message.author),
          "avatar_url": str(message.author.avatar_url),
          "embeds": [
            {
              "title": f":hand_splayed: {str(message.author)} 舉起了手",
              "color": 0x2f3136
            }
          ]
        }
    for guild in client.guilds:
          for ch in guild.channels:
            if str(ch.type) == "text" and ch.name == "didi-network":
              url = await checkWebhook(ch)
              requests.post(url, json=json)
    return
  if id.startswith("script:"):
    a = id.replace("script:", "", 1)
    type = a.split(",")[0]
    author = int(a.split(",")[1])
    message = int(a.split(",")[2])
    if author != ctx.author.id:
      return await ctx.send("哞! 試試看 `/didi help`", hidden=True)

    ttl = discord.Embed(title="   ", color=0x2f3136)
    ttl.set_image(url="https://cdn.discordapp.com/attachments/858984158620286998/960159452814802984/unknown.png")
    msgemoji = client.get_emoji(960162221864914954)
    scripts = []
    await ctx.edit_origin(content="Cow Script Widget (簡化版)", components=[
      create_actionrow(
        create_button(
          style=ButtonStyle.green,
          label="傳送訊息",
          custom_id="type:send",
          emoji=msgemoji
        )
      )
    ], embeds=[
      ttl,
      discord.Embed(
        title="點擊以下按鈕以新增內容",
        description="**目前的Script：**\n- 無 -",
        color=0x2f3136
      )
    ])
    while True:
      EDITOR = await ctx.channel.fetch_message(message)
      def check(a):
        return a.author.id == ctx.author.id
      res: ComponentContext = await wait_for_component(
        client,
        messages=EDITOR.id,
        check=check
      )
      await res.defer(ignore=True)
      if res.component['custom_id'] == "type:send":
        TODEL = await ctx.channel.send("要傳送的訊息是什麼？")
        def checker(m):
          return m.author.id == ctx.author.id and m.channel.id == ctx.channel.id
    
        a = await client.wait_for("message", check=checker)
        await TODEL.delete()
        scripts.append(
          f"傳送： {a.content}"
        )
      other = '\n'.join(scripts)
      await EDITOR.edit(content="Cow Script Widget", components=[
        create_actionrow(
          create_button(
            style=ButtonStyle.green,
            label="傳送訊息",
            custom_id="type:send",
            emoji=msgemoji
          )
        )
      ], embed=discord.Embed(
          title="點擊以下按鈕以新增內容",
          description=f"**目前的Script：**\n{other}",
          color=0x2f3136
        )
      )


  if id.startswith("help:"):
    a = id.replace("help:", "", 1)
    type = a.split(",")[0]
    author = int(a.split(",")[1])
    if author != ctx.author.id:
      return await ctx.send(f"哞! 試試看 `/didi help`", hidden=True)
    if type == "main":
      now = datetime.datetime.now()
      embed = discord.Embed(title="  ", description="哞! 我是牛弟弟!", color=0x2f3136)
      embed.set_image(url="https://cdn.discordapp.com/attachments/858984158620286998/959757351521513482/unknown.png")
      res = await get_part_of_day(now.hour)
      para = client.get_emoji(959765608768090142)
      
      await ctx.edit_origin(content=res + "，" + str(ctx.author.nick or ctx.author.name), embed=embed, components=[create_actionrow(create_button(style=ButtonStyle.gray, label="繼續", emoji=para, custom_id=f"help:next,{ctx.author.id}"))])
    if type == "next":
      node = client.get_emoji(888543969825423360)
      py = client.get_emoji(888544183042838578)
      embed1 = discord.Embed(title="  ", color=0x2f3136)
      embed1.set_image(url="https://cdn.discordapp.com/attachments/858984158620286998/959774538902695956/unknown.png")
      left = client.get_emoji(959779548243849286)
      row = create_actionrow(
        create_button(
          style=ButtonStyle.blurple,
          label="上一頁",
          custom_id=f"help:main,{ctx.author.id}",
          emoji=left
        )
      )
      embed2 = discord.Embed(title="關於牛弟弟", description=f"牛弟弟是由 **CharlieMoomoo#9491** 旗下的機器牛之一，主要程式語言為：\n:small_blue_diamond: {node} Node.js (CharlieMoomoo)\n:small_blue_diamond: {py} Python (主要, AWeirdScratcher)\n\n開發者名單：\n- CharlieMoomoo#9491\n- Apple Inc.#1342\n- AWeirdScratcher#1744", color=0x2f3136)
      await ctx.edit_origin(embeds=[embed1, embed2], components=[row])

#@client.command()
async def __leave(ctx):
  await ctx.guild.leave()



@slash.subcommand(base="didi", name="button", description="玩玩看按鈕遊戲!")
async def button(ctx: SlashContext):
  await ctx.defer()
  await asyncio.sleep(0.5)
  embed=discord.Embed(title="哞! 今晚，我想來點...", color=0x2f3136)
  msg = await ctx.send(embed=embed)
  await asyncio.sleep(0.5)
  __list__ = [
    "藍色的按鈕",
    "紅色的按鈕",
    "灰色的按鈕",
    "綠色的按鈕"
  ]
  colors = [
    ButtonStyle.blurple,
    ButtonStyle.red,
    ButtonStyle.gray,
    ButtonStyle.green,
  ]
  a = []
  for i in range(len(colors)):
    chosen = random.choice(colors)
    tag = __list__[colors.index(chosen)]
    a.append(
      create_actionrow(
        create_button(
          style=chosen,
          label=tag
        )
      )
    )
    colors.remove(chosen)
    __list__.remove(tag)
    __list__2 = [
    "藍色的按鈕",
    "紅色的按鈕",
    "灰色的按鈕",
    "綠色的按鈕"
  ]
  ans = random.choice(__list__2)
  await msg.edit(embed=discord.Embed(title=f"哞! 今晚，我想來點{ans}", color=0x2f3136), components=a)
  
  start = time.time()
  
  try:
    res: ComponentContext = await wait_for_component(client, messages=msg.id, timeout=2)
  except:
    return await msg.edit(embed=discord.Embed(title="時間到!", color=0x2f3136), components=[create_actionrow(
      create_button(
        style=ButtonStyle.red,
        label="太慢了",
        disabled=True
      )
    )])
    
  took = time.time() - start
  main = "%.2f" % took
  if res.component['label'] == ans:
    await res.edit_origin(embed=discord.Embed(title="答對了!", description=f"花費了{main} 秒", color=0x2f3136), components=[create_actionrow(
      create_button(
        style=ButtonStyle.blurple,
        label="結束",
        disabled=True
      )
    )])
  else:
    await res.edit_origin(embed=discord.Embed(title="答錯了..", color=0x2f3136, description=f"花費了{main} 秒"), components=[create_actionrow(
      create_button(
        style=ButtonStyle.red,
        label="結束 (失敗)",
        disabled=True
      )
    )])


#!important
#0x2f3136


def a():
  app.run(port=8080, host="0.0.0.0")

Thread(target=a).start()
client.run("It is how wonderful to use this token!")
