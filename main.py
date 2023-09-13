import discord
from discord import app_commands
import asyncio
import os
from keep_alive import keep_alive
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
import time

url = "https://neptun-web4.tr.pte.hu/hallgato/login.aspx"
req = Request(url)

intents = discord.Intents.all()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)


@tree.command(name="help",
              description="...",
              guild=discord.Object(id=1144550911268626482))
async def help_command(interaction):
  embed = discord.Embed(
    title="nem",
    color=0xffffff)
  await interaction.response.send_message(embed=embed)

@tree.command(name="neptunstatus",
              description="Neptun státusz / valaszidő",
              guild=discord.Object(id=1144550911268626482))
async def neptunstatus_command(interaction):
  try:
    start_time = time.time()  # Record the start time
    response = urlopen(req)
    end_time = time.time()  # Record the end time
    response_time = end_time - start_time
  except HTTPError as e:
    print('The server couldn\'t fulfill the request.')
    print('Error code: ', e.code)
    embed = discord.Embed(title="Neptun nem válaszolt. Error code: " + str(e.code), color=0xe74c3c)

  except URLError as e:

    embed = discord.Embed(title="Neptun nem elérhető. Indok: " + str(e.reason), color=0xe74c3c)

  else:
    embed = discord.Embed(
      title="Neptun fut. "+ f'Válaszidő: {response_time:.2f}mp',description="https://neptun-web3.tr.pte.hu/hallgato/login.aspx",color=0x2ecc71)
  await interaction.response.send_message(embed=embed)

@client.event
async def on_message(message):
  print(message.content)

  msg = ""
  reaction = ""
  if 'pte' == message.content.lower():
    msg = "TTK"
    reaction = "<:ttk:1145420618087546940>"
  elif 'ping' == message.content.lower():
      start_time = time = asyncio.get_event_loop().time()
      msg = await message.channel.send("Pinging...")
      end_time = asyncio.get_event_loop().time()
      ping = (end_time - start_time) * 1000
      await msg.edit(content=f"Pong! Bot's ping is {ping:.2f}ms")
      msg = ""
  
  
  if msg != "":
    await message.reply(msg)
  if reaction != "":
    await message.add_reaction(reaction)


keep_alive()

try:
  client.run(
    "TOKEN")
except discord.errors.HTTPException:
  print("\n\n\nBLOCKED BY RATE LIMITS\nRESTARTING NOW\n\n\n")
  os.system('kill 1')
  os.system("python restarter.py")
