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
from requests_html import HTML, HTMLSession

bot = commands.Bot(command_prefix = '?', help_command=None)
bottoken = "NzkyODU1MjY5MjQzMjI0MTQ1.X-jyAg.CD0xNJ37E5n_xt8x96TxCCEb_EY"

@bot.event
async def on_ready():
	print('Bot is ready.')
	pass


@bot.command()
async def qt(context, store, pid):
	store = str.lower(store)
	lines = context.message.content.splitlines()
	newpid = ",".join(lines).replace("?qt ","").replace(store,"").replace(" ","")
	pid = str.lower(pid).replace("\n","").replace(" ","")
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
		url = "https://www.footpatrol.com/product/pigeon-oos/" + pid
	elif store == "fpfr" or store == "footpatrolfr":
		store = "footpatrol"
		region = "fr"
		qtstore = "footpatrol"
		qtregion = "fr"
		url = "https://www.footpatrol.fr/product/pigeon-oos/" + pid
	elif store == "size" or store == "sz" or store == "sizeuk" or store == "sizegb" or store == "szuk" or store == "szgb":
		store = "size"
		region = ""
		qtstore = ""
		qtregion = ""
		url = "https://www.size.co.uk/product/pigeon-oos/" + pid
	elif store == "sizede" or store == "szde":
		store = "size"
		region = "de"
		qtstore = "size"
		qtregion = "de"
		url = " https://www.sizeofficial." + qtregion + "/product/pigeon-oos/" + pid
	elif store == "sizefr" or store == "szfr":
		store = "size"
		region = "fr"
		qtstore = "size"
		qtregion = "fr"
		url = " https://www.sizeofficial.fr/product/pigeon-oos/" + pid
	elif store == "sizenl" or store == "sznl":
		store = "size"
		region = "nl"
		qtstore = "size"
		qtregion = "nl"
		url = " https://www.sizeofficial." + qtregion + "/product/pigeon-oos/" + pid
	elif store == "sizees" or store == "szes":
		store = "size"
		region = "es"
		qtstore = "size"
		qtregion = "es"
		url = " https://www.sizeofficial." + qtregion + "/product/pigeon-oos/" + pid
	elif store == "sizedk" or store == "szdk":
		store = "size"
		region = "dk"
		qtstore = "size"
		qtregion = "dk"
		url = " https://www.sizeofficial." + qtregion + "/product/pigeon-oos/" + pid
	elif store == "sizeie" or store == "szie":
		store = "size"
		region = "ie"
		qtstore = "size"
		qtregion = "ie"
		url = " https://www.sizeofficial." + qtregion + "/product/pigeon-oos/" + pid
	elif store == "sizese" or store == "szse":
		store = "size"
		region = "se"
		qtstore = "size"
		qtregion = "se"
		url = " https://www.sizeofficial." + qtregion + "/product/pigeon-oos/" + pid
	elif store == "jdgb" or store == "jduk" or store == "jdsports" or store == "jdsportsuk" or store == "jdsportsgb":
		store = "jdsports"
		region = "uk"
		qtstore = ""
		qtregion = ""
		url = "https://www.jdsports.co.uk/product/pigeon-oos/" + pid
	elif store == "jdfr" or store == "jdsportsfr":
		store = "jdsports"
		region = "fr"
		qtstore = "jdsports"
		qtregion = "fr"
		url = "https://www.jdsports." + qtregion + "/product/pigeon-oos/" + pid
	elif store == "jdbe" or store == "jdsportsbe":
		store = "jdsports"
		region = "be"
		qtstore = "jdsports"
		qtregion = "be"
		url = "https://www.jdsports." + qtregion + "/product/pigeon-oos/" + pid
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
		url = "https://www.jdsports." + qtregion + "/product/pigeon-oos/" + pid
	elif store == "jdes" or store == "jdsportses":
		store = "jdsports"
		region = "es"
		qtstore = "jdsports"
		qtregion = "es"
		url = "https://www.jdsports." + qtregion + "/product/pigeon-oos/" + pid
	elif store == "jdit" or store == "jdsportsit":
		store = "jdsports"
		region = "it"
		qtstore = "jdsports"
		qtregion = "it"
		url = "https://www.jdsports." + qtregion + "/product/pigeon-oos/" + pid
	elif store == "jdat" or store == "jdsportsat":
		store = "jdsports"
		region = "at"
		qtstore = "jdsports"
		qtregion = "at"
		url = "https://www.jdsports." + qtregion + "/product/pigeon-oos/" + pid
	elif store == "jddk" or store == "jdsportsdk":
		store = "jdsports"
		region = "dk"
		qtstore = "jdsports"
		qtregion = "dk"
		url = "https://www.jdsports." + qtregion + "/product/pigeon-oos/" + pid
	elif store == "jdie" or store == "jdsportsie":
		store = "jdsports"
		region = "ie"
		qtstore = "jdsports"
		qtregion = "ie"
		url = "https://www.jdsports." + qtregion + "/product/pigeon-oos/" + pid
	elif store == "jdauf" or store == "jdsportsauf" or store == "jdsportsau" or store == "jdau":
		store = "jdsports"
		region = "au"
		qtstore = "jdsports"
		qtregion = "au"
		url = "https://www.jdsports." + qtregion + "/product/pigeon-oos/" + pid
	elif store == "jdsg" or store == "jdsportssg":
		store = "jdsports"
		region = "sg"
		qtstore = "jdsports"
		qtregion = "sg"
		url = "https://www.jdsports." + qtregion + "/product/pigeon-oos/" + pid
	elif store == "jdpt" or store == "jdsportspt":
		store = "jdsports"
		region = "pt"
		qtstore = "jdsports"
		qtregion = "pt"
		url = "https://www.jdsports." + qtregion + "/product/pigeon-oos/" + pid
	elif store == "jdjx" or store == "jdsportsjx" or store == "jdsportsglobal" or store == "jdglobal":
		store = "jdsports"
		region = "jx"
		qtstore = "jdsports"
		qtregion = "jx"
		url = "https://www.jdsports." + qtregion + "/product/pigeon-oos/" + pid
	elif store == "jdmyf" or store == "jdsportsmyf":
		store = "jdsports"
		region = "myf"
		qtstore = "jdsports"
		qtregion = "myf"
		url = "https://www.jdsports." + qtregion + "/product/pigeon-oos/" + pid

	if store == "fpgb" or store == "footpatrolgb" or store == "footpatrol" or store == "fpcom" or store == "footpatrolcom" or store == "footpatroluk" or store == "fpuk" or store == "fpde" or store == "footpatrolde" or store == "fpfr" or store == "footpatrolfr" or store == "size" or store == "sz" or store == "sizeuk" or store == "sizegb" or store == "szuk" or store == "szgb" or store == "sizede" or store == "szde" or store == "sizefr" or store == "szfr" or store == "sizenl" or store == "sznl" or store == "sizees" or store == "szes" or store == "sizedk" or store == "szdk" or store == "sizeie" or store == "szie" or store == "sizese" or store == "szse" or store == "jdfr" or store == "jdsportsfr" or store == "jdgb" or store == "jduk" or store == "jdsports" or store == "jdsportsuk" or store == "jdsportsgb" or store == "jdbe" or store == "jdsportsbe" or store == "jdde" or store == "jdsportsde" or store == "jdnl" or store == "jdsportsnl" or store == "jdes" or store == "jdsportses" or store == "jdit" or store == "jdsportsit" or store == "jdat" or store == "jdsportsat" or store == "jddk" or store == "jdsportsdk" or store == "jdie" or store == "jdsportsie" or store == "jdauf" or store == "jdsportsauf" or store == "jdsportsau" or store == "jdau" or store == "jdsg" or store == "jdsportssg" or store == "jdpt" or store == "jdsportspt" or store == "jdjx" or store == "jdsportsjx" or store == "jdsportsglobal" or store == "jdglobal" or store == "jdmyf" or store == "jdsportsmyf":
		if qtstore == "" :
			underline = ""
		else:
			underline = "_"
		print("Finishing QT for " + newpid + " / " + store + region)
		try:
			if pid[6] == ".":
				pidlist = newpid.split(",")
				for i in range(len(pidlist)):
					singlepid = pidlist[i]
					pid2 = singlepid.split(".",1)[1]
					newpidlist.append(singlepid[:6] + underline + qtstore + qtregion + "." + pid2)
					finalpidlist = ",".join(newpidlist)
			elif pid[8] == ".":
				pidlist = newpid.split(",")
				for i in range(len(pidlist)):
					singlepid = pidlist[i]
					pid2 = singlepid.split(".",1)[1]
					newpidlist.append(singlepid[:8] + underline + qtstore + qtregion + "." + pid2)
					finalpidlist = ",".join(newpidlist)
			elif pid[17] == ".":
				pidlist = newpid.split(",")
				for i in range(len(pidlist)):
					singlepid = pidlist[i]
					pid2 = singlepid.split(".",1)[1]
					newpidlist.append(singlepid[:6] + underline + qtstore + qtregion + "." + pid2)
					finalpidlist = ",".join(newpidlist)
			elif pid[19] == ".":
				pidlist = newpid.split(",")
				for i in range(len(pidlist)):
					singlepid = pidlist[i]
					pid2 = singlepid.split(".",1)[1]
					newpidlist.append(singlepid[:8] + underline + qtstore + qtregion + "." + pid2)
					finalpidlist = ",".join(newpidlist)
			else:
				finalpidlist = newpid
				pidlist = newpid.split(",")
		except(IndexError):
			if pid.isnumeric():
				if len(pid) == 8:
					pidlist = newpid.split(",")
					for i in range(len(pidlist)):
						newpidlist.append(pidlist[i] + underline + qtstore + qtregion)
						finalpidlist = ",".join(newpidlist)
				elif len(pid) == 6:
					pidlist = newpid.split(",")
					for i in range(len(pidlist)):
						newpidlist.append(pidlist[i] + underline + qtstore + qtregion)
						finalpidlist = ",".join(newpidlist)
			else:
				finalpidlist = newpid
				pidlist = newpid.split(",")
		print("Finished QT for " + finalpidlist + " / " + store + region)		
		mbotqt = "https://mbot.app/" + store + region + "/variant/" + finalpidlist
		mbotqt = mbotqt.replace("/" + underline + qtstore + qtregion,("/")).replace("/,","/")
		hawkqt = "https://hawkmesh.com/quicktask/" + store + region+ "/" + finalpidlist
		hawkqt = hawkqt.replace("/" + underline + qtstore + qtregion,("/")).replace("/,","/")
		skulen = mbotqt.partition(qtstore + qtregion + "/")
		skulen = skulen[2].split(",")
		list(skulen)
		skuamount = len(skulen)
		embedlink = []
		embedlink.append("[MBOT QT]("+mbotqt+")")
		embedlink.append("[HAWK QT]("+hawkqt+")")
		embedstore = []
		embedstore.append(" - MBOT")
		embedstore.append(" - HAWK")
		meshpic = ["https://media.discordapp.net/attachments/681635149586104343/804628109399687188/J_0r5Du6_400x400.png","https://media.discordapp.net/attachments/681635149586104343/804628280434753596/7UR98tbB_400x400.png"]
		pidlink = finalpidlist[:19] 
		url = "https://www.jdsports." + qtregion + "/product/pigeon-oos/" + pidlink
		try:
			response = requests.get(url, headers=headers)
			soup = bs(response.content, 'html.parser')
			shoepic = soup.find("meta", {"property":"og:image"})["content"]
			embed=discord.Embed(title="MESH QT", color=0x0000FF)
			if region == "uk" or region == "":
				region = "gb"
			embed.add_field(name="SKU Amount", value="*" + str(skuamount) + " SKUs loaded*")
			embed.add_field(name=str.upper(store) + " :flag_"+ str.lower(region)+":", value="[" + str(embedlink[0]) + "]" + "  [" + str(embedlink[1]) + "]", inline=False)
			embed.set_thumbnail(url=shoepic)
			embed.set_footer(text="Pigeon Helper <?mbothelp> made by OOS#4315", icon_url="https://cdn.discordapp.com/attachments/797052521582952468/797231957951643668/Pigeon_Proxies3.png")
			await context.send(embed=embed)
		except(Exception,TypeError):
			for i in range(2):
				embed=discord.Embed(title="MESH QT" + embedstore[i], color=0x0000FF)
				if region == "uk" or region == "":
					region = "gb"
				embed.add_field(name="SKU Amount", value="*" + str(skuamount) + " SKUs loaded*")
				embed.add_field(name=str.upper(store) + " :flag_"+ str.lower(region)+":", value="[" + str(embedlink[i]) + "]", inline=False)
				shoepid = finalpidlist.split(",")[0]
				if "_" in shoepid:
					shoepid = shoepid.split("_")[0]
				if len(str(shoepid)) <= 6:
					embed.set_thumbnail(url="https://i8.amplience.net/i/jpl/"+ picstore + "_" + shoepid +"_a?qlt=92&w=900&h=637&v=1&fmt=webp")
				else:
					embed.set_thumbnail(url=str(meshpic[i]))
				embed.set_footer(text="Pigeon Helper <?mbothelp> made by OOS#4315", icon_url="https://cdn.discordapp.com/attachments/797052521582952468/797231957951643668/Pigeon_Proxies3.png")
				await context.send(embed=embed)
	else:
		embed=discord.Embed(title="Wrong Command!\nUse ?mbothelp for more information", color=0x0000FF)
		embed.set_footer(text="Pigeon Helper <?mbothelp> made by OOS#4315", icon_url="https://cdn.discordapp.com/attachments/797052521582952468/797231957951643668/Pigeon_Proxies3.png")
		await context.send(embed=embed)

@bot.command()
async def pid(context, link):
	if "footpatrolcom" in link and len(link) < 25:
		url = "https://m.footpatrol.com/product/pigeon-oos/" + link
	elif "footpatrolfr" in link and len(link) < 25:
		url = "https://m.footpatrol.fr/product/pigeon-oos/" + link
	elif "footpatrolfi" in link and len(link) < 25:
		url = "https://m.footpatrol.fi/product/pigeon-oos/" + link
	elif "sizeuk" in link and len(link) < 25:
		link = link.replace("sizeuk","")
		url = "https://m.size.co.uk/product/pigeon-oos/" + link
	elif "sizegb" in link and len(link) < 25:
		link = link.replace("sizegb","")
		url = "https://m.size.co.uk/product/pigeon-oos/" + link
	elif "sizede" in link and len(link) < 25:
		url = " https://m.sizeofficial.de/product/pigeon-oos/" + link
	elif "sizefr" in link and len(link) < 25:
		url = " https://m.sizeofficial.fr/product/pigeon-oos/" + link
	elif "sizenl" in link and len(link) < 25:
		url = " https://m.sizeofficial.nl/product/pigeon-oos/" + link
	elif "sizees" in link and len(link) < 25:
		url = " https://m.sizeofficial.es/product/pigeon-oos/" + link
	elif "sizedk" in link and len(link) < 25:
		url = " https://m.sizeofficial.dk/product/pigeon-oos/" + link
	elif "sizeie" in link and len(link) < 25:
		url = " https://m.sizeofficial.ie/product/pigeon-oos/" + link
	elif "sizese" in link and len(link) < 25:
		url = " https://m.sizeofficial.se/product/pigeon-oos/" + link
	elif "jdsportsgb" in link and len(link) < 25:
		url = "https://m.jdsports.co.uk/product/pigeon-oos/" + link
	elif "jdsportsuk" in link and len(link) < 25:
		link = link.replace("jdsportsuk","")
		url = "https://m.jdsports.co.uk/product/pigeon-oos/" + link
	elif "jduk" in link and len(link) < 25:
		link = link.replace("jduk","")
		url = "https://m.jdsports.co.uk/product/pigeon-oos/" + link
	elif "jdsportsfr" in link and len(link) < 25:
		url = "https://m.jdsports.fr/product/pigeon-oos/" + link
	elif "jdsportsbe" in link and len(link) < 25:
		url = "https://m.jdsports.be/product/pigeon-oos/" + link
	elif "jdsportsde" in link and len(link) < 25:
		url = "https://m.jdsports.de/product/pigeon-oos/" + link
	elif "jdsportsnl" in link and len(link) < 25:
		url = "https://m.jdsports.nl/product/pigeon-oos/" + link
	elif "jdsportses" in link and len(link) < 25:
		url = "https://m.jdsports.es/product/pigeon-oos/" + link
	elif "jdsportsit" in link and len(link) < 25:
		url = "https://m.jdsports.it/product/pigeon-oos/" + link
	elif "jdsportsat" in link and len(link) < 25:
		url = "https://m.jdsports.at/product/pigeon-oos/" + link
	elif "jdsportsdk" in link and len(link) < 25:
		url = "https://m.jdsports.dk/product/pigeon-oos/" + link
	elif "jdsportsie" in link and len(link) < 25:
		url = "https://m.jdsports.ie/product/pigeon-oos/" + link
	elif "jd-sportscomau" in link and len(link) < 25:
		url = "https://m.jdsports.com.au/product/pigeon-oos/" + link
	elif "jdsportssg" in link and len(link) < 25:
		url = "https://m.jdsports.com.sg/product/pigeon-oos/" + link
	elif "jdsportspt" in link and len(link) < 25:
		url = "https://m.jdsports.pt/product/pigeon-oos/" + link
	elif "jdsportsmy" in link and len(link) < 25:
		url = "https://m.jdsports.my/product/pigeon-oos/" + link
	elif link.isnumeric():
		embed=discord.Embed(title="Error Scraping SKUs", color=0x66ffff)
		embed.add_field(name=":flag_gb: SKU Scraper via PID - JDSports", value="Make sure to add `jd, jdsportsuk or jduk` to the end of the pid", inline=False)
		embed.add_field(name=":flag_gb: SKU Scraper via PID - Size?", value="Make sure to add `sz, sizeuk or szuk` to the end of the pid", inline=False)
		embed.set_footer(text="Pigeon Helper made by OOS#4315", icon_url="https://cdn.discordapp.com/attachments/797052521582952468/797231957951643668/Pigeon_Proxies3.png")
		await context.send(embed=embed)
	else:
		if link.split('//')[1].split('.')[0] == "www":
			url = link.replace("www","m")
		else:
			url = link
	print(link)
	store = url.split('/m.')[1].split('/')[0]
	store = store.replace(".","")

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
	elif store == "jdsportsmyf":
		store = "jdsports"
		region = "myf"
		qtstore = "jdsports"
		qtregion = "myf"

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
	try:
		response = requests.get(url, headers=headers)
		if "THE PRODUCT YOU'RE ATTEMPTING TO VIEW" in response.text:
			embed=discord.Embed(title="Error scraping SKUs", color=0x66ffff)
			embed.add_field(name="Error - 1", value="Site might not be live", inline=False)
			embed.set_footer(text="Pigeon Helper made by OOS#4315", icon_url="https://cdn.discordapp.com/attachments/797052521582952468/797231957951643668/Pigeon_Proxies3.png")
			await context.send(embed=embed)
		elif "Footpatrol - Waiting Page" in response.text:
			embed=discord.Embed(title="Error scraping SKUs", color=0x66ffff)
			embed.add_field(name="Error - 1", value="Page not found -  Site might not be live", inline=False)
			embed.set_footer(text="Pigeon Helper made by OOS#4315", icon_url="https://cdn.discordapp.com/attachments/797052521582952468/797231957951643668/Pigeon_Proxies3.png")
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
			allpidslist = ",".join(allpids)
			print(allpidslist)
			mbotqtallpids = "https://mbot.app/" + store + region + "/variant/" + allpidslist
			mbotqtallpids = "[[MBOT]]("+mbotqtallpids+")"
			hawkqtallpids = "https://hawkmesh.com/quicktask/" + store + region+ "/" + allpidslist
			hawkqtallpids = "[[HAWK]]("+hawkqtallpids+")"
			embedpids = "\n".join(allpids)
			embedpids2 = "\n".join(size)
			embedpids3 = "\n".join("{0} {1} ".format(x,y) for x,y in zip(embedlinkmbot,embedlinkhawk))
			shoepic = soup.find("meta", {"property":"og:image"})["content"]
			image = "https://images.weserv.nl/?url="+link
			try:
				embed=discord.Embed(title="MESH PID SCRAPER", color=0x66ffff)
				if region == "uk" or region == "":
					region = "gb"
				embed.add_field(name="Store", value=str.upper(store) + " :flag_" + region + ":", inline=False)
				embed.add_field(name="Size SKU", value=embedpids, inline=True)
				embed.add_field(name="Size", value=embedpids2, inline=True)
				embed.add_field(name="QT", value=embedpids3, inline=True)
				embed.add_field(name="QT for all SKUs", value=mbotqtallpids + " " + hawkqtallpids, inline=False)
				embed.set_thumbnail(url=shoepic)
				embed.set_footer(text="Pigeon Helper made by OOS#4315", icon_url="https://cdn.discordapp.com/attachments/797052521582952468/797231957951643668/Pigeon_Proxies3.png")
				await context.send(embed=embed)
			except(Exception):
				embed=discord.Embed(title="MESH PID SCRAPER", color=0x66ffff)
				if region == "uk" or region == "":
					region = "gb"
				embed.add_field(name="Store", value=str.upper(store) + " :flag_" + region + ":", inline=False)
				embed.add_field(name="Size SKU", value=embedpids, inline=True)
				embed.add_field(name="Size", value=embedpids2, inline=True)
				embed.add_field(name="QT Error", value="The embed message is to long!\nUse QT command to get the QTs ready. \nRefer to `?meshhelp`", inline=False)
				embed.set_thumbnail(url=shoepic)
				embed.set_footer(text="Pigeon Helper made by OOS#4315", icon_url="https://cdn.discordapp.com/attachments/797052521582952468/797231957951643668/Pigeon_Proxies3.png")
				await context.send(embed=embed)
	except(Exception):
		embed=discord.Embed(title="Error scraping SKUs", color=0x66ffff)
		embed.add_field(name="Error - 2", value="Check your PID or use `?meshhelp for more information", inline=False)
		embed.set_footer(text="Pigeon Helper made by OOS#4315", icon_url="https://cdn.discordapp.com/attachments/797052521582952468/797231957951643668/Pigeon_Proxies3.png")
		await context.send(embed=embed)

@bot.command()
async def meshhelp(context):
	fpregions = ["gb","fr"]
	fpflag = [":flag_gb:",":flag_fr:"]
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

	embed=discord.Embed(title="MESH QT / SKU Scraper HELP", color=0x66ffff)
	embed.add_field(name="SKU Scraper", value="?pid  <full link here>", inline=False)
	embed.add_field(name="MBot QT Setup", value="?mbot  <store>  <PIDs/SKUs>", inline=True)
	embed.add_field(name="Hawk QT Setup", value="?hawk  <store>  <PIDs/SKUs>", inline=True)
	embed.add_field(name="QT Example Commands", value="?mbot jdgb 16048706.0194498070598\n?hawk jdsportsde 16048706_jdsportsde\n?mbot fpgb 418943_footpatrolcom.002117383,418943_footpatrolcom.002117384", inline=False)
	embed.add_field(name="Info", value="A image of the shoe will be applied for FP and Size QTs", inline=False)
	embed.add_field(name="JDSports", value=jdstores, inline=True)
	embed.add_field(name="Size?", value=szstores, inline=True)
	embed.add_field(name="Footpatrol", value=fpstores, inline=True)
	embed.set_footer(text="Pigeon Helper made by OOS#4315", icon_url="https://cdn.discordapp.com/attachments/797052521582952468/797231957951643668/Pigeon_Proxies3.png")
	await context.send(embed=embed)

bot.run(bottoken)