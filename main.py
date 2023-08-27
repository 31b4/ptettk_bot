import discord
from discord import app_commands
import asyncio
import os
from keep_alive import keep_alive

intents = discord.Intents.all()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)


@tree.command(name="help",
              description="...",
              guild=discord.Object(id=1040967504006217808))
async def help_command(interaction):
  embed = discord.Embed(
    title="nem",
    color=0xffffff)
  await interaction.response.send_message(embed=embed)


@client.event
async def on_ready():

  await tree.sync(guild=discord.Object(id=1040967504006217808))

  print("Ready!")


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
