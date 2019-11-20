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
status = cycle(['+help', '+stock', '+spotify', '+origin', '+steam', '+hulu', '+fortnite', '+minecraft', '+uplay', 'wwe', 'pornhub', 'mail'])

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


    if message.content.startswith('+invite'):
        await message.author.send("Click To Invite Bot In Your Server https://discordapp.com/api/oauth2/authorize?client_id=619923933109420097&permissions=0&scope=bot")

    if message.content.startswith('+help'):
        await message.author.send(" https://discord.gg/44PFcRr ")
        await message.author.send("You Can Invite This Bot To Your Server +invite")
        await message.author.send("Rare Account Generating Bot")
        await message.author.send("You Can Check Available Stock In BOT +stock")


    if message.content.startswith('+fortnite'):
        randomlist = ['']
        await message.author.send("Join Server To Keep Updated About Bot")
        await message.author.send(" Official Server https://discord.gg/44PFcRr ")
        msg = ' ' + author + '. Fortnite Account : '
        await message.author.send(msg + (random.choice(randomlist)))

    if message.content.startswith('+spotify'):
        randomlist = ['']
        await message.author.send("Join Server To Keep Updated About Bot")
        await message.author.send(" Official Server https://discord.gg/44PFcRr ")
        msg = ' ' + author + '. Spotify Account : '
        await message.author.send(msg + (random.choice(randomlist)))

    if message.content.startswith('+stock'):
        await message.author.send("Origin: 670 .Hulu: 421 .Spotify: 621 .Fortnite: 1000 .Nordvpn: 444 .Crunchyroll: 272 .Uplay: 300 .Minecraft: 441")
        await message.author.send("Available Stocks 26 October")
        await message.author.send(" Official Server https://discord.gg/44PFcRr ")
        

    if message.content.startswith('+nordvpn'):
        randomlist = ['']
        await message.author.send("Join Server To Keep Updated About Bot")
        await message.author.send(" Official Server https://discord.gg/44PFcRr ")
        msg = ' ' + author + '. Nord Vpn Account : '
        await message.author.send(msg + (random.choice(randomlist)))



    if message.content.startswith('+origin'):
        randomlist = ['']
        await message.author.send("Join Server To Keep Updated About Bot")
        await message.author.send(" Official Server https://discord.gg/44PFcRr ")
        msg = ' ' + author + '. Origin Account : '
        await message.author.send(msg + (random.choice(randomlist)))

    if message.content.startswith('+hulu'):
        randomlist = ['Imnotmadnah@gmail.com:Right12345','Kungii0@gmail.com:Hussain123','Thebestgecko@gmail.com:Pickapassword1','a.thunder11@yahoo.com:scooter08','ambernc_77@hotmail.com:malachi2','amer.kachmar@live.com:kash9578','atorellini@gmail.com:chicho1265','audiefitradi@gmail.com:marianne83','bdz_rdm00@yahoo.com:Simon1300','brg413@cox.net:avag9903','camden399@gmail.com:piepiepie399','cdnhill@gmail.com:star69','cdusher@charter.net:cudcud22','chrisjcoble@gmail.com:Msjamsja1','cjb233@cox.net:sonnyb233','colezuller@yahoo.com:bz071602','courtneylovelace0911@gmail.com:ckl0911','davylamb@gmail.com:david2001','deion.j.p@gmail.com:wPzLcv5q','dixonsmama@gmail.com:bbmama13','dpleggenkuhle15@gmail.com:meatdude24','elbrugy2663@aim.com:Brugy123','gabrieliuc11@gmail.com:radeikis2','gao.lesley@gmail.com:gaowanzhen','hellwick@gmail.com:agrogazm','hosadavid@gmail.com:2d7a7v3i1d6','jaimearellanoq@gmail.com:pitusking','jgaminde67@gmail.com:Jan311994','karol0209@gmail.com:karol2976','lordneeku@gmail.com:outerspace345','marcphelps@hotmail.com:beatty42','masoudi.malek@gmail.com:malek12646','mdehart53@gmail.com:mwd53dh71','modrexler@gmail.com:studio1','qpalmer7055@gmail.com:myheadhurts1','seregon43087@gmail.com:vq8yG2N','shiningstars93@yahoo.com:mlm123','syqin86@gmail.com:midnight1223','tk.kimende@gmail.com:Kuria1969','tlc.cole57@gmail.com:terrell10','tristan6520@gmail.com:tristan3','williamw4555@gmail.com:beefTacoS4','ztytank123@live.com:mtdd1997']
        await message.author.send("Join Server To Keep Updated About Bot")
        await message.author.send(" Official Server https://discord.gg/44PFcRr ")
        msg = ' ' + author + '. Hulu Account : '
        await message.author.send(msg + (random.choice(randomlist)))

    if message.content.startswith('+steam'):
        randomlist = ['']
        await message.author.send("Join Server To Keep Updated About Bot")
        await message.author.send(" Official Server https://discord.gg/44PFcRr ")
        msg = ' ' + author + '. Steam Account : '
        await message.author.send(msg + (random.choice(randomlist)))

    if message.content.startswith('+mail'):
        randomlist = ['']
        await message.author.send("Join Server To Keep Updated About Bot")
        await message.author.send(" Official Server https://discord.gg/44PFcRr ")
        msg = ' ' + author + '. Mail Access Account : '
        await message.author.send(msg + (random.choice(randomlist)))

    if message.content.startswith('+uplay'):
        randomlist = ['']
        await message.author.send("Join Server To Keep Updated About Bot")
        await message.author.send(" Official Server https://discord.gg/44PFcRr ")
        msg = ' ' + author + '. Uplay Account : '
        await message.author.send(msg + (random.choice(randomlist)))

    if message.content.startswith('+crunchyroll'):
        randomlist = ['']
        await message.author.send("Join Server To Keep Updated About Bot")
        await message.author.send(" Official Server https://discord.gg/44PFcRr ")
        msg = ' ' + author + '. Crunchyroll Account : '
        await message.author.send(msg + (random.choice(randomlist)))

    if message.content.startswith('+wwe'):
        randomlist = ['']
        await message.author.send("Join Server To Keep Updated About Bot")
        await message.author.send(" Official Server https://discord.gg/44PFcRr ")
        msg = ' ' + author + '. WWE Account : '
        await message.author.send(msg + (random.choice(randomlist)))
                    

    if message.content.startswith('+pornhub'):
        randomlist = ['']
        await message.author.send("Join Server To Keep Updated About Bot")
        await message.author.send(" Official Server https://discord.gg/44PFcRr ")
        msg = ' ' + author + '. Pornhub Account : '
        await message.author.send(msg + (random.choice(randomlist)))

    if message.content.startswith('+minecraft'):
        randomlist = ['']
        await message.author.send("Join Server To Keep Updated About Bot")
        await message.author.send(" Official Server https://discord.gg/44PFcRr ")
        msg = ' ' + author + '. Minecraft Account : '
        await message.author.send(msg + (random.choice(randomlist)))


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
