import discord
from discord.ext import commands, tasks
from discord_webhook import DiscordEmbed, DiscordWebhook
from itertools import cycle
import json
import os
from pprint import pprint
from bs4 import BeautifulSoup as bs
import requests
import platform
import sys
import random, ast
import xml.etree.ElementTree as ET
from urllib.request import urlopen
import xmltodict
from decimal import Decimal
bot = commands.Bot(command_prefix = '?', help_command=None)

bottoken ="Nzk4NTY2ODE4ODEzMDUwOTYw.X_25Tg.Fgr9xvAtE0qkJnmHL_dz4gZ3ofw"
setembedcolor = 0x66FFFF
setfooterimage = "https://media.discordapp.net/attachments/791440600301961246/797258002159239298/Pigeon_Proxies_DiscordBot.png?width=1274&height=1274"
setfootertext = "@PigeoHelpbox | Zalando Stock Checker"

@bot.event
async def on_ready():
	print('Bot is ready.')
	pass

def check_if_it_is_me(ctx):
	return ctx.message.author.id == 175953718750085121 or ctx.message.author.id == 351639955531104258 or ctx.message.author.id == 243519195529084939 or ctx.message.author.id == 272815177659842561 or ctx.message.author.id == 418649205494775820


@bot.command()
@commands.check(check_if_it_is_me)
async def zalando(ctx, link):
	text = link.split(".html")[0].split("-")[-2]
	text2 = link.split(".html")[0].split("-")[-1]
	productid = text + "-" + text2
	countrycode = str(link.split("zalando.")[1].split("/")[0])
	headers = {
		"authority": "www.zalando.de", 
		"pragma": "no-cache", 
		"cache-control": "no-cache", 
		"upgrade-insecure-requests": "1", 
		"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36", 
		"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", 
		"sec-fetch-site": "same-origin", 
		"sec-fetch-mode": "navigate", 
		"sec-fetch-user": "?1", 
		"sec-fetch-dest": "document", 
		"accept-language": "de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7"
	}

	print("Getting Stock for " + productid + " on Zalando " + countrycode)
	embed3=discord.Embed(title="Zalando Stock Checker :flag_" + countrycode + ":", description='Checking backend...', color=setembedcolor)
	embed3.set_footer(text=setfootertext, icon_url=setfooterimage)
	test91 = await ctx.send(embed=embed3)

	response = requests.get(link, headers=headers)
	soup = bs(response.content, 'html.parser')
	text = soup.find("script",{"id":"z-vegas-pdp-props"}).text
	strtext = str(text)
	newtext = strtext.replace("""\xa0€""","€").replace("<![CDATA[","")
	if countrycode == "fr" or countrycode == "es":
		newstrtext = newtext.split('"units":')[1].split(',"partnerTncUrl')[0]
	else:
		newstrtext = newtext.split('"units":')[1].split("""}]""")[0]
		newstrtext = newstrtext + "}]"
		#jsondata = json.loads(newstrtext)
		count = newstrtext.count("displayPrice")
		valuecount = newstrtext.count("value")
		newvalue2 = newstrtext.split('"percentageDiscount":')[1].split(",")[0]
		newstock = []
		legacyPartnerId = []
		newvalue = []

		for i in range(count):
			newstock.append(newstrtext.split('"stock":')[i+1].split(",")[0])
			try:
				legacyPartnerId.append(str(newstrtext.split('"legacyPartnerId":')[i+1].split(",")[0]))
			except IndexError:
				continue
		for i in range(valuecount):
			newvalue.append(newstrtext.split('"value":')[i+1].split(",")[0])
		newstock = list(newstock)
		newstock = list(dict.fromkeys(newstock))
		legacyPartnerId = list(legacyPartnerId)
		legacyPartnerId = list(dict.fromkeys(legacyPartnerId))
		newvalue = list(newvalue)
		newvalue = list(dict.fromkeys(newvalue))
		newstrtext = newstrtext.replace('"percentageDiscount":' + str(newvalue2) + ",",'"percentageDiscount":"' + str(newvalue2) + '",')
		newstrtext = newstrtext.replace("false",'"false"').replace("true",'"true"').replace(',"deliveryPromises":[]',"")
		for i in range(len(newstock)):
			newstrtext = newstrtext.replace('"stock":' + str(newstock[i]) + ",",'"stock":"' + str(newstock[i]) + '",')
		for i in range(len(legacyPartnerId)):
			try:
				newstrtext = newstrtext.replace('"legacyPartnerId":' + str(legacyPartnerId[i]) + ",",'"legacyPartnerId":"' + str(legacyPartnerId[i]) + '",')
			except IndexError:
				continue
		for i in range(len(newvalue)):
			newstrtext = newstrtext.replace('"value":'+str(newvalue[i])+",",'"value":"'+str(newvalue[i])+'",')
	jsondata = json.loads(newstrtext)
	stock = []
	size = []
	sku = []
	data = jsondata[0]
	displayPrice = data["displayPrice"]
	price = displayPrice["price"]
	correctprice = price["formatted"]
	for i in range(len(jsondata)):
		newdata = jsondata[i]
		stock.append(str(newdata["stock"]))
		manufacturer = newdata["size"]
		sku.append(str(newdata["id"]))
		size.append(str(manufacturer["local"]))

	shoepic = soup.find("meta", {"property":"og:image"})["content"]
	shoename1 = soup.find("meta", {"property":"og:title"})["content"]
	newtext = shoename1.split("-")[0]
	newtext2 = shoename1.split("-")[1]
	shoename = newtext + newtext2
	totalstock = sum(Decimal(i) for i in stock)
	discsize = "\n".join(size)
	discstock = "\n".join(stock)
	discsku = "\n".join(sku)

	embed=discord.Embed(title="Zalando Stock Checker :flag_" + countrycode + ":", description='['+str.upper(shoename)+']('+link+')', color=setembedcolor)
	embed.set_thumbnail(url=shoepic)
	embed.add_field(name=":bar_chart: Size", value=discsize, inline=True)
	embed.add_field(name=":bar_chart: Stock", value=discstock, inline=True)
	embed.add_field(name=":pushpin: SKUs", value=discsku, inline=True)
	embed.add_field(name="Total Stock", value="`"+str(totalstock)+"`", inline=True)
	embed.add_field(name="Price", value=str(correctprice), inline=True)
	embed.set_footer(text=setfootertext, icon_url=setfooterimage)
	await ctx.message.delete()
	await ctx.send(embed=embed)
	await test91.delete()

bot.run(bottoken)





