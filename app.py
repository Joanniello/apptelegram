
#ok
    #trader modificado....
        #send ⚗️Alchemy...(20)
        #send /sc {} {}... (20)
    #the orde...
        #order()       
            #order_alliance
                #Sentinel... def...tactic
    
            #casti
                #Sentinel... def...tactic

########################
#06/15/21
#reset dts...reset_stuff()
    #craft = True
    #arena = True
    #craft_alch = True
#squad_report...    
    # -fw_report()....--else sin guild    
#no opponent...find_opponent()
    #cambio time de respuesta a 10-15

#orderROS()...random(0, 1)
        #0.castillo
            #Sentinel... def...tactic
            #Alchemist... def...on_506
            #Alchemist... atk...on_508
        #1.guild
            #gdef OPK
                #Sentinel... def...tactic
                #Alchemist... def...on_506
                #Alchemist... atk...on_508

#MOBS ON/OFF in grupos
    #fix guild
    #probar q funcione???
#arenas_end
    #arena = False
#battle_coming_cw
    #-- send me()    

##############################################
#cambio de version v1.2
    #foray ciclo
        #add foray_was
            #guild=ROS and lvl>=70
                #/gd_s08 peace
                #/gd_s09 rage   
                #stop foray
            #foray+1
                #time +5 (5)...(10)
        #add foray_stop 
            #foray+1
    #inervene
        #+time 5s (20,30)...(25,35)
    #pledge
        #+time 5s (20)...(25)
    #-- xd_stop():
    #-- stop_quest(msg)  
    #full_stamina 
        #add condicion gold > 120 in ROS y lvl >= 70
    #sin_stamina
        #add condicion gold > 120 in ROS
        
##############################################
#cambio de version v1.3        
    #RANGER 40>=55
        #Check the order
            #minutes_before_war(65)...(80)
        #send_order_ranger
            #minutes_before_war(60)...(75)    
    #RANGER>55
        #Check the order bot
            #minutes_before_war(35)...(50)
        #send_order_ranger
            #minutes_before_war(30)...(45)
##############################################
############################################
#cambio de version v2.0 v2.1 v2.2 v2.3
    #posiones[]
        #se ellimina /b_p10
    #send_craft_potions
        #fix no enviaba de manera auto
    #add trade
        #trader
            #trader_alch by trade
                #trader_gone() off by trade
                #trader_gold() off by trade   
    #add variable gd_aut a rest_dts()
    #orderROS
        #lvl > 70 fijo en gdef OPK
    #fix hunter mobs
    #fix gdon +2s
    #add CD grupo CD
        #send report 
        #fw_monsters 
        #hunter
        #fw_preparing
        #/MOBS_ON/OFF
    #fix trade  
        #alchmsg valor inicial false 
        #quantity eliminar valor despues del trade
    #oreder
        #add check order rage and peace 
        #add send rage and peace (:57)
            #+time V.+5s.P.+10s.B.
        #add check and send skill_atk
            #coll_sense---/use_crl
            #battle_cry---/use_cry
        #check bot // send order ranger
            #-34....+48     
    #fix send_craft_potions
    #fix Congratulations! ..5s../w..+10s../f..+15s../me..
    #fix This is sad ..5s../w..+10s../me..
    #add matas al trade del senti 
        #'Cliff Rue': '41','Ilaves': '46','Ephijora': '47','Cave Garlic': '49',
        #'Yellow Seed': '50','Ash Rosemary': '53','Sun Tarragon': '55','Dragon Seed': '57'
#V3
    #v.3.0
        #add handler
            #(recuperar cuenta en caso de no cell)    
        #add botniato3.0
            #BOTNIATO = 1561523253           #BOT ALIANCE
        #check_order 
            #cambios en la update del bot alianza(/order)
        #check_order_ranger_one...check_order_ranger_nine
            #cambios en la update del bot alianza(/order)
        #bot_security_order
            #set sms q se espera....(for security....)        
    #v.3.0.1
        #fix...#bot_security_order    
    #V.3.0.2
        #ADD /join_guild    
        #add gd_alch
#################################################
#version V3
    #en progreso add aiming{lv:t_chek:t_order}
#################################################

from telethon import TelegramClient, events, connection
import asyncio
from telethon.tl.functions.messages import GetBotCallbackAnswerRequest
from random import seed, randint
import random, re
#import socks
import time
import logging
import config
import aiocron
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', level=logging.WARNING)

#variab
castle_emojis = ['🥔', '🦅', '🦌', '🐉', '🦈', '🐺']
order_alliance =  ''
order_cast = ''
emoji = ''
class_master = ['Blacksmith', 'Alchemist', 'Collector']
class_esquire = ['Knight', 'Sentinel', 'Ranger']
tactic = ['/tactics_potato', '/tactics_highnest', '/tactics_deerhorn', '/tactics_dragonscale', '/tactics_sharkteeth', '/tactics_wolfpack']
posiones = ['/b_507', '/b_509','/b_p01']
recursos = ['/c_21', '/c_22', '/c_23']
#quest
doing_quest = False
doing_quest_F = False
doing_quest_S = False
doing_quest_V = False
doing_quest_Y = False
fire = False
sec = 0
mobs = True
mobsx = ''
#deposit aut
gd_aut = False
gd_alch = False 
#trader
alch = {
    'Cliff Rue': '41',
    'Ilaves': '46',
    'Ephijora': '47',
    'Cave Garlic': '49',
    'Yellow Seed': '50',
    'Ash Rosemary': '53',
    'Sun Tarragon': '55',
    'Dragon Seed': '57'
} 
alchmsg = False
quantity = 0
#
rage = False
peace = False
morph = False
invite_guild = False
onGM = False
stock = {
    'Pelt': '03',
    'Powder': '07',
    'Iron ore': '08',
    'Cloth': '09',
    'Silver ore': '10',
    'Bone powder': '21'
}
#arenas
opponent = 0
#pendientes
    #aiming = {
    #    '20':'185':'180',
    #    '22':'170':'165',
    #    '24':'155':'150',
    #    '26':'140':'135',
    #    '28':'125':'120',
    #    '30':'110':'105',
    #    '32':'100':'95',
    #    '34':'90':'85',
    #    '36':'80':'75',
    #    '38':'70':'65',
    #    '40':'65':'60',
    #    '42':'60':'55',
    #    '44':'55':'50',
    #    '46':'50':'45',
    #    '48':'45':'40'
    #}

    #withdraw = False
    
    #craft = True
    #arena = True 
    #craft_alch = True
#
class ChatWarsCron():
    def __init__(self, server_utc):
        self.utc_delay = server_utc
        self.war_times = [7, 15, 23]

    def minutes_before_war(self, m, h=0):
        assert m >= 0 and h >= 0
        if m >= 60:
            h += m // 60
            m =  m % 60
        m = 60 - m
        mstr = str(m)
        vals = [mstr.zfill(2-len(mstr))] + [(24 + i + self.utc_delay - (h + 1))%24 for i in self.war_times]
        return '{} {},{},{} * * *'.format(*vals)
    def hours_before_war(self, h):
        assert  h >= 0
        return '00 {},{},{} * * *'.format(*((24 + i + self.utc_delay - h)%24 for i in self.war_times))

    def minutes_after_war(self, m, h=0):
        assert m >= 0 and  h >= 0
        if m >= 60:
            h += m // 60
            m = m % 60
        mstr = str(m)
        vals = [mstr.zfill(2-len(mstr))] + [(24 + i + self.utc_delay + h)%24 for i in self.war_times]
        return '{} {},{},{} * * *'.format(*vals)
    def hours_after_war(self, h):
        assert  h >= 0
        return '00 {},{},{} * * *'.format(*((24 + i + self.utc_delay + h)%24 for i in self.war_times))

    #def reset_time(self):
    #    return '30 {} * * *'.format(8 + self.utc_delay)

def welcome():
    global hero
    print(time.asctime(), '----->', 'Automatizacion Iniciada')
    
    sending_me()
    #
    sending_clas()

def sending_me():
    task = loop.create_task(me())
async def me():
    await asyncio.sleep(2)
    await client.send_message('chtwrsbot', '🏅Me')

def sending_clas():
    task = loop.create_task(clas())
async def clas():
    await asyncio.sleep(5)
    await client.send_message('chtwrsbot', '/class')  

#HERO
class Hero(object):
    """docstring for Hero"""
    def __init__(self, lvl, guild, hp, max_hp, stamina, max_stamina, gold, clas, rest, vers):
        self.lvl = lvl
        self.guild = guild
        self.hp = hp
        self.stamina = stamina
        self.max_stamina = max_stamina
        self.rest = rest
        self.max_hp = max_hp
        self.gold = gold
        self.clas = clas
        self.vers = "v3.0.2 Server 1"
def __str__(self):
    return "Lvl:  {}\n Guild:  {}\n HP:  {}\n Max_HP:  {}\n Stamina:  {}\n Max_stamina:  {}\n Gold:  {}\n Clas: {}\n Rest: {}\n Vers: {}".format(self.lvl, self.guild, self.hp, self.max_hp , self.stamina, self.max_stamina, self.gold, self.clas, self.rest, self.vers)

#dts hero    
async def collecting_data(msg):
    global hero, doing_quest

    hero.rest = collecting_data_resting(msg)
    hero.lvl = collecting_data_lvl(msg)
    hero.hp, hero.max_hp = collecting_data_hp(msg)
    hero.stamina, hero.max_stamina = collecting_data_stamina(msg)
    hero.gold = collecting_data_gold(msg)
    hero.guild = collecting_data_guild(msg)
    if hero.stamina == hero.max_stamina:
        doing_quest = True
        await asyncio.sleep(5)
        await go_quest()
    
def collecting_data_stamina(msg):
    stamina = int(re.search(r'Stamina: (\d+)', msg).group(1))
    max_stamina = int(re.search(r'Stamina: (\d+)/(\d+)', msg).group(2))
    return stamina, max_stamina 
def collecting_data_lvl(msg):
    msg_lvl = "🏅Level: "
    index = msg.find(msg_lvl) + len(msg_lvl)
    return (int)(msg[index:index+2])
def collecting_data_hp(msg):
    msg_hp = "❤️Hp: "
    msg_stamina = "🔋Stamina: "
    index = msg.find(msg_hp) + len(msg_hp)
    indey = msg.find(msg_stamina)
    hp = msg[index:indey].split("/")[0]
    max_hp = msg[index:indey].split("/")[1]
    return (int)(hp), (int)(max_hp)
def collecting_data_resting(msg):
    state = re.search(r'State:\n(.*)', msg).group(1)
    return state
def collecting_data_gold(msg):
    lines = msg.split('\n')
    for i, line in enumerate(lines):
        if len(line):
            if line[0].startswith('💰'):
                gold = int(line[1:].split()[0])
    return gold    
def collecting_data_clas(msgc):
    end = msgc.find("\n")
    return msgc[0:end-15]
def collecting_data_guild(msg):
    try:
        guildtag = msg.split('[')[1].split(']')[0]
        guild = "[{}]".format(guildtag)
        return guild
    except:
        guild = "[{}]".format('')
        return guild
        
hero = Hero(0,' ', 0, 0, 0, 0, 0,' ', True,'')

cwc = ChatWarsCron(config.UTC_DELAY)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    client = TelegramClient(config.SESSION, config.API_ID, config.API_HASH, timeout = 5, connection_retries = None, retry_delay = 5, sequential_updates=True, auto_reconnect = True)
    # client.start(MY_PHONE)
    client.start()
    welcome()

#*********** parse me **************************
@client.on(events.NewMessage(chats = 'chtwrsbot' , incoming = True, pattern=r'Battle of the seven castles in|🌟Congratulations! New level!🌟'))
async def parse_me(event):
    await collecting_data(event.message.message)

#*********** parse class **************************
@client.on(events.NewMessage(chats = 'chtwrsbot' , incoming = True, pattern='((.|\n)*)skills levels:((.|\n)*)'))
async def parse_clas(event):
    global hero
    hero.clas = collecting_data_clas(event.message.message)

#************reset dts **************
@aiocron.crontab(cwc.minutes_after_war(10))
def rest_dts():
    global doing_quest, doing_quest_F, doing_quest_S, doing_quest_V, doing_quest_Y, fire
    global order_alliance, order_cast, emoji
    global mobs, gd_aut, gd_alch
    
    order_alliance =  ''
    order_cast = ''
    emoji = ''
    doing_quest = False
    doing_quest_F = False
    doing_quest_S = False
    doing_quest_V = False
    doing_quest_Y = False
    fire = False
    mobs = True
    gd_aut = False
    gd_alch = False

##new
    ##************reset dts **************
    #@aiocron.crontab(cwc.reset_time())
    #async def reset_stuff():
    #    craft = True
    #    arena = True
    #    craft_alch = True
    
#*********** send_report ***********
@aiocron.crontab(cwc.minutes_after_war(randint(15,30)))
def send_report():
    task = loop.create_task(report())

#*********** the report ***********
async def report():
    await asyncio.sleep(2)
    await client.send_message('chtwrsbot', '/report')

#*********** squad_report ***********
@client.on(events.NewMessage(chats = 'chtwrsbot', pattern='((.|\n)*)Your result on the battlefield((.|\n)*)'))
async def fw_report(event):
    global hero
    if not 'Encounter' in event.message.message:
        if hero.guild =='[CD]':
            await asyncio.sleep(2)
            await client.forward_messages(config.MOBS_COLL, event.message)
        if hero.guild =='[ROS]':
            await asyncio.sleep(2)
            await client.forward_messages(config.MOBS_KNIGTH, event.message)
        if hero.guild =='[OPK]':
            await asyncio.sleep(2)
            await client.forward_messages(config.SQUAD, event.message)    
        #else:
        #    await asyncio.sleep(2)
        #    await client.forward_messages(config.GROUP, event.message)        

#*********** send_arenas ***********
@aiocron.crontab(cwc.minutes_after_war(randint(60,75)))
def send_arenas():
    task = loop.create_task(arenas())

#*********** the arenas ***********
async def arenas():
    await client.send_message('chtwrsbot', '▶️Fast fight')

#*********** the arenas +1 ***********
@client.on(events.NewMessage(chats = 'chtwrsbot' , incoming = True, pattern='((.|\n)*)stands victorious over((.|\n)*)'))
async def arenas_on(event):
    opponent = 0
    await asyncio.sleep(randint(15,20))
    await client.send_message('chtwrsbot', '▶️Fast fight')

#*********** no opponent ***********
@client.on(events.NewMessage(chats = 'chtwrsbot' , incoming = True, pattern='((.|\n)*)You didn’t find an opponent. Return later((.|\n)*)'))
async def find_opponent(event):
    global opponent
    if opponent < 3:
        opponent += 1
        await asyncio.sleep(randint(10,15))
        await client.send_message('chtwrsbot', '▶️Fast fight')

#IN class ************************************************************************************************************************

#*********** send_craft_diario ***********
@aiocron.crontab(cwc.minutes_after_war(randint(35,40)))
def send_craft():
    global hero
    #if craft: 
    if hero.clas in class_master:
        task = loop.create_task(craft())

#v2.2...if 'Alchemist' in hero.clas:
#*********** craft_diario ***********
async def craft():
    global hero
    msg = random.choice(recursos)
    if 'Alchemist' in hero.clas:
        await asyncio.sleep(2)
        await client.send_message('chtwrsbot', '/c_23')
    else:
        await asyncio.sleep(2)
        await client.send_message('chtwrsbot', msg)

#v2.2...if 'Alchemist' in hero.clas:
#*********** craft_diario +1 ***********
@client.on(events.NewMessage(chats = 'chtwrsbot' , incoming = True, pattern='.*Crafted: .*'))
async def craft_diario(event):
    msg = random.choice(recursos)
    if 'Earned:' in event.message.message:
        await asyncio.sleep(5)
        if 'Alchemist' in hero.clas:
            await asyncio.sleep(2)
            await client.send_message('chtwrsbot', '/c_23')
        else:
            await asyncio.sleep(2)
            await client.send_message('chtwrsbot', msg)
    #else: 
    #    craft = False

@client.on(events.NewMessage(chats = 'chtwrsbot' , incoming = True, pattern='.*Not enough materials to craft Bone powder.*'))   
async def not_bone_powder(event):
    await asyncio.sleep(4)
    await client.send_message('chtwrsbot', '/c_22')

#new
    #@client.on(events.NewMessage(chats = 'chtwrsbot' , incoming = True, pattern='.*Not enough materials to craft String.*'))    
    #async def not_string(event):
    #    await asyncio.sleep(4)
    #    await client.send_message('chtwrsbot', '/c_23')

@client.on(events.NewMessage(chats = 'chtwrsbot' , incoming = True, pattern='.*Not enough materials to craft Coke.*'))    
async def not_coke(event):
    await asyncio.sleep(4)
    await client.send_message('chtwrsbot', '/c_21')

#v2.2...if 'Alchemist' in hero.clas:
#*********** send_craft_potions ***********
@aiocron.crontab(cwc.minutes_after_war(randint(45,50)))
def send_craft_potions():
    global hero 
    if 'Alchemist' in hero.clas:
        task = loop.create_task(craft_potions())

#*********** send_craft_diario_potions ***********
async def craft_potions():
    msg = random.choice(posiones)
    await asyncio.sleep(2)
    await client.send_message('chtwrsbot', msg)
    
#*********** send_craft_diario_potions +1 ***********
@client.on(events.NewMessage(chats = 'chtwrsbot' , incoming = True, pattern='.*Brewed: .*'))
async def craft_diario_potions(event):
    msg = random.choice(posiones)
    if 'Earned:' in event.message.message:
        await asyncio.sleep(5)
        await client.send_message('chtwrsbot', msg)
        
@client.on(events.NewMessage(chats = 'chtwrsbot' , incoming = True, pattern='.*Not enough materials to craft Poison pack.*'))
async def not_poison(event):
    await asyncio.sleep(4)
    await client.send_message('chtwrsbot', '/b_507')

@client.on(events.NewMessage(chats = 'chtwrsbot' , incoming = True, pattern='.*Not enough materials to craft Remedy pack.*'))
async def not_remedy(event):
   await asyncio.sleep(4)
   await client.send_message('chtwrsbot', '/b_p01')

#v2.2
#********** inervene **************************
@client.on(events.NewMessage(chats = 'chtwrsbot' , incoming = True, pattern='((.|\n)*)You were strolling around on your horse when you noticed((.|\n)*)'))
async def intervene(event):
    time.sleep(randint(25,35))
    await event.message.buttons[0][0].click()
    await asyncio.sleep(30)
    await client.request

#v2.2
#***********class 'Knight' ***********
@client.on(events.NewMessage(chats = 'chtwrsbot' , incoming = True, pattern='((.|\n)*)After a successful act of violence, as a brave knight((.|\n)*)'))
async def pledge(event):
    await asyncio.sleep(25)
    await client.send_message('chtwrsbot', '/pledge')

#v2.2
#***********class 'senti' ***********
@client.on(events.NewMessage(chats = 'chtwrsbot' , incoming = True, pattern='((.|\n)*)However, he is leaving to distant lands and his caravan can only carry((.|\n)*)'))
async def trader(event):
    global alchmsg, quantity
    alchmsg = True
    trader = event.message.message
    init = trader.find("only carry")

    end = trader.find("\n")
    quantity = (int)(trader[init+11:end-2]) 
    await asyncio.sleep(20)
    await client.send_message('chtwrsbot' , '⚗️Alchemy')

#v3.0.2 gdalch
@client.on(events.NewMessage(chats = 'chtwrsbot' , incoming = True, pattern=r'Cliff Rue|Ash Rosemary|Cave Garlic|Ephijora|Ilaves|Sun Tarragon|Yellow Seed|Dragon Seed'))
async def trader_alch(event):
    #print('trader')
    global quantity, alchmsg, alch
    global gd_alch

    if alchmsg:
        for resource in event.message.message.split('\n'): 
            if (int)(resource.split('(')[1].split(')')[0]) >= quantity:
                if resource.split(' (')[0].strip() in alch.keys():                    
                    code = alch[resource.split(' (')[0].strip()] 
        await asyncio.sleep(20)
        await client.send_message('chtwrsbot' , '/sc {} {}'.format(code, quantity))
    elif gd_alch:
        if event.message.buttons[0][0].text == '👥Deposit':
            await asyncio.sleep(5)
            await event.message.buttons[0][0].click()   
        else:
            if gd_alch:
                lines = event.message.message.split('\n')
                first = lines[0][0]
                line_full = None
                resource_sin = None
                user_stock = [ ]
                for i, line in enumerate(lines):
                    if len(line):
                        if line[0] == '[empty]':
                            return 'no data'
                        else:
                            line_full = line.split(' (')
                            if line_full[0] == '[empty]':
                                pass
                            else:
                                result = re.match(r"\A[/gd_].*[0-9]\s", line_full[0])
                                if result:
                                    resource_sin = line_full[0].split(' ')[0]
                                    if '/gd_41' in resource_sin or '/gd_46' in resource_sin or '/gd_47' in resource_sin or '/gd_49' in resource_sin or '/gd_50' in resource_sin or '/gd_53' in resource_sin or '/gd_55' in resource_sin or '/gd_57' in resource_sin:
                                        pass
                                    else:
                                        await asyncio.sleep(7)
                                        await client.send_message('chtwrsbot',resource_sin)          

#v2.2
@client.on(events.NewMessage(chats = 'chtwrsbot' , incoming = True, pattern='((.|\n)*)Oh no, you were turtling for too long, the trader is gone((.|\n)*)'))
async def trader_gone(event):
    global alchmsg, quantity
    await asyncio.sleep(4)
    alchmsg = False
    quantity = 0
    
#2.2
@client.on(events.NewMessage(chats = 'chtwrsbot' , incoming = True, pattern='((.|\n)*)The trader gave you some gold and left((.|\n)*)'))
async def trader_gold(event):
    global alchmsg, quantity
    await asyncio.sleep(4)
    alchmsg = False
    quantity = 0

#END class ************************************************************************************************************************

#IN ORDEN***************************************************************************************

#***********Check the order bot<30 ***********
    #@aiocron.crontab(cwc.minutes_before_war(125))
    #async def check_order_ranger_one():
    #    global hero
    #    if 'Ranger' in hero.clas:
    #        if hero.lvl < 30:
    #            await client.send_message(config.BOTNIATO, '⚜️ Order')

#***********Check the order bot30<40 ***********
    #@aiocron.crontab(cwc.minutes_before_war(95))
    #async def check_order_ranger_two():
    #    global hero
    #    if 'Ranger' in hero.clas:
    #        if (hero.lvl >= 30) and (hero.lvl < 40):
    #            await client.send_message(config.BOTNIATO, '⚜️ Order')

#revisar con luis.b
#***********Check the order bot40<55 ***********
    #@aiocron.crontab(cwc.minutes_before_war(80))
    #async def check_order_ranger_three():
    #    global hero
    #    if 'Ranger' in hero.clas:
    #        if (hero.lvl >= 40) and (hero.lvl < 55):
    #            await client.send_message(config.BOTNIATO, '⚜️ Order')

#newrevisar con rob
#***********Check the order bot55+ ***********

#***********Check the order bot ***********
@aiocron.crontab(cwc.minutes_before_war(10))
async def check_order():
    global hero
    if 'Ranger' not in hero.clas:
        await client.send_message(config.BOTNIATO, '/order')    

################################################
#check bot // send order ranger

#*********** check / send -34 ***********
@aiocron.crontab(cwc.minutes_before_war(125))
async def check_order_ranger_one():
    global hero
    if ('Ranger' in hero.clas) and (hero.guild =='[OPK]'):
        if hero.lvl < 34:
            await client.send_message(config.BOTNIATO, '/order')

@aiocron.crontab(cwc.hours_before_war(2))
def send_order_ranger_one():
    global hero
    global mobs
    if 'Ranger' in hero.clas:
        if hero.lvl < 34:
            mobs = False
            task = loop.create_task(order())
            
#*********** check / send 34//36 ***********
@aiocron.crontab(cwc.minutes_before_war(90))
async def check_order_ranger_two():
    global hero
    if ('Ranger' in hero.clas) and (hero.guild =='[OPK]'):
        if (hero.lvl >= 34) and (hero.lvl < 36):
            await client.send_message(config.BOTNIATO, '/order')

@aiocron.crontab(cwc.minutes_before_war(85))
def send_order_ranger_two():
    global hero
    global mobs
    if 'Ranger' in hero.clas:
        if (hero.lvl >= 34) and (hero.lvl < 36):
            mobs = False
            task = loop.create_task(order())

#*********** check / send 36//38 ***********
@aiocron.crontab(cwc.minutes_before_war(80))
async def check_order_ranger_three():
    global hero
    if ('Ranger' in hero.clas) and (hero.guild =='[OPK]'):
        if (hero.lvl >= 36) and (hero.lvl < 38):
            await client.send_message(config.BOTNIATO, '/order')

@aiocron.crontab(cwc.minutes_before_war(75))
def send_order_ranger_three():
    global hero
    global mobs
    if 'Ranger' in hero.clas:
        if (hero.lvl >= 36) and (hero.lvl < 38):
            mobs = False
            task = loop.create_task(order())

#*********** check / send 38//40 ***********
@aiocron.crontab(cwc.minutes_before_war(70))
async def check_order_ranger_four():
    global hero
    if ('Ranger' in hero.clas) and (hero.guild =='[OPK]'):
        if (hero.lvl >= 38) and (hero.lvl < 40):
            await client.send_message(config.BOTNIATO, '/order')

@aiocron.crontab(cwc.minutes_before_war(65))
def send_order_ranger_four():
    global hero
    global mobs
    if 'Ranger' in hero.clas:
        if (hero.lvl >= 38) and (hero.lvl < 40):
            mobs = False
            task = loop.create_task(order())

#*********** check / send 40//42 ***********
@aiocron.crontab(cwc.minutes_before_war(65))
async def check_order_ranger_five():
    global hero
    if ('Ranger' in hero.clas) and (hero.guild =='[OPK]'):
        if (hero.lvl >= 40) and (hero.lvl < 42):
            await client.send_message(config.BOTNIATO, '/order')

@aiocron.crontab(cwc.hours_before_war(1))
def send_order_ranger_five():
    global hero
    global mobs
    if 'Ranger' in hero.clas:
        if (hero.lvl >= 40) and (hero.lvl < 42):
            mobs = False
            task = loop.create_task(order())

#*********** check / send 42//44 ***********
@aiocron.crontab(cwc.hours_before_war(1))
async def check_order_ranger_six():
    global hero
    if ('Ranger' in hero.clas) and (hero.guild =='[OPK]'):
        if (hero.lvl >= 42) and (hero.lvl < 44):
            await client.send_message(config.BOTNIATO, '/order')

@aiocron.crontab(cwc.minutes_before_war(55))
def send_order_ranger_six():
    global hero
    global mobs
    if 'Ranger' in hero.clas:
        if (hero.lvl >= 42) and (hero.lvl < 44):
            mobs = False
            task = loop.create_task(order())

#*********** check / send 44//46 ***********
@aiocron.crontab(cwc.minutes_before_war(55))
async def check_order_ranger_seven():
    global hero
    if ('Ranger' in hero.clas) and (hero.guild =='[OPK]'):
        if (hero.lvl >= 44) and (hero.lvl < 46):
            await client.send_message(config.BOTNIATO, '/order')

@aiocron.crontab(cwc.minutes_before_war(50))
def send_order_ranger_seven():
    global hero
    global mobs
    if 'Ranger' in hero.clas:
        if (hero.lvl >= 44) and (hero.lvl < 46):
            mobs = False
            task = loop.create_task(order())

#*********** check / send 46//48 ***********
@aiocron.crontab(cwc.minutes_before_war(50))
async def check_order_ranger_eight():
    global hero
    if ('Ranger' in hero.clas) and (hero.guild =='[OPK]'):
        if (hero.lvl >= 46) and (hero.lvl < 48):
            await client.send_message(config.BOTNIATO, '/order')

@aiocron.crontab(cwc.minutes_before_war(45))
def send_order_ranger_eight():
    global hero
    global mobs
    if 'Ranger' in hero.clas:
        if (hero.lvl >= 46) and (hero.lvl < 48):
            mobs = False
            task = loop.create_task(order())

#*********** check / send 48+ ***********
@aiocron.crontab(cwc.minutes_before_war(45))
async def check_order_ranger_nine():
    global hero
    if ('Ranger' in hero.clas) and (hero.guild =='[OPK]'):
        if hero.lvl >= 48:
            await client.send_message(config.BOTNIATO, '/order')

@aiocron.crontab(cwc.minutes_before_war(40))
def send_order_ranger_nine():
    global hero
    global mobs
    if 'Ranger' in hero.clas:
        if hero.lvl >= 48:
            mobs = False
            task = loop.create_task(order())            

################################################

#***********Check the order bot ***********
#@client.on(events.NewMessage(chats= config.BOTNIATO, pattern='((.|\n)*)For security reasons you need to execute this command first((.|\n)*)'))
'''@client.on(events.NewMessage(chats= config.BOTNIATO, pattern='((.|\n)*)For security reasons you are asked to run this additional command((.|\n)*)'))
async def bot_security_order(event):
    security = '/' + event.message.text.split('/')[-1]
    await client.send_message(config.BOTNIATO, security)'''

#v2.3...morph
'''@client.on(events.NewMessage(chats= config.BOTNIATO, pattern='((.|\n)*)Orders for next battle((.|\n)*)'))
async def bot_order(event):
    global order_alliance
    global rage, peace, morph'''
    
'''order_alliance = '/ga_' + event.message.text.split('url?url=/ga_')[1].split()[0].split(')')[0]

    if 'use_p01' in event.message.text:
        rage = True
    if 'use_p04' in event.message.text:
        peace = True
    if 'use_p19' in event.message.text:
        morph = True'''
#***********order CHANNEL***********
@client.on(events.NewMessage(chats = config.ORDER_CHANNEL, incoming =True))
async def order_group(event):
    global order_cast
    global emoji
    sms_emoji = event.raw_text
    if '⚔' in sms_emoji:
        for e in castle_emojis:
            if e in sms_emoji:
                emoji = e
                order_cast = '⚔Attack'

#??
#*********** send_order_ranger*********** 
    #@aiocron.crontab(cwc.hours_before_war(2))
    #def send_order_ranger_one():
    #    global hero
    #    global mobs
    #    if 'Ranger' in hero.clas:
    #        if hero.lvl < 30:
    #            mobs = False
    #            task = loop.create_task(order())

#??
#*********** send_order_ranger*********** 
    #@aiocron.crontab(cwc.minutes_before_war(90))
    #def send_order_ranger_two():
    #    global hero
    #    global mobs
    #    if 'Ranger' in hero.clas:
    #        if (hero.lvl >= 30) and (hero.lvl < 40):
    #            mobs = False
    #            task = loop.create_task(order())

#??revisar con luis.b
#*********** send_order_ranger*********** 
    #@aiocron.crontab(cwc.minutes_before_war(75))
    #def send_order_ranger_three():
    #    global hero
    #    global mobs
    #    if 'Ranger' in hero.clas:
    #        if (hero.lvl >= 40) and (hero.lvl < 55):
    #            mobs = False
    #            task = loop.create_task(order())

#???
#*********** send_order*********** 
@aiocron.crontab(cwc.minutes_before_war(4))
def send_order():
    global hero
    if 'Ranger' not in hero.clas:
        if hero.guild =='[OPK]':
            task = loop.create_task(order())    
        elif hero.guild =='[ROS]':
            task = loop.create_task(orderROS())
        else:
            task = loop.create_task(order())

#??
#*********** the order***********
async def order():
    global order_cast
    global emoji
    global order_alliance
    global hero
    msg = random.choice(tactic)
    
    if order_alliance:
        await client.send_message('chtwrsbot', order_alliance)
        if 'Sentinel' in hero.clas:
            if order_alliance.split('_')[1]=='def':
                await asyncio.sleep(4)
                await client.send_message('chtwrsbot', msg)
        elif 'Alchemist' in hero.clas:
            if order_alliance.split('_')[1]=='def':
                await asyncio.sleep(4)
                await client.send_message('chtwrsbot', '/on_506')
            else:
                await asyncio.sleep(4)
                await client.send_message('chtwrsbot', '/on_508')
    else:
        if 'Sentinel' in hero.clas:
            await client.send_message('chtwrsbot', '🛡Defend') 
            await asyncio.sleep(4)
            await client.send_message('chtwrsbot', msg) 
        else:
            if emoji:
                await client.send_message('chtwrsbot', order_cast)
                await asyncio.sleep(5)
                await client.send_message('chtwrsbot', emoji)
                if 'Alchemist' in hero.clas:
                    await asyncio.sleep(4)
                    await client.send_message('chtwrsbot', '/on_508')                  
            else:
                await client.send_message('chtwrsbot', '🛡Defend')
                if 'Alchemist' in hero.clas:
                    await asyncio.sleep(4)
                    await client.send_message('chtwrsbot', '/on_506')
#v3.0.2 fix gdef+80
async def orderROS():
    global order_cast
    global emoji
    # global order_alliance
    global hero
    msg = random.choice(tactic)
    go = random.choice((0, 1))
    
    if hero.lvl > 80:
        await client.send_message('chtwrsbot', '/g_def OPK')
        if 'Sentinel' in hero.clas:
            await asyncio.sleep(4)
            await client.send_message('chtwrsbot', msg) 
        elif 'Alchemist' in hero.clas:
            await asyncio.sleep(4)
            await client.send_message('chtwrsbot', '/on_506')
    else:
        if go == 0:
            if 'Sentinel' in hero.clas:
                await client.send_message('chtwrsbot', '🛡Defend') 
                await asyncio.sleep(4)
                await client.send_message('chtwrsbot', msg) 
            else:
                if emoji:
                    await client.send_message('chtwrsbot', order_cast)
                    await asyncio.sleep(5)
                    await client.send_message('chtwrsbot', emoji)
                    if 'Alchemist' in hero.clas:
                        await asyncio.sleep(4)
                        await client.send_message('chtwrsbot', '/on_508')
                else:
                    await client.send_message('chtwrsbot', '🛡Defend')
                    if 'Alchemist' in hero.clas:
                        await asyncio.sleep(4)
                        await client.send_message('chtwrsbot', '/on_506')
        if go == 1:
            await client.send_message('chtwrsbot', '/g_def OPK')
            if 'Sentinel' in hero.clas:
                await asyncio.sleep(4)
                await client.send_message('chtwrsbot', msg) 
            elif 'Alchemist' in hero.clas:
                await asyncio.sleep(4)
                await client.send_message('chtwrsbot', '/on_506')
    
#END ORDEN***************************************************************************************
#add gd_aut on/off
#-COMANDOS-(Autorespuesta) sms guardados
@client.on(events.NewMessage(chats = config.MY_ID ,outgoing =True))
async def handle_out_message(event):
    '''output msg handler'''
    global hero, mobs
    global doing_quest, doing_quest_F, doing_quest_S, doing_quest_V, doing_quest_Y, fire
    global gd_aut, gd_alch, onGM 

    if event.from_id is not None:
        try:
            user = await event.client.get_entity(event.from_id)
        except Exception as e:
            pass
    else:
        user = None
    msg = event.message
    try:
        chat = await client.get_entity(msg.to_id)
    except:
        chat = None
    if chat.id == config.MY_ID:
        if (("hero" in msg.message) or ("Hero" in msg.message)):
            sending_me()
            await client.send_message(chat, __str__(hero))
            print(__str__(hero))
        if ("arena" in msg.message) or ("Arena" in msg.message):
            await client.send_message('chtwrsbot','▶️Fast fight')  
            await client.send_message(chat,"realizando arenas!!!")         
        if ("craft" in msg.message) or ("Craft" in msg.message):
            await client.send_message('chtwrsbot','/c_22') 
            await client.send_message(chat,"a gastar recursos!!!")  
        if ("mobs_on" in msg.message) or ("Mobs_on" in msg.message):
            mobs = True
            await client.send_message(chat,"MOBS ON")  
        if ("mobs_off" in msg.message) or ("Mobs_off" in msg.message):
            mobs = False
            await client.send_message(chat,"MOBS OFF")       
        if ("autoq" in msg.message) or ("Autoq" in msg.message):
            await client.send_message(chat,"Autoquest Iniciado")
            doing_quest = True
            doing_quest_F = False
            doing_quest_S = False
            doing_quest_V = False
            doing_quest_Y = False
            fire = False
            gd_aut = False
            await go_quest()
        if ("qon f" in msg.message) or ("Qon f" in msg.message):
            await client.send_message(chat,"Iniciando Autoquesting En 🌲Forest")
            doing_quest = False
            doing_quest_F = True
            doing_quest_S = False
            doing_quest_V = False
            doing_quest_Y = False
            fire = False
            gd_aut = False
            await go_quest() 
        if ("qon s" in msg.message) or ("Qon s" in msg.message):
            await client.send_message(chat,"Iniciando Autoquesting En 🍄Swamp")
            doing_quest = False
            doing_quest_F = False
            doing_quest_S = True
            doing_quest_V = False
            doing_quest_Y = False
            fire = False
            gd_aut = False
            await go_quest()
        if ("qon v" in msg.message) or ("Qon v" in msg.message):
            await client.send_message(chat,"Iniciando Autoquesting En 🏔Valley")
            doing_quest = False
            doing_quest_F = False
            doing_quest_S = False
            doing_quest_V = True
            doing_quest_Y = False
            fire = False
            gd_aut = False
            await go_quest()
        if ("qon y" in msg.message) or ("Qon y" in msg.message):
            await client.send_message(chat,"Iniciando Autoquesting En Foray")
            doing_quest = False
            doing_quest_F = False
            doing_quest_S = False
            doing_quest_V = False
            doing_quest_Y = True
            fire = False
            gd_aut = False
            await go_quest()                
        if ("qoff" in msg.message) or ("Qoff" in msg.message):
            await client.send_message(chat,"Autoquest Detenido")
            doing_quest = False
            doing_quest_F = False
            doing_quest_S = False
            doing_quest_V = False
            doing_quest_Y = False
            fire = False
            mobs = True
            
        if ("/gdon" in msg.message) or ("/gd_on" in msg.message):
            gd_aut = True
            doing_quest = False
            doing_quest_F = False
            doing_quest_S = False
            doing_quest_V = False
            doing_quest_Y = False
            fire = False
            await client.send_message('chtwrsbot','📦Resources')  
            await client.send_message(chat,"gd automatic on")       
        
        if ("/gdalch" in msg.message) or ("/gd_alch" in msg.message):
            gd_alch = True 
            gd_aut = False
            doing_quest = False
            doing_quest_F = False
            doing_quest_S = False
            doing_quest_V = False
            doing_quest_Y = False
            fire = False
            await client.send_message('chtwrsbot','⚗️Alchemy')  
            await client.send_message(chat,"gd automatic on")       
        
        if ("/gdoff" in msg.message) or ("/gd_off" in msg.message):
            await client.send_message(chat,"gd automatic off")
            gd_aut = False
            gd_alch = False 
            doing_quest = False
            doing_quest_F = False
            doing_quest_S = False
            doing_quest_V = False
            doing_quest_Y = False
            fire = False 

        if ("gm_on" in msg.message) or ("GM_ON" in msg.message):
            await client.send_message(chat,"GM activado")
            onGM = True
        if ("gm_off" in msg.message) or ("GM_OFF" in msg.message):
            await client.send_message(chat,"GM desactivado")
            onGM = False    
#IN quest******************************************************************************************************************************
async def go_quest():
    '''initial go quest func '''
    await client.send_message('chtwrsbot','🗺Quests')

#@aiocron.crontab(cwc.minutes_before_war(16))
    #def xd_stop():
    #    task = loop.create_task(stop_quest())
    #
#async def stop_quest(msg):
    #    '''initial go quest func '''
    #    global doing_quest
    #    global doing_quest_F
    #    global doing_quest_S
    #    global doing_quest_V
    #    global doing_quest_Y
    #    global fire
    #    global mobs 
    #
    #    await asyncio.sleep(2)
    #    doing_quest = False
    #    doing_quest_F = False
    #    doing_quest_S = False
    #    doing_quest_V = False
    #    doing_quest_Y = False
    #    fire = False
    #    mobs = True
    #    await asyncio.sleep(2)
    #    await sending_me()

@aiocron.crontab(cwc.minutes_before_war(18))
async def stop():
    global doing_quest, doing_quest_F, doing_quest_S, doing_quest_V, doing_quest_Y, fire
    
    await asyncio.sleep(2)
    doing_quest = False
    doing_quest_F = False
    doing_quest_S = False
    doing_quest_V = False
    doing_quest_Y = False
    fire = False 
    await asyncio.sleep(2)
    await sending_me()

@client.on(events.NewMessage(chats = 'chtwrsbot' , incoming = True, pattern='((.|\n)*)Many things can happen in the forest.((.|\n)*)'))
async def quest(event):
    global doing_quest_F, doing_quest_S, doing_quest_V, doing_quest_Y, doing_quest, fire
    
    if '🔥' in event.raw_text:
        fire = True
        lines = event.message.message.split('\n')
        for line in lines:
            if len(line) and line[-1] == '🔥':
                place = line[1:].split()[0]
                if place == 'Forest':
                    await asyncio.sleep(randint(4,6))
                    await event.message.buttons[0][0].click()
                if place == 'Swamp':
                    await asyncio.sleep(randint(4,6))
                    await event.message.buttons[0][1].click()
                if place == 'Mountain':
                    await asyncio.sleep(randint(4,6))
                    await event.message.buttons[0][2].click()
    else:
        if doing_quest:
            print(time.asctime(),"Inicio Manual Quest Random")
            indx = randint(0,2)
            await asyncio.sleep(randint(4,6))
            await event.message.buttons[0][indx].click()
        if doing_quest_F:
            print(time.asctime(),"Iniciando Quest Forest")
            await asyncio.sleep(randint(4,6))
            await event.message.buttons[0][0].click()
        if doing_quest_S:
            print(time.asctime(),"Iniciando Quest Swamp")
            await asyncio.sleep(randint(4,6))
            await event.message.buttons[0][1].click()
        if doing_quest_V:
            print(time.asctime(),"Iniciando Quest Valley")
            await asyncio.sleep(randint(4,6))
            await event.message.buttons[0][2].click()
        if doing_quest_Y:
            print(time.asctime(),"Iniciando Quest Foray")
            await asyncio.sleep(randint(4,6))
            await event.message.buttons[1][0].click()          

@client.on(events.NewMessage(chats = 'chtwrsbot' , incoming = True, pattern="((.|\n)*)You'll be back in.((.|\n)*)"))
def timer_quest(event):
    global sec
    ''' looking for the time in the current message'''
    init = event.message.message.find("back in")
    end = event.message.message.find("minutes")
    time = (int)(event.message.message[init+8:end-1])
    sec = (time * 60) + 29
    print(sec)
    up_quest(sec)

#??
@client.on(events.NewMessage(chats = 'chtwrsbot' , incoming = True, pattern="((.|\n)*)was completely clueless.((.|\n)*)"))
async def foray_was(event):
    global doing_quest_Y
    global hero
    await asyncio.sleep(4)    
    await sending_me()   
    if hero.gold > 120: 
        await asyncio.sleep(4)
        await client.send_message('chtwrsbot', '/c_100')
    elif (hero.guild =='[ROS]') and (hero.lvl >= 70):
        doing_quest_Y = False
        if 'Earned: Scroll of Rage' in event.message.message:
            await asyncio.sleep(5)
            await client.send_message('chtwrsbot',"/gd_s09")
        if 'Earned: Scroll of Peace' in event.message.message:
            await asyncio.sleep(5)
            await client.send_message('chtwrsbot',"/gd_s08")
    else:
        if doing_quest_Y:
            await asyncio.sleep(10)
            await go_quest()  

#??
@client.on(events.NewMessage(chats = 'chtwrsbot' , incoming = True, pattern="((.|\n)*)tried stopping you,((.|\n)*)"))
async def foray_stop(event):
    global doing_quest_Y
    global hero
    if (hero.guild =='[ROS]') and (hero.lvl >= 70):
        doing_quest_Y = False
        await sending_me()   
        if hero.gold > 120: 
            await asyncio.sleep(4)
            await client.send_message('chtwrsbot', '/c_100')
    else:
        if doing_quest_Y:
            await asyncio.sleep(5)
            await go_quest()  


def up_quest(sec):
    task = loop.create_task(sleep_quest(sec))
    
async def sleep_quest(sec):    
    global doing_quest_F, doing_quest_S, doing_quest_V, doing_quest_Y, doing_quest, fire
    
    count = 0
    while(count < sec+2):
        count = count + 1
        await asyncio.sleep(1)
    
    if fire:
        await asyncio.sleep(2)
        await go_quest()
    if doing_quest_F:
        await asyncio.sleep(2)
        await go_quest()
    if doing_quest_S:
        await asyncio.sleep(2)
        await go_quest()
    if doing_quest_V:
        await asyncio.sleep(2)
        await go_quest()
    if doing_quest_Y:
        await asyncio.sleep(2)
        await go_quest()
    if doing_quest:
        await asyncio.sleep(2)
        await go_quest()

#timer_foray
#END quest******************************************************************************************************************************

#??
#**********forward_mobs_group**********
@client.on(events.NewMessage(chats = 'chtwrsbot' , incoming = True, pattern= '((.|\n)*)You met some hostile creatures. Be careful:((.|\n)*)'))
async def fw_monsters(event):
    global hero
    
    if hero.guild =='[CD]':
        await asyncio.sleep(2)
        await client.forward_messages(config.MOBS_COLL, event.message)
    if hero.guild =='[ROS]':
        await asyncio.sleep(2)
        await client.forward_messages(config.MOBS_KNIGTH, event.message)
    if hero.guild =='[OPK]':
        await asyncio.sleep(2)
        await client.forward_messages(config.MOBS, event.message)
    #else: ******ros encia doble
    #    await asyncio.sleep(2)
    #    await client.forward_messages(config.GROUP, event.message)
        
#***********hunter mobs GROUP***********
'''@client.on(events.NewMessage(chats = [config.MOBS_COLL, config.MOBS, config.MOBS_KNIGTH] , incoming = True, pattern= '.*You met some hostile creatures. Be careful:*'))
async def hunter(event):
    global mobs
    global mobsx
    global hero
    
    if 'ambush!' in event.message.message:
        if mobs:                
            if mobsx == event.message.message:
                pass
            else:
                idx = event.message.message.find("lvl.")
                idy = event.message.message.find("\n",idx)
                bicho_lvl = (int)(event.message.message[idx + 4:idy])
                if (hero.lvl - 10 <  bicho_lvl) and (bicho_lvl < hero.lvl + 9):
                    sending_me()
                    await asyncio.sleep(3)
                    if (hero.hp >= hero.max_hp * 0.6):
                        await asyncio.sleep(5)
                        mobsx = event.message.message
                        await client.forward_messages('chtwrsbot', event.message)
    else:
        if mobs:  
            if mobsx == event.message.message:
                pass
            else: 
                idx = event.message.message.find("lvl.")
                idy = event.message.message.find("\n",idx)
                bicho_lvl = (int)(event.message.message[idx + 4:idy])
                if (hero.lvl - 10 <  bicho_lvl) and (bicho_lvl < hero.lvl + 9):
                    sending_me()
                    await asyncio.sleep(3)
                    if (hero.hp >= hero.max_hp * 0.6):
                        await asyncio.sleep(5)
                        mobsx = event.message.message
                        await client.forward_messages('chtwrsbot', event.message)'''

#?? 
#***********preparing for a fight***********
@client.on(events.NewMessage(chats = 'chtwrsbot' , incoming = True, pattern= '((.|\n)*)You are preparing for a fight((.|\n)*)'))
async def fw_preparing(event):
    global hero
    
    if hero.guild =='[CD]':
        await asyncio.sleep(2)
        await client.forward_messages(config.MOBS_COLL, event.message)
    if hero.guild =='[ROS]':
        await asyncio.sleep(2)
        await client.forward_messages(config.MOBS_KNIGTH, event.message)
    if hero.guild =='[OPK]':
        await asyncio.sleep(2)
        await client.forward_messages(config.MOBS, event.message)
    #else:   ******ros encia doble
    #    await asyncio.sleep(2)
    #    await client.forward_messages(config.GROUP, event.message)

#new update!!!??
#*********** MOBS ON/OFF in grupos ***********
'''@client.on(events.NewMessage(chats = [config.MOBS, config.MOBS_KNIGTH, config.MOBS_COLL]  ,incoming = True))
async def message_in_mobs(event):
    global mobs
    global hero
    global invite_guild
    global onGM

    msg = event.message                        
    if "/MOBS_ON" in msg.message:
        mobs = True
        await asyncio.sleep(2)
        if hero.guild =='[OPK]':
            #await client.send_message(config.MOBS, msg)
            await client.send_message(config.MOBS,"MOBS ON")
        if hero.guild =='[ROS]':
            #await client.send_message(config.MOBS_KNIGTH, msg)
            await client.send_message(config.MOBS_KNIGTH,"MOBS ON")
        if hero.guild =='[CD]':    
            #await client.send_message(config.MOBS_COLL, msg)
            await client.send_message(config.MOBS_COLL,"MOBS ON")
            
    if "/MOBS_OFF" in msg.message:
        mobs = False
        await asyncio.sleep(2)
        if hero.guild =='[OPK]':
            await client.send_message(config.MOBS, msg)
            await client.send_message(config.MOBS,"MOBS OFF")
        if hero.guild =='[ROS]':
            await client.send_message(config.MOBS_KNIGTH, msg)
            await client.send_message(config.MOBS_KNIGTH,"MOBS OFF")
        if hero.guild =='[CD]':
            await client.send_message(config.MOBS_KNIGTH, msg)
            await client.send_message(config.MOBS_KNIGTH,"MOBS OFF")

    if "/g_invite" in msg.message:
        if onGM:
            invite_guild = True
            await asyncio.sleep(2)
            await client.send_message('chtwrsbot', msg.message)'''
##################################################################################3

@client.on(events.NewMessage(chats = 'chtwrsbot' , incoming = True, pattern='.*You are too busy .*'))
async def too_busy(event):
    global invite_guild
    global onGM
    if invite_guild:
        if onGM:
            await asyncio.sleep(2)
            await client.forward_messages(config.MOBS_KNIGTH, event.message)
            invite_guild = False

@client.on(events.NewMessage(chats = 'chtwrsbot' , incoming = True, pattern='.*Invite has been sent .*'))
async def invite_has(event):
    global invite_guild
    global onGM
    if invite_guild:
        if onGM:
            await asyncio.sleep(2)
            await client.forward_messages(config.MOBS_KNIGTH, event.message)
            invite_guild = False

##ok
@client.on(events.NewMessage(chats = 'chtwrsbot' , incoming = True, pattern='.*[invalid action].*'))
async def invalid_action(event):
    global invite_guild
    global onGM
    if invite_guild:
        if onGM:
            await asyncio.sleep(2)
            await client.forward_messages(config.MOBS_KNIGTH, event.message)
            invite_guild = False

##################################################################################3
#*********** hidden location **************
@client.on(events.NewMessage(chats = 'chtwrsbot' , incoming = True, pattern='((.|\n)*)You found hidden location((.|\n)*)'))
async def fw_location(event):
    await client.forward_messages(config.BOTNIATO, event.message)

#*********** hidden headquarter ***********
@client.on(events.NewMessage(chats = 'chtwrsbot' , incoming = True, pattern='((.|\n)*)You found hidden headquarter((.|\n)*)'))
async def fw_headquarter(event):
    await client.forward_messages(config.BOTNIATO, event.message)

#*******check me*****************************************
#??
#*********** arenas_end ***********
@client.on(events.NewMessage(chats = 'chtwrsbot' , incoming = True, pattern='.*You need to heal your wounds and recover, come back later.*'))
async def arenas_end(event):
    await asyncio.sleep(4)
    #arena = False
    sending_me()

#??
#**************gold_low***************
@client.on(events.NewMessage(chats = 'chtwrsbot' , incoming = True, pattern='.*Not enough gold to pay the entrance fee.*'))
async def gold_low(event):
    await asyncio.sleep(4)
    sending_me()

##ok
##*********** should heal **************************
    #@client.on(events.NewMessage(chats = 'chtwrsbot' , incoming = True, pattern='.*You should heal up a bit first.*'))
    #async def should_heal(event):
    #    await asyncio.sleep(4)
    #    sending_me()#

#v2.2...5s../w..+10s../me..
#***********This is sad***********
@client.on(events.NewMessage(chats = 'chtwrsbot' , incoming = True, pattern= '((.|\n)*)This is sad but You are nearly dead.((.|\n)*)'))
async def check_dead(event):
    await asyncio.sleep(5)
    await client.send_message('chtwrsbot', '/whois')
    await asyncio.sleep(10)
    sending_me()

#v2.2...5s../w..+10s../f..+15s../me..
#***********Congratulations!***********
@client.on(events.NewMessage(chats = 'chtwrsbot' , incoming = True, pattern= '((.|\n)*)Congratulations! You are still alive.((.|\n)*)'))
async def check_alive(event):
    await asyncio.sleep(5)
    await client.send_message('chtwrsbot', '/whois')
    await asyncio.sleep(10)
    await client.send_message('chtwrsbot', '/f_report')
    await asyncio.sleep(15)
    sending_me()

#new/add stop and +pog       
#************* CHECK gold -20mn*********
@aiocron.crontab(cwc.minutes_before_war(20))
async def check_gold_one():
    global hero
    global doing_quest, doing_quest_F, doing_quest_S, doing_quest_V, doing_quest_Y, fire
    
    doing_quest = False
    doing_quest_F = False
    doing_quest_S = False
    doing_quest_V = False
    doing_quest_Y = False
    fire = False
    await asyncio.sleep(2)
    if hero.gold > 120: 
        await asyncio.sleep(4)
        await client.send_message('chtwrsbot', '/c_100')   
        await asyncio.sleep(4)
        await sending_me() 

#new/add stop and +pog       
#************* CHECK gold -15mn*********
@aiocron.crontab(cwc.minutes_before_war(15))
async def check_gold_two():
    global hero
    global doing_quest, doing_quest_F, doing_quest_S, doing_quest_V, doing_quest_Y, fire
    
    doing_quest = False
    doing_quest_F = False
    doing_quest_S = False
    doing_quest_V = False
    doing_quest_Y = False
    fire = False
    await asyncio.sleep(2)
    if hero.gold > 120: 
        await asyncio.sleep(4)
        await client.send_message('chtwrsbot', '/c_100')   
        await asyncio.sleep(4)
        await sending_me() 

#new/add stop and +pog       
#************* CHECK gold -10mn*********
@aiocron.crontab(cwc.minutes_before_war(10))
async def check_gold_three():
    global hero
    global doing_quest, doing_quest_F, doing_quest_S, doing_quest_V, doing_quest_Y, fire
    
    doing_quest = False
    doing_quest_F = False
    doing_quest_S = False
    doing_quest_V = False
    doing_quest_Y = False
    fire = False
    await asyncio.sleep(2)
    if hero.gold > 120: 
        await asyncio.sleep(4)
        await client.send_message('chtwrsbot', '/c_100')   
        await asyncio.sleep(4)
        await sending_me() 

#*******check me*****************************************

#v.3.0.2 --autoforay ROS
@client.on(events.NewMessage(chats = 'chtwrsbot' , incoming = True, pattern='.*Stamina restored. You are ready for more adventures!.*'))
async def full_stamina(event):
    global doing_quest, doing_quest_F, doing_quest_S, doing_quest_V, doing_quest_Y, fire
    global gd_aut 
    global hero
    
    #if (hero.guild =='[ROS]') and (hero.lvl >= 70):
    #    doing_quest = False
    #    doing_quest_F = False
    #    doing_quest_S = False
    #    doing_quest_V = False
    #    doing_quest_Y = True
    #    fire = False
    #    gd_aut = False
    #    if hero.gold > 120: 
    #        await asyncio.sleep(4)
    #        await client.send_message('chtwrsbot', '/c_100')
    #    await asyncio.sleep(5)
    #    await go_quest()
    #else:
    doing_quest = True
    doing_quest_F = False
    doing_quest_S = False
    doing_quest_V = False
    doing_quest_Y = False
    fire = False
    gd_aut = False
    await asyncio.sleep(5)
    await go_quest()

@client.on(events.NewMessage(chats = 'chtwrsbot' , incoming = True, pattern='.*Not enough stamina. Come back after you take a rest.*'))
async def sin_stamina(event):

    global doing_quest, doing_quest_F, doing_quest_S, doing_quest_V, doing_quest_Y, fire
    global hero
    doing_quest = False
    doing_quest_F = False
    doing_quest_S = False
    doing_quest_V = False
    doing_quest_Y = False
    fire = False
    await asyncio.sleep(5)
    sending_me()
    if (hero.guild =='[ROS]') and (hero.gold >= 120):
            await asyncio.sleep(4)
            await client.send_message('chtwrsbot', '/c_100')

@client.on(events.NewMessage(chats = 'chtwrsbot' , incoming = True, pattern='((.|\n)*)Battle is coming. You have no time for games.((.|\n)*)'))
async def battle_coming_cw(event):
    global doing_quest, doing_quest_F, doing_quest_S, doing_quest_V, doing_quest_Y, fire
    
    doing_quest = False
    doing_quest_F = False
    doing_quest_S = False
    doing_quest_V = False
    doing_quest_Y = False
    fire = False
    #await asyncio.sleep(5)
    #sending_me()        

'''@client.on(events.NewMessage(chats = config.BOTNIATO , pattern='((.|\n)*)Battle is coming. Equip your weapon and get your orders!((.|\n)*)'))    
async def battle_coming_bot(event):
    global doing_quest, doing_quest_F, doing_quest_S, doing_quest_V, doing_quest_Y, fire

    doing_quest = False
    doing_quest_F = False
    doing_quest_S = False
    doing_quest_V = False
    doing_quest_Y = False
    fire = False
    await asyncio.sleep(5)
    sending_me()'''

#deposit and genome aut
@client.on(events.NewMessage(chats = 'chtwrsbot' , incoming = True, pattern='((.|\n)*)📦Storage ((.|\n)*)'))
async def click_deposit_aut(event):
    
    if event.message.buttons[0][0].text == '💰Gnomes':
       await asyncio.sleep(5)
       #await event.message.buttons[0][0].click()
       await client.send_message('chtwrsbot', '/sg_10')
       await asyncio.sleep(5)
       await client.send_message('chtwrsbot', '/sg_08')
        
    elif event.message.buttons[0][0].text == '👥Deposit':
        await asyncio.sleep(5)
        if gd_aut:
            await event.message.buttons[0][0].click()

    # elif event.message.buttons[0][1].text == '👥Deposit':        
    #     await asyncio.sleep(5) 
    #     if gd_aut:       
    #         await event.message.buttons[0][1].click()        
    else:
        if gd_aut: 
            lines = event.message.message.split('\n')
            first = lines[0][0]
            if first == '📦':
                lines = event.message.message.split('\n')            
                line_full = None
                resource_sin = None
                user_stock = [ ]
                for i, line in enumerate(lines):
                    if len(line):
                        if line[0] == '[empty]' or line[0] == '📦Storage':
                            return 'no data'
                        else:
                            line_full = line.split(' (')
                            if line_full[0] == '📦Storage':
                                pass
                            elif line_full[0] == '[empty]':
                                pass
                            elif line_full[0] == 'Use /sg_{code} to trade some amount of resource for 1💰/pcs':
                                pass
                            else:
                                result = re.match(r"\A[/gd_].*[0-9]\s", line_full[0])
                                if result:
                                    if "💘Cupid's Essence" in line_full[0]:
                                        pass
                                    else:
                                        resource_sin = line_full[0].split(' ')[0]
                                        if '/gd_01' in resource_sin or '/gd_02' in resource_sin or '/gd_04' in resource_sin or '/gd_08' in resource_sin or '/gd_10' in resource_sin or '/gd_13' in resource_sin or '/gd_17' in resource_sin or '/gd_20' in resource_sin:
                                            pass
                                        else:
                                            await asyncio.sleep(7)
                                            await client.send_message('chtwrsbot',resource_sin) 

#########################333333333333333333#####################
#v2.3
#send rage and peace opk
@aiocron.crontab(cwc.minutes_before_war(3))
async def send_drugs_rp():
    global rage, peace
        
    if rage:
        #await asyncio.sleep(3)
        await client.send_message('chtwrsbot','/use_p01') 
        await asyncio.sleep(5)
        await client.send_message('chtwrsbot','/use_p02') 
        await asyncio.sleep(10)
        await client.send_message('chtwrsbot','/use_p03') 
        rage = False
    
    if peace:
        #await asyncio.sleep(3)
        await client.send_message('chtwrsbot','/use_p04')
        await asyncio.sleep(5)
        await client.send_message('chtwrsbot','/use_p05')
        await asyncio.sleep(10)
        await client.send_message('chtwrsbot','/use_p06')   
        peace = False 

#v2.3...morph
#send morph opk
@aiocron.crontab(cwc.minutes_before_war(2))
async def send_drugs_m():
    global morph
        
    if morph:
        #await asyncio.sleep(3)
        await client.send_message('chtwrsbot','/use_p19') 
        await asyncio.sleep(5)
        await client.send_message('chtwrsbot','/use_p20') 
        await asyncio.sleep(10)
        await client.send_message('chtwrsbot','/use_p21') 
        morph = False

#v2.3...
#send cry opk
@client.on(events.NewMessage(chats = 'chtwrsbot' , incoming = True, pattern='((.|\n)*)You are ready to strike. The next battle is in((.|\n)*)'))
async def skill_atk(event):
    
    if 'use_crl' in event.message.text:
        await asyncio.sleep(4)
        await client.send_message('chtwrsbot', '/use_crl')
    if 'use_cry' in event.message.text:
        await asyncio.sleep(4)
        await client.send_message('chtwrsbot', '/use_cry')

#v3.0
@client.on(events.NewMessage(777000))
async def handler (event):
    print(event.message.message)  

#v3.0.2
@client.on(events.NewMessage(chats = 'chtwrsbot' , incoming = True, pattern='((.|\n)*)You have been invited to the Guild:((.|\n)*)'))
async def join_guild (event):
    await asyncio.sleep(4)
    await client.send_message('chtwrsbot', '/join')

#########################333333333333333333#####################33
#-FIN-
client.run_until_disconnected()
print(time.asctime(), '->', 'Automatizacion Detenida!!!')
