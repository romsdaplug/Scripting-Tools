import discord
from discord.ext import commands, tasks
from discord_webhook import DiscordEmbed, DiscordWebhook
from itertools import cycle
import json
import os
from pprint import pprint
from discord_webhook import DiscordEmbed, DiscordWebhook
from bs4 import BeautifulSoup as bs
import re
import requests
import platform
import sys
import random, ast
from discord.ext.commands import CommandNotFound,MissingRequiredArgument
from datetime import datetime
from colorama import Fore, Back, Style, init

bot = commands.Bot(command_prefix = '?', help_command=None)
bottoken = "YOUR_DISCORD_BOT_TOKEN"

@bot.event
async def on_ready():
	print('Bot is ready.')
	pass


def check_if_it_is_me(ctx):
    return ctx.message.author.id == 351639955531104258 or ctx.message.author.id == 272815177659842561 or ctx.message.author.id == 175953718750085121 or ctx.message.author.id == 690309758791450634 or ctx.message.author.id == 552991640978063371

setfootertextmesh = "@ScriptingToolsPublic | <?meshhelp>"
setfooterimage = "https://images-ext-1.discordapp.net/external/atwFnJRaXHB0ebXrVSPjVWDXe5hL2OQ0JBWopjGcVCY/https/images-ext-2.discordapp.net/external/gGrbK8FUkmby_Ao8mmH9dZ4RI1cvfkhpUNBlIB46XQE/https/media.discordapp.net/attachments/460974692073734164/680067025493950474/Wcu7EAAAAASUVORK5CYII.png"
setembedcolor = 0x000000

@bot.command()
async def qt(context, store, pid):

	now = datetime.now()
	try:
		server_name = context.guild.name
	except AttributeError:
		server_name = "DM"

	user_name_id = context.author.name + ' ID : ' + str(context.author.id)
	log2 = Fore.CYAN +f'[{server_name}]'
	log3 = Fore.CYAN + f'[{user_name_id}] '
	log = log2 + ' ' + log3

	store = str.lower(store)
	lines = context.message.content.splitlines()
	newpid = ",".join(lines).replace("?qt ","").replace(store,"").replace(" ","")

	if not newpid[0]:
		newpid.pop(0)

	pid = str.lower(pid).replace("\n","").replace(" ","")
	qtpid = lines[0].replace("?qt ","").replace(store,"").replace(" ","")
	if qtpid == "":
		qtpid = lines[1]

	if "." in qtpid:
		pidlink = qtpid.split(".")[0]
	else:
		pidlink = qtpid
	newpidlist = []

	headers = {
		"pragma": "no-cache",
		"cache-control": "no-cache",
		"upgrade-insecure-requests": "1",
		"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36",
		"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
		"sec-fetch-site": "same-origin",
		"sec-fetch-mode": "navigate",
		"sec-fetch-user": "?1",
		"sec-fetch-dest": "document",
		"accept-language": "de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7"
		}

	if store == "fpgb" or store == "footpatrolgb" or store == "footpatroluk" or store == "fpuk" or store == "fpcom" or store == "footpatrolcom":
		store = "footpatrol"
		region = "gb"
		qtstore = "footpatrol"
		qtregion = "com"
		url = "https://www.footpatrol.com/product/pigeon-oos/"
	elif store == "fpde" or store == "footpatrolde":
		store = "footpatrol"
		region = "de"
		qtstore = "footpatrol"
		qtregion = "de"
		url = "https://www.footpatrol.de/product/pigeon-oos/"
	elif store == "fpdk" or store == "footpatroldk":
		store = "footpatrol"
		region = "dk"
		qtstore = "footpatrol"
		qtregion = "dk"
		url = "https://www.footpatrol.dk/product/pigeon-oos/"
	elif store == "fpie" or store == "footpatrolie":
		store = "footpatrol"
		region = "ie"
		qtstore = "footpatrol"
		qtregion = "ie"
		url = "https://www.footpatrol.ie/product/pigeon-oos/"
	elif store == "fpit" or store == "footpatrolit":
		store = "footpatrol"
		region = "it"
		qtstore = "footpatrol"
		qtregion = "it"
		url = "https://www.footpatrol.it/product/pigeon-oos/"
	elif store == "fpnl" or store == "footpatrolnl":
		store = "footpatrol"
		region = "nl"
		qtstore = "footpatrol"
		qtregion = "nl"
		url = "https://www.footpatrol.nl/product/pigeon-oos/"
	elif store == "fpse" or store == "footpatrolse":
		store = "footpatrol"
		region = "se"
		qtstore = "footpatrol"
		qtregion = "se"
		url = "https://www.footpatrol.se/product/pigeon-oos/"
	elif store == "fpfr" or store == "footpatrolfr":
		store = "footpatrol"
		region = "fr"
		qtstore = "footpatrol"
		qtregion = "fr"
		url = "https://www.footpatrol.fr/product/pigeon-oos/"
	elif store == "size" or store == "sz" or store == "sizeuk" or store == "sizegb" or store == "szuk" or store == "szgb":
		store = "size"
		region = ""
		qtstore = ""
		qtregion = ""
		url = "https://www.size.co.uk/product/pigeon-oos/"
	elif store == "sizede" or store == "szde":
		store = "size"
		region = "de"
		qtstore = "size"
		qtregion = "de"
		url = " https://www.sizeofficial." + qtregion + "/product/pigeon-oos/"
	elif store == "sizefr" or store == "szfr":
		store = "size"
		region = "fr"
		qtstore = "size"
		qtregion = "fr"
		url = " https://www.sizeofficial.fr/product/pigeon-oos/"
	elif store == "sizenl" or store == "sznl":
		store = "size"
		region = "nl"
		qtstore = "size"
		qtregion = "nl"
		url = " https://www.sizeofficial." + qtregion + "/product/pigeon-oos/"
	elif store == "sizees" or store == "szes":
		store = "size"
		region = "es"
		qtstore = "size"
		qtregion = "es"
		url = " https://www.sizeofficial." + qtregion + "/product/pigeon-oos/"
	elif store == "sizedk" or store == "szdk":
		store = "size"
		region = "dk"
		qtstore = "size"
		qtregion = "dk"
		url = " https://www.sizeofficial." + qtregion + "/product/pigeon-oos/"
	elif store == "sizeie" or store == "szie":
		store = "size"
		region = "ie"
		qtstore = "size"
		qtregion = "ie"
		url = " https://www.sizeofficial." + qtregion + "/product/pigeon-oos/"
	elif store == "sizese" or store == "szse":
		store = "size"
		region = "se"
		qtstore = "size"
		qtregion = "se"
		url = " https://www.sizeofficial." + qtregion + "/product/pigeon-oos/"
	elif store == "jdgb" or store == "jduk" or store == "jdsports" or store == "jdsportsuk" or store == "jdsportsgb":
		store = "jdsports"
		region = "uk"
		qtstore = ""
		qtregion = ""
		url = "https://www.jdsports.co.uk/product/pigeon-oos/"
	elif store == "jdfr" or store == "jdsportsfr":
		store = "jdsports"
		region = "fr"
		qtstore = "jdsports"
		qtregion = "fr"
		url = "https://www.jdsports." + qtregion + "/product/pigeon-oos/"
	elif store == "jdbe" or store == "jdsportsbe":
		store = "jdsports"
		region = "be"
		qtstore = "jdsports"
		qtregion = "be"
		url = "https://www.jdsports." + qtregion + "/product/pigeon-oos/"
	elif store == "jdde" or store == "jdsportsde":
		store = "jdsports"
		region = "de"
		qtstore = "jdsports"
		qtregion = "de"
	elif store == "jdnl" or store == "jdsportsnl":
		store = "jdsports"
		region = "nl"
		qtstore = "jdsports"
		qtregion = "nl"
		url = "https://www.jdsports." + qtregion + "/product/pigeon-oos/"
	elif store == "jdes" or store == "jdsportses":
		store = "jdsports"
		region = "es"
		qtstore = "jdsports"
		qtregion = "es"
		url = "https://www.jdsports." + qtregion + "/product/pigeon-oos/"
	elif store == "jdit" or store == "jdsportsit":
		store = "jdsports"
		region = "it"
		qtstore = "jdsports"
		qtregion = "it"
		url = "https://www.jdsports." + qtregion + "/product/pigeon-oos/"
	elif store == "jdat" or store == "jdsportsat":
		store = "jdsports"
		region = "at"
		qtstore = "jdsports"
		qtregion = "at"
		url = "https://www.jdsports." + qtregion + "/product/pigeon-oos/"
	elif store == "jddk" or store == "jdsportsdk":
		store = "jdsports"
		region = "dk"
		qtstore = "jdsports"
		qtregion = "dk"
		url = "https://www.jdsports." + qtregion + "/product/pigeon-oos/"
	elif store == "jdie" or store == "jdsportsie":
		store = "jdsports"
		region = "ie"
		qtstore = "jdsports"
		qtregion = "ie"
		url = "https://www.jdsports." + qtregion + "/product/pigeon-oos/"
	elif store == "jdauf" or store == "jdsportsauf" or store == "jdsportsau" or store == "jdau":
		store = "jdsports"
		region = "au"
		qtstore = "jdsports"
		qtregion = "au"
		url = "https://www.jdsports." + qtregion + "/product/pigeon-oos/"
	elif store == "jdsg" or store == "jdsportssg":
		store = "jdsports"
		region = "sg"
		qtstore = "jdsports"
		qtregion = "sg"
		url = "https://www.jdsports." + qtregion + "/product/pigeon-oos/"
	elif store == "jdpt" or store == "jdsportspt":
		store = "jdsports"
		region = "pt"
		qtstore = "jdsports"
		qtregion = "pt"
		url = "https://www.jdsports." + qtregion + "/product/pigeon-oos/"
	elif store == "jdjx" or store == "jdsportsjx" or store == "jdsportsglobal" or store == "jdglobal":
		store = "jdsports"
		region = "jx"
		qtstore = "jdsports"
		qtregion = "jx"
		url = "https://www.jdsports." + qtregion + "/product/pigeon-oos/"
	elif store == "jdmy" or store == "jdsportsmy":
		store = "jdsports"
		region = "my"
		qtstore = "jdsports"
		qtregion = "my"
		url = "https://www.jdsports." + qtregion + "/product/pigeon-oos/"
	elif store == "jdth" or store == "jdsportsth":
		store = "jdsports"
		region = "th"
		qtstore = "jdsports"
		qtregion = "th"
		url = "https://www.jdsports.co." + qtregion + "/product/pigeon-oos/"


	if store == "fpgb" or store == "footpatrolgb" or store == "footpatrol" or store == "fpcom" or store == "footpatrolcom" or store == "footpatroluk" or store == "fpuk" or store == "fpde" or store == "footpatrolde" or store == "fpfr" or store == "footpatrolfr" or store == "size" or store == "sz" or store == "sizeuk" or store == "sizegb" or store == "szuk" or store == "szgb" or store == "sizede" or store == "szde" or store == "sizefr" or store == "szfr" or store == "sizenl" or store == "sznl" or store == "sizees" or store == "szes" or store == "sizedk" or store == "szdk" or store == "sizeie" or store == "szie" or store == "sizese" or store == "szse" or store == "jdfr" or store == "jdsportsfr" or store == "jdgb" or store == "jduk" or store == "jdsports" or store == "jdsportsuk" or store == "jdsportsgb" or store == "jdbe" or store == "jdsportsbe" or store == "jdde" or store == "jdsportsde" or store == "jdnl" or store == "jdsportsnl" or store == "jdes" or store == "jdsportses" or store == "jdit" or store == "jdsportsit" or store == "jdat" or store == "jdsportsat" or store == "jddk" or store == "jdsportsdk" or store == "jdie" or store == "jdsportsie" or store == "jdauf" or store == "jdsportsauf" or store == "jdsportsau" or store == "jdau" or store == "jdsg" or store == "jdsportssg" or store == "jdpt" or store == "jdsportspt" or store == "jdjx" or store == "jdsportsjx" or store == "jdsportsglobal" or store == "jdglobal" or store == "jdmy" or store == "jdsportsmy" or store == "jdth" or store == "jdsportsth":
		if qtstore == "" :
			underline = ""
		else:
			underline = "_"
		try:
			if pid[6] == ".":
				pidlist = newpid.split(",")
				if not pidlist[0]:
						pidlist.pop(0)
				for i in range(len(pidlist)):
					singlepid = pidlist[i]
					pid2 = singlepid.split(".",1)[1]
					newpidlist.append(singlepid[:6] + underline + qtstore + qtregion + "." + pid2)
					finalpidlist = ",".join(newpidlist)
			elif pid[8] == ".":
				pidlist = newpid.split(",")
				if not pidlist[0]:
						pidlist.pop(0)
				for i in range(len(pidlist)):
					singlepid = pidlist[i]
					pid2 = singlepid.split(".",1)[1]
					newpidlist.append(singlepid[:8] + underline + qtstore + qtregion + "." + pid2)
					finalpidlist = ",".join(newpidlist)
			elif pid[7] == ".":
				pidlist = newpid.split(",")
				if not pidlist[0]:
						pidlist.pop(0)
				for i in range(len(pidlist)):
					singlepid = pidlist[i]
					pid2 = singlepid.split(".",1)[1]
					newpidlist.append(singlepid[:7] + underline + qtstore + qtregion + "." + pid2)
					finalpidlist = ",".join(newpidlist)
			elif pid[17] == ".":
				pidlist = newpid.split(",")
				if not pidlist[0]:
						pidlist.pop(0)
				for i in range(len(pidlist)):
					singlepid = pidlist[i]
					pid2 = singlepid.split(".",1)[1]
					newpidlist.append(singlepid.split("_")[0] + underline + qtstore + qtregion + "." + pid2)
					finalpidlist = ",".join(newpidlist)
			elif pid[19] == ".":
				pidlist = newpid.split(",")
				if not pidlist[0]:
						pidlist.pop(0)
				for i in range(len(pidlist)):
					singlepid = pidlist[i]
					pid2 = singlepid.split(".",1)[1]
					newpidlist.append(singlepid.split("_")[0] + underline + qtstore + qtregion + "." + pid2)
					finalpidlist = ",".join(newpidlist)
			elif pid[18] == ".":
				pidlist = newpid.split(",")
				if not pidlist[0]:
						pidlist.pop(0)
				for i in range(len(pidlist)):
					singlepid = pidlist[i]
					pid2 = singlepid.split(".",1)[1]
					newpidlist.append(singlepid.split("_")[0] + underline + qtstore + qtregion + "." + pid2)
					finalpidlist = ",".join(newpidlist)
			elif pid[13] == ".":
				pidlist = newpid.split(",")
				if not pidlist[0]:
						pidlist.pop(0)
				for i in range(len(pidlist)):
					singlepid = pidlist[i]
					pid2 = singlepid.split(".",1)[1]
					newpidlist.append(singlepid.split("_")[0] + underline + qtstore + qtregion + "." + pid2)
					finalpidlist = ",".join(newpidlist)
			elif pid[20] == ".":
				pidlist = newpid.split(",")
				if not pidlist[0]:
						pidlist.pop(0)
				for i in range(len(pidlist)):
					singlepid = pidlist[i]
					pid2 = singlepid.split(".",1)[1]
					newpidlist.append(singlepid.split("_")[0] + underline + qtstore + qtregion + "." + pid2)
					finalpidlist = ",".join(newpidlist)
			else:
				finalpidlist = newpid
				pidlist = newpid.split(",")
		except(IndexError):
			if pid.isnumeric():
				if len(pid) == 8:
					pidlist = newpid.split(",")
					if not pidlist[0]:
						pidlist.pop(0)
					for i in range(len(pidlist)):
						newpidlist.append(pidlist[i] + underline + qtstore + qtregion)
						finalpidlist = ",".join(newpidlist)
				elif len(pid) == 6:
					pidlist = newpid.split(",")
					if not pidlist[0]:
						pidlist.pop(0)
					for i in range(len(pidlist)):
						newpidlist.append(pidlist[i] + underline + qtstore + qtregion)
						finalpidlist = ",".join(newpidlist)
			else:
				pidlist = newpid.split(",")
				if not pidlist[0]:
					pidlist.pop(0)
				if "_" in pidlist[0]:
					for i in range(len(pidlist)):
						singlepid = pidlist[i]
						pid2 = singlepid.split(".",1)[1]
						newpidlist.append(singlepid.split("_")[0] + underline + qtstore + qtregion + "." + pid2)
						finalpidlist = ",".join(newpidlist)
				elif "." in pidlist[0]:
					for i in range(len(pidlist)):
						singlepid = pidlist[i]
						pid2 = singlepid.split(".",1)[1]
						newpidlist.append(singlepid.split(".")[0] + underline + qtstore + qtregion + "." + pid2)
						finalpidlist = ",".join(newpidlist)

		allembedlist = "\n".join(newpidlist)
		mbotqt = "https://mbot.app/" + store + region + "/variant/" + finalpidlist
		mbotqt = mbotqt.replace("/" + underline + qtstore + qtregion,("/")).replace("/,","/")
		hawkqt = "https://hawkmesh.com/quicktask/" + store + region+ "/" + finalpidlist
		hawkqt = hawkqt.replace("/" + underline + qtstore + qtregion,("/")).replace("/,","/")
		skuamount = len(newpidlist)
		oosqt = "http://localhost:9099/mesh?store=" + store + region + "&pid=" + finalpidlist + "&amount=" + str(skuamount)
		oosqt = oosqt.replace("/" + underline + qtstore + qtregion,("/")).replace("/,","/")
		embedlink = []
		embedlink.append("place holder")
		embedlink.append("[MBOT QT]("+mbotqt+")")
		embedlink.append("[HAWK QT]("+hawkqt+")")
		embedlink.append("[OOSBot QT]("+oosqt+")")
		embedstore = []
		embedstore.append("place holder")
		embedstore.append(" - MBOT")
		embedstore.append(" - HAWK")
		embedstore.append(" - OOSBot")
		embedemote = []
		embedemote.append("place holder")
		embedemote.append("<:mbotoos:807792807326253077>")
		embedemote.append("<:hawkoos:807792754260181023>")
		embedemote.append("<:oosbot:828748333173440583>")
		print(Fore.MAGENTA + f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] " + log + Fore.GREEN + f"[Creating QT for - {qtpid}][{store}][{qtregion}]")
		try:
			templist = finalpidlist.split(",")
			if "." in templist[0]:
				pidlink = templist[0].split(".")[0]
			else:
				pidlink = templist[0]
			url = url.replace(" ","") + pidlink
			clitext = finalpidlist.split(",")[0]
			response = requests.get(url, headers=headers)
			soup = bs(response.content, 'html.parser')
			shoepic = soup.find("meta", {"property":"og:image"})["content"]
			embed=discord.Embed(title="MESH QT", color=setembedcolor)
			if region == "uk" or region == "":
				region = "gb"
			embed.add_field(name="SKU Amount", value="*" + str(skuamount) + " SKUs loaded*", inline=False)
			embed.add_field(name="SKU", value=allembedlist, inline=False)
			embed.add_field(name=f"HAWK {embedemote[1]}", value="[" + str(embedlink[1]) + "]", inline=True)
			embed.add_field(name=f"MBOT {embedemote[2]}", value="[" + str(embedlink[2]) + "]", inline=True)
			embed.add_field(name=f"OOSBot {embedemote[3]}", value="[" + str(embedlink[3]) + "]", inline=True)
			embed.set_thumbnail(url=shoepic)
			embed.set_footer(text=setfootertextmesh, icon_url=setfooterimage)
			await context.send(embed=embed)
			print(Fore.MAGENTA + f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] " + log + Fore.GREEN + f"[Webhook sent!]")
		except(Exception,TypeError):
			embed=discord.Embed(title="MESH QT", color=setembedcolor)
			embed.add_field(name="SKU Amount", value="*" + str(skuamount) + " SKUs loaded*", inline=False)
			embed.add_field(name="SKU", value=allembedlist, inline=False)

			if region == "uk" or region == "":
				region = "gb"
			embed.add_field(name=f"HAWK {embedemote[1]}", value="[" + str(embedlink[1]) + "]", inline=True)
			embed.add_field(name=f"MBOT {embedemote[2]}", value="[" + str(embedlink[2]) + "]", inline=True)
			embed.add_field(name=f"OOSBot {embedemote[3]}", value="[" + str(embedlink[3]) + "]", inline=True)
			shoepid = finalpidlist.split(",")[0]
			if "," in shoepid:
				shoepid = finalpidlist.split(",")[1]
			if "_" in shoepid:
				shoepid = shoepid.split("_")[0]
			if "." in shoepid:
				shoepid = shoepid.split(".")[0]
			if len(str(shoepid)) <= 6:
				if store == "size":
					picstore = "sz"
				elif store == "footpatrol":
					picstore = "fp"
				elif store == "jdsports":
					picstore = "jd"
				embed.set_thumbnail(url="https://i8.amplience.net/i/jpl/"+ picstore + "_" + shoepid +"_a?qlt=92&w=900&h=637&v=1&fmt=webp")
			embed.set_footer(text=setfootertextmesh, icon_url=setfooterimage)
			await context.send(embed=embed)
			print(Fore.MAGENTA + f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] " + log + Fore.GREEN + f"[Webhook sent!]")
	else:
		embed=discord.Embed(title="Command Error", color=setembedcolor)
		embed.add_field(name="Command Format", value="?qt <store> <PIDs/SKUs>", inline=False)
		embed.set_footer(text=setfootertextmesh, icon_url=setfooterimage)
		await context.send(embed=embed)

@bot.command()
async def region(context, pid):

	now = datetime.now()
	try:
		server_name = context.guild.name
	except AttributeError:
		server_name = "DM"

	user_name_id = context.author.name + ' ID : ' + str(context.author.id)
	log2 = Fore.CYAN +f'[{server_name}]'
	log3 = Fore.CYAN + f'[{user_name_id}] '
	log = log2 + ' ' + log3

	lines = context.message.content.splitlines()
	lines.pop(0)

	uk = []
	de = []
	fr = []
	es = []
	print(Fore.MAGENTA + f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] " + log + Fore.GREEN + f"[Creating Region SKUs for - {lines[0]}]")

	for i in range(len(lines)):

		if "jdsports" in lines[i]:
			uk.append(lines[i].replace(lines[i].split("_")[1].split(".")[0],""))
			de.append(lines[i].replace(lines[i].split("_")[1].split(".")[0],"jdsportsde"))
			fr.append(lines[i].replace(lines[i].split("_")[1].split(".")[0],"jdsportsfr"))
			es.append(lines[i].replace(lines[i].split("_")[1].split(".")[0],"jdsportses"))

		else:
			uk.append(lines[i].replace(".","."))
			de.append(lines[i].replace(".","_jdsportsde."))
			fr.append(lines[i].replace(".","_jdsportsfr."))
			es.append(lines[i].replace(".","_jdsportses."))

	embeduk = "\n".join(uk)
	embedde = "\n".join(de)
	embedfr = "\n".join(fr)
	embedes = "\n".join(es)

	for i in range(4):
		if i == 0:
			embed=discord.Embed(title="Mesh Format :flag_gb:", color=setembedcolor)
			embed.add_field(name="SKU", value=embeduk, inline=False)
			embed.set_footer(text=setfootertextmesh, icon_url=setfooterimage)
			await context.send(embed=embed)

		if i == 1:
			embed=discord.Embed(title="Mesh Format :flag_de:", color=setembedcolor)
			embed.add_field(name="SKU", value=embedde, inline=False)
			embed.set_footer(text=setfootertextmesh, icon_url=setfooterimage)
			await context.send(embed=embed)

		if i == 2:
			embed=discord.Embed(title="Mesh Format :flag_fr:", color=setembedcolor)
			embed.add_field(name="SKU", value=embedfr, inline=False)
			embed.set_footer(text=setfootertextmesh, icon_url=setfooterimage)
			await context.send(embed=embed)

		if i == 3:
			embed=discord.Embed(title="Mesh Format :flag_es:", color=setembedcolor)
			embed.add_field(name="SKU", value=embedes, inline=False)
			embed.set_footer(text=setfootertextmesh, icon_url=setfooterimage)
			await context.send(embed=embed)
	print(Fore.MAGENTA + f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] " + log + Fore.GREEN + f"[Webhook sent!]")


@bot.command()
async def mesh(context, link):

	nopidfound = 0
	now = datetime.now()
	try:
		server_name = context.guild.name
	except AttributeError:
		server_name = "DM"

	user_name_id = context.author.name + ' ID : ' + str(context.author.id)
	log2 = Fore.CYAN +f'[{server_name}]'
	log3 = Fore.CYAN + f'[{user_name_id}] '
	log = log2 + ' ' + log3
	if "." in link and len(link) < 35:
		link = link.split(".")[0]

	link = str.lower(link)

	pid2 = link
	if "." in pid2 and len(pid2) < 35:
		pid2 = pid2.split(".")[0]
	elif len(pid2) > 35:
		pid2 = link
	else:
		pid2 = str.lower(link)

	print(Fore.MAGENTA + f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] " + log + Fore.GREEN + f"[Scraping SKUs of - {pid2}]")

	with open('mesh.json') as json_file:
		data = json.load(json_file)
		for i in range(len(data["MESH"])):            
			for R in range(len(data["MESH"][i])):
				try:
					if pid2 in data["MESH"][i][R]:
						nopidfound = 1
				except (TypeError,KeyError,IndexError) as e:
					continue
	try:
		if "footpatrolcom" in pid2 and len(pid2) < 25:
			url = "https://www.footpatrol.com/product/pigeon-oos/" + pid2
		elif "footpatrolfr" in pid2 and len(pid2) < 25:
			url = "https://www.footpatrol.fr/product/pigeon-oos/" + pid2
		elif "footpatrolfi" in pid2 and len(pid2) < 25:
			url = "https://www.footpatrol.fi/product/pigeon-oos/" + pid2
		elif "footpatrolde" in pid2 and len(pid2) < 25:
			url = "https://www.footpatrol.de/product/pigeon-oos/" + pid2
		elif "footpatroldk" in pid2 and len(pid2) < 25:
			url = "https://www.footpatrol.dk/product/pigeon-oos/" + pid2
		elif "footpatrolit" in pid2 and len(pid2) < 25:
			url = "https://www.footpatrol.it/product/pigeon-oos/" + pid2
		elif "footpatrolnl" in pid2 and len(pid2) < 25:
			url = "https://www.footpatrol.nl/product/pigeon-oos/" + pid2
		elif "footpatrolse" in pid2 and len(pid2) < 25:
			url = "https://www.footpatrol.se/product/pigeon-oos/" + pid2
		elif "footpatrolie" in pid2 and len(pid2) < 25:
			url = "https://www.footpatrol.ie/product/pigeon-oos/" + pid2
		elif "sizeuk" in pid2 and len(pid2) < 25:
			pid2 = pid2.replace("sizeuk","").replace("_","")
			url = "https://www.size.co.uk/product/pigeon-oos/" + pid2
		elif "szuk" in pid2 and len(pid2) < 25:
			pid2 = pid2.replace("szuk","").replace("_","")
			url = "https://www.size.co.uk/product/pigeon-oos/" + pid2
		elif "sizegb" in pid2 and len(pid2) < 25:
			pid2 = pid2.replace("sizegb","").replace("_","")
			url = "https://www.size.co.uk/product/pigeon-oos/" + pid2
		elif "sizede" in pid2 and len(pid2) < 25:
			url = " https://www.sizeofficial.de/product/pigeon-oos/" + pid2
		elif "sizefr" in pid2 and len(pid2) < 25:
			url = " https://www.sizeofficial.fr/product/pigeon-oos/" + pid2
		elif "sizenl" in pid2 and len(pid2) < 25:
			url = " https://www.sizeofficial.nl/product/pigeon-oos/" + pid2
		elif "sizees" in pid2 and len(pid2) < 25:
			url = " https://www.sizeofficial.es/product/pigeon-oos/" + pid2
		elif "sizedk" in pid2 and len(pid2) < 25:
			url = " https://www.sizeofficial.dk/product/pigeon-oos/" + pid2
		elif "sizeie" in pid2 and len(pid2) < 25:
			url = " https://www.sizeofficial.ie/product/pigeon-oos/" + pid2
		elif "sizese" in pid2 and len(pid2) < 25:
			url = " https://www.sizeofficial.se/product/pigeon-oos/" + pid2
		elif "jdsportsgb" in pid2 and len(pid2) < 25:
			url = "https://www.jdsports.co.uk/product/pigeon-oos/" + pid2
		elif "jdsportsuk" in pid2 and len(pid2) < 25:
			pid2 = pid2.replace("jdsportsuk","").replace("_","")
			url = "https://www.jdsports.co.uk/product/pigeon-oos/" + pid2
		elif "jduk" in pid2 and len(pid2) < 25:
			pid2 = pid2.replace("jduk","").replace("_","")
			url = "https://www.jdsports.co.uk/product/pigeon-oos/" + pid2
		elif "jdsportsfr" in pid2 and len(pid2) < 25:
			url = "https://www.jdsports.fr/product/pigeon-oos/" + pid2
		elif "jdsportsbe" in pid2 and len(pid2) < 25:
			url = "https://www.jdsports.be/product/pigeon-oos/" + pid2
		elif "jdsportsde" in pid2 and len(pid2) < 25:
			url = "https://www.jdsports.de/product/pigeon-oos/" + pid2
		elif "jdsportsnl" in pid2 and len(pid2) < 25:
			url = "https://www.jdsports.nl/product/pigeon-oos/" + pid2
		elif "jdsportses" in pid2 and len(pid2) < 25:
			url = "https://www.jdsports.es/product/pigeon-oos/" + pid2
		elif "jdsportsit" in pid2 and len(pid2) < 25:
			url = "https://www.jdsports.it/product/pigeon-oos/" + pid2
		elif "jdsportsat" in pid2 and len(pid2) < 25:
			url = "https://www.jdsports.at/product/pigeon-oos/" + pid2
		elif "jdsportsdk" in pid2 and len(pid2) < 25:
			url = "https://www.jdsports.dk/product/pigeon-oos/" + pid2
		elif "jdsportsie" in pid2 and len(pid2) < 25:
			url = "https://www.jdsports.ie/product/pigeon-oos/" + pid2
		elif "jd-sportscomau" in pid2 and len(pid2) < 25:
			url = "https://www.jdsports.com.au/product/pigeon-oos/" + pid2
		elif "jdsportssg" in pid2 and len(pid2) < 25:
			url = "https://www.jdsports.com.sg/product/pigeon-oos/" + pid2
		elif "jdsportspt" in pid2 and len(pid2) < 25:
			url = "https://www.jdsports.pt/product/pigeon-oos/" + pid2
		elif "jdsportsmy" in pid2 and len(pid2) < 25:
			url = "https://www.jdsports.my/product/pigeon-oos/" + pid2
		elif "jdsportsth" in pid2 and len(pid2) < 25:
			url = "https://www.jdsports.co.th/product/pigeon-oos/" + pid2
		elif "global" in pid2 and len(pid2) < 25:
			pid2 = pid2.replace("global","")
			url = "https://www.global.jdsports.com/product/pigeon-oos/" + pid2

		elif pid2.isnumeric():
			embed=discord.Embed(title="Error Scraping SKUs", color=setembedcolor)
			embed.add_field(name=":flag_gb: SKU Scraper via PID - JDSports", value="Make sure to add `jd, jdsportsuk or jduk` to the end of the pid", inline=False)
			embed.add_field(name=":flag_gb: SKU Scraper via PID - Size?", value="Make sure to add `sz, sizeuk or szuk` to the end of the pid", inline=False)
			embed.set_footer(text=setfootertextmesh, icon_url=setfooterimage)
			await context.send(embed=embed)
		else:
			if link.split('//')[1].split('.')[0] == "m":
				url = link.replace("m","www")
			else:
				url = link
		store = url.split('/www.')[1].split('/')[0]
		store = store.replace(".","")
		if store == "jdsportscoth":
			store = "jdsportsth"

		if store == "footpatrolcom":
			store = "footpatrol"
			region = "gb"
			qtstore = "footpatrol"
			qtregion = "com"
		elif store == "footpatrolfr":
			store = "footpatrol"
			region = "fr"
			qtstore = "footpatrol"
			qtregion = "fr"
		elif store == "footpatrolde":
			store = "footpatrol"
			region = "de"
			qtstore = "footpatrol"
			qtregion = "de"
		elif store == "footpatroldk":
			store = "footpatrol"
			region = "dk"
			qtstore = "footpatrol"
			qtregion = "dk"
		elif store == "footpatrolie":
			store = "footpatrol"
			region = "ie"
			qtstore = "footpatrol"
			qtregion = "ie"
		elif store == "footpatrolit":
			store = "footpatrol"
			region = "it"
			qtstore = "footpatrol"
			qtregion = "it"
		elif store == "footpatrolnl":
			store = "footpatrol"
			region = "nl"
			qtstore = "footpatrol"
			qtregion = "nl"
		elif store == "footpatrolse":
			store = "footpatrol"
			region = "se"
			qtstore = "footpatrol"
			qtregion = "se"
		elif store == "sizecouk":
			store = "size"
			region = ""
			qtstore = ""
			qtregion = ""
		elif store == "sizeofficialde":
			store = "size"
			region = "de"
			qtstore = "size"
			qtregion = "de"
		elif store == "sizeofficialfr":
			store = "size"
			region = "fr"
			qtstore = "size"
			qtregion = "fr"
		elif store == "sizeofficialnl":
			store = "size"
			region = "nl"
			qtstore = "size"
			qtregion = "nl"
		elif store == "sizeofficiales":
			store = "size"
			region = "es"
			qtstore = "size"
			qtregion = "es"
		elif store == "sizeofficialdk":
			store = "size"
			region = "dk"
			qtstore = "size"
			qtregion = "dk"
		elif store == "sizeofficialie" or store == "szie":
			store = "size"
			region = "ie"
			qtstore = "size"
			qtregion = "ie"
		elif store == "sizeofficialse" or store == "szse":
			store = "size"
			region = "se"
			qtstore = "size"
			qtregion = "se"
		elif store == "jdsportscouk":
			store = "jdsports"
			region = "uk"
			qtstore = ""
			qtregion = ""
		elif store == "jdsportsfr":
			store = "jdsports"
			region = "fr"
			qtstore = "jdsports"
			qtregion = "fr"
		elif store == "jdsportsbe":
			store = "jdsports"
			region = "be"
			qtstore = "jdsports"
			qtregion = "be"
		elif store == "jdsportsde":
			store = "jdsports"
			region = "de"
			qtstore = "jdsports"
			qtregion = "de"
		elif store == "jdsportsnl":
			store = "jdsports"
			region = "nl"
			qtstore = "jdsports"
			qtregion = "nl"
		elif store == "jdsportses":
			store = "jdsports"
			region = "es"
			qtstore = "jdsports"
			qtregion = "es"
		elif store == "jdsportsit":
			store = "jdsports"
			region = "it"
			qtstore = "jdsports"
			qtregion = "it"
		elif store == "jdsportsat":
			store = "jdsports"
			region = "at"
			qtstore = "jdsports"
			qtregion = "at"
		elif store == "jdsportsdk":
			store = "jdsports"
			region = "dk"
			qtstore = "jdsports"
			qtregion = "dk"
		elif store == "jdsportsie":
			store = "jdsports"
			region = "ie"
			qtstore = "jdsports"
			qtregion = "ie"
		elif store == "jd-sportscomau":
			store = "jdsports"
			region = "au"
			qtstore = "jdsports"
			qtregion = "au"
		elif store == "jdsportscomsg":
			store = "jdsports"
			region = "sg"
			qtstore = "jdsports"
			qtregion = "sg"
		elif store == "jdsportspt":
			store = "jdsports"
			region = "pt"
			qtstore = "jdsports"
			qtregion = "pt"
		elif store == "jdsportsmy":
			store = "jdsports"
			region = "my"
			qtstore = "jdsports"
			qtregion = "my"
		elif store == "jdsportsth":
			store = "jdsports"
			region = "th"
			qtstore = "jdsports"
			qtregion = "th"
		elif store == "globaljdsportscom":
			store = "jdsports"
			region = "global"
			qtstore = ""
			qtregion = ""

		headers = {
			"pragma": "no-cache",
			"cache-control": "no-cache",
			"upgrade-insecure-requests": "1",
			"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36",
			"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
			"sec-fetch-site": "same-origin",
			"sec-fetch-mode": "navigate",
			"sec-fetch-user": "?1",
			"sec-fetch-dest": "document",
			"accept-language": "de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7"
			}

		allpids = []
		embedlinkmbot = []
		embedlinkhawk = []
		size = []
		
		response = requests.get(url, headers=headers)
		if "THE PRODUCT YOU'RE ATTEMPTING TO VIEW" in response.text:
			embed=discord.Embed(title="Error scraping SKUs", color=setembedcolor)
			embed.add_field(name="Error - 1", value="Site might not be live", inline=False)
			embed.add_field(name="Command", value="?pid <link>   or   ?pid <pid>", inline=False)
			embed.add_field(name=":flag_gb: JDSports UK", value="Make sure to add `jdsportsuk or jduk` to the end of the pid", inline=False)
			embed.add_field(name=":flag_gb: Size? UK", value="Make sure to add `sizeuk or szuk` to the end of the pid", inline=False)
			embed.set_footer(text=setfootertextmesh, icon_url=setfooterimage)
			await context.send(embed=embed)
		elif "Footpatrol - Waiting Page" in response.text:
			embed=discord.Embed(title="Error scraping SKUs", color=setembedcolor)
			embed.add_field(name="Error - 1", value="Page not found -  Site might not be live", inline=False)
			embed.add_field(name="Command", value="?pid <link>   or   ?pid <pid>", inline=False)
			embed.add_field(name=":flag_gb: JDSports UK", value="Make sure to add `jdsportsuk or jduk` to the end of the pid", inline=False)
			embed.add_field(name=":flag_gb: Size? UK", value="Make sure to add `sizeuk or szuk` to the end of the pid", inline=False)
			embed.set_footer(text=setfootertextmesh, icon_url=setfooterimage)
			await context.send(embed=embed)
		else:
			soup = bs(response.content, 'html.parser')

			pids = soup.find("script", text = re.compile("dataObject"))
			
			text = pids.text
			splittext = text.split('variants')[1].split('};')[0]
			newtext = "{"+'"'+"variants"+'"'+ splittext + "\n}"
			newtext = newtext.replace('name','"name"').replace('upc','"upc"').replace('page_id_variant','"page_id_variant"')
			newtextjson = json.loads(newtext)
			for i in range(20):
				try:
					allpids.append(newtextjson["variants"][i]["page_id_variant"])
					size.append(newtextjson["variants"][i]["name"])
					mbotqt = "https://mbot.app/" + store + region + "/variant/" + str(allpids[i])
					embedlinkmbot.append("[[MBOT]]("+mbotqt+")")
					hawkqt = "https://hawkmesh.com/quicktask/" + store + region+ "/" + str(allpids[i])
					embedlinkhawk.append("[[HAWK]]("+hawkqt+")")
				except(IndexError,UnboundLocalError):
					break;
			pidlist = list(allpids)
			skuamount = len(pidlist)
			allpidslist = ",".join(allpids)
			mbotqtallpids = "https://mbot.app/" + store + region + "/variant/" + allpidslist
			mbotqtallpids = "[[MBOT QT]("+mbotqtallpids+")]"
			hawkqtallpids = "https://hawkmesh.com/quicktask/" + store + region+ "/" + allpidslist
			hawkqtallpids = "[[HAWK QT]("+hawkqtallpids+")]"
			oosbotqtallpids = "http://localhost:9099/mesh?store=" + store + region+ "&pid=" + allpidslist + "&amount=" + str(skuamount)
			oosbotqtallpids = "[[OOSBot QT]("+oosbotqtallpids+")]"
			embedpids = "\n".join(allpids)
			embedpids2 = "\n".join(size)
			embedpids3 = "\n".join("{0} {1} ".format(x,y) for x,y in zip(embedlinkmbot,embedlinkhawk))
			shoepic = soup.find("meta", {"property":"og:image"})["content"]
			image = "https://images.weserv.nl/?url="+link
			embedstore = []
			embedstore.append("space holder")
			embedstore.append(" - MBOT")
			embedstore.append(" - HAWK")
			embedlink = []
			embedlink.append("space holder")
			embedlink.append(str(mbotqtallpids))
			embedlink.append(str(hawkqtallpids))
			embedemote = []
			embedemote.append("space holder")
			embedemote.append("<:mbotoos:807792807326253077>")
			embedemote.append("<:hawkoos:807792754260181023>")
			embedemote.append("<:oosbot:828748333173440583>")
			meshpic = ["space holder","https://media.discordapp.net/attachments/681635149586104343/804628109399687188/J_0r5Du6_400x400.png","https://media.discordapp.net/attachments/681635149586104343/804628280434753596/7UR98tbB_400x400.png"]

			data = {}
			data["MESH"] = []
			y = data["MESH"]

			with open('mesh.json', 'r') as data_file:
				data = json.load(data_file)

				for i in range(len(data["MESH"])):            
					for R in range(len(data["MESH"][i])):
						try:
							for w in range(len(pidlist)):
								piddelete = pidlist[w].split(".")[0]
								if piddelete in data["MESH"][i][R]:
									data["MESH"][i][R].pop(piddelete)
									break;
						except (TypeError,KeyError,IndexError) as e:
							continue

			with open('mesh.json', 'w') as data_file:
				data = json.dump(data, data_file, indent=2)

			data = {}
			data["MESH"] = []
			y = data["MESH"]

			name = str(pid2)
			for j in range(len(pidlist)):
				y.append({
					name:[{
						"variantid": str(pidlist[j]),
						"Size": str(size[j]),
						"region": str(region),
						"image": shoepic,
						"store": store
					}]
				})

			def write_json(data, filename='mesh.json'): 
				with open(filename,'w') as f: 
					json.dump(data, f, indent=2)

			with open('mesh.json') as json_file: 
				data = json.load(json_file)
				temp = data["MESH"]
				temp.append(y)

			write_json(data) 
			json_file.close()

			embed=discord.Embed(title="MESH PID SCRAPER", description="*SKU Amount: " + str(skuamount) + "*", color=setembedcolor)
			if region == "uk" or region == "":
				region = "gb"
			embed.add_field(name="Store", value=str.upper(store) + " :flag_" + region + ":", inline=False)
			embed.add_field(name="Size SKU", value=embedpids, inline=True)
			embed.add_field(name="Size", value=embedpids2, inline=True)
			embed.add_field(name=f"MBOT {embedemote[1]}", value=mbotqtallpids, inline=False)
			embed.add_field(name=f"HAWK {embedemote[2]}", value=hawkqtallpids, inline=False)
			embed.add_field(name=f"OOSBot {embedemote[3]}", value=oosbotqtallpids, inline=False)
			embed.set_thumbnail(url=shoepic)
			embed.set_footer(text=setfootertextmesh, icon_url=setfooterimage)
			await context.send(embed=embed)

			print(Fore.MAGENTA + f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] " + log + Fore.GREEN + f"[Webhook sent!]")

	except(Exception,IndexError):
		if nopidfound == 1:
			print(Fore.MAGENTA + f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] " + log + Fore.GREEN + f"[FOUND PID]")
			jsoninfo = []
			size = []
			variantId = []
			with open('mesh.json') as json_file: 
				data = json.load(json_file)
				for i in range(len(data["MESH"])):            
					for R in range(len(data["MESH"][i])):
						try:
							jsoninfo.append(data["MESH"][i][R][pid2])
						except (TypeError,KeyError,IndexError) as e:
							continue

			store = jsoninfo[0][0]["store"]
			region = jsoninfo[0][0]["region"]
			shoepic = jsoninfo[0][0]["image"]

			for n in range(len(jsoninfo)):
				size.append(jsoninfo[n][0]["Size"])
				variantId.append(jsoninfo[n][0]["variantid"])

			embedpids = "\n".join(variantId)
			embedpids2 = "\n".join(size)
			qtpidlist = ",".join(variantId)
			skuamount = len(variantId)

			mbotqt = "https://mbot.app/" + store + region + "/variant/" + qtpidlist
			hawkqt = "https://hawkmesh.com/quicktask/" + store + region + "/" + qtpidlist
			oosbotqt = "http://localhost:9099/mesh?store=" + store + region + "&pid=" + qtpidlist + "&amount=" + str(skuamount)

			json_file.close()

			embedemote = []
			embedemote.append("place holder")
			embedemote.append("<:mbotoos:807792807326253077>")
			embedemote.append("<:hawkoos:807792754260181023>")
			embedemote.append("<:oosbot:828748333173440583>")

			embed=discord.Embed(title="MESH PID SCRAPER", description= "*SKU Amount: " + str(skuamount) + "*",color=setembedcolor)
			if region == "uk" or region == "":
				region = "gb"
			embed.add_field(name="Store", value=str.upper(store) + " :flag_" + region + ":", inline=False)
			embed.add_field(name="Size SKU", value=embedpids, inline=True)
			embed.add_field(name="Size", value=embedpids2, inline=True)
			embed.add_field(name=f"MBOT {embedemote[1]}", value=f"[MBOT QT]({mbotqt})", inline=False)
			embed.add_field(name=f"HAWK {embedemote[2]}", value=f"[HAWK QT]({hawkqt})", inline=False)
			embed.add_field(name=f"OOSBot {embedemote[3]}", value=f"[OOSBot QT]({oosbotqt})", inline=False)
			embed.set_thumbnail(url=shoepic)
			embed.set_footer(text=setfootertextmesh, icon_url=setfooterimage)
			await context.send(embed=embed)
			print(Fore.MAGENTA + f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] " + log + Fore.GREEN + f"[Webhook sent!]")
		else:
			embed=discord.Embed(title="Error scraping SKUs", color=setembedcolor)
			embed.add_field(name="Error - 1", value="Page is not LIVE!", inline=False)
			embed.add_field(name="Error - 2", value="Check your PID or use `?meshhelp for more information", inline=False)
			embed.add_field(name="Command", value="?pid <link>   or   ?pid <pid>", inline=False)
			embed.add_field(name=":flag_gb: ONLY for JDSports UK", value="Make sure to add `jdsportsuk or jduk` to the end of the pid\nExample:\n?mesh 16080111jduk\n?mesh 16080111jduk.0194502875782", inline=False)
			embed.add_field(name=":flag_gb: ONLY for Size? UK", value="Make sure to add `sizeuk or szuk` to the end of the pid", inline=False)
			embed.add_field(name="**GLOBAL** ONLY for JD Global", value="Make sure to add `global` to the end of the pid", inline=False)
			embed.set_footer(text=setfootertextmesh, icon_url=setfooterimage)
			await context.send(embed=embed)


@bot.command()
@commands.check(check_if_it_is_me)
async def meshdelete(context, info):

    now = datetime.now()
    try:
        server_name = context.guild.name
    except AttributeError:
        server_name = "DM"

    user_name_id = context.author.name + ' ID : ' + str(context.author.id)
    log2 = Fore.CYAN +f'[{server_name}]'
    log3 = Fore.CYAN + f'[{user_name_id}] '
    log = log2 + ' ' + log3

    data = {}
    data["MESH"] = []
    y = data["MESH"]
    lines = context.message.content.splitlines()
    lines.pop(0)



    with open('mesh.json', 'r') as data_file:
        data = json.load(data_file)

        for i in range(len(data["MESH"])):            
            for R in range(len(data["MESH"][i])):
                try:
                    for w in range(len(lines)):
                        if lines[w] in data["MESH"][i][R]:
                            data["MESH"][i][R].pop(lines[w])
                            break;
                except (TypeError,KeyError,IndexError) as e:
                    continue

    with open('mesh.json', 'w') as data_file:
        data = json.dump(data, data_file, indent=2)

    variantIdlist = "\n".join(lines)

    embed=discord.Embed(title="Succesfully deleted from MESH", color=setembedcolor)
    embed.add_field(name=":pushpin: SKUs", value=variantIdlist, inline=False)
    embed.set_footer(text=setfootertextmesh, icon_url=setfooterimage)
    await context.send(embed=embed)

@bot.command()
async def quiver(context, pid):
	now = datetime.now()
	try:
		server_name = context.guild.name
	except AttributeError:
		server_name = "DM"

	user_name_id = context.author.name + ' ID : ' + str(context.author.id)
	log2 = Fore.CYAN +f'[{server_name}]'
	log3 = Fore.CYAN + f'[{user_name_id}] '
	log = log2 + ' ' + log3

	lines = context.message.content.splitlines()
	lines.pop(0)
	print(Fore.MAGENTA + f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] " + log + Fore.GREEN + f"[Creating Quiver PID List of - {lines[0]}]")

	sizes = []
	sku = []

	pidamount = len(lines)

	if "QUIVER" in lines[0]:
		for i in range(len(lines)):
			size = lines[i].split("-")[1].replace(" ","")
			sizes.append(size)
			sku.append(lines[i])

	elif "-" in lines[0]:
		firstpid = lines[0].split("-")[0]
		if len(firstpid) < 5: #size at start
			for i in range(len(lines)):
				size = lines[i].split("-")[0].replace(" ","")
				pid = lines[i].split("-")[1].replace(" ","")
				sizes.append(size)
				sku.append(pid)

		elif len(firstpid) > 5:   #pid at start
			for i in range(len(lines)):
				size = lines[i].split("-")[1].replace(" ","")
				pid = lines[i].split("-")[0].replace(" ","")
				sizes.append(size)
				sku.append(pid)
	else:
		for i in range(len(lines)):
			sizes.append("N/A")
			sku.append(lines[i])

	embedsizes = "\n".join(sizes)
	embedsku = "\n".join(sku)
	pidlist = ",".join(sku)

	image = "https://cdn.discordapp.com/attachments/681635149586104343/821146301164945408/rzxTeaJa_400x400-removebg-preview.png"

	embed=discord.Embed(title="Quiver SKU List", description = str(pidamount) + " SKUs Loaded",color=setembedcolor)
	embed.add_field(name="SKUs", value=embedsku, inline=True)
	embed.add_field(name="Size", value=embedsizes, inline=True)
	embed.add_field(name="Quiver SKU List", value=pidlist, inline=False)
	embed.set_thumbnail(url=image)
	embed.set_footer(text=setfootertextmesh, icon_url=setfooterimage)
	await context.send(embed=embed)
	print(Fore.MAGENTA + f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] " + log + Fore.GREEN + f"[Webhook sent!]")


@bot.command()
async def meshhelp(context):
	embed=discord.Embed(title="MESH QT / SKU Scraper HELP", color=setembedcolor)
	embed.add_field(name="SKU Scraper", value="?mesh  <full link here>\n?mesh <meshpid>", inline=False)
	embed.add_field(name="QT Setup", value="?qt  <store>  <PIDs/SKUs>", inline=False)
	embed.add_field(name="QT Setup - Example", value="`?qt szuk 16080252.2510891\n16080252.2510892\n16080252.2510893`\n\n`?qt jdgb 16048706.0194498070598`\n\n`?qt fpgb 418943_footpatrolcom,418943_footpatrolcom`", inline=False)
	embed.add_field(name="Country Format", value="?meshcountries", inline=True)
	embed.add_field(name="Info", value="A image of the shoe will be applied for FP and Size QTs", inline=False)
	embed.set_footer(text=setfootertextmesh, icon_url=setfooterimage)
	await context.send(embed=embed)

@bot.command()
async def meshcountries(context):
	fpregions = ["gb","fr","de","dk","it","nl","se","ie"]
	fpflag = [":flag_gb:",":flag_fr:",":flag_de:",":flag_dk:",":flag_it:",":flag_nl:",":flag_se:",":flag_ie:"]
	szregions = ["gb","de","dk","es","fr","ie","it","nl","se"]
	szflag = [":flag_gb:",":flag_de:",":flag_dk:",":flag_es:",":flag_fr:",":flag_ie:",":flag_it:",":flag_nl:",":flag_se:"]
	jdregions = ["gb","at","au","be","de","dk","es","fr","ie","it","my","nl","pt","se","sg"]
	jdflag = [":flag_gb:",":flag_at:",":flag_au:",":flag_be:",":flag_de:",":flag_dk:",":flag_es:",":flag_fr:",":flag_ie:",":flag_it:",":flag_my:",":flag_nl:",":flag_pt:",":flag_se:",":flag_sg:"]
	jdsportsregions = ["jdsports" + i for i in jdregions]
	jdshortregions = ["jd" + i for i in jdregions]
	footpatrolregions = ["footpatrol" + i for i in fpregions]
	fpshortregion = ["fp" + i for i in fpregions]
	sizeregion = ["size" + i for i in szregions]
	sizeshortregion = ["sz" + i for i in szregions]

	
	fpstores = "\n".join("{0} {1} {2}".format(x,y,z) for x,y,z in zip(fpflag,footpatrolregions,fpshortregion))
	szstores = "\n".join("{0} {1} {2}".format(x,y,z) for x,y,z in zip(szflag,sizeregion,sizeshortregion))
	jdstores = "\n".join("{0} {1} {2}".format(x,y,z) for x,y,z in zip(jdflag,jdsportsregions,jdshortregions))
	embed=discord.Embed(title="MESH QT Country Format", color=setembedcolor)
	embed.add_field(name="JDSports", value=jdstores, inline=True)
	embed.add_field(name="Size?", value=szstores, inline=True)
	embed.add_field(name="Footpatrol", value=fpstores, inline=True)
	embed.set_footer(text=setfootertextmesh, icon_url=setfooterimage)
	await context.send(embed=embed)

@bot.command()
@commands.check(check_if_it_is_me)
async def early(context,region,shoegunplug,mainpid,info):
	wrongpid = 0
	country = ""
	store = ""

	now = datetime.now()
	try:
		server_name = context.guild.name
	except AttributeError:
		server_name = "DM"

	user_name_id = context.author.name + ' ID : ' + str(context.author.id)
	log2 = Fore.CYAN +f'[{server_name}]'
	log3 = Fore.CYAN + f'[{user_name_id}] '
	log = log2 + ' ' + log3

	lines = context.message.content.splitlines()
	shoesku = []
	size = []

	region = str.lower(region)

	if len(mainpid) == 6:

		if region == "jdpt" or region == "jdsportspt":
			store = "jdsports"
			country = "pt"
			skucountry = "pt"
			checkstore = "jdpt"

		elif region == "fpgb" or region == "fpcom" or region == "fpuk":
			store = "footpatrol"
			country = "gb"
			skucountry = "com"
			checkstore = "fpcom"

		elif region == "sznl" or region == "sizenl":
			store = "size"
			country = "nl"
			skucountry = "nl"
			checkstore = "sznl"

		elif region == "szfr" or region == "sizefr":
			store = "size"
			country = "fr"
			skucountry = "fr"
			checkstore = "szfr"

		lines.pop(0)
		for i in range(len(lines)):
			if len(lines[i]) == 7:
				shoesku.append(mainpid + "_" + store + skucountry + ".00" + lines[i])
			elif len(lines[i]) < 5:
				lines[i] = lines[i].replace(",",".")
				size.append(lines[i])
			else:
				wrongpid = 1

		embedsize = "\n".join(size)
		embedsku = "\n".join(shoesku)

	elif len(mainpid) == 8:
		if region == "jdde":
			store = "jdsports"
			country = "de"
			skucountry = "de"
			checkstore = "jdde"

		elif region == "jdes":
			store = "jdsports"
			country = "es"
			skucountry = "es"
			checkstore = "jdes"

		elif region == "jdfr":
			store = "jdsports"
			country = "fr"
			skucountry = "fr"
			checkstore = "jdfr"

		elif region == "jdit":
			store = "jdsports"
			country = "it"
			skucountry = "it"
			checkstore = "jdit"

		elif region == "jdgb" or region == "jduk":
			store = "jdsports"
			country = "gb"
			skucountry = "gb"
			checkstore = "jdgb"

		elif region == "szuk" or region == "szgb":
			store = "size"
			country = "gb"
			skucountry = "gb"
			checkstore = "szgb"

		if checkstore == "jdgb" or checkstore == "jdfr" or checkstore == "jdde":

			lines.pop(0)
			for i in range(len(lines)):
				if len(lines[i]) == 12:
					if not country == "gb":
						shoesku.append(mainpid + "_" + store + skucountry + ".0" + lines[i])
					else:
						shoesku.append(mainpid  + ".0" + lines[i])
				elif len(lines[i]) < 5:
					lines[i] = lines[i].replace(",",".")
					size.append(lines[i])
				else:
					wrongpid = 1
		elif checkstore == "jdes" or checkstore == "jdit" or checkstore == "szgb":
			lines.pop(0)
			for i in range(len(lines)):
				if len(lines[i]) == 7:
					if country == "gb":
						shoesku.append(mainpid + "." + lines[i])
					else:
						shoesku.append(mainpid + "_" + store + skucountry + "." + lines[i])

				elif len(lines[i]) < 5:
					lines[i] = lines[i].replace(",",".")
					size.append(lines[i])
				else:
					wrongpid = 1		

		embedsize = "\n".join(size)
		embedsku = "\n".join(shoesku)

	else:
		wrongpid = 1


	if wrongpid == 1:

		if checkstore == "jdpt" or checkstore == "fpcom" or checkstore == "sznl" or checkstore == "szfr":
			embed=discord.Embed(title="Error", color=setembedcolor)
			embed.add_field(name="Wrong SKU", value="SKUs need to be 7 Digit!", inline=False)
			embed.add_field(name="Wrong PID", value="Main PID needs to be 6 Digit!", inline=False)
			embed.set_footer(text=setfootertextmesh, icon_url=setfooterimage)
			await context.send(embed=embed)

		if checkstore == "jdde":
			embed=discord.Embed(title="Error", color=setembedcolor)
			embed.add_field(name="Wrong SKU", value="SKUs need to be 12 Digit!", inline=False)
			embed.add_field(name="Wrong PID", value="Main PID needs to be 8 Digit!", inline=False)
			embed.set_footer(text=setfootertextmesh, icon_url=setfooterimage)
			await context.send(embed=embed)

		if checkstore == "jdes" or country == "jdit":
			embed=discord.Embed(title="Error", color=setembedcolor)
			embed.add_field(name="Wrong SKU", value="SKUs need to be 7 Digit!", inline=False)
			embed.add_field(name="Wrong PID", value="Main PID needs to be 8 Digit!", inline=False)
			embed.set_footer(text=setfootertextmesh, icon_url=setfooterimage)
			await context.send(embed=embed)

		elif not country:
			embed=discord.Embed(title="Error", color=setembedcolor)
			embed.add_field(name="Wrong PID", value="Check your main PID or missing shoegunplu PID", inline=False)
			embed.add_field(name="Command Format", value="?early <region> <shoegunplu> <MAIN PID>\n<ALL SKUS>\n<ALL Sizes>", inline=False)
			embed.set_footer(text=setfootertextmesh, icon_url=setfooterimage)
			await context.send(embed=embed)

	if wrongpid == 0:
		if store == "jdsports":
			picstore = "jd"
		elif store == "size":
			picstore = "sz"
		elif store == "footpatrol":
			picstore = "fp"
		
		embedtitle = str.upper(store) + " " + str.upper(country) + " :flag_" + str.lower(country) + ":"


		shoepic = "https://i8.amplience.net/i/jpl/"+ picstore + "_" + shoegunplug +"_a?qlt=92"
		embed=discord.Embed(title=embedtitle, color=setembedcolor)
		embed.add_field(name="Size", value=embedsize, inline=True)
		embed.add_field(name="SKU", value=embedsku, inline=True)
		embed.set_thumbnail(url=shoepic)
		embed.set_footer(text=setfootertextmesh, icon_url=setfooterimage)
		await context.send(embed=embed)
		
		webhook = DiscordWebhook(url="https://discord.com/api/webhooks/829457848860934214/8Xg74V_s6fv1N-oMBpObmKdu4YUg25hhFX_lxUqZ3RkAjRgwK6moMT5HH6vXFSeBLiaj")
		embed = DiscordEmbed(title=embedtitle, color=setembedcolor)
		embed.add_embed_field(name="Size", value=embedsize, inline=True)
		embed.add_embed_field(name="SKU", value=embedsku, inline=True)
		embed.set_footer(text=setfootertextmesh, icon_url=setfooterimage)
		embed.set_thumbnail(url=shoepic)
		webhook.add_embed(embed)
		webhook.execute()

@bot.command()
@commands.check(check_if_it_is_me)
async def earlyhelp(context):
		embed=discord.Embed(title="Error", color=setembedcolor)
		embed.add_field(name="Command Format", value="?early <region> <shoegunplu> <MAIN PID>\n<ALL SKUS>\n<ALL Sizes>", inline=False)
		embed.add_field(name="Example", value="""?early sznl 387344 387344
1868054
1868055
1868056
1868058
1868059
1868060
4,5
5
5,5
6
6
6,5""", inline=False)
		embed.set_footer(text=setfootertextmesh, icon_url=setfooterimage)
		await context.send(embed=embed)

@bot.event
async def on_command_error(ctx, error):
	if isinstance(error, CommandNotFound):
		return
	elif isinstance(error,MissingRequiredArgument):
		embed=discord.Embed(title="Command Error", color=setembedcolor)
		embed.add_field(name="Error", value="Your are missing an argument", inline=True)
		embed.add_field(name="Command - SKU Scraper", value="?mesh <meshpid>\n?mesh <link>", inline=False)
		embed.add_field(name="Command - QT", value="?qt <store> <PIDs/SKUs>", inline=False)
		embed.set_footer(text=setfootertextmesh, icon_url=setfooterimage)
		await ctx.send(embed=embed)
		return
	raise error

bot.run(bottoken)
