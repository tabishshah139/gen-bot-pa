import discord
from discord.ext import commands, tasks
import os
import asyncio
import random
import time
from itertools import cycle
from discord.utils import get
from discord import Game
import os

from discord import Activity, ActivityType


client = commands.Bot(command_prefix='+')
#client = discord.Client()
Clientdiscord = discord.Client()


#create an arraylist containing phrases you want your bot to switch through.
status = cycle(['+help', '+gen'])

client.remove_command('help')

# this is only for test if bot working
@client.event
async def on_message(message):
    message.content = message.content.lower()
    author = '{0.author.mention}'.format(message)
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

# this lines you can modify  

    if message.content.startswith('+hello'):
        msg = 'Hello python {0.author.mention}'.format(message)
        await message.author.send(msg)
        
    if(message.content == '+stock', '-stock', '!stock', '>stock', '+stocks', '-stocks', '!stocks', '>stocks', '!invite', '-invite', '!help', '!gen', '-gen', '!gen', '-help', '!gen fortnite', '!fortnite', '-fortnite', '!steam', '!spotify', '-spotify', '-steam', '!uplay', '-uplay', '!netflix', '-netflix'):
        await message.author.send("```Sorry There is Just One Command (+gen) to generate all account which is available at stocks type +gen```")



    if message.content == '!hulu', '-hulu', '!crunchyroll', '-crunchyroll', '!nordvpn', '-nordvpn', '!pornhub', '-pornhub', '!minecraft', '-minecraft', '!wwe', '-wwe', '!mailaccess', '-mailaccess', '!origin', '-origin', '!hbo', '-hbo', '!pubg', '-pubg', '!minty', '-minty', '!ebay', '-ebay', '!nitro', '-nitro', '!gen uplay'):
        await message.author.send("```Sorry There is Just One Command (+gen) to generate all account which is available at stocks type +gen``")
        

    if message.content.startswith('+invite'):
        await message.author.send("Click To Invite Bot In Your Server https://discordapp.com/api/oauth2/authorize?client_id=619923933109420097&permissions=0&scope=bot")

    if message.content.startswith('+help'):
        await message.author.send(" https://discord.gg/44PFcRr ")
        await message.author.send("You Can Invite This Bot To Your Server +invite")
        await message.author.send("Rare Account Generating Bot type +gen")
        await message.author.send("You Can Check generate all accounts type +gen")



 
        
        
    

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    change_status.start()

@tasks.loop(seconds=5)
async def change_status():
        await client.change_presence(activity=Activity(name=f"{len(client.guilds)} servers!| +help | Members ", 
                                                type=ActivityType.watching))

client.run(os.getenv('BOT_TOKEN'))
