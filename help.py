import discord
from discord.ext import commands, tasks
from discord_webhook import DiscordEmbed, DiscordWebhook
from itertools import cycle
import json
import os
from pprint import pprint
from discord_webhook import DiscordEmbed, DiscordWebhook
from bs4 import BeautifulSoup as bs
import requests
import platform
import sys
import random, ast
import xml.etree.ElementTree as ET
from urllib.request import urlopen
import xmltodict
from datetime import datetime
import aiohttp
from colorama import Fore, Back, Style, init
from discord.ext.commands import CommandNotFound


bot = commands.Bot(command_prefix = '?', help_command=None)
bottoken ="Nzk4NTY2ODE4ODEzMDUwOTYw.X_25Tg.Fgr9xvAtE0qkJnmHL_dz4gZ3ofw"

setembedcolor = 0
setfooterimage = "https://media.discordapp.net/attachments/460974692073734164/680067025493950474/Wcu7EAAAAASUVORK5CYII.png"
setfootertext = "@ScriptingTools |"

init(autoreset=True)

def check_if_it_is_me(ctx):
	return ctx.message.author.id == 175953718750085121 or ctx.message.author.id == 351639955531104258 

@bot.command()
@commands.check(check_if_it_is_me)
async def staffhelp(context):
	embed=discord.Embed(title="Snipes - Add Product Help", color=setembedcolor)
	embed.add_field(name="Command Format - ?snipesadd", value="```?snipesadd\nprice\nproductName\nimage\nsku\nAll PIDS\nALL SIZES```", inline=False)
	embed.add_field(name="Example - ?snipesadd", value="```?snipesadd\n99,99 €\nDunk High Retro\nhttps://www.snipes.at/dw/image/v2/BDCB_PRD/on/demandware.static/-/Sites-snse-master-eu/default/dwc5049674/1899784_P.jpg?sw=450&sh=450&sm=fit&sfrm=png\nCV12344-123\n0001380189978400000001\n0001380189978400000002\n0001380189978400000002\n41\n42\n42.5```", inline=False)
	embed.add_field(name="Command Format - ?snipesdelete", value="```?snipesdelete\nAll PIDS```", inline=False)
	embed.add_field(name="Example - ?snipesdelete", value="```?snipesdelete\n000138018952400000006\n000138018952400000007```", inline=False)
	embed.add_field(name="Command Format - ?checksnipes", value="```?checksnipes\nAll PIDS```", inline=False)
	embed.add_field(name="Example - ?checksnipes", value="```?checksnipes\n000138018952400000006\n000138018952400000007```", inline=False)
	embed.add_field(name="Command Format - FTL - ?release", value="?release <FTL Link>")
	embed.add_field(name="Information", value="""*Change "snipes" with solebox or onygo to use the other commands for selected store*""" , inline=False)
	embed.set_footer(text=setfootertext + ' Snipes Scraper', icon_url=setfooterimage)
	await context.send(embed=embed)

@bot.command()
async def help(context):
	embed=discord.Embed(title="All commands", color=setembedcolor)
	embed.add_field(name="Mesh Tracker  <:hawkoos:807792754260181023> <:mbotoos:807792807326253077>", value="?orderhelp\n?orderstore\n\n?order <store> <postcode>\n<ordernr>\n\n?orderbulk <store> <postcode>\n<ordernr>\n<ordernr>", inline=False)
	embed.add_field(name="Mesh QT / Scraper  <:hawkoos:807792754260181023> <:mbotoos:807792807326253077>", value="?meshhelp\n?mesh <full link here>\n?mesh <meshpid>\n?qt <store> <PIDs/SKUs>\n?meshcountries", inline=False)
	embed.add_field(name="UPS Tracker  <:UPS:808299085496713257>", value="?upshelp\n\n?ups\n<Tracking NR. 1>\n<Tracking NR. 2>\n<Tracking NR. 3>\n\n?upsbulk\n<Tracking NR. 1>\n<Tracking NR. 2>\n<Tracking NR. 3>", inline=False)
	embed.add_field(name="UPS Tracker  105+ Nrs. or 26+ Links<:UPS:808299085496713257>", value="?upshelp\n\n?upsbulk\ntext\n<paste all ordernrs. discord creates message.txt>", inline=False)
	embed.add_field(name="Footlocker / Side-Step Stock Checker  <:ftl:809892922387595314> <:sidestep:809894025636216902>", value="?ftlhelp\n?stock <link>\n?side <link>\n?ftlcountries\n", inline=False)
	embed.add_field(name="Zalando Stock / PID Scraper inkl. Bot Format  <:zalando:809893400718737508>", value="?zalandohelp\n?zalando <full link here>\n?zalandopid <full link here>", inline=False)
	embed.add_field(name="Restocks Price Checker  <:restocks:809892862400921640>", value="?restocks <shoename>", inline=False)
	embed.add_field(name="StockX Price Checker  <:stockx:810352884608532531>", value="?stockx <shoename>", inline=False)
	embed.add_field(name="Nike Early Link <:nike:809892892654305300>", value="?nikehelp\nSupported Countries: CH, CA, AU, RU, SG\n?nike <full link here>", inline=False)
	embed.set_thumbnail(url=setfooterimage)
	embed.set_footer(text=setfootertext + ' All Commands', icon_url=setfooterimage)
	await context.send(embed=embed)


bot.run(bottoken)
