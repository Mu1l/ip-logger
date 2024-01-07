import discord
import socket
import sys

intents = discord.Intents.default()
intents.messages = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
 for guild in client.guilds:
   general_channel = discord.utils.get(guild.text_channels, name='general')
   if general_channel is not None:
       hostname = socket.gethostname()
       ip_address = socket.gethostbyname(hostname)
       await general_channel.send(f'Running on Hostname: {hostname}, IP Address: {ip_address}')
       await client.close()
   else:
       print(f"No 'general' channel found in guild: {guild}")

client.run('your bots token here)
