import os
import base64
import pyperclip
import discord
import random
import re
from discord.ext import commands
from colorama import Fore
from tqdm import tqdm, trange
from time import sleep

def clear(): return os.system('cls') if os.name == 'nt' else os.system('clear')
os.system(f'mode 140,60')

clear()
token = ('add your oauth token here')
            

class counter(discord.Client):
    async def on_ready(self):
        clear()
        os.system(f'title Val AFK Counter | Logged into: {self.user}')
        print(f""" \u001b[43m

██╗   ██╗ █████╗ ██╗     
██║   ██║██╔══██╗██║     
██║   ██║███████║██║     
╚██╗ ██╔╝██╔══██║██║     
 ╚████╔╝ ██║  ██║███████╗
  ╚═══╝  ╚═╝  ╚═╝╚══════╝
               """)

    async def on_message(self, x):
        regex = re.findall(r'<@!?([0-9]+)>', x.content)
        if regex and 'afk' in x.content.lower() and x.author == self.user:
            for i in range(2, 10001):
                await x.channel.send(i)


client = counter()
client.run(token, bot=False)
