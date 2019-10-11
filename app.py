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
status = cycle(['+help', '+stock', '+spotify', '+origin', '+steam', '+hulu', '+fortnite', '+minecraft', '+uplay'])

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
        await message.author.send("Introducing TABISH SHAH BOT")
        await message.author.send("You Can Invite This Bot To Your Server +invite")
        await message.author.send("Rare Account Generating Bot")
        await message.author.send("You Can Check Available Stock In BOT +stock")


    if message.content.startswith('+fortnite'):
        randomlist = ['youngmulah49@yahoo.com:Aceisb123','sanjibmegh@gmail.com:sanjibmegh78','cavecow878@gmail.com:ryebread1','kayciegiles@gmail.com:soccergirl78','avoegm@gmail.com:11co1w9upi','caithss@gmail.com:dd6ad66','heineken_barcelona@hotmail.com:heineken12','jeanpot4545@gmail.com:Lankie10','alejandrob111@hotmail.com:Neongreen12','jakewheal@hotmail.co.uk:SUPERM4N1','robert.parker@bell.net:Roma2601','ashley.swim18@gmail.com:HMSTdhr2','niyaun@msn.com:sting455','diego.vargas1118@gmail.com:boombom1','ziuzad@gmail.com:sheepa1994','domen.sustaric@gmail.com:Racunalnica1','thoms.colombo@gmail.com:toto1994','weistart.ryan@hotmail.com:147853Ry','miguelamartinez0224@gmail.com:dreamchasing09','rowanhamdouglas@gmail.com:Hamilton1!','Cjjchickey178@gmail.com:paint123','spaikesalonika@hotmail.com:spaikeole1','salwanarjun@gmail.com:DrJackal@05','Robertsingh67@gmail.com:Yankees2','cheesee12@gmail.com:Chrisi96','ian0008@hotmail.com:godfrey23','crunch.matic23@gmail.com:Dsavage23','id4shopping@gmail.com:Gustnsh84','dazedconfuzed11@gmail.com:Strange1love','jasonroivas@gmail.com:superman08','sargolinibrody12@gmail.com:Brody123','C.keioglian@yahoo.com:Fuckoff1','gas.ezequieldiaz@gmail.com:totito91','sgarvey99@gmail.com:diamond2001','stepanov.george@gmail.com:Madzigon1','paulnelson8@hotmail.com:Bruins11','maharned02@gmail.com:Lifeisgood010101!','xaviermattingly@yahoo.com:Xm101690','jan130798.55@gmail.com:nintendo1307','cberesford422@gmail.com:colin1196','stephen.martinez728@gmail.com:Steve741.','jruzza89@gmail.com:Ciaosusy1','colin.simonetta@gmail.com:bongbong22','slim9081@hotmail.com:Tagboy12','thomasbohnhorst@gmx.de:Bohni100','jaosn11214@gmail.com:Jasonmei123','brendasano@gmail.com:network1.','jackhalpin@ymail.com:redbull1231','damiencopeland@gmail.com:D6210696!','rob.stal@hotmail.com:Prullenbak1','marc.bourgier@hotmail.fr:Namar666','mamalucco@gmail.com:ilpassero81','pounder08@hotmail.com:Kp16051990','autumnsummers1@hotmail.com:Ilkailka17','ritagarmi@gmail.com:penaguila7','krat654@gmail.com:vlad2004','jalen99@live.com:Masterkey1234','mimic.972@hotmail.fr:Souris55','rachelfortt@yahoo.co.uk:oliver2007','brescoach@gmail.com:Maddux31!','sunnygeegee@gmail.com:Dogpoop123a','sanji1209@gmail.com:tkdals43','piko29minecraft@gmail.com:piko0228','somakasan@yandex.ru:somakasan1','holz.leonie@web.de:Celinale1','meandmy2jlvs@yahoo.com:Stealth123!','andykang01@hotmail.com:Superhigh1!','spardinu69@gmail.com:qwerty21','emiliebouman@gmail.com:Mismus0078','rockylong84@gmail.com:Hendrix84','alonso_07-10@hotmail.com:Jklfds0710','melialava2006@gmail.com:meli2006','aryan2012amit@gmail.com:deepraj1','wielokropek6@gmail.com:szyk2000','priscillaberstler@aol.com:tycoon1','pedobaer007@hotmail.com:Gaggi123','alexr0x@gmail.com:As056999420','p.berger1990@web.de:O1o11oo1','petergiampaoli@gmail.com:ginger86','jday216@gmail.com:leahbaby216','rgchapman21@gmail.com:michelle926','aittor_herndz09@hotmail.com:Badajocense9.','jasoncartwright96@gmail.com:12345jason','justin.hall12@yahoo.com:Sprint10','markus.maul92@gmail.com:Handball1','fera.marsh@gmail.com:Kambenk1992','tophergrafixs@gmail.com:1jasmyn','eje0203@gmail.com:cetw1993','b.rod94@hotmail.com:brod0794','dalehall17@gmail.com:rodger11','cemmons08@gmail.com:Danger123','harleesuggs@yahoo.com:smokey1997','e.swag923@gmail.com:rosasse10','sanheim.sama@gmail.com:JuanDeJuanes16','gagesj1210@yahoo.com:Gage1210','brunoqueado2004@hotmail.com:lesluthiers3','ttc123401321@gmail.com:abc01321','gaara9518@gmail.com:gaara1795','jessicabuser@gmx.ch:Sultan123','edwardh0922@gmail.com:Oldhouse1','leandrorebellato@gmail.com:dieguito1','benlmaden@hotmail.co.uk:autumn91','darkthony@hotmail.com:hermanos12','razva.bebe@gmail.com:Delian12','dylansulak@gmail.com:doolie21','chrissocci901@gmail.com:iliketurtlez123','mimiche66@hotmail.com:LILIAN2005','4mcgovern.dillon@gmail.com:ironman6','colten_stephens@hotmail.com:Speeder1','brescina00@hotmail.com:anna1234','alejandroamarof@gmail.com:padres011','jaylynkinslow880@gmail.com:Jck828800','makayla.knott@yahoo.com.au:Rapalas09','cinus.marco@libero.it:Eugenio89','jmtguimaraes@gmail.com:Putavida1','cody.m.langley@gmail.com:skidoosh1','sabludau@gmail.com:dgbczusa1','edward_redko@hotmail.co.uk:1basketball','nkallio11@gmail.com:Steelers43','chicokablau@gmail.com:m7ecdi7j','rnh0925@gmail.com:cabezon06','malcolmpattern@gmail.com:reddwarf1','Gvdheijden01@hotmail.com:trampo123','victor19990315@me.com:Dewalt123','brenton_af@hotmail.com:surf1986','flippinj21@yahoo.com:skyblue2','rjgreaves@yahoo.co.uk:Manutd73','jeffkapelke32547@gmail.com:katia5299','dr.mad.01@mail.ru:maksimus2008','Mmanson702@yahoo.com:Lucas123','gustavosilvalima@hotmail.com:120392gu','tifok3@gmail.com:zxcvb213','th3ph4nt0mcarsteam@gmail.com:caca1234','CadienteJulian@gmail.com:Jjll0094','comodon14@gmail.com:Anakin14','iangarciaquerol@gmail.com:annaquerol1','colleen.propst@gmail.com:cooking123','alistair404@gmail.com:F15fighter','gustavandersson40@yahoo.com:Gretzky99']
        await message.author.send("Join Server To Keep Updated About Bot")
        await message.author.send(" https://discord.gg/sZpqqWX ")
        msg = ' ' + author + '. Fortnite Account : '
        await message.author.send(msg + (random.choice(randomlist)))

    if message.content.startswith('+spotify'):
        randomlist = ['1dgabbymalik@gmail.com:Gabrie11a!','3dretsam@gmail.com:bmmf2707','SiestaDr@hotmail.com:Tacobell963','a.muqattash@yahoo.com:Slayer16','almogaizik1@gmail.com:Itay1000','alyssalax8@aol.com:Jackson8','amber.hirsch@yahoo.com:Wufta468','andrescogollo29@gmail.com:andres29','arlenewilliamsg@yahoo.com:mylove052108','armylook2@hotmail.com:browjr401025','arnepeirs@hotmail.com:habbos007','bank.attila99@gmail.com:Attila99','benrocks52@gmail.com:Rosie500','bjm02@yahoo.com:Deathwish1','brownbearjames10@gmail.com:james2006','cathy.c.chang@gmail.com:FlorraGoulder','chavezmichael20026@gmail.com:yh3or2sd','cooksrus5@sbcglobal.net:Shadow66','cschultz022@yahoo.com:brett1224','daniel_runge@web.de:gina1828','danylopez1@gmail.com:1728agus','devrim1@hotmail.fr:Glamour57','dgrdz@hotmail.com:OMARlove1982','dobbinandrew@ymail.com:poopoo666','eagercharch@gmail.com:phantom32','echonationYT@gmail.com:Triggerd1','ellinhax@gmail.com:borboleta123','esqueletina.491@gmail.com:ToyGaby0202','even.henriksen1@hotmail.com:sheena123','floor.fca@live.nl:marijekim1','fran_chua08@hotmail.com:naciel16996.','gavinwjs123@gmail.com:wong2459','gemw07@aol.co.uk:ryder2341','h.william.lee@gmail.com:illwill21','jbstraub@gmail.com:godsson3','johansoct9@yahoo.com:tadlas98','kobex016@umn.edu:Chester4609','krycha8917@gmail.com:Piesio123','ladiela18@hotmail.com:CABI0312','leichawocha@yahoo.it:pregno','lovebama21@gmail.com:Earlenzia21','luiz.afonso_jr@uol.com.br:la051935','lyesbouacem@gmail.com:Marseille59','m.quanah55@hotmail.com:qwerty55','ma__mario@hotmail.com:mario1988','madornetto1@gmail.com:183319zk','mallory_wheeler4@icloud.com:mw108704','manbcn@yahoo.com:SuperMario','marcelocdomingues@hotmail.com:d11m5a71','margot.hoffmann97@gmail.com:bigoudi57','mathieuhurtubise1@hotmail.com:hockeyman64','matthewstclair85@gmail.com:Anlamalo1234','migrose3@gmail.com:bear0566','mohdjuhayry@gmail.com:juhayry123','nickgibboni1@gmail.com:sk84lyfe','noah.piccolillo@gmail.com:Bbnoah34','notinazuma@gmail.com:Damaris3','oaelkins@gmail.com:owen11004','oov_22@hotmail.com:ardepapi123','opuchaudhuri@gmail.com:dreamdancer1801','osghar_ag@hotmail.com:Marcos8702','patrickleen01@hotmail.com:rooney2001','pattytooo18@hotmail.com:PGR81101','polaroid.polaroid@gmail.com:superfalsa1','rafaelribeiro02.rr@gmail.com:rafa19rafa','rdeblouw@gmail.com:rd111986','rivers2007@hotmail.com:NSWrule20','robertalarosa@gmail.com:roby231093','rohit.baghit@gmail.com:Rohit1998','ronaldinhosoares13@hotmail.com:jonas.s13','roshandatolson@yahoo.com:Monday01','sietebarrasbajas@gmail.com:personal95','stewarta06@yahoo.com:atx51227','teresafarina@hotmail.it:love260585','trenttigner@gmail.com:Zoladz12','triciacabral3@gmail.com:cabral03','uchuari10@gmail.com:mary2001','victoriakinross@gmail.com:vk23tors','victormendoza1918@gmail.com:newpass2','vincentyaptablets@gmail.com:Rahsia88','vshari20@gmail.com:warriors21','yejunkwon@gmail.com:Ygun5571','yosen1@hotmail.com:Memo1984','yu_jun@hotmail.com:tiger7yj','zmedhaug@gmail.com:colleen1']
        await message.author.send("Join Server To Keep Updated About Bot")
        await message.author.send(" https://discord.gg/sZpqqWX ")
        msg = ' ' + author + '. Spotify Account : '
        await message.author.send(msg + (random.choice(randomlist)))

    if message.content.startswith('+stock'):
        await message.author.send("Origin: 1000 .Hulu: 1000 .Spotify: 1000 .Fortnite: 1000 .Nordvpn: 1000 .Crunchyroll: 1000 .Uplay: 600 .Minecraft: 120")
        await message.author.send("Available Stocks")

    if message.content.startswith('+nordvpn'):
        randomlist = ['abbas35@live.com:abbasdf123','cbilzx@tom.com:tmen0201','chad_greenaway@hotmail.com:mainas123','cherry.cleary@gmail.com:dannie1023','cole070500@gmail.com:trooper20','colmasimone@gmail.com:left4dead2','colten-james@hotmail.com:guitarhero15','craig.mogi@gmail.com:Mustang63','damien2007@MSN.com:damianos2007','dgoza16@gmail.com:Danthe1man','diegosaravia65@gmail.com:notedigo','flytouk@gmail.com:19831017','gichuhi@hotmail.com:sylvia323','jessie.ceyssens@telenet.be:yorkoo101171','king_aafuw@yahoo.com:aafuw123','lewis.w.94@hotmail.co.uk:arsenal5','mario.maldonado9@gmail.com:PIZZA123','max-tutzschke@t-online.de:lenny001','mdjones1776@yahoo.com:mdj1776a','mr.fnaf.mc@gmail.com:XPXP1234','mr84xx@gmail.com:insanity1988','orangefingerz1@gmail.com:Cranstoneast1','paterson.rhys@gmail.com:Mithrandir311','pureobbyz@hotmail.com:tootcat2','raamiz2k1@gmail.com:raamiz2001','rdaigle404@gmail.com:47855web','rio_a1988@aol.com:alanis88','ritchea95@yahoo.com:Jakobritchea95','rmorlarived@yahoo.es:Telefonica1','robbie68@hotmail.com:bonethugs','ross2g1@gmail.com:walnut82','salinas.jose80@hotmail.com:Awesome1','slebodnik.michal151@gmail.com:jamnik151','smart.abraham@gmail.com:doombringer','spence77@live.co.uk:Saskia55','syqin86@gmail.com:midnight1223','teflonaudi@gmail.com:Thesoup1','timothyvanarem@gmail.com:milodehond','zorgish@hotmail.com:Tissekatt1']
        await message.author.send("Join Server To Keep Updated About Bot")
        await message.author.send(" https://discord.gg/sZpqqWX ")
        msg = ' ' + author + '. Nord Vpn Account : '
        await message.author.send(msg + (random.choice(randomlist)))



    if message.content.startswith('+origin'):
        randomlist = ['asianpwnage@yahoo.com:megaman28','chris.gravenmier@yahoo.com:9449295a','jayden3221@yahoo.com:penguin77','thimodejonge@hotmail.com:Killer33','Brandon.Allin@yahoo.com:357Bolter','Josephjones2014@hotmail.com:Mookie08','ajringor@rocketmail.com:pogiako22','alecwbaugher@gmail.com:Masseffect3','alex.boswell87@gmail.com:Alexeb87','alexanderdevlin@yahoo.com:MKaasr12','allyblacksinger@gmail.com:greenbowAL123','anh11_fox@yahoo.com:flyingfoxx11','asianpwnage@yahoo.com:megaman28','badcreeper58@gmail.com:1556431113','bfrench1999@gmail.com:Branden99','chris.gravenmier@yahoo.com:9449295a','colejr3@comcast.net:Pickle00','crazyboydiamond@gmail.com:yahoo123','djunknow@wp.pl:tomek1988','dragons1182@gmail.com:muppet11','eracsgod@gmail.com:ferrum26','espartan208@hotmail.com:halowars11','falcon5840@yahoo.com:67Corvette','hunttheer@gmail.com:Hunter27','iuzaru@yahoo.com:zxcvbn98','jaja808@wp.pl:kometa666','jayden3221@yahoo.com:penguin77','jensa96@hotmail.com:C3oNimaH','jordanxchang@yahoo.com:Abcde123','juozaskarciauskas@gmail.com:hesoyam','madmadammoll@yahoo.com:Molly0826','marauder6307@yahoo.com:Ringwraith3321','marlisasikkema@outlook.com:Krabeltje1','mikicom11@gmail.com:mikit6266','momluvsglass@ymail.com:Lucky1967','mstsant@yahoo.com:Fs841110','natemcginnis29@gmail.com:Godawgs1','rie.nateriver@gmail.com:mamake92','sepulvedam90@yahoo.com:cowboys24','shane.henniger@yahoo.com:Isaac100','simon36123@yahoo.com:12345678As','slmtrm@charter.net:Excalibur1','szadowk2000@wp.pl:Animelike2000','tazzydevil2002@live.com:monkeyboyabc123','trieuvan171@gmail.com:171993771','vacus619@yahoo.com:volleyforged','w.beer208@gmx.de:ChefSache1','waynet3ch@gmail.com:Cowboy19']
        await message.author.send("Join Server To Keep Updated About Bot")
        await message.author.send(" https://discord.gg/sZpqqWX ")
        msg = ' ' + author + '. Origin Account : '
        await message.author.send(msg + (random.choice(randomlist)))

    if message.content.startswith('+hulu'):
        randomlist = ['Haymae11@yahoo.com:Missme27','acex8781@gmail.com:Dragones6','alec.olen@yahoo.com:1Tennisfreak','alondra-acosta@hotmail.com:22happy22','andrei.sel.12@gmail.com:Andrew2503','anonymousdude666@gmail.com:momdad','azarmir.kasra@gmail.com:4008086q','b.aguilar34@yahoo.com:Acura2004','ben.reeves@gmail.com:skull9062','cam.williams0824@gmail.com:Cameron098','catguitarist@hotmail.co.uk:Dr34dw1ng','cesar.a.vieira@hotmail.com:forever3390','cuellarrico@yahoo.com:Yelitza7','cvmissy16@gmail.com:sweets2','daniel_jared@live.com:frida2011','dantealhigeri@hotmail.com:liukan15','desireianngalgana@hotmail.com:galgana1','dibl_96@hotmail.com:Diblteam06','dillonrockson@gmail.com:shaggy66','dino.duel@hotmail.com:Killer123','does_molly_ring_a_bell@yahoo.com:Jetaime23','ecchizz@live.com:seay15','elanning@gmail.com:althain2k9','esa0705@gmail.com:natsudragneel123','fireworks125machinima@gmail.com:poopoo10','gerard_liwanag@hotmail.com:Boxing101','glztiger@hotmail.it:somuas35','grimreaper0x0@yahoo.com:darkblade99','guigui2397@gmail.com:doudou98','hellscream0@hotmail.com:cotton99','henrikyo_inteligente@hotmail.com:99585849','imdewidesigns@gmail.com:Memelose1','isabelcalle_17@hotmail.com:kurosagi21','jiiub@hotmail.com:sebhan89','jmholohan@hotmail.com:Cc6260368','jnguyen5151@yahoo.com:bobby5151','jose15tito@msn.com:champ247','jroxendine@rocketmail.com:rxw420','jstanton14@hotmail.com:netx4984','kokiks101@gmail.com:shadow12','lastshogun@gmail.com:moses100','ldavis4127@aol.com:bingo222','leep.egerton@ntlworld.com:Abigail1','mapcra500@live.com:destroyer1','marcelocdomingues@hotmail.com:d11m5a71','marci690@gmail.com:risiko123','mattspvfx@gmail.com:power544','mauro_852@hotmail.com:marc1993','mdlmx19@gmail.com:xpootanX18','mikerob175@gmail.com:canes175','mykiddani@yahoo.com:bobby5689','naderpug@gmail.com:soarer','nekoiv9@gmail.com:aaaaaakiba04','nicholasmireles@yahoo.com:nick1998','nsjames7000@gmail.com:poopster2','ongteckwei@yahoo.com:keropi','pablo.asin@hotmail.es:barrancas1','pieguy798@gmail.com:HONDARIDER98','pirateking_nick@yahoo.com:my2ndname2','ptvheather@gmail.com:sept22000','quinnfoley@gmail.com:bears2012','rafaelflorers@yahoo.com:clubyes09','rezafatul@yahoo.co.id:moskwa','rodri9044@hotmail.com:huehue123','rodrigo.neta@gmail.com:lego541998','rolandcmorales08@gmail.com:000black','savualexandru0@gmail.com:ronaldo99','shinigmainox@gmail.com:miniwiflyXD1','shizzy186@yahoo.com:Warlover101','simen@vetaas-hoie.com:12Oktober','slipknot_dark1496@hotmail.com:presario14','speightquantez@gmail.com:speight1','sphireos@gmail.com:thailson1','steam21@vp.pl:Aezakmi12','steven.hellingh@gmail.com:3A55word','subtil.guilherme@gmail.com:rock4ever','t.ingh@live.nl:WIIkey25','themathwhizo@gmail.com:Mathpro2013','timmy_cattan@hotmail.com:Electrical1','travis.ber@gmail.com:Polpol123','vajsteve@gmail.com:thug4life','vigotheyt@gmail.com:pirate11','vijyaraj@gmail.com:rajmahal25','wbluke7000@gmail.com:moses711','westell626@gmail.com:godofwar','zach.ricketts@gmail.com:Smith230']
        await message.author.send("Join Server To Keep Updated About Bot")
        await message.author.send(" https://discord.gg/sZpqqWX ")
        msg = ' ' + author + '. Hulu Account : '
        await message.author.send(msg + (random.choice(randomlist)))

    if message.content.startswith('+steam'):
        randomlist = ['https://filemedia.net/27527/steam	','https://filemedia.net/27527/steam	','https://filemedia.net/27527/steam	']
        await message.author.send("Join Server To Keep Updated About Bot")
        await message.author.send(" https://discord.gg/sZpqqWX ")
        msg = ' ' + author + '. Steam Account : '
        await message.author.send(msg + (random.choice(randomlist)))

    if message.content.startswith('+udemy'):
        randomlist = ['https://filemedia.net/27527/udemy2','https://up-to-down.net/27527/udemy','https://up-to-down.net/27527/udemy']
        msg = 'Hello ' + author + '. Your link: '
        await message.author.send(msg + (random.choice(randomlist)))

    if message.content.startswith('+uplay'):
        randomlist = ['https://up-to-down.net/27527/uplay2','https://up-to-down.net/27527/uplay2','https://up-to-down.net/27527/uplay']
        await message.author.send("Join Server To Keep Updated About Bot")
        await message.author.send(" https://discord.gg/sZpqqWX ")
        msg = ' ' + author + '. Uplay Account : '
        await message.author.send(msg + (random.choice(randomlist)))

    if message.content.startswith('+crunchyroll'):
        randomlist = ['https://up-to-down.net/27527/crunchyroll','https://up-to-down.net/27527/crunchyroll','https://up-to-down.net/27527/crunchyroll']
        await message.author.send("Join Server To Keep Updated About Bot")
        await message.author.send(" https://discord.gg/sZpqqWX ")
        msg = ' ' + author + '. Crunchyroll Account : '
        await message.author.send(msg + (random.choice(randomlist)))

    if message.content.startswith('+scribd'):
        randomlist = ['https://direct-link.net/27527/Scribd','https://direct-link.net/27527/Scribd','https://direct-link.net/27527/Scribd']
        msg = 'Hello ' + author + '. Your link: '
        await message.author.send(msg + (random.choice(randomlist)))

    if message.content.startswith('+familyowner'):
        randomlist = ['https://direct-link.net/27527/familyowner','https://direct-link.net/27527/familyowner','https://direct-link.net/27527/familyowner']
        msg = 'Hello ' + author + '. Your link: '
        await message.author.send(msg + (random.choice(randomlist)))

    if message.content.startswith('+minecraft'):
        randomlist = ['https://link-to.net/27527/Minecraft001','https://up-to-down.net/27527/minecrafts','https://filemedia.net/27527/Minecraft']
        await message.author.send("Join Server To Keep Updated About Bot")
        await message.author.send(" https://discord.gg/sZpqqWX ")
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
        await client.change_presence(activity=Activity(name=f"{len(client.guilds)} servers!| !help | Members ", 
                                                type=ActivityType.watching))

client.run(os.getenv('BOT_TOKEN'))
