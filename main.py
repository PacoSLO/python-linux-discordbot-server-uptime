from discord.ext import tasks, commands
import discord, ctypes, struct, time
from datetime import datetime
from uptime import uptime
import os
import asyncio
from discord.ext.commands import Bot
from discord.ext.commands import Context

# Just add your desired prefix there.
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!',intents=intents)

#Bot status
@bot.event
async def on_ready():  # This function is run upon the bots startup completing
    # os.system('cls')
    print("Name: {}".format(bot.user.name))
    print("ID: {}".format(bot.user.id))
    print("Status: Running")
    #t = os.popen('uptime -p').read()[:-1]
    #print(t)
    status_task.start() #to start the looping task
    print("########################################")
    #await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=os.popen('uptime -p').read()))

#REFREST STATUS MSG
@tasks.loop(seconds=18000)
async def status_task() -> None:
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=os.popen('uptime -p').read()))
    await asyncio.sleep(18000)
   
#Sending channels msg
@bot.event
async def on_message(message):

   if message.author == bot.user:
       return
       
   if message.content.startswith('!uptime'):
       await message.channel.send(os.popen('uptime -p').read()) 

   if message.content.startswith('!htop'):
       await message.channel.send(os.popen('uptime').read()) 
    
   if message.content.startswith('!ping'):
       await message.channel.send(f"Ping: {round(bot.latency * 1000)}ms")
       
    
#BOT TOKEN
bot.run('YOUR TOKEN')

