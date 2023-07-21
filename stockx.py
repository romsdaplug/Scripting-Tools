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
from discord.ext.commands import CommandNotFound,MissingRequiredArgument

bot = commands.Bot(command_prefix = '?', help_command=None)
bottoken = "YOUR_DISCORD_BOT_TOKEN"

@bot.event
async def on_ready():
	print('Bot is ready.')
	pass

def prepend(list, str): 
    # Using format() 
    str += '{0}'
    list = [str.format(i) for i in list] 
    return(list)

setfootertextstockx = "@ScriptingToolsPublic | StockX"
setfooterimage = "https://images-ext-1.discordapp.net/external/atwFnJRaXHB0ebXrVSPjVWDXe5hL2OQ0JBWopjGcVCY/https/images-ext-2.discordapp.net/external/gGrbK8FUkmby_Ao8mmH9dZ4RI1cvfkhpUNBlIB46XQE/https/media.discordapp.net/attachments/460974692073734164/680067025493950474/Wcu7EAAAAASUVORK5CYII.png"
setembedcolor = 0x000000


@bot.command()
async def stockx(context, *stockx):
	lines = context.message.content.splitlines()
	stockx = lines[0].replace("?stockx ","")
	link = lines[0].replace("?stockx ","").replace(" ","%20")

	headers = {
	    'authority': 'stockx.com',
	    'pragma': 'no-cache',
	    'cache-control': 'no-cache',
	    'appos': 'web',
	    'x-requested-with': 'XMLHttpRequest',
	    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.146 Safari/537.36',
	    'appversion': '0.1',
	    'accept': '*/*',
	    'sec-fetch-site': 'same-origin',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-dest': 'empty',
	    'referer': 'https://stockx.com/de-de/search?s=' + link,
	    'accept-language': 'de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7',
	}

	params = (
	    ('currency', 'EUR'),
	    ('_search', stockx),
	    ('dataType', 'product'),
	)

	response = requests.get('https://stockx.com/api/browse', headers=headers, params=params)
	jsondata = json.loads(response.text)
	product = jsondata["Products"][0]["urlKey"]

	producturl = "https://stockx.com/de-de/" + str(product)
	newurlsell = "https://stockx.com/api/products/" + str(product)

	headers2 = {
	    'authority': 'stockx.com',
	    'pragma': 'no-cache',
	    'cache-control': 'no-cache',
	    'appos': 'web',
	    'x-requested-with': 'XMLHttpRequest',
	    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.146 Safari/537.36',
	    'appversion': '0.1',
	    'accept': '*/*',
	    'sec-fetch-site': 'same-origin',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-dest': 'empty',
	    'referer': producturl,
	    'accept-language': 'de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7',
	}


	headers3 = {
	    'authority': 'stockx.com',
	    'pragma': 'no-cache',
	    'cache-control': 'no-cache',
	    'upgrade-insecure-requests': '1',
	    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.146 Safari/537.36',
	    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
	    'sec-fetch-site': 'none',
	    'sec-fetch-mode': 'navigate',
	    'sec-fetch-user': '?1',
	    'sec-fetch-dest': 'document',
	    'accept-language': 'de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7',
	}

	params2 = (
	    ('includes', 'market,360'),
	    ('currency', 'EUR'),
	    ('country', 'DE'),
	)

	responsesell = requests.get(newurlsell, headers=headers3, params=params2)
	jsonsell = json.loads(responsesell.text)
	sellproduct = jsonsell["Product"]
	productinfo = sellproduct["children"]

	lowestAskSize = []
	newlowestAsk = []
	lowestAsk = []
	newlowestAskSize = []
	highestBid = []
	highestBidSize = []
	newhighestBid = []
	newhighestBidSize = []
	productkey = []

	for key in productinfo.keys():
		productkey.append(key)

	for i in range(len(productinfo)):
		lowestAskSize.append(productinfo[productkey[i]]["market"]["lowestAskSize"])
		lowestAsk.append(productinfo[productkey[i]]["market"]["lowestAsk"])
		highestBid.append(productinfo[productkey[i]]["market"]["highestBid"])
		highestBidSize.append(productinfo[productkey[i]]["market"]["highestBidSize"])
		shoename = productinfo[productkey[i]]["shoe"]
		shoecw = productinfo[productkey[i]]["name"]
		shoepic = productinfo[productkey[i]]["media"]["360"][0]
		try:
			releaseDate = productinfo[productkey[i]]["releaseDate"]
		except KeyError:
			releaseDate = "N/A"
		sku = productinfo[productkey[i]]["styleId"]

	for i in range(len(lowestAskSize)):
		if lowestAsk[i] == 0 or lowestAsk[i] == None:
			newlowestAsk.append("No Ask")
		else:
			newlowestAsk.append(lowestAsk[i])

		if highestBidSize[i] == 0 or highestBidSize[i] == None:
			newhighestBidSize.append("No Ask")
		else:
			newhighestBidSize.append(highestBidSize[i])
				
		if highestBid[i] == 0 or highestBid[i] == None:
			newhighestBid.append("No Bid")
		else:
			newhighestBid.append(highestBid[i])

		if lowestAskSize[i] == 0 or lowestAskSize[i] == None:
			newlowestAskSize.append("N/A")
		else:
			newlowestAskSize.append(lowestAskSize[i])

	listindex = [index for index, value in enumerate(newlowestAskSize) if value == "N/A"]

	for i in range(len(listindex)):
	    newlowestAskSize[listindex[i]]= newhighestBidSize[listindex[i]]

	productname = str(shoename) + " " + str(shoecw)

	embedlowestask = prepend(newlowestAsk, "L: € ")
	embedhighestBid = prepend(newhighestBid, "H: € ")
	data = ",".join("{0}\n{1}".format(x,y) for x,y in zip(embedlowestask,embedhighestBid))
	data = data.split(",")
	data2 = ",".join(newlowestAskSize)
	data2 = data2.split(",")
	list(data)
	list(data2)
	newembed = list(zip(data2,data))

	embed=discord.Embed(title=productname, url = producturl, description="> *L - Lowest Ask*\n> *H - Highest Bid*\n"+"> *SKU - " + sku + "*\n> *Release Date - " + str(releaseDate) + "*",color=setembedcolor)
	for i in range(len(newembed)):
		embed.add_field(name=newembed[i][0],value=newembed[i][1],inline=True)
	embed.set_thumbnail(url=shoepic)
	embed.set_footer(text=setfootertextstockx, icon_url=setfooterimage)
	await context.send(embed=embed)

@bot.event
async def on_command_error(ctx, error):
	if isinstance(error, CommandNotFound):
		return
	elif isinstance(error,MissingRequiredArgument):
		embed=discord.Embed(title="Command Error", color=setembedcolor)
		embed.add_field(name="Error", value="Your are missing an argument", inline=True)
		embed.add_field(name="Command Format", value="?restocks <shoe name>\n?restocks <Shoe ID>", inline=False)
		embed.set_footer(text=setfootertext, icon_url=setfooterimage)
		await ctx.send(embed=embed)
		return
	raise error

bot.run(bottoken)
