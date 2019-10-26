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
        await message.author.send(" https://discord.gg/44PFcRr ")
        await message.author.send("You Can Invite This Bot To Your Server +invite")
        await message.author.send("Rare Account Generating Bot")
        await message.author.send("You Can Check Available Stock In BOT +stock")


    if message.content.startswith('+fortnite'):
        randomlist = ['youngmulah49@yahoo.com:Aceisb123','sanjibmegh@gmail.com:sanjibmegh78','cavecow878@gmail.com:ryebread1','kayciegiles@gmail.com:soccergirl78','avoegm@gmail.com:11co1w9upi','caithss@gmail.com:dd6ad66','heineken_barcelona@hotmail.com:heineken12','jeanpot4545@gmail.com:Lankie10','alejandrob111@hotmail.com:Neongreen12','jakewheal@hotmail.co.uk:SUPERM4N1','robert.parker@bell.net:Roma2601','ashley.swim18@gmail.com:HMSTdhr2','niyaun@msn.com:sting455','diego.vargas1118@gmail.com:boombom1','ziuzad@gmail.com:sheepa1994','domen.sustaric@gmail.com:Racunalnica1','thoms.colombo@gmail.com:toto1994','weistart.ryan@hotmail.com:147853Ry','miguelamartinez0224@gmail.com:dreamchasing09','rowanhamdouglas@gmail.com:Hamilton1!','Cjjchickey178@gmail.com:paint123','spaikesalonika@hotmail.com:spaikeole1','salwanarjun@gmail.com:DrJackal@05','Robertsingh67@gmail.com:Yankees2','cheesee12@gmail.com:Chrisi96','ian0008@hotmail.com:godfrey23','crunch.matic23@gmail.com:Dsavage23','id4shopping@gmail.com:Gustnsh84','dazedconfuzed11@gmail.com:Strange1love','jasonroivas@gmail.com:superman08','sargolinibrody12@gmail.com:Brody123','C.keioglian@yahoo.com:Fuckoff1','gas.ezequieldiaz@gmail.com:totito91','sgarvey99@gmail.com:diamond2001','stepanov.george@gmail.com:Madzigon1','paulnelson8@hotmail.com:Bruins11','maharned02@gmail.com:Lifeisgood010101!','xaviermattingly@yahoo.com:Xm101690','jan130798.55@gmail.com:nintendo1307','cberesford422@gmail.com:colin1196','stephen.martinez728@gmail.com:Steve741.','jruzza89@gmail.com:Ciaosusy1','colin.simonetta@gmail.com:bongbong22','slim9081@hotmail.com:Tagboy12','thomasbohnhorst@gmx.de:Bohni100','jaosn11214@gmail.com:Jasonmei123','brendasano@gmail.com:network1.','jackhalpin@ymail.com:redbull1231','damiencopeland@gmail.com:D6210696!','rob.stal@hotmail.com:Prullenbak1','marc.bourgier@hotmail.fr:Namar666','mamalucco@gmail.com:ilpassero81','pounder08@hotmail.com:Kp16051990','autumnsummers1@hotmail.com:Ilkailka17','ritagarmi@gmail.com:penaguila7','krat654@gmail.com:vlad2004','jalen99@live.com:Masterkey1234','mimic.972@hotmail.fr:Souris55','rachelfortt@yahoo.co.uk:oliver2007','brescoach@gmail.com:Maddux31!','sunnygeegee@gmail.com:Dogpoop123a','sanji1209@gmail.com:tkdals43','piko29minecraft@gmail.com:piko0228','somakasan@yandex.ru:somakasan1','holz.leonie@web.de:Celinale1','meandmy2jlvs@yahoo.com:Stealth123!','andykang01@hotmail.com:Superhigh1!','spardinu69@gmail.com:qwerty21','emiliebouman@gmail.com:Mismus0078','rockylong84@gmail.com:Hendrix84','alonso_07-10@hotmail.com:Jklfds0710','melialava2006@gmail.com:meli2006','aryan2012amit@gmail.com:deepraj1','wielokropek6@gmail.com:szyk2000','priscillaberstler@aol.com:tycoon1','pedobaer007@hotmail.com:Gaggi123','alexr0x@gmail.com:As056999420','p.berger1990@web.de:O1o11oo1','petergiampaoli@gmail.com:ginger86','jday216@gmail.com:leahbaby216','rgchapman21@gmail.com:michelle926','aittor_herndz09@hotmail.com:Badajocense9.','jasoncartwright96@gmail.com:12345jason','justin.hall12@yahoo.com:Sprint10','markus.maul92@gmail.com:Handball1','fera.marsh@gmail.com:Kambenk1992','tophergrafixs@gmail.com:1jasmyn','eje0203@gmail.com:cetw1993','b.rod94@hotmail.com:brod0794','dalehall17@gmail.com:rodger11','cemmons08@gmail.com:Danger123','harleesuggs@yahoo.com:smokey1997','e.swag923@gmail.com:rosasse10','sanheim.sama@gmail.com:JuanDeJuanes16','gagesj1210@yahoo.com:Gage1210','brunoqueado2004@hotmail.com:lesluthiers3','ttc123401321@gmail.com:abc01321','gaara9518@gmail.com:gaara1795','jessicabuser@gmx.ch:Sultan123','edwardh0922@gmail.com:Oldhouse1','leandrorebellato@gmail.com:dieguito1','benlmaden@hotmail.co.uk:autumn91','darkthony@hotmail.com:hermanos12','razva.bebe@gmail.com:Delian12','dylansulak@gmail.com:doolie21','chrissocci901@gmail.com:iliketurtlez123','mimiche66@hotmail.com:LILIAN2005','4mcgovern.dillon@gmail.com:ironman6','colten_stephens@hotmail.com:Speeder1','brescina00@hotmail.com:anna1234','alejandroamarof@gmail.com:padres011','jaylynkinslow880@gmail.com:Jck828800','makayla.knott@yahoo.com.au:Rapalas09','cinus.marco@libero.it:Eugenio89','jmtguimaraes@gmail.com:Putavida1','cody.m.langley@gmail.com:skidoosh1','sabludau@gmail.com:dgbczusa1','edward_redko@hotmail.co.uk:1basketball','nkallio11@gmail.com:Steelers43','chicokablau@gmail.com:m7ecdi7j','rnh0925@gmail.com:cabezon06','malcolmpattern@gmail.com:reddwarf1','Gvdheijden01@hotmail.com:trampo123','victor19990315@me.com:Dewalt123','brenton_af@hotmail.com:surf1986','flippinj21@yahoo.com:skyblue2','rjgreaves@yahoo.co.uk:Manutd73','jeffkapelke32547@gmail.com:katia5299','dr.mad.01@mail.ru:maksimus2008','Mmanson702@yahoo.com:Lucas123','gustavosilvalima@hotmail.com:120392gu','tifok3@gmail.com:zxcvb213','th3ph4nt0mcarsteam@gmail.com:caca1234','CadienteJulian@gmail.com:Jjll0094','comodon14@gmail.com:Anakin14','iangarciaquerol@gmail.com:annaquerol1','colleen.propst@gmail.com:cooking123','alistair404@gmail.com:F15fighter','gustavandersson40@yahoo.com:Gretzky99']
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
        await message.author.send("Origin: 1000 .Hulu: 1000 .Spotify: 1000 .Fortnite: 1000 .Nordvpn: 1000 .Crunchyroll: 1000 .Uplay: 600 .Minecraft: 120")
        await message.author.send("Available Stocks")
        await message.author.send(" Official Server https://discord.gg/44PFcRr ")
        

    if message.content.startswith('+nordvpn'):
        randomlist = ['abbas35@live.com:abbasdf123','cbilzx@tom.com:tmen0201','chad_greenaway@hotmail.com:mainas123','cherry.cleary@gmail.com:dannie1023','cole070500@gmail.com:trooper20','colmasimone@gmail.com:left4dead2','colten-james@hotmail.com:guitarhero15','craig.mogi@gmail.com:Mustang63','damien2007@MSN.com:damianos2007','dgoza16@gmail.com:Danthe1man','diegosaravia65@gmail.com:notedigo','flytouk@gmail.com:19831017','gichuhi@hotmail.com:sylvia323','jessie.ceyssens@telenet.be:yorkoo101171','king_aafuw@yahoo.com:aafuw123','lewis.w.94@hotmail.co.uk:arsenal5','mario.maldonado9@gmail.com:PIZZA123','max-tutzschke@t-online.de:lenny001','mdjones1776@yahoo.com:mdj1776a','mr.fnaf.mc@gmail.com:XPXP1234','mr84xx@gmail.com:insanity1988','orangefingerz1@gmail.com:Cranstoneast1','paterson.rhys@gmail.com:Mithrandir311','pureobbyz@hotmail.com:tootcat2','raamiz2k1@gmail.com:raamiz2001','rdaigle404@gmail.com:47855web','rio_a1988@aol.com:alanis88','ritchea95@yahoo.com:Jakobritchea95','rmorlarived@yahoo.es:Telefonica1','robbie68@hotmail.com:bonethugs','ross2g1@gmail.com:walnut82','salinas.jose80@hotmail.com:Awesome1','slebodnik.michal151@gmail.com:jamnik151','smart.abraham@gmail.com:doombringer','spence77@live.co.uk:Saskia55','syqin86@gmail.com:midnight1223','teflonaudi@gmail.com:Thesoup1','timothyvanarem@gmail.com:milodehond','zorgish@hotmail.com:Tissekatt1']
        await message.author.send("Join Server To Keep Updated About Bot")
        await message.author.send(" Official Server https://discord.gg/44PFcRr ")
        msg = ' ' + author + '. Nord Vpn Account : '
        await message.author.send(msg + (random.choice(randomlist)))



    if message.content.startswith('+origin'):
        randomlist = ['asianpwnage@yahoo.com:megaman28','chris.gravenmier@yahoo.com:9449295a','jayden3221@yahoo.com:penguin77','thimodejonge@hotmail.com:Killer33','Brandon.Allin@yahoo.com:357Bolter','Josephjones2014@hotmail.com:Mookie08','ajringor@rocketmail.com:pogiako22','alecwbaugher@gmail.com:Masseffect3','alex.boswell87@gmail.com:Alexeb87','alexanderdevlin@yahoo.com:MKaasr12','allyblacksinger@gmail.com:greenbowAL123','anh11_fox@yahoo.com:flyingfoxx11','asianpwnage@yahoo.com:megaman28','badcreeper58@gmail.com:1556431113','bfrench1999@gmail.com:Branden99','chris.gravenmier@yahoo.com:9449295a','colejr3@comcast.net:Pickle00','crazyboydiamond@gmail.com:yahoo123','djunknow@wp.pl:tomek1988','dragons1182@gmail.com:muppet11','eracsgod@gmail.com:ferrum26','espartan208@hotmail.com:halowars11','falcon5840@yahoo.com:67Corvette','hunttheer@gmail.com:Hunter27','iuzaru@yahoo.com:zxcvbn98','jaja808@wp.pl:kometa666','jayden3221@yahoo.com:penguin77','jensa96@hotmail.com:C3oNimaH','jordanxchang@yahoo.com:Abcde123','juozaskarciauskas@gmail.com:hesoyam','madmadammoll@yahoo.com:Molly0826','marauder6307@yahoo.com:Ringwraith3321','marlisasikkema@outlook.com:Krabeltje1','mikicom11@gmail.com:mikit6266','momluvsglass@ymail.com:Lucky1967','mstsant@yahoo.com:Fs841110','natemcginnis29@gmail.com:Godawgs1','rie.nateriver@gmail.com:mamake92','sepulvedam90@yahoo.com:cowboys24','shane.henniger@yahoo.com:Isaac100','simon36123@yahoo.com:12345678As','slmtrm@charter.net:Excalibur1','szadowk2000@wp.pl:Animelike2000','tazzydevil2002@live.com:monkeyboyabc123','trieuvan171@gmail.com:171993771','vacus619@yahoo.com:volleyforged','w.beer208@gmx.de:ChefSache1','waynet3ch@gmail.com:Cowboy19']
        await message.author.send("Join Server To Keep Updated About Bot")
        await message.author.send(" Official Server https://discord.gg/44PFcRr ")
        msg = ' ' + author + '. Origin Account : '
        await message.author.send(msg + (random.choice(randomlist)))

    if message.content.startswith('+hulu'):
        randomlist = ['Haymae11@yahoo.com:Missme27','acex8781@gmail.com:Dragones6','alec.olen@yahoo.com:1Tennisfreak','alondra-acosta@hotmail.com:22happy22','andrei.sel.12@gmail.com:Andrew2503','anonymousdude666@gmail.com:momdad','azarmir.kasra@gmail.com:4008086q','b.aguilar34@yahoo.com:Acura2004','ben.reeves@gmail.com:skull9062','cam.williams0824@gmail.com:Cameron098','catguitarist@hotmail.co.uk:Dr34dw1ng','cesar.a.vieira@hotmail.com:forever3390','cuellarrico@yahoo.com:Yelitza7','cvmissy16@gmail.com:sweets2','daniel_jared@live.com:frida2011','dantealhigeri@hotmail.com:liukan15','desireianngalgana@hotmail.com:galgana1','dibl_96@hotmail.com:Diblteam06','dillonrockson@gmail.com:shaggy66','dino.duel@hotmail.com:Killer123','does_molly_ring_a_bell@yahoo.com:Jetaime23','ecchizz@live.com:seay15','elanning@gmail.com:althain2k9','esa0705@gmail.com:natsudragneel123','fireworks125machinima@gmail.com:poopoo10','gerard_liwanag@hotmail.com:Boxing101','glztiger@hotmail.it:somuas35','grimreaper0x0@yahoo.com:darkblade99','guigui2397@gmail.com:doudou98','hellscream0@hotmail.com:cotton99','henrikyo_inteligente@hotmail.com:99585849','imdewidesigns@gmail.com:Memelose1','isabelcalle_17@hotmail.com:kurosagi21','jiiub@hotmail.com:sebhan89','jmholohan@hotmail.com:Cc6260368','jnguyen5151@yahoo.com:bobby5151','jose15tito@msn.com:champ247','jroxendine@rocketmail.com:rxw420','jstanton14@hotmail.com:netx4984','kokiks101@gmail.com:shadow12','lastshogun@gmail.com:moses100','ldavis4127@aol.com:bingo222','leep.egerton@ntlworld.com:Abigail1','mapcra500@live.com:destroyer1','marcelocdomingues@hotmail.com:d11m5a71','marci690@gmail.com:risiko123','mattspvfx@gmail.com:power544','mauro_852@hotmail.com:marc1993','mdlmx19@gmail.com:xpootanX18','mikerob175@gmail.com:canes175','mykiddani@yahoo.com:bobby5689','naderpug@gmail.com:soarer','nekoiv9@gmail.com:aaaaaakiba04','nicholasmireles@yahoo.com:nick1998','nsjames7000@gmail.com:poopster2','ongteckwei@yahoo.com:keropi','pablo.asin@hotmail.es:barrancas1','pieguy798@gmail.com:HONDARIDER98','pirateking_nick@yahoo.com:my2ndname2','ptvheather@gmail.com:sept22000','quinnfoley@gmail.com:bears2012','rafaelflorers@yahoo.com:clubyes09','rezafatul@yahoo.co.id:moskwa','rodri9044@hotmail.com:huehue123','rodrigo.neta@gmail.com:lego541998','rolandcmorales08@gmail.com:000black','savualexandru0@gmail.com:ronaldo99','shinigmainox@gmail.com:miniwiflyXD1','shizzy186@yahoo.com:Warlover101','simen@vetaas-hoie.com:12Oktober','slipknot_dark1496@hotmail.com:presario14','speightquantez@gmail.com:speight1','sphireos@gmail.com:thailson1','steam21@vp.pl:Aezakmi12','steven.hellingh@gmail.com:3A55word','subtil.guilherme@gmail.com:rock4ever','t.ingh@live.nl:WIIkey25','themathwhizo@gmail.com:Mathpro2013','timmy_cattan@hotmail.com:Electrical1','travis.ber@gmail.com:Polpol123','vajsteve@gmail.com:thug4life','vigotheyt@gmail.com:pirate11','vijyaraj@gmail.com:rajmahal25','wbluke7000@gmail.com:moses711','westell626@gmail.com:godofwar','zach.ricketts@gmail.com:Smith230']
        await message.author.send("Join Server To Keep Updated About Bot")
        await message.author.send(" Official Server https://discord.gg/44PFcRr ")
        msg = ' ' + author + '. Hulu Account : '
        await message.author.send(msg + (random.choice(randomlist)))

    if message.content.startswith('+steam'):
        randomlist = ['https://filemedia.net/27527/steam	','https://filemedia.net/27527/steam	','https://filemedia.net/27527/steam	']
        await message.author.send("Join Server To Keep Updated About Bot")
        await message.author.send(" Official Server https://discord.gg/44PFcRr ")
        msg = ' ' + author + '. Steam Account : '
        await message.author.send(msg + (random.choice(randomlist)))

    if message.content.startswith('+udemy'):
        randomlist = ['https://filemedia.net/27527/udemy2','https://up-to-down.net/27527/udemy','https://up-to-down.net/27527/udemy']
        msg = 'Hello ' + author + '. Your link: '
        await message.author.send(msg + (random.choice(randomlist)))

    if message.content.startswith('+uplay'):
        randomlist = ['sjanewickman@gmail.com:sydney13','samuel.55321@gmail.com:5532184de','michelepolentino@live.com:Michele1','mazsafc1973@gmail.com:Safc1973','blawkgirl@gmail.com:bribri4462','rgxbatman@gmail.com:robbie17','gottsnack123@gmail.com:lucas123','greyzzer@gmail.com:iamsocool1','lanceswow@hotmail.com:Skinner123','deadvalentine187@gmail.com:Suicide69','rjusus@att.net:Summer09','shelbybioware@gmail.com:qazwsx12','kuehlcassi@gmail.com:taylorswift','jon_goldhammer@yahoo.com:base13ball','haleynicole125@yahoo.com:Purple1','provenom8@gmail.com:phones22','blackendogame@hotmail.com:yunus1983','pokemonomega98@hotmail.com:thesims1234','macawsome13@gmail.com:telephone13','xbrxghosty@gmail.com:Fatality','cohenalieen@yahoo.com:qazwsx3edc','thepissedoffcanadian@gmail.com:bobbob12','decriot@gmail.com:Matches16','kyle116cobra@gmail.com:dodgeviper07','pewdie.00@hotmail.com:pewdiepie123','lewiswatkins2010@gmail.com:Trollface123','mdewey1174@gmail.com:qwertyuiop','fakhryauliyar@gmail.com:qrwe1423','shariqarain12@gmail.com:awesomeman3','the_buffalo1@hotmail.com:Brothers#1','blackjac97@yahoo.com:easy2remember','aligan147@yandex.com:1a2a3a4a5a6a','deaviontheus@gmail.com:deavion5','kr_sniper_2002@hotmail.com:pppppppp','brendonio@hotmail.com:horuslv8','buranku@outlook.com:1w2q3e4r','joshimac77@bigpond.com:skunk007','ndallemang@gmail.com:butthead00','coltsrno1@comcast.net:Marlboro1','superpleune@hotmail.com:Martin01','sorlis53@gmail.com:bloodflood64','tcallaway10@yahoo.com:pokemon10','jaspykins@gmail.com:Jasper97','goatsdominate@gmail.com:gamerswin','dummdummgamingg@gmail.com:stoney11','denis.almiron@yahoo.com:De15304423','gucluemir-2000@hotmail.com:1a2b3c4d','pmwilliford@gmail.com:oldgreg1','jimmyniggen10@gmail.com:abc123321','Angelo1995_23_@live.com:albania1995','kmj39037@gmail.com:Michelle7','sethbville2001@yahoo.com:michael01','andreastarck99@gmail.com:sandy2009','davantahorner3@yahoo.com:dada1234','chaoscakes21@gmail.com:igwaa2w2','rokasradiv@gmail.com:erelis488','kuba-g@hotmail.com:welcome99','kelly.luo2255@gmail.com:jess2222','ggohas@gmail.com:Minecraft8','zouphi16@msn.com:mel16061988','fuzzdood@outlook.com:Monkmonk1','leidbafutgol@hotmail.com:fireside1','aiden.reiff@gmail.com:Asdf1177','emireren-17@hotmail.com:wasdwasd123','cokecsgo@gmail.com:ringring1','ekarvan@gmail.com:helpme12','justinthekid747@gmail.com:Justinp1','shawn330king@gmail.com:kingster123','waffles8cookiesgaming@gmail.com:waffles88','darrecfonti@hotmail.com:blitzbeam1','jackie.jh@hotmail.com:boopwoop1','withereddeath@gmail.com:drdead1337','vedad.sitarevic@hotmail.com:Metro2033','kakashiokazaki15@gmail.com:Orange1205','adriensimon91@gmail.com:tupuduku','micnreg@gmail.com:Dominic29','rui47fernandes@hotmail.com:0fad4137','rnick54@yahoo.com:tombrady12','jeremyvann121@gmail.com:m1247r9p','cuorerossonero6@gmail.com:albertino','thecreativeemailaddress@gmail.com:hudson123','tristenredmond27@yahoo.com:download12','xa.go@aol.com:spark123','aidanyepson@yahoo.com:logan123','minecraftman979@gmail.com:superplayer','rafael.iago@hotmail.com:kaumendes3','sethobrien34@gmail.com:Nofear88','amitstuff@hotmail.com:engerto','mcangelvb@hotmail.com:kieke123','steeley661@gmail.com:11Thomasb!31','vikingflowerweek@gmail.com:alicia02','mkidxxs@gmail.com:markel13','therealgagewood@gmail.com:passw0rd','rellergert1@aol.com:little1234','eimantas.fiodorovas@gmail.com:vilkaspilkas666','haloman7min@yahoo.com:Tanner77','patrickmarfia2000@hotmail.com:halo2000','abeatty1717@yahoo.com:smokey1','masons12@att.net:Murphy01','pimped_dude@hotmail.com:Corv3tt3','ty95dixon@gmail.com:Fallen18','carmelfootball85@gmail.com:gavin2002','connorh4@bigpond.com:Jack0101','cerbugabriel@gmail.com:flatronl1918s','tylerstephens14@gmail.com:thetachi','dwmathias720@aol.com:inferno99','sorianotorneroalejandro@gmail.com:940725alejandro','xyeljackman@hotmail.com:puppy100','bi0hazardg3n3sis@gmail.com:El3phant','nates.familiar@gmail.com:summoner','widou98@hotmail.com:adam2000','anders.hansen2003@gmail.com:anders03','leanderdrakeiv@gmail.com:Dillmus12','karaka4ankata@gmail.com:1qa2ws3ed123','ps2005@outlook.com:patrik05','kanetrenouth95@gmail.com:Mooncow7','gravekeeperspy@gmail.com:tac0salad','schwing.david@yahoo.com:schwing123','justinmodern@hotmail.com:football44','nicolas.peron10@gmail.com:Chevalier1','iach.ia2016@yandex.com:iachester345','pjallard13@gmail.com:pieguy12','arthur.wii@hotmail.com:bozo1234','yentl3005@gmail.com:voetbal2','yorick.deprijcker@gmail.com:naruto1995','king.jack79@yahoo.com:greenday17','timoeo@yahoo.com:wicked101','augustineconnolly@gmail.com:sergio03','edaquino@verizon.net:Cronaldo7','kittitad5835@hotmail.com:jeab7556','bradyvl@hotmail.com:147852369b','cdees99@gmail.com:Chaser99','deany-boy@hotmail.com:Rangers94','101canun@gmail.com:apelsinas1','spencer.vallely@outlook.com:september9','firejuice@hotmail.com:45blood45','herosandgenerals1@gmail.com:Henry2013','johncorrado30@yahoo.com:snowball','antonioruggeri95@gmail.com:manuela95','mattgibbons07@gmail.com:ultimate2','paulkipps0822@gmail.com:jeopardy1','justin.gonzalez06@yahoo.com:thebeast06','timothyconti.tc.tc@gmail.com:power123','saro_sharma67@yahoo.com:sharma22','thecourtesan01@gmail.com:wings4me','comleycrt8@gmail.com:Bailey2000','enzoant2000@gmail.com:antonio10','jacknaylor578@gmail.com:samjack1','skylane184@hotmail.com:cessna89','remybouchet3011@gmail.com:remy3011','christian11danielsen@gmail.com:christian09','sam.c.n.collins@gmail.com:mississippi10','fariasrichard9@gmail.com:Richard02','neicechance@gmail.com:October911','kinghtnonza@hotmail.com:Winner55','pmns08@gmail.com:jeffhardy12','noorthekiller568@gmail.com:killer568','adinosek43@gmail.com:ADRian999','csbreder@yahoo.com:yankees55','alexsisouphone2@gmail.com:paradisefalls','andersemaegaard@gmail.com:kcx96xkv','servus375@gmail.com:1m2n3b4v5c','greer_joseph@yahoo.com:1qaz2wsx!QAZ','aidanmcphee11@hotmail.com:catman123','assasinnacho@hotmail.com:kaey1234','bottinoalex4@gmail.com:blaze123','dragoxgaming10@gmail.com:nutella66','kodydchurch@aol.com:Church1999','etb050702@yahoo.com:Harley4me','dulldarkdude21@outlook.com:Creeper21','joaosimon@msn.com:060789sp','vega_jovan@yahoo.com:dede1234','handfuloanvils@aim.com:4hxmvbdb8z','spudderswag@gmail.com:Trapper1','mkouchi2@gmail.com:godismyrock1','mdoyley87@gmail.com:charlie87','novell212@yahoo.com:PassWord1234','ozwhovian@gmail.com:hagrid123','moosywhistle@gmail.com:army123456','robotakh@hotmail.com:zgmfx42s','jim59lea61@aol.com:Buddyboy1','zapdos-moltres@hotmail.com:ddr2667mhz','bobbytibber@yahoo.com:webkinz123','erhanemreozkara@gmail.com:1q2w3e4r5t','khaled_ahmed_99@outlook.com:killer090','pat-levesque@hotmail.com:qazwsx123','millamaxwell@outlook.com:123abd']
        await message.author.send("Join Server To Keep Updated About Bot")
        await message.author.send(" Official Server https://discord.gg/44PFcRr ")
        msg = ' ' + author + '. Uplay Account : '
        await message.author.send(msg + (random.choice(randomlist)))

    if message.content.startswith('+crunchyroll'):
        randomlist = ['Haymae11@yahoo.com:Missme27','acex8781@gmail.com:Dragones6','alec.olen@yahoo.com:1Tennisfreak','alondra-acosta@hotmail.com:22happy22','andrei.sel.12@gmail.com:Andrew2503','anonymousdude666@gmail.com:momdad','azarmir.kasra@gmail.com:4008086q','b.aguilar34@yahoo.com:Acura2004','ben.reeves@gmail.com:skull9062','cam.williams0824@gmail.com:Cameron098','catguitarist@hotmail.co.uk:Dr34dw1ng','cesar.a.vieira@hotmail.com:forever3390','cuellarrico@yahoo.com:Yelitza7','cvmissy16@gmail.com:sweets2','daniel_jared@live.com:frida2011','dantealhigeri@hotmail.com:liukan15','desireianngalgana@hotmail.com:galgana1','dibl_96@hotmail.com:Diblteam06','dillonrockson@gmail.com:shaggy66','dino.duel@hotmail.com:Killer123','does_molly_ring_a_bell@yahoo.com:Jetaime23','ecchizz@live.com:seay15','elanning@gmail.com:althain2k9','esa0705@gmail.com:natsudragneel123','fireworks125machinima@gmail.com:poopoo10','gerard_liwanag@hotmail.com:Boxing101','glztiger@hotmail.it:somuas35','grimreaper0x0@yahoo.com:darkblade99','guigui2397@gmail.com:doudou98','hellscream0@hotmail.com:cotton99','henrikyo_inteligente@hotmail.com:99585849','imdewidesigns@gmail.com:Memelose1','isabelcalle_17@hotmail.com:kurosagi21','jiiub@hotmail.com:sebhan89','jmholohan@hotmail.com:Cc6260368','jnguyen5151@yahoo.com:bobby5151','jose15tito@msn.com:champ247','jroxendine@rocketmail.com:rxw420','jstanton14@hotmail.com:netx4984','kokiks101@gmail.com:shadow12','lastshogun@gmail.com:moses100','ldavis4127@aol.com:bingo222','leep.egerton@ntlworld.com:Abigail1','mapcra500@live.com:destroyer1','marcelocdomingues@hotmail.com:d11m5a71','marci690@gmail.com:risiko123','mattspvfx@gmail.com:power544','mauro_852@hotmail.com:marc1993','mdlmx19@gmail.com:xpootanX18','mikerob175@gmail.com:canes175','mykiddani@yahoo.com:bobby5689','naderpug@gmail.com:soarer','nekoiv9@gmail.com:aaaaaakiba04','nicholasmireles@yahoo.com:nick1998','nsjames7000@gmail.com:poopster2','ongteckwei@yahoo.com:keropi','pablo.asin@hotmail.es:barrancas1','pieguy798@gmail.com:HONDARIDER98','pirateking_nick@yahoo.com:my2ndname2','ptvheather@gmail.com:sept22000','quinnfoley@gmail.com:bears2012','rafaelflorers@yahoo.com:clubyes09','rezafatul@yahoo.co.id:moskwa','rodri9044@hotmail.com:huehue123','rodrigo.neta@gmail.com:lego541998','rolandcmorales08@gmail.com:000black','savualexandru0@gmail.com:ronaldo99','shinigmainox@gmail.com:miniwiflyXD1','shizzy186@yahoo.com:Warlover101','simen@vetaas-hoie.com:12Oktober','slipknot_dark1496@hotmail.com:presario14','speightquantez@gmail.com:speight1','sphireos@gmail.com:thailson1','steam21@vp.pl:Aezakmi12','steven.hellingh@gmail.com:3A55word','subtil.guilherme@gmail.com:rock4ever','t.ingh@live.nl:WIIkey25','themathwhizo@gmail.com:Mathpro2013','timmy_cattan@hotmail.com:Electrical1','travis.ber@gmail.com:Polpol123','vajsteve@gmail.com:thug4life','vigotheyt@gmail.com:pirate11','vijyaraj@gmail.com:rajmahal25','wbluke7000@gmail.com:moses711','westell626@gmail.com:godofwar','zach.ricketts@gmail.com:Smith230']
        await message.author.send("Join Server To Keep Updated About Bot")
        await message.author.send(" Official Server https://discord.gg/44PFcRr ")
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
