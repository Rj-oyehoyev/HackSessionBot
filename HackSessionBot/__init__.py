import os
import asyncio
import logging
from config import Config
from pyrogram import Client
from rich.console import Console
from rich.table import Table
from HackSessionBot.Helpers.data import LOG_TEXT
from pyromod import listen 

#getting variables
API_ID = Config.API_ID
API_HASH = Config.API_HASH
TOKEN = Config.TOKEN
START_PIC = Config.START_PIC



if not START_PIC:
    START_PIC = "https://telegra.ph//file/a9a90059ae47fa840b0b3.jpg"

#rich
LOG = Console()

#logger
logging.basicConfig(level=logging.INFO)

#client
app = Client(
    "SupremeStark",
    api_id = API_ID,
    api_hash = API_HASH,
    bot_token = TOKEN )
    


async def HackSessionBot():
    os.system("clear")
    header = Table(show_header=True, header_style="bold green")
    header.add_column(LOG_TEXT)
    LOG.print(header)
    LOG.print(f"[bold cyan]πππππππ β₯οΈπΎπ‘οΈποΈποΈπΎ...")
    LOG.print("[bold yellow]sα΄α΄Κα΄ΙͺΙ΄Ι’ Κα΄α΄Κ Κα΄α΄ Ι΄α΄α΄‘.......")
    await app.start()    
    


loop = asyncio.get_event_loop()
loop.run_until_complete(HackSessionBot())    



    
    

    
    



