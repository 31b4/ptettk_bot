import discord
import asyncio

from discord_slash import SlashCommand
from discord_slash.utils.manage_commands import create_option

# Enter your bot token here
TOKEN = 'MTA4OTIxOTI3MTYwMDY1MjM2OA.GMy1aF.FYiVdVG5ALPGv8aHOjrDA-aj4bcEM8lpTXdv4M'

# Enter the channel ID of the channel you want to rename
CHANNEL_ID = 1089229506201534586

# Enter the list of names you want to cycle through every hour
NAMES = ['Channel 1', 'Channel 2', 'Channel 3']

# Create a Discord client and slash command object
client = discord.Client(intents=discord.Intents.all())
slash = SlashCommand(client, sync_commands=True)

# Define a function to rename the channel
async def rename_channel():
    channel = client.get_channel(CHANNEL_ID)
    name = NAMES.pop(0)
    NAMES.append(name)
    await channel.edit(name=name)

# Define a function to handle slash commands
@slash.slash(name="help", description="DMs the admins", guild_ids=[123456789012345678])
async def help(ctx):
    await ctx.send(f"{ctx.author.mention} dm admins")

# Define a function to run the bot
async def run_bot():
    await client.wait_until_ready()
    while not client.is_closed():
        await rename_channel()
        await asyncio.sleep(3600)  # Wait for an hour before renaming again

# Start the bot
client.loop.create_task(run_bot())
client.run(TOKEN)
