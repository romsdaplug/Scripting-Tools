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
from decimal import Decimal
from discord.ext.commands import CommandNotFound,MissingRequiredArgument

bot = commands.Bot(command_prefix = '?', help_command=None)
bottoken = "YOUR_DISCORD_BOT_TOKEN"

@bot.event
async def on_ready():
	print('Bot is ready.')
	pass

setfootertextftl = "@ScriptingToolsPublic | FTL / SIDE Stock Checker | <?ftlhelp>"
setfootertextmesh = "@ScriptingToolsPublic | Mesh QT / PID Scraper | <?meshhelp>"
setfootertextnike = "@ScriptingToolsPublic | Nike Early Links | <?nikehelp>"
setfootertextorder = "@ScriptingToolsPublic | Mesh Order Tracker | <?orderhelp>"
setfootertextrestocks = "@ScriptingToolsPublic | Restocks"
setfootertextstockx = "@ScriptingToolsPublic | StockX"
setfootertextups = "@ScriptingToolsPublic | UPS Order Tracker | <?upshelp>"
setfootertextzalando = "@ScriptingToolsPublic | <?zalandohelp>"
setfooterimage = "https://images-ext-1.discordapp.net/external/atwFnJRaXHB0ebXrVSPjVWDXe5hL2OQ0JBWopjGcVCY/https/images-ext-2.discordapp.net/external/gGrbK8FUkmby_Ao8mmH9dZ4RI1cvfkhpUNBlIB46XQE/https/media.discordapp.net/attachments/460974692073734164/680067025493950474/Wcu7EAAAAASUVORK5CYII.png"
setembedcolor = 0x00000
setthumbnailorder = setfooterimage
setthumbnailups = setfooterimage

euregionhook = ["YOUR_DISCORD_WEBHOOK_URL","YOUR_DISCORD_WEBHOOK_URL2"]
asiaregionhook = ["YOUR_DISCORD_WEBHOOK_URL","YOUR_DISCORD_WEBHOOK_URL2"]
newregionhook = ["YOUR_DISCORD_WEBHOOK_URL","YOUR_DISCORD_WEBHOOK_URL2"]

def split_list(a_list):
    half = len(a_list)//2
    return a_list[:half], a_list[half:]

def divide_chunks(l, n): 
      
    # looping till length l 
    for i in range(0, len(l), n):  
        yield l[i:i + n]

def prepend(list, str): 
    # Using format() 
    str += '{0}'
    list = [str.format(i) for i in list] 
    return(list)

def check_if_it_is_me(ctx):
	return ctx.message.author.id == 175953718750085121 or ctx.message.author.id == 351639955531104258

##############################################################################################################################################################
##############################################################################################################################################################
############## FOOTLOCKER - FOOTLOCKER - FOOTLOCKER - FOOTLOCKER - FOOTLOCKER - FOOTLOCKER - FOOTLOCKER - FOOTLOCKER - FOOTLOCKER - FOOTLOCKER ###############
##############################################################################################################################################################
##############################################################################################################################################################

#@commands.has_any_role(644574705990238210,644574707475152926,806766600686010432,806855381656928266,790654515899662366,791044154351157328)
@bot.command()
async def stock(ctx, link):
	print(ctx.channel.type)
	headers = ''
	url = ''
	pid = ''
	shoename = ''
	countrycode = ''
	region = str(link.split("footlocker.")[1].split("/")[0]).replace(".","")

	if region == 'FR' or region == 'fr':
		headers = {
		'pragma': "no-cache",
		'cache-control': "no-cache",
		'accept': "application/json, text/javascript, /; q=0.01",
		'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
		'x-requested-with': "XMLHttpRequest",
		'sec-fetch-site': "same-origin",
		'sec-fetch-mode': "cors",
		'sec-fetch-dest': "empty",
		'referer': link,
		'accept-language': "de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7"
		}
		url = (
			"https://www.footlocker.fr/INTERSHOP/web/FLE"
			"/Footlocker-Footlocker_FR-Site/fr_FR/-/EUR"
			"/ViewProduct-ProductVariationSelect"
			)
		countrycode = 'fr'
		regioncountry = 'France'

	elif region == 'NL' or region == 'nl':
		headers = {
		'pragma': "no-cache",
		'cache-control': "no-cache",
		'accept': "application/json, text/javascript, /; q=0.01",
		'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
		'x-requested-with': "XMLHttpRequest",
		'sec-fetch-site': "same-origin",
		'sec-fetch-mode': "cors",
		'sec-fetch-dest': "empty",
		'referer': link,
		'accept-language': "de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7"
		}
		url = (
			"https://www.footlocker.fr/INTERSHOP/web/FLE"
			"/Footlocker-Footlocker_FR-Site/fr_FR/-/EUR"
			"/ViewProduct-ProductVariationSelect"
			)
		countrycode = 'nl'
		regioncountry = 'Netherlands'

	elif region == 'UK' or region == 'uk' or region == 'GB' or region == 'gb' or region == "couk":
		headers = {
		'pragma': "no-cache",
		'cache-control': "no-cache",
		'accept': "application/json, text/javascript, /; q=0.01",
		'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
		'x-requested-with': "XMLHttpRequest",
		'sec-fetch-site': "same-origin",
		'sec-fetch-mode': "cors",
		'sec-fetch-dest': "empty",
		'referer': link,
		'accept-language': "de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7"
		}
		url = (
			"https://www.footlocker.co.uk/INTERSHOP/web/FLE"
			"/Footlocker-Footlocker_GB-Site/en_GB/-/GBP"
			"/ViewProduct-ProductVariationSelect"
			)
		countrycode = 'gb'
		regioncountry = 'United Kingdom'

	elif region == 'SG' or region == 'sg':
		headers = {
		'pragma': "no-cache",
		'cache-control': "no-cache",
		'accept': "application/json, text/javascript, /; q=0.01",
		'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
		'x-requested-with': "XMLHttpRequest",
		'sec-fetch-site': "same-origin",
		'sec-fetch-mode': "cors",
		'sec-fetch-dest': "empty",
		'referer': link,
		'accept-language': "de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7"
		}
		url = (
			"https://www.footlocker.sg/INTERSHOP/web/FLE"
			"/FootlockerAsiaPacific-Footlocker_SG-Site/en_GB/-/SGD"
			"/ViewProduct-ProductVariationSelect"
			)
		countrycode = 'sg'
		regioncountry = 'Singapore'

	elif region == 'MY' or region == 'my':
		headers = {
		'pragma': "no-cache",
		'cache-control': "no-cache",
		'accept': "application/json, text/javascript, /; q=0.01",
		'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
		'x-requested-with': "XMLHttpRequest",
		'sec-fetch-site': "same-origin",
		'sec-fetch-mode': "cors",
		'sec-fetch-dest': "empty",
		'referer': link,
		'accept-language': "de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7"
		}
		url = (
			"https://www.footlocker.my/INTERSHOP/web/FLE"
			"/FootlockerAsiaPacific-Footlocker_MY-Site/en_GB/-/MYD"
			"/ViewProduct-ProductVariationSelect"
			)
		countrycode = 'my'
		regioncountry = 'Malaysia'

	elif region == 'HK' or region == 'hk':
		headers = {
		'pragma': "no-cache",
		'cache-control': "no-cache",
		'accept': "application/json, text/javascript, /; q=0.01",
		'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
		'x-requested-with': "XMLHttpRequest",
		'sec-fetch-site': "same-origin",
		'sec-fetch-mode': "cors",
		'sec-fetch-dest': "empty",
		'referer': link,
		'accept-language': "de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7"
		}
		url = (
			"https://www.footlocker.hk/INTERSHOP/web/FLE"
			"/FootlockerAsiaPacific-Footlocker_HK-Site/en_GB/-/HKD"
			"/ViewProduct-ProductVariationSelect"
			)
		countrycode = 'hk'
		regioncountry = 'Hong Kong'

	elif region == 'MO' or region == 'mo':
		headers = {
		'pragma': "no-cache",
		'cache-control': "no-cache",
		'accept': "application/json, text/javascript, /; q=0.01",
		'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
		'x-requested-with': "XMLHttpRequest",
		'sec-fetch-site': "same-origin",
		'sec-fetch-mode': "cors",
		'sec-fetch-dest': "empty",
		'referer': link,
		'accept-language': "de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7"
		}
		url = (
			"https://www.footlocker.mo/INTERSHOP/web/FLE"
			"/FootlockerAsiaPacific-Footlocker_MO-Site/en_GB/-/MOP"
			"/ViewProduct-ProductVariationSelect"
			)
		
		countrycode = 'mo'
		regioncountry = 'Macau'

	elif region == 'AU' or region == 'au' or region == "comau":
		headers = {
		'authority': "www.footlocker.com.au",
		'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
		'accept': "application/json, text/javascript, */*; q=0.01",
		'x-requested-with': "XMLHttpRequest",
		'sec-ch-ua-mobile': "?0",
		'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
		'sec-fetch-site': "same-origin",
		'sec-fetch-mode': "cors",
		'sec-fetch-dest': "empty",
		'referer': link,
		'accept-language': "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7"
		}
		url = ("https://www.footlocker.com.au/INTERSHOP/web/WFS/FootlockerAustraliaPacific-Footlocker_AU-Site/en_AU/-/AUD/ViewProduct-ProductVariationSelect")
		countrycode = 'au'
		regioncountry = 'Australia'

###################################################################################################################################################
#---NEW REGION------NEW REGION------NEW REGION------NEW REGION------NEW REGION------NEW REGION------NEW REGION------NEW REGION------NEW REGION---
###################################################################################################################################################


	elif region == 'IT' or region == 'it':
		url = ("https://www.footlocker.it/api/products/pdp/")
		countrycode = 'it'
		regioncountry = 'Italy'

	elif region == 'HU' or region == 'hu':
		url = ("https://www.footlocker.hu/api/products/pdp/")
		countrycode = 'hu'
		regioncountry = 'Hungary'

	elif region == 'PL' or region == 'pl':
		url = ("https://www.footlocker.pl/api/products/pdp/")
		countrycode = 'pl'
		regioncountry = 'Poland'

	elif region == 'ES' or region == 'es':
		url = ("https://www.footlocker.es/api/products/pdp/")
		countrycode = 'es'
		regioncountry = 'Spain'

	elif region == 'PT' or region == 'pt':
		url = ("https://www.footlocker.pt/api/products/pdp/")
		countrycode = 'pt'
		regioncountry = 'Portugal'

	elif region == 'GR' or region == 'gr':
		url = ("https://www.footlocker.gr/api/products/pdp/")
		countrycode = 'gr'
		regioncountry = 'Greece'

	elif region == 'AT' or region == 'at':
		url = ("https://www.footlocker.at/api/products/pdp/")
		countrycode = 'at'
		regioncountry = 'Austria'

	elif region == 'NO' or region == 'no':
		url = ("https://www.footlocker.no/api/products/pdp/")
		countrycode = 'no'
		regioncountry = 'Norway'

	elif region == 'BE' or region == 'be':
		url = ("https://www.footlocker.be/api/products/pdp/")
		countrycode = 'be'
		regioncountry = 'Belgium'

	elif region == 'IE' or region == 'ie':
		url = ("https://www.footlocker.ie/api/products/pdp/")
		countrycode = 'ie'
		regioncountry = 'Ireland'

	elif region == 'LU' or region == 'lu':
		url = ("https://www.footlocker.lu/api/products/pdp/")
		countrycode = 'lu'
		regioncountry = 'Luxembourg'

	elif region == 'CZ' or region == 'cz':
		url = ("https://www.footlocker.cz/api/products/pdp/")
		countrycode = 'cz'
		regioncountry = 'Czech Republic'

	elif region == 'SE' or region == 'se':
		url = ("https://www.footlocker.se/api/products/pdp/")
		countrycode = 'se'
		regioncountry = 'Sweden'

	elif region == 'DK' or region == 'dk':
		url = ("https://www.footlocker.dk/api/products/pdp/")
		countrycode = 'dk'
		regioncountry = 'Denmark'
		setwebhook = newregionhook
	elif region == 'DE' or region == 'de':
		url = ("https://www.footlocker.de/api/products/pdp/")
		countrycode = 'de'
		regioncountry = 'Germany'
		setwebhook = newregionhook

	else:
		await ctx.send('This region is not supported by our stock checker.')

	if region == 'FR' or region == 'fr' or region == 'NL' or region == 'nl' or region == 'UK' or region == 'couk' or region == 'GB' or region == 'gb' or region == 'SG' or region == 'sg' or region == 'MY' or region == 'my' or region == 'HK' or region == 'hk' or region == 'MO' or region == 'mo' or region == 'AU' or region == 'comau':
		pid = link.split("?v=")[1][:12]
		print("Getting Stock for " + pid + " on FTL " + countrycode)
		embed3=discord.Embed(title="Footlocker Stock Checker :flag_" + countrycode + ":", description='Checking backend...', color=setembedcolor)
		embed3.set_footer(text=setfootertextftl, icon_url=setfooterimage)
		test91 = await ctx.send(embed=embed3)
		parameters = {
		"BaseSKU": pid,
		"InventoryServerity": "ProductDetail",
		}
		getpid7 = pid + "070"
		response = requests.get(url, headers=headers, params=parameters)
		if 'Foot Locker - Please Stand By' in response.text:
			embed=discord.Embed(title="Footlocker Stock Checker - Failed", color=setembedcolor)
			img = 'https://images.footlocker.com/is/image/FLEU/' + pid + '_01?wid=763&hei=538&fmt=png-alpha'
			embed.set_thumbnail(url=img)
			embed.add_field(name="Info", value="Queue is up, we can't check stock!", inline=False)
			embed.set_footer(text=setfootertextftl, icon_url=setfooterimage)
			await ctx.send(embed=embed)
		elif 'Foot Locker - Sold Out!' in response.text:
			embed=discord.Embed(title="Footlocker Stock Checker - Failed", color=setembedcolor)
			img = 'https://images.footlocker.com/is/image/FLEU/' + pid + '_01?wid=763&hei=538&fmt=png-alpha'
			embed.set_thumbnail(url=img)
			embed.add_field(name="Info", value="Product is loaded as Sold out!", inline=False)
			embed.set_footer(text=setfootertextftl, icon_url=setfooterimage)
			await ctx.send(embed=embed)
		elif 'Please enable JS and disable any ad' in response.text:
			embed=discord.Embed(title="Footlocker Stock Checker - Failed", color=setembedcolor)
			img = 'https://images.footlocker.com/is/image/FLEU/' + pid + '_01?wid=763&hei=538&fmt=png-alpha'
			embed.set_thumbnail(url=img)
			embed.add_field(name="Info", value="Datadome is up - Please try later", inline=False)
			embed.set_footer(text=setfootertextftl, icon_url=setfooterimage)
			await ctx.send(embed=embed)
		elif not getpid7 in response.text:
			embed=discord.Embed(title="Footlocker Stock Checker - Failed", color=setembedcolor)
			response2 = requests.get(link)
			soup2 = BeautifulSoup(response2.content, "html.parser")
			img = soup2.find("meta", {"property":"og:image"})["content"]
			embed.set_thumbnail(url=img)
			embed.add_field(name="Info", value="Product has no stock loaded", inline=False)
			embed.set_footer(text=setfootertextftl, icon_url=setfooterimage)
			await ctx.send(embed=embed)
		response.raise_for_status()
		soup = BeautifulSoup(response.json()["content"], "html.parser")
		response2 = requests.get(link, headers=headers)
		soup2 = BeautifulSoup(response2.content, "html.parser")
		json_attribute_name = "data-product-variation-info-json"
		div_node = soup.find("div", {json_attribute_name: True})
		my_dict = json.loads(div_node.get(json_attribute_name))

		sizepids = list(my_dict.keys())
		data2 = "\n".join(sizepids)

		qbotsizerange = sizepids[0][-3:] + "-" + sizepids[-1][-3:]

		onlylastthreepids= []
		mojisizerange = []
		onlylastthreepids = [sub[12:] for sub in sizepids]
		for string in onlylastthreepids:
			new_string = string.replace("040", "4").replace("045", "4.5").replace("050", "5").replace("055", "5.5").replace("060", "6").replace("065", "6.5").replace("070", "7").replace("075", "7.5").replace("080", "8").replace("085", "8.5").replace("090", "9").replace("095", "9.5").replace("100", "10").replace("105", "10.5").replace("110", "11").replace("115", "11.5").replace("120", "12").replace("125", "12.5").replace("130", "13").replace("135", "13.5").replace("140", "14").replace("145", "14.5").replace("150", "15").replace("155", "15").replace("160", "16")
			mojisizerange.append(new_string)
		discordmojisizerange = ",".join(mojisizerange)

		size = []
		stock = []
		for i in my_dict:
			size.append(my_dict[i]['sizeValue'])
			if not size:
				webhook = DiscordWebhook(url=setwebhook)
				embed=DiscordEmbed(title="Footlocker Stock Checker :flag_" + countrycode + ":", description='['+str.upper(shoename)+']('+link+')', color=setembedcolor)
				embed.set_thumbnail(url=shoepic)
				embed.add_embed_field(name="Info", value="No Stock Loaded", inline=True)
				embed.set_footer(text=setfootertextftl, icon_url=setfooterimage)
				webhook.add_embed(embed)
				response = webhook.execute()
				break
			stock.append(my_dict[i]['inventoryLevel'])
			sizerange = list(size)

		for index,item in enumerate(stock):
			if item=="GREEN":
				stock[index]=":green_square:"
			elif item=="YELLOW":
				stock[index]=":yellow_square:"
			elif item=="RED":
				stock[index]=":red_square:"
		data = "\n".join("{0} {1}".format(x,y) for x,y in zip(stock,size))


		shoepic = soup2.find("meta", {"property":"og:image"})["content"]
		shoename = soup2.find("meta", {"property":"og:title"})["content"]
		shoesku = soup2.find_all("li", {"class":"fl-list--item"})
		shoelen = int(len(shoesku))-1
		shoesku = shoesku[shoelen].text
		shoesku = shoesku.replace("ID","").replace(" ","").replace(":","").replace("ProductCode","").replace("ProduktCode","").replace("Code produit","").replace("Codeproduit","").replace("Produkt Code","").replace("Product Code","")
		size8 = str(pid)+'070'
		date = my_dict[size8]['quantityMessage']
		if region == "nl":
			date = date.replace("Ce produit sera disponible à partir de","Dit product is verkrijgbaar vanaf")
		if not date:
			date = "Live"
		stockinfo = ":green_square:  -  More than 6 stock\n:yellow_square:  -  6 or less stock\n:red_square:  -  Out of Stock"

	if region == "DE" or region == "de" or region == 'IT' or region == 'it' or region == 'AT' or region == 'at' or region == 'dk' or region == 'HU' or region == 'hu' or region == 'PL' or region == 'pl' or region == 'ES' or region == 'es' or region == 'PT' or region == 'pt' or region == 'GR' or region == 'gr' or region == 'NO' or region == 'no' or region == 'BE' or region == 'be' or region == 'IE' or region == 'ie' or region == 'CZ' or region == 'cz' or region == 'SE' or region == 'se':
		pid = link.split(".html")[0][-12:]
		print("Getting Stock for " + pid + " on FTL " + countrycode)
		embed3=discord.Embed(title="Footlocker Stock Checker :flag_" + countrycode + ":", description='Checking backend...', color=setembedcolor)
		embed3.set_footer(text=setfootertextftl, icon_url=setfooterimage)
		test91 = await ctx.send(embed=embed3)
		urllink = url + pid
		response = requests.get(urllink)
		response2 = requests.get(link)
		if 'Please enable JS and disable any ad' in response.text:
			embed=discord.Embed(title="Footlocker Stock Checker - Failed", color=setembedcolor)
			img = 'https://images.footlocker.com/is/image/FLEU/' + pid + '_01?wid=763&hei=538&fmt=png-alpha'
			embed.set_thumbnail(url=img)
			embed.add_field(name="Info", value="Datadome is up - Please try later", inline=False)
			embed.set_footer(text=setfootertextftl, icon_url=setfooterimage)
			await ctx.send(embed=embed)
		elif 'FlBusinessErrorWebServiceException' in response.text:
			embed=discord.Embed(title="Footlocker Stock Checker - Failed", color=setembedcolor)
			img = 'https://images.footlocker.com/is/image/FLEU/' + pid + '_01?wid=763&hei=538&fmt=png-alpha'
			embed.set_thumbnail(url=img)
			embed.add_field(name="Info", value="An error occured, product might be pulled or sold out", inline=False)
			embed.set_footer(text=setfootertextftl, icon_url=setfooterimage)
			await ctx.send(embed=embed)
		soup2 = BeautifulSoup(response2.content, "html.parser")
		file = urlopen(urllink)
		datafile = file.read()
		my_dict = json.loads(datafile)
		file.close()

		sizelist = []
		allsizepids = []
		allstocklevel = []
		shoename = my_dict['name']
		shoepic = 'https://images.footlocker.com/is/image/FLEU/' + pid + '_01?wid=763&hei=538&fmt=png-alpha'



		for sellableUnits in my_dict['sellableUnits']:
			stocklevel = sellableUnits['stockLevelStatus']
			sizepids = sellableUnits['sku']
			size = sellableUnits['attributes'][0]['value']
			sizelist += [size]
			allsizepids += [sizepids]
			allstocklevel += [stocklevel]

		sizelistwithoutdups = []
		allsizepidswithoutdups = []
		
		allsizepids = [*map(str, allsizepids)]
		allcoorectsizepids = []
		for j,i in enumerate(allsizepids):
			if pid in i:
				allcoorectsizepids.append(i)
				sizelistwithoutdups.append(sizelist[j])
		
		data2 = "\n".join(allcoorectsizepids)
		qbotsizerange = allcoorectsizepids[0][-3:] + "-" + allcoorectsizepids[-1][-3:]
		discordmojisizerange = ",".join(sizelistwithoutdups)

		discordstocklevel = [w.replace('inStock', ':green_square:'  ) for w in allstocklevel]
		discordstocklevel = [w.replace('outOfStock', ':red_square:' ) for w in discordstocklevel]

		data = "\n".join("{0} {1}".format(x,y) for x,y in zip(discordstocklevel,sizelistwithoutdups))
		stockinfo = ':green_square:  -  Product has stock! \n :red_square:  -  Product has no stock!'
		if my_dict["variantAttributes"][0]["displayCountDownTimer"]:
			date2 = my_dict["variantAttributes"][0]["definedTimeForCountDown"]
			date = date2.replace("+0000", "")
		else:
			date = "Live"
		shoesku = "Not Available"

	embed=discord.Embed(title="Footlocker Stock Checker :flag_" + countrycode + ":", description='['+str.upper(shoename)+']('+link+')', color=setembedcolor)
	embed.set_thumbnail(url=shoepic)
	embed.add_field(name="Footlocker PID", value=str(pid), inline=True)
	embed.add_field(name="Shoe SKU", value=str(shoesku), inline=True)
	embed.add_field(name = chr(173), value = chr(173))
	embed.add_field(name="Region", value=regioncountry, inline=True)
	if date == "Live":
		embed.add_field(name="Availability", value=str(date), inline=True)
		embed.add_field(name = chr(173), value = chr(173))
	else:
		embed.add_field(name="Availability", value=str(date), inline=False)
	embed.add_field(name="Stock & Sizes", value = data, inline=True)
	embed.add_field(name="Size PIDS", value = data2, inline=True)
	embed.add_field(name="Moji Custom Size", value = discordmojisizerange, inline=False)
	embed.add_field(name="Qbot Size Range", value = qbotsizerange, inline=False)
	embed.add_field(name="Stock Information", value=stockinfo, inline=False)
	embed.set_footer(text=setfootertextftl, icon_url=setfooterimage)
	if "private" in ctx.channel.type:
		member = ctx.author
		await member.send(embed=embed)
		await test91.delete()
	else:
		await ctx.send(embed=embed)
		await test91.delete()

@bot.command()
@commands.check(check_if_it_is_me)
async def release(ctx, link):

	headers = ''
	url = ''
	pid = ''
	shoename = ''
	countrycode = ''
	region = str(link.split("footlocker.")[1].split("/")[0]).replace(".","")

	if region == 'FR' or region == 'fr':
		headers = {
		'pragma': "no-cache",
		'cache-control': "no-cache",
		'accept': "application/json, text/javascript, /; q=0.01",
		'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
		'x-requested-with': "XMLHttpRequest",
		'sec-fetch-site': "same-origin",
		'sec-fetch-mode': "cors",
		'sec-fetch-dest': "empty",
		'referer': link,
		'accept-language': "de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7"
		}
		url = (
			"https://www.footlocker.fr/INTERSHOP/web/FLE"
			"/Footlocker-Footlocker_FR-Site/fr_FR/-/EUR"
			"/ViewProduct-ProductVariationSelect"
			)
		countrycode = 'fr'
		regioncountry = 'France'
		setwebhook = euregionhook

	elif region == 'NL' or region == 'nl':
		headers = {
		'pragma': "no-cache",
		'cache-control': "no-cache",
		'accept': "application/json, text/javascript, /; q=0.01",
		'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
		'x-requested-with': "XMLHttpRequest",
		'sec-fetch-site': "same-origin",
		'sec-fetch-mode': "cors",
		'sec-fetch-dest': "empty",
		'referer': link,
		'accept-language': "de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7"
		}
		url = (
			"https://www.footlocker.fr/INTERSHOP/web/FLE"
			"/Footlocker-Footlocker_FR-Site/fr_FR/-/EUR"
			"/ViewProduct-ProductVariationSelect"
			)
		countrycode = 'nl'
		regioncountry = 'Netherlands'
		setwebhook = euregionhook

	elif region == 'UK' or region == 'couk' or region == 'GB' or region == 'gb':
		headers = {
		'pragma': "no-cache",
		'cache-control': "no-cache",
		'accept': "application/json, text/javascript, /; q=0.01",
		'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
		'x-requested-with': "XMLHttpRequest",
		'sec-fetch-site': "same-origin",
		'sec-fetch-mode': "cors",
		'sec-fetch-dest': "empty",
		'referer': link,
		'accept-language': "de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7"
		}
		url = (
			"https://www.footlocker.co.uk/INTERSHOP/web/FLE"
			"/Footlocker-Footlocker_GB-Site/en_GB/-/GBP"
			"/ViewProduct-ProductVariationSelect"
			)
		countrycode = 'gb'
		regioncountry = 'United Kingdom'
		setwebhook = euregionhook


	elif region == 'SG' or region == 'sg':
		headers = {
		'pragma': "no-cache",
		'cache-control': "no-cache",
		'accept': "application/json, text/javascript, /; q=0.01",
		'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
		'x-requested-with': "XMLHttpRequest",
		'sec-fetch-site': "same-origin",
		'sec-fetch-mode': "cors",
		'sec-fetch-dest': "empty",
		'referer': link,
		'accept-language': "de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7"
		}
		url = (
			"https://www.footlocker.sg/INTERSHOP/web/FLE"
			"/FootlockerAsiaPacific-Footlocker_SG-Site/en_GB/-/SGD"
			"/ViewProduct-ProductVariationSelect"
			)
		countrycode = 'sg'
		regioncountry = 'Singapore'
		setwebhook = asiaregionhook

	elif region == 'MY' or region == 'my':
		headers = {
		'pragma': "no-cache",
		'cache-control': "no-cache",
		'accept': "application/json, text/javascript, /; q=0.01",
		'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
		'x-requested-with': "XMLHttpRequest",
		'sec-fetch-site': "same-origin",
		'sec-fetch-mode': "cors",
		'sec-fetch-dest': "empty",
		'referer': link,
		'accept-language': "de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7"
		}
		url = (
			"https://www.footlocker.my/INTERSHOP/web/FLE"
			"/FootlockerAsiaPacific-Footlocker_MY-Site/en_GB/-/MYD"
			"/ViewProduct-ProductVariationSelect"
			)
		countrycode = 'my'
		regioncountry = 'Malaysia'
		setwebhook = asiaregionhook

	elif region == 'HK' or region == 'hk':
		headers = {
		'pragma': "no-cache",
		'cache-control': "no-cache",
		'accept': "application/json, text/javascript, /; q=0.01",
		'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
		'x-requested-with': "XMLHttpRequest",
		'sec-fetch-site': "same-origin",
		'sec-fetch-mode': "cors",
		'sec-fetch-dest': "empty",
		'referer': link,
		'accept-language': "de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7"
		}
		url = (
			"https://www.footlocker.hk/INTERSHOP/web/FLE"
			"/FootlockerAsiaPacific-Footlocker_HK-Site/en_GB/-/HKD"
			"/ViewProduct-ProductVariationSelect"
			)
		countrycode = 'hk'
		regioncountry = 'Hong Kong'
		setwebhook = asiaregionhook

	elif region == 'MO' or region == 'mo':
		headers = {
		'pragma': "no-cache",
		'cache-control': "no-cache",
		'accept': "application/json, text/javascript, /; q=0.01",
		'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
		'x-requested-with': "XMLHttpRequest",
		'sec-fetch-site': "same-origin",
		'sec-fetch-mode': "cors",
		'sec-fetch-dest': "empty",
		'referer': link,
		'accept-language': "de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7"
		}
		url = (
			"https://www.footlocker.mo/INTERSHOP/web/FLE"
			"/FootlockerAsiaPacific-Footlocker_MO-Site/en_GB/-/MOP"
			"/ViewProduct-ProductVariationSelect"
			)
		
		countrycode = 'mo'
		regioncountry = 'Macau'
		setwebhook = asiaregionhook

	elif region == 'AU' or region == 'comau':
		headers = {
		'authority': "www.footlocker.com.au",
		'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
		'accept': "application/json, text/javascript, */*; q=0.01",
		'x-requested-with': "XMLHttpRequest",
		'sec-ch-ua-mobile': "?0",
		'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
		'sec-fetch-site': "same-origin",
		'sec-fetch-mode': "cors",
		'sec-fetch-dest': "empty",
		'referer': link,
		'accept-language': "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7"
		}
		url = ("https://www.footlocker.com.au/INTERSHOP/web/WFS/FootlockerAustraliaPacific-Footlocker_AU-Site/en_AU/-/AUD/ViewProduct-ProductVariationSelect")
		countrycode = 'au'
		regioncountry = 'Australia'
		setwebhook = asiaregionhook

###################################################################################################################################################
#---NEW REGION------NEW REGION------NEW REGION------NEW REGION------NEW REGION------NEW REGION------NEW REGION------NEW REGION------NEW REGION---
###################################################################################################################################################


	elif region == 'IT' or region == 'it':
		url = ("https://www.footlocker.it/api/products/pdp/")
		countrycode = 'it'
		regioncountry = 'Italy'
		setwebhook = newregionhook

	elif region == 'DK' or region == 'dk':
		url = ("https://www.footlocker.dk/api/products/pdp/")
		countrycode = 'dk'
		regioncountry = 'Denmark'
		setwebhook = newregionhook

	elif region == 'HU' or region == 'hu':
		url = ("https://www.footlocker.hu/api/products/pdp/")
		countrycode = 'hu'
		regioncountry = 'Hungary'
		setwebhook = newregionhook

	elif region == 'PL' or region == 'pl':
		url = ("https://www.footlocker.pl/api/products/pdp/")
		countrycode = 'pl'
		regioncountry = 'Poland'
		setwebhook = newregionhook

	elif region == 'ES' or region == 'es':
		url = ("https://www.footlocker.es/api/products/pdp/")
		countrycode = 'es'
		regioncountry = 'Spain'
		setwebhook = newregionhook

	elif region == 'PT' or region == 'pt':
		url = ("https://www.footlocker.pt/api/products/pdp/")
		countrycode = 'pt'
		regioncountry = 'Portugal'
		setwebhook = newregionhook

	elif region == 'GR' or region == 'gr':
		url = ("https://www.footlocker.gr/api/products/pdp/")
		countrycode = 'gr'
		regioncountry = 'Greece'
		setwebhook = newregionhook

	elif region == 'AT' or region == 'at':
		url = ("https://www.footlocker.at/api/products/pdp/")
		countrycode = 'at'
		regioncountry = 'Austria'
		setwebhook = newregionhook

	elif region == 'NO' or region == 'no':
		url = ("https://www.footlocker.no/api/products/pdp/")
		countrycode = 'no'
		regioncountry = 'Norway'
		setwebhook = newregionhook

	elif region == 'BE' or region == 'be':
		url = ("https://www.footlocker.be/api/products/pdp/")
		countrycode = 'be'
		regioncountry = 'Belgium'
		setwebhook = newregionhook

	elif region == 'IE' or region == 'ie':
		url = ("https://www.footlocker.ie/api/products/pdp/")
		countrycode = 'ie'
		regioncountry = 'Ireland'
		setwebhook = newregionhook

	elif region == 'LU' or region == 'lu':
		url = ("https://www.footlocker.lu/api/products/pdp/")
		countrycode = 'lu'
		regioncountry = 'Luxembourg'
		setwebhook = newregionhook

	elif region == 'CZ' or region == 'cz':
		url = ("https://www.footlocker.cz/api/products/pdp/")
		countrycode = 'cz'
		regioncountry = 'Czech Republic'
		setwebhook = newregionhook

	elif region == 'SE' or region == 'se':
		url = ("https://www.footlocker.se/api/products/pdp/")
		countrycode = 'se'
		regioncountry = 'Sweden'
		setwebhook = newregionhook
	elif region == 'DE' or region == 'de':
		url = ("https://www.footlocker.de/api/products/pdp/")
		countrycode = 'de'
		regioncountry = 'Germany'
		setwebhook = newregionhook

	if region == 'FR' or region == 'fr' or region == 'NL' or region == 'nl' or region == 'UK' or region == 'couk' or region == 'GB' or region == 'gb' or region == 'SG' or region == 'sg' or region == 'MY' or region == 'my' or region == 'HK' or region == 'hk' or region == 'MO' or region == 'mo' or region == 'AU' or region == 'comau':
		pid = link.split("?v=")[1][:12]
		print("Getting Stock for " + pid + " on FTL " + countrycode)
		embed3=discord.Embed(title="Footlocker Stock Checker :flag_" + countrycode + ":", description='Checking backend...', color=setembedcolor)
		embed3.set_footer(text=setfootertextftl, icon_url=setfooterimage)
		test91 = await ctx.send(embed=embed3)
		parameters = {
		"BaseSKU": pid,
		"InventoryServerity": "ProductDetail",
		}
		getpid7 = pid + "070"
		response = requests.get(url, headers=headers, params=parameters, verify=False)
		if 'Foot Locker - Please Stand By' in response.text:
			embed=discord.Embed(title="Footlocker Stock Checker - Failed", color=setembedcolor)
			img = 'https://images.footlocker.com/is/image/FLEU/' + pid + '_01?wid=763&hei=538&fmt=png-alpha'
			embed.set_thumbnail(url=img)
			embed.add_field(name="Info", value="Queue is up, we can't check stock!", inline=False)
			embed.set_footer(text=setfootertextftl, icon_url=setfooterimage)
			await ctx.send(embed=embed)
		elif 'Foot Locker - Sold Out!' in response.text:
			embed=discord.Embed(title="Footlocker Stock Checker - Failed", color=setembedcolor)
			img = 'https://images.footlocker.com/is/image/FLEU/' + pid + '_01?wid=763&hei=538&fmt=png-alpha'
			embed.set_thumbnail(url=img)
			embed.add_field(name="Info", value="Product is loaded as Sold out!", inline=False)
			embed.set_footer(text=setfootertextftl, icon_url=setfooterimage)
			await ctx.send(embed=embed)
		elif 'Please enable JS and disable any ad' in response.text:
			embed=discord.Embed(title="Footlocker Stock Checker - Failed", color=setembedcolor)
			img = 'https://images.footlocker.com/is/image/FLEU/' + pid + '_01?wid=763&hei=538&fmt=png-alpha'
			embed.set_thumbnail(url=img)
			embed.add_field(name="Info", value="Datadome is up - Please try later", inline=False)
			embed.set_footer(text=setfootertextftl, icon_url=setfooterimage)
			await ctx.send(embed=embed)
		elif not getpid7 in response.text:
			embed=discord.Embed(title="Footlocker Stock Checker - Failed", color=setembedcolor)
			response2 = requests.get(link, headers=headers, verify=False)
			soup2 = BeautifulSoup(response2.content, "html.parser")
			img = soup2.find("meta", {"property":"og:image"})["content"]
			embed.set_thumbnail(url=img)
			embed.add_field(name="Info", value="Product has no stock loaded", inline=False)
			embed.set_footer(text=setfootertextftl, icon_url=setfooterimage)
			await ctx.send(embed=embed)

		response.raise_for_status()
		soup = BeautifulSoup(response.json()["content"], "html.parser")
		response2 = requests.get(link, headers=headers, verify=False)
		soup2 = BeautifulSoup(response2.content, "html.parser")
		json_attribute_name = "data-product-variation-info-json"
		div_node = soup.find("div", {json_attribute_name: True})
		my_dict = json.loads(div_node.get(json_attribute_name))

		sizepids = list(my_dict.keys())
		data2 = "\n".join(sizepids)

		qbotsizerange = sizepids[0][-3:] + "-" + sizepids[-1][-3:]

		onlylastthreepids= []
		mojisizerange = []
		onlylastthreepids = [sub[12:] for sub in sizepids]
		for string in onlylastthreepids:
			new_string = string.replace("040", "4").replace("045", "4.5").replace("050", "5").replace("055", "5.5").replace("060", "6").replace("065", "6.5").replace("070", "7").replace("075", "7.5").replace("080", "8").replace("085", "8.5").replace("090", "9").replace("095", "9.5").replace("100", "10").replace("105", "10.5").replace("110", "11").replace("115", "11.5").replace("120", "12").replace("125", "12.5").replace("130", "13").replace("135", "13.5").replace("140", "14").replace("145", "14.5").replace("150", "15").replace("155", "15").replace("160", "16")
			mojisizerange.append(new_string)
		discordmojisizerange = ",".join(mojisizerange)

		size = []
		stock = []
		for i in my_dict:
			size.append(my_dict[i]['sizeValue'])
			if not size:
				webhook = DiscordWebhook(url=setwebhook)
				embed=DiscordEmbed(title="Footlocker Stock Checker :flag_" + countrycode + ":", description='['+str.upper(shoename)+']('+link+')', color=setembedcolor)
				embed.set_thumbnail(url=shoepic)
				embed.add_embed_field(name="Info", value="No Stock Loaded", inline=True)
				embed.set_footer(text=setfootertextftl, icon_url=setfooterimage)
				webhook.add_embed(embed)
				response = webhook.execute()
				break
			stock.append(my_dict[i]['inventoryLevel'])
			sizerange = list(size)

		for index,item in enumerate(stock):
			if item=="GREEN":
				stock[index]=":green_square:"
			elif item=="YELLOW":
				stock[index]=":yellow_square:"
			elif item=="RED":
				stock[index]=":red_square:"
		data = "\n".join("{0} {1}".format(x,y) for x,y in zip(stock,size))


		shoepic = soup2.find("meta", {"property":"og:image"})["content"]
		shoename = soup2.find("meta", {"property":"og:title"})["content"]
		shoesku = soup2.find_all("li", {"class":"fl-list--item"})
		shoelen = int(len(shoesku))-1
		shoesku = shoesku[shoelen].text
		shoesku = shoesku.replace("ID","").replace(" ","").replace(":","").replace("ProductCode","").replace("ProduktCode","").replace("Code produit","").replace("Codeproduit","").replace("Produkt Code","").replace("Product Code","")
		size8 = str(pid)+'070'
		date = my_dict[size8]['quantityMessage']
		if region == "nl":
			date = date.replace("Ce produit sera disponible à partir de","Dit product is verkrijgbaar vanaf")
		if not date:
			date = "Live"
		stockinfo = ":green_square:  -  More than 6 stock\n:yellow_square:  -  6 or less stock\n:red_square:  -  Out of Stock"

	if region == 'DE' or region == 'de' or region == 'IT' or region == 'it' or region == 'dk' or region == 'AT' or region == 'at' or region == 'HU' or region == 'hu' or region == 'PL' or region == 'pl' or region == 'ES' or region == 'es' or region == 'PT' or region == 'pt' or region == 'GR' or region == 'gr' or region == 'NO' or region == 'no' or region == 'BE' or region == 'be' or region == 'IE' or region == 'ie' or region == 'CZ' or region == 'cz' or region == 'SE' or region == 'se':
		pid = link.split(".html")[0][-12:]
		print("Getting Stock for " + pid + " on FTL " + countrycode)
		embed3=discord.Embed(title="Footlocker Stock Checker :flag_" + countrycode + ":", description='Checking backend...', color=setembedcolor)
		embed3.set_footer(text=setfootertextftl, icon_url=setfooterimage)
		test91 = await ctx.send(embed=embed3)
		urllink = url + pid
		response = requests.get(urllink)
		response2 = requests.get(link)
		if 'Please enable JS and disable any ad' in response.text:
			embed=discord.Embed(title="Footlocker Stock Checker - Failed", color=setembedcolor)
			img = 'https://images.footlocker.com/is/image/FLEU/' + pid + '_01?wid=763&hei=538&fmt=png-alpha'
			embed.set_thumbnail(url=img)
			embed.add_field(name="Info", value="Datadome is up - Please try later", inline=False)
			embed.set_footer(text=setfootertextftl, icon_url=setfooterimage)
			await ctx.send(embed=embed)
		elif 'FlBusinessErrorWebServiceException' in response.text:
			embed=discord.Embed(title="Footlocker Stock Checker - Failed", color=setembedcolor)
			img = 'https://images.footlocker.com/is/image/FLEU/' + pid + '_01?wid=763&hei=538&fmt=png-alpha'
			embed.set_thumbnail(url=img)
			embed.add_field(name="Info", value="An error occured, product might be pulled or sold out", inline=False)
			embed.set_footer(text=setfootertextftl, icon_url=setfooterimage)
			await ctx.send(embed=embed)
		soup2 = BeautifulSoup(response2.content, "html.parser")
		file = urlopen(urllink)
		datafile = file.read()
		my_dict = json.loads(datafile)
		file.close()

		sizelist = []
		allsizepids = []
		allstocklevel = []
		shoename = my_dict['name']
		shoepic = 'https://images.footlocker.com/is/image/FLEU/' + pid + '_01?wid=763&hei=538&fmt=png-alpha'



		for sellableUnits in my_dict['sellableUnits']:
			stocklevel = sellableUnits['stockLevelStatus']
			sizepids = sellableUnits['sku']
			size = sellableUnits['attributes'][0]['value']
			sizelist += [size]
			allsizepids += [sizepids]
			allstocklevel += [stocklevel]

		sizelistwithoutdups = []
		allsizepidswithoutdups = []
		
		allsizepids = [*map(str, allsizepids)]
		allcoorectsizepids = []
		for j,i in enumerate(allsizepids):
			if pid in i:
				allcoorectsizepids.append(i)
				sizelistwithoutdups.append(sizelist[j])
		
		data2 = "\n".join(allcoorectsizepids)
		qbotsizerange = allcoorectsizepids[0][-3:] + "-" + allcoorectsizepids[-1][-3:]
		discordmojisizerange = ",".join(sizelistwithoutdups)

		discordstocklevel = [w.replace('inStock', ':green_square:'  ) for w in allstocklevel]
		discordstocklevel = [w.replace('outOfStock', ':red_square:' ) for w in discordstocklevel]

		data = "\n".join("{0} {1}".format(x,y) for x,y in zip(discordstocklevel,sizelistwithoutdups))
		stockinfo = ':green_square:  -  Product has stock! \n :red_square:  -  Product has no stock!'
		if my_dict["variantAttributes"][0]["displayCountDownTimer"]:
			date2 = my_dict["variantAttributes"][0]["definedTimeForCountDown"]
			date = date2.replace("+0000", "")
		else:
			date = "Live"
		shoesku = "Not Available"

	webhook = DiscordWebhook(url=setwebhook)
	embed = DiscordEmbed(title="Footlocker Stock Checker :flag_" + countrycode + ":", description='['+str.upper(shoename)+']('+link+')', color=setembedcolor)
	embed.add_embed_field(name="Footlocker PID", value=str(pid), inline=True)
	embed.add_embed_field(name="Shoe SKU", value=str(shoesku), inline=True)
	embed.add_embed_field(name = chr(173), value = chr(173))
	embed.add_embed_field(name="Region", value=regioncountry, inline=True)
	if date == "Live":
		embed.add_embed_field(name="Availability", value=str(date), inline=True)
		embed.add_embed_field(name = chr(173), value = chr(173))
	else:
		embed.add_embed_field(name="Availability", value=str(date), inline=False)
	embed.add_embed_field(name="Stock & Sizes", value = data, inline=True)
	embed.add_embed_field(name="Size PIDS", value = data2, inline=True)
	embed.add_embed_field(name="Moji Custom Size", value = discordmojisizerange, inline=False)
	embed.add_embed_field(name="Qbot Size Range", value = qbotsizerange, inline=False)
	embed.add_embed_field(name="Stock Information", value=stockinfo, inline=False)
	embed.set_footer(text=setfootertextftl, icon_url=setfooterimage)
	embed.set_thumbnail(url=shoepic)
	webhook.add_embed(embed)
	webhook.execute()
	if "private" in ctx.channel.type:
		member = ctx.author
		await member.send(embed=embed)
		await test91.delete()
	else:
		await ctx.send(embed=embed)
		await test91.delete()

@bot.command()
@commands.check(check_if_it_is_me)
async def side(ctx, link):
	
	headers = ''
	url = ''
	pid = ''
	shoename = ''
	countrycode = ''
	region = str(link.split("shoes.")[1].split("/")[0]).replace("\n","")
	print(region)
	if region == 'de':
		print("i'm here")
		headers = {
		'pragma': "no-cache",
		'cache-control': "no-cache",
		'accept': "application/json, text/javascript, /; q=0.01",
		'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
		'x-requested-with': "XMLHttpRequest",
		'sec-fetch-site': "same-origin",
		'sec-fetch-mode': "cors",
		'sec-fetch-dest': "empty",
		'referer': link,
		'accept-language': "de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7"
		}
		url = (
		"https://www.sidestep-shoes.de/INTERSHOP/web/WFS"
		"/Sidestep-Sidestep_DE-Site/en_GB/-/EUR"
		"/ViewProduct-ProductVariationSelect"
		)
		pid = link[-12:]
		countrycode = 'de'
		print("Getting Stock for " + pid + " on Sidestep " + countrycode)
		embed3=discord.Embed(title="Side-Step Stock Checker :flag_" + countrycode + ":", description='Checking backend...', color=setembedcolor)
		embed3.set_footer(text=setfootertextftl, icon_url=setfooterimage)
		test91 = await ctx.send(embed=embed3)
		regioncountry = 'Germany'
	elif region == 'NL' or region == 'nl':
		headers = {
		'authority': 'www.footlocker.nl',
	    'cache-control': 'max-age=0',
	    'sec-ch-ua': '"Chromium";v="88", "Google Chrome";v="88", ";Not A Brand";v="99"',
	    'sec-ch-ua-mobile': '?0',
	    'upgrade-insecure-requests': '1',
	    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36',
	    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
	    'sec-fetch-site': 'none',
	    'sec-fetch-mode': 'navigate',
	    'sec-fetch-user': '?1',
	    'sec-fetch-dest': 'document',
	    'accept-language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7',
	    'cookie': 'sto-id-47873=ALPOBFKMPMCA; fl-test-cookie-exist=Exist; fl-notice-cookie=true; country_notify=true; pgid-Footlocker-Footlocker_NL-Site=WfTmDbwkzEZSRppca.Ed8cqq0000-KnAisre; SecureSessionID-0j.sFf0LPPAAAAFNly35GNaA=1ff6888eb001885d446d7388c853d3f0ef38104a8c378f963114f44aee8c2d13; OptanonConsent=isIABGlobal=false&datestamp=Fri+Feb+05+2021+18%3A40%3A09+GMT%2B0100+(heure+normale+d%E2%80%99Europe+centrale)&version=6.7.0&landingPath=https%3A%2F%2Fwww.footlocker.nl%2Fnl%2Fp%2Fnike-dunk-high-heren-schoenen-42516%3Fv%3D314101084904&groups=1%3A1%2C2%3A1%2C3%3A1%2C4%3A0%2C101%3A0%2C102%3A0%2C103%3A0; _crbx=98d1069d-5bb6-4515-b59a-a3c692a323e4; _ga=GA1.2.1080231609.1612546810; _hjTLDTest=1; _hjid=c18e59a4-0dd1-40b2-876e-4183b9e04abf; sid=GVIuhiPMntlei0PsEp8leDZgCYkEtJcGoTOws8MAjDzp9DoqjTk3UDfu; SecureSessionID-0IsKAB2lRJkAAAE2VGg53VCE=bfc4b78796ec747649db368df9a4867b96adc59c32fad4d39589d4397ecb3bef; datadome=CIdVVE5.SRVTinKuRVthIJ-giRJV_qMwBdYJleWE.pPbG3SemClfzcK_~kHMgI.hCajNxIVdA3H~sdjldCW0WnlPMV8gV5tI_EEk15QWFP',
	    }
		url = (
		"https://www.sidestep-shoes.nl/INTERSHOP/web/WFS"
		"/Sidestep-Sidestep_NL-Site/nl_NL/-/EUR"
		"/ViewProduct-ProductVariationSelect"
		)
		pid = link[-12:]
		countrycode = 'nl'
		print("Getting Stock for " + pid + " on Sidestep " + countrycode)
		embed3=discord.Embed(title="Footlocker Stock Checker :flag_" + countrycode + ":", description='Checking backend...', color=setembedcolor)
		embed3.set_footer(text=setfootertextftl, icon_url=setfooterimage)
		test91 = await ctx.send(embed=embed3)
		regioncountry = 'Netherlands'
	else:
		await ctx.send('This region is not supported by our stock checker.')

	if region == 'de' or region == "nl":
		parameters = {
		"BaseSKU": pid,
		"InventoryServerity": "ProductDetail",
		}
		response = requests.get(url, headers=headers, params=parameters)
		if 'Foot Locker - Please Stand By' in response.text:
			embed=discord.Embed(title="Sidestep Stock Checker - Failed", color=setembedcolor)
			img = 'https://images.footlocker.com/is/image/FLEU/' + pid + '_01?wid=763&hei=538&fmt=png-alpha'
			embed.set_thumbnail(url=img)
			embed.add_field(name="Info", value="Queue is up, we can't check stock!", inline=False)
			embed.set_footer(text=setfootertextftl, icon_url=setfooterimage)
			await ctx.send(embed=embed)
		elif 'Foot Locker - Sold Out!' in response.text:
			embed=discord.Embed(title="Sidestep Stock Checker - Failed", color=setembedcolor)
			img = 'https://images.footlocker.com/is/image/FLEU/' + pid + '_01?wid=763&hei=538&fmt=png-alpha'
			embed.set_thumbnail(url=img)
			embed.add_field(name="Info", value="Product is loaded as Sold out!", inline=False)
			embed.set_footer(text=setfootertextftl, icon_url=setfooterimage)
			await ctx.send(embed=embed)
		elif 'Please enable JS and disable any ad' in response.text:
			embed=discord.Embed(title="Sidestep Stock Checker - Failed", color=setembedcolor)
			img = 'https://images.footlocker.com/is/image/FLEU/' + pid + '_01?wid=763&hei=538&fmt=png-alpha'
			embed.set_thumbnail(url=img)
			embed.add_field(name="Info", value="Datadome is up - Please try later", inline=False)
			embed.set_footer(text=setfootertextftl, icon_url=setfooterimage)
			await ctx.send(embed=embed)
		response.raise_for_status()
		soup = BeautifulSoup(response.json()["content"], "html.parser")
		response2 = requests.get(link, headers=headers)
		soup2 = BeautifulSoup(response2.content, "html.parser")
		json_attribute_name = "data-product-variation-info-json"
		div_node = soup.find("div", {json_attribute_name: True})
		my_dict = json.loads(div_node.get(json_attribute_name))
		sizepids = list(my_dict.keys())
		data2 = "\n".join(sizepids)

		qbotsizerange = sizepids[0][-3:] + "-" + sizepids[-1][-3:]

		size = []
		stock = []

		for i in my_dict:
			size.append(my_dict[i]['sizeValue'].replace(",","."))
			stock.append(my_dict[i]['inventoryLevel'])
			sizerange = list(size)
			mojisizerange = ",".join(sizerange)
		for index,item in enumerate(stock):
			if item=="GREEN":
				stock[index]=":green_square:"
			elif item=="YELLOW":
				stock[index]=":yellow_square:"
			elif item=="RED":
				stock[index]=":red_square:"
		data = "\n".join("{0} {1}".format(x,y) for x,y in zip(stock,size))
		shoepic = soup2.find("meta", {"property":"og:image"})["content"]
		shoename = soup2.find("meta", {"property":"og:title"})["content"]
		size8 = str(pid)+'070'
		stockinfo = ':green_square:  -  More than 6 stock\n:yellow_square:  -  6 or less stock\n:red_square:  -  Out of Stock'

	embed=discord.Embed(title="Sidestep Stock Checker :flag_" + countrycode + ":", description='['+str.upper(shoename)+']('+link+')', color=setembedcolor)
	embed.set_thumbnail(url=shoepic)
	embed.add_field(name="Sidestep PID", value=str(pid), inline=True)
	embed.add_field(name="Region", value=regioncountry, inline=False)
	#embed.add_field(name="Availability", value=str(date), inline=False)
	embed.add_field(name="Stock & Sizes", value = data, inline=True)
	embed.add_field(name="Size PIDS", value = data2, inline=True)
	embed.add_field(name="Moji Custom Size", value = mojisizerange, inline=False)
	embed.add_field(name="Qbot Size Range", value = qbotsizerange, inline=False)
	embed.add_field(name="Stock Information", value=stockinfo, inline=False)
	embed.set_footer(text=setfootertextftl, icon_url=setfooterimage)
	if "private" in ctx.channel.type:
		member = ctx.author
		await member.send(embed=embed)
		await test91.delete()
	else:
		await ctx.send(embed=embed)
		await test91.delete()


@bot.command()
async def ftlnew(context, link):

	loadedregion = []
	loadedregionurl = []
	notloadedregion = []
	notloadedregionurl = []

	pid = link.split(".html")[0][-12:]
	shoepic = 'https://images.footlocker.com/is/image/FLEU/' + pid + '_01?wid=763&hei=538&fmt=png-alpha'

	allregionlinksec = link.split("product/")[1]
	allregionlinksec = "product/" + allregionlinksec
	allregionlinkfirst = "https://www.footlocker."

	region = ["de/en/","at/en/","be/en/","dk/en/","gr/en/","hu/en/","ie/en/","it/en/","lu/en/","no/en/","cz/en/","pl/en/","pt/en/","es/en/","se/en/"]

	for i in range(len(region)):
		url = allregionlinkfirst + region[i] + allregionlinksec
		response = requests.get(url)
		if "Heading-main font-body-2" in response.text:
			notloadedregion.append(region[i])
			notloadedregionurl.append(url)
		elif "ProductName-alt" in response.text:
			loadedregion.append(region[i])
			loadedregionurl.append(url)

	for i in range(len(loadedregion)):
		loadedregion[i] = loadedregion[i].replace("/en/","")
		loadedregion[i] = ":flag_" + loadedregion[i] + ":"

	for i in range(len(notloadedregion)):
		notloadedregion[i] = notloadedregion[i].replace("/en/","")
		notloadedregion[i] = ":flag_" + notloadedregion[i] + ":"

	loadedURL = "\n".join("{0} {1}".format(x,y) for x,y in zip(loadedregion,loadedregionurl))
	notloadedURL = "\n".join("{0} {1}".format(x,y) for x,y in zip(notloadedregion,notloadedregionurl))


	for i in range(2):
		if i == 0:
			if not loadedURL:
				embed=discord.Embed(title="Footlocker New Region Links", color=setembedcolor)
				embed.add_field(name="Product Page Live", value="No Region is Live!", inline=False)
				embed.set_footer(text=setfootertextftl, icon_url=setfooterimage)
				embed.set_thumbnail(url=shoepic)
				await context.send(embed=embed)
			else:
				try:
					embed=discord.Embed(title="Footlocker New Region Links", color=setembedcolor)
					embed.add_field(name=":white_check_mark: Product Page Live", value=loadedURL, inline=False)
					embed.set_footer(text=setfootertextftl, icon_url=setfooterimage)
					embed.set_thumbnail(url=shoepic)
					await context.send(embed=embed)
				except(Exception):						
					loadedURL1, loadedURL2 = split_list(loadedURL)
					for j in range(2):
						if j == 0:
							embed=discord.Embed(title="Footlocker New Region Links", color=setembedcolor)
							embed.add_field(name=":white_check_mark: Product Page Live", value=loadedURL1, inline=False)
							embed.set_footer(text=setfootertextftl, icon_url=setfooterimage)
							embed.set_thumbnail(url=shoepic)
							await context.send(embed=embed)
						elif j == 1:
							embed=discord.Embed(title="Footlocker New Region Links", color=setembedcolor)
							embed.add_field(name=":white_check_mark: Product Page Live", value=loadedURL2, inline=False)
							embed.set_footer(text=setfootertextftl, icon_url=setfooterimage)
							embed.set_thumbnail(url=shoepic)
							await context.send(embed=embed)
		if i == 1:
			if not notloadedregionurl:
				embed=discord.Embed(title="Footlocker New Region Links", color=setembedcolor)
				embed.add_field(name="No Product Page loaded", value="ALL Regions are loaded!", inline=False)
				embed.set_footer(text=setfootertextftl, icon_url=setfooterimage)
				embed.set_thumbnail(url=shoepic)
				await context.send(embed=embed)
			else:
				try:
					embed=discord.Embed(title="Footlocker New Region Links", color=setembedcolor)
					embed.add_field(name=":x: No Product Page loaded", value=notloadedURL, inline=False)
					embed.set_footer(text=setfootertextftl, icon_url=setfooterimage)
					embed.set_thumbnail(url=shoepic)
					await context.send(embed=embed)
				except(Exception):			
					newloadedURL1, newloadedURL2 = split_list(notloadedURL)		
					for j in range(2):
						if j == 0:						
							embed=discord.Embed(title="Footlocker New Region Links", color=setembedcolor)
							embed.add_field(name=":x: No Product Page loaded", value=newloadedURL1, inline=False)
							embed.set_footer(text=setfootertextftl, icon_url=setfooterimage)
							embed.set_thumbnail(url=shoepic)
							await context.send(embed=embed)
						elif j == 1:
							embed=discord.Embed(title="Footlocker New Region Links", color=setembedcolor)
							embed.add_field(name=":x: No Product Page loaded", value=newloadedURL2, inline=False)
							embed.set_footer(text=setfootertextftl, icon_url=setfooterimage)
							embed.set_thumbnail(url=shoepic)
							await context.send(embed=embed)

##############################################################################################################################################################
##############################################################################################################################################################
############## MESH - MESH - MESH - MESH - MESH - MESH - MESH - MESH - MESH - MESH - MESH - MESH - MESH - MESH - MESH - MESH - MESH - MESH - MESH ############
##############################################################################################################################################################
##############################################################################################################################################################

@bot.command()
async def qt(context, store, pid):
	store = str.lower(store)
	lines = context.message.content.splitlines()
	newpid = ",".join(lines).replace("?qt ","").replace(store,"").replace(" ","")
	pid = str.lower(pid).replace("\n","").replace(" ","")
	qtpid = lines[0].replace("?qt ","").replace(store,"").replace(" ","")
	if qtpid == "":
		qtpid = lines[1]

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
	elif store == "fpde" or store == "footpatrolde":
		store = "footpatrol"
		region = "de"
		qtstore = "footpatrol"
		qtregion = "de"
		url = "https://www.footpatrol.de/product/pigeon-oos/" + pid
	elif store == "fpdk" or store == "footpatroldk":
		store = "footpatrol"
		region = "dk"
		qtstore = "footpatrol"
		qtregion = "dk"
		url = "https://www.footpatrol.dk/product/pigeon-oos/" + pid
	elif store == "fpie" or store == "footpatrolie":
		store = "footpatrol"
		region = "ie"
		qtstore = "footpatrol"
		qtregion = "ie"
		url = "https://www.footpatrol.ie/product/pigeon-oos/" + pid
	elif store == "fpit" or store == "footpatrolit":
		store = "footpatrol"
		region = "it"
		qtstore = "footpatrol"
		qtregion = "it"
		url = "https://www.footpatrol.it/product/pigeon-oos/" + pid
	elif store == "fpnl" or store == "footpatrolnl":
		store = "footpatrol"
		region = "nl"
		qtstore = "footpatrol"
		qtregion = "nl"
		url = "https://www.footpatrol.nl/product/pigeon-oos/" + pid
	elif store == "fpse" or store == "footpatrolse":
		store = "footpatrol"
		region = "se"
		qtstore = "footpatrol"
		qtregion = "se"
		url = "https://www.footpatrol.se/product/pigeon-oos/" + pid
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
	elif store == "jdmy" or store == "jdsportsmy":
		store = "jdsports"
		region = "my"
		qtstore = "jdsports"
		qtregion = "my"
		url = "https://www.jdsports." + qtregion + "/product/pigeon-oos/" + pid

	if store == "fpgb" or store == "footpatrolgb" or store == "footpatrol" or store == "fpcom" or store == "footpatrolcom" or store == "footpatroluk" or store == "fpuk" or store == "fpde" or store == "footpatrolde" or store == "fpfr" or store == "footpatrolfr" or store == "size" or store == "sz" or store == "sizeuk" or store == "sizegb" or store == "szuk" or store == "szgb" or store == "sizede" or store == "szde" or store == "sizefr" or store == "szfr" or store == "sizenl" or store == "sznl" or store == "sizees" or store == "szes" or store == "sizedk" or store == "szdk" or store == "sizeie" or store == "szie" or store == "sizese" or store == "szse" or store == "jdfr" or store == "jdsportsfr" or store == "jdgb" or store == "jduk" or store == "jdsports" or store == "jdsportsuk" or store == "jdsportsgb" or store == "jdbe" or store == "jdsportsbe" or store == "jdde" or store == "jdsportsde" or store == "jdnl" or store == "jdsportsnl" or store == "jdes" or store == "jdsportses" or store == "jdit" or store == "jdsportsit" or store == "jdat" or store == "jdsportsat" or store == "jddk" or store == "jdsportsdk" or store == "jdie" or store == "jdsportsie" or store == "jdauf" or store == "jdsportsauf" or store == "jdsportsau" or store == "jdau" or store == "jdsg" or store == "jdsportssg" or store == "jdpt" or store == "jdsportspt" or store == "jdjx" or store == "jdsportsjx" or store == "jdsportsglobal" or store == "jdglobal" or store == "jdmyf" or store == "jdsportsmyf":
		if qtstore == "" :
			underline = ""
		else:
			underline = "_"
		#print("Finishing QT for " + newpid + " / " + store + region)
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

		print("Finished QT for " + finalpidlist + " / " + store + region)		
		mbotqt = "https://mbot.app/" + store + region + "/variant/" + finalpidlist
		mbotqt = mbotqt.replace("/" + underline + qtstore + qtregion,("/")).replace("/,","/")
		hawkqt = "https://hawkmesh.com/quicktask/" + store + region+ "/" + finalpidlist
		hawkqt = hawkqt.replace("/" + underline + qtstore + qtregion,("/")).replace("/,","/")
		skulen = mbotqt.partition(qtstore + qtregion + "/")
		if store == "footpatrol":
			skulen = mbotqt.partition(qtstore + region + "/")
		skulen = list(skulen)
		print(skulen[0])
		if "mbot" in skulen[0]:
			skulen.pop(0)
		if qtstore in skulen[0]:
			skulen.pop(0)
		skulen = skulen[0].split(",")
		if qtpid == "":
			skuamount = len(skulen) - 1

		else:
			skuamount = len(skulen)
		embedlink = []
		embedlink.append("[MBOT QT]("+mbotqt+")")
		embedlink.append("[HAWK QT]("+hawkqt+")")
		embedstore = []
		embedstore.append(" - MBOT")
		embedstore.append(" - HAWK")
		embedemote = []
		embedemote.append("<:mbotoos:807792807326253077>")
		embedemote.append("<:hawkoos:807792754260181023>")
		pidlink = finalpidlist[:19] 
		url = "https://www.jdsports." + qtregion + "/product/pigeon-oos/" + pidlink
		try:
			response = requests.get(url, headers=headers)
			soup = bs(response.content, 'html.parser')
			shoepic = soup.find("meta", {"property":"og:image"})["content"]
			embed=discord.Embed(title="MESH QT", color=setembedcolor)
			if region == "uk" or region == "":
				region = "gb"
			embed.add_field(name="SKU Amount", value="*" + str(skuamount) + " SKUs loaded*")
			embed.add_field(name=str.upper(store) + " :flag_"+ str.lower(region)+":", value="[" + str(embedlink[0]) + "]" + "  [" + str(embedlink[1]) + "]", inline=False)
			embed.set_thumbnail(url=shoepic)
			embed.set_footer(text=setfootertextmesh, icon_url=setfooterimage)
			await context.send(embed=embed)
		except(Exception,TypeError):
			for i in range(2):
				embed=discord.Embed(title="MESH QT" + embedstore[i] + " " + embedemote[i], color=setembedcolor)
				if region == "uk" or region == "":
					region = "gb"
				embed.add_field(name="SKU Amount", value="*" + str(skuamount) + " SKUs loaded*", inline=True)
				embed.add_field(name=str.upper(store) + " :flag_"+ str.lower(region)+":", value="[" + str(embedlink[i]) + "]", inline=True)
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
	else:
		embed=discord.Embed(title="Command Error", color=setembedcolor)
		embed.add_field(name="Command Format", value="?qt <store> <PIDs/SKUs>", inline=False)
		embed.set_footer(text=setfootertextmesh, icon_url=setfooterimage)
		await context.send(embed=embed)

@bot.command()
async def mesh(context, link):
	link = str.lower(link)
	try:
		if "footpatrolcom" in link and len(link) < 25:
			url = "https://m.footpatrol.com/product/pigeon-oos/" + link
		elif "footpatrolfr" in link and len(link) < 25:
			url = "https://m.footpatrol.fr/product/pigeon-oos/" + link
		elif "footpatrolfi" in link and len(link) < 25:
			url = "https://m.footpatrol.fi/product/pigeon-oos/" + link
		elif "footpatrolde" in link and len(link) < 25:
			url = "https://m.footpatrol.de/product/pigeon-oos/" + link
		elif "footpatroldk" in link and len(link) < 25:
			url = "https://m.footpatrol.dk/product/pigeon-oos/" + link
		elif "footpatrolit" in link and len(link) < 25:
			url = "https://m.footpatrol.it/product/pigeon-oos/" + link
		elif "footpatrolnl" in link and len(link) < 25:
			url = "https://m.footpatrol.nl/product/pigeon-oos/" + link
		elif "footpatrolse" in link and len(link) < 25:
			url = "https://m.footpatrol.se/product/pigeon-oos/" + link
		elif "footpatrolie" in link and len(link) < 25:
			url = "https://m.footpatrol.ie/product/pigeon-oos/" + link
		elif "sizeuk" in link and len(link) < 25:
			link = link.replace("sizeuk","").replace("_","")
			url = "https://m.size.co.uk/product/pigeon-oos/" + link
		elif "sizegb" in link and len(link) < 25:
			link = link.replace("sizegb","").replace("_","")
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
			link = link.replace("jdsportsuk","").replace("_","")
			url = "https://m.jdsports.co.uk/product/pigeon-oos/" + link
		elif "jduk" in link and len(link) < 25:
			link = link.replace("jduk","").replace("_","")
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
			embed=discord.Embed(title="Error Scraping SKUs", color=setembedcolor)
			embed.add_field(name=":flag_gb: SKU Scraper via PID - JDSports", value="Make sure to add `jd, jdsportsuk or jduk` to the end of the pid", inline=False)
			embed.add_field(name=":flag_gb: SKU Scraper via PID - Size?", value="Make sure to add `sz, sizeuk or szuk` to the end of the pid", inline=False)
			embed.set_footer(text=setfootertextmesh, icon_url=setfooterimage)
			await context.send(embed=embed)
		else:
			if link.split('//')[1].split('.')[0] == "www":
				url = link.replace("www","m")
			else:
				url = link
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
			meshpic = ["space holder","https://media.discordapp.net/attachments/681635149586104343/804628109399687188/J_0r5Du6_400x400.png","https://media.discordapp.net/attachments/681635149586104343/804628280434753596/7UR98tbB_400x400.png"]
			try:
				embed=discord.Embed(title="MESH PID SCRAPER", color=setembedcolor)
				if region == "uk" or region == "":
					region = "gb"
				embed.add_field(name="Store", value=str.upper(store) + " :flag_" + region + ":", inline=False)
				embed.add_field(name="Size SKU", value=embedpids, inline=True)
				embed.add_field(name="Size", value=embedpids2, inline=True)
				embed.add_field(name="QT", value=embedpids3, inline=True)
				embed.add_field(name="QT for all SKUs", value=mbotqtallpids + " " + hawkqtallpids, inline=False)
				embed.set_thumbnail(url=shoepic)
				embed.set_footer(text=setfootertextmesh, icon_url=setfooterimage)
				await context.send(embed=embed)
			except(Exception):
				for i in range(3):
					if i == 0:
						embed=discord.Embed(title="MESH PID SCRAPER", color=setembedcolor)
						if region == "uk" or region == "":
							region = "gb"
						embed.add_field(name="Store", value=str.upper(store) + " :flag_" + region + ":", inline=False)
						embed.add_field(name="Size SKU", value=embedpids, inline=True)
						embed.add_field(name="Size", value=embedpids2, inline=True)
						embed.set_thumbnail(url=shoepic)
						embed.set_footer(text=setfootertextmesh, icon_url=setfooterimage)
						await context.send(embed=embed)
					else:
						embed=discord.Embed(title="MESH QT" + embedstore[i] + " " + embedemote[i], color=setembedcolor)
						if region == "uk" or region == "":
							region = "gb"
						embed.add_field(name="SKU Amount", value="*" + str(skuamount) + " SKUs loaded*", inline=True)
						embed.add_field(name=str.upper(store) + " :flag_"+ str.lower(region)+":", value=str(embedlink[i]), inline=True)
						embed.set_thumbnail(url=shoepic)
						embed.set_footer(text=setfootertextmesh, icon_url=setfooterimage)
						await context.send(embed=embed)
	except(Exception,IndexError):
		embed=discord.Embed(title="Error scraping SKUs", color=setembedcolor)
		embed.add_field(name="Error - 2", value="Check your PID or use `?meshhelp for more information", inline=False)
		embed.add_field(name="Command", value="?pid <link>   or   ?pid <pid>", inline=False)
		embed.add_field(name=":flag_gb: JDSports UK", value="Make sure to add `jdsportsuk or jduk` to the end of the pid", inline=False)
		embed.add_field(name=":flag_gb: Size? UK", value="Make sure to add `sizeuk or szuk` to the end of the pid", inline=False)
		embed.set_footer(text=setfootertextmesh, icon_url=setfooterimage)
		await context.send(embed=embed)

##############################################################################################################################################################
##############################################################################################################################################################
############## NIKE EARLY LINKS - NIKE EARLY LINKS - NIKE EARLY LINKS - NIKE EARLY LINKS - NIKE EARLY LINKS - NIKE EARLY LINKS - NIKE EARLY LINKS ############
##############################################################################################################################################################
##############################################################################################################################################################

@bot.command()
async def nike(context, link):
	nikeregion = link.split("www.nike.com/")[1].split("/")[0]
	headers = {
	    'authority': 'www.nike.com',
	    'pragma': 'no-cache',
	    'cache-control': 'no-cache',
	    'upgrade-insecure-requests': '1',
	    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.146 Safari/537.36',
	    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
	    'sec-fetch-site': 'same-origin',
	    'sec-fetch-mode': 'navigate',
	    'sec-fetch-user': '?1',
	    'sec-fetch-dest': 'document',
	    'accept-language': 'de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7',
	}
	if nikeregion == "ch":
		firstpartlink = link.split("ch/")[0]
		secondpartlink = link.split("/launch/")[1]

		response = requests.get(link, headers=headers)
		soup = bs(response.content, 'html.parser')
		text = soup.find("meta", {"name":"branch:deeplink:productId"})["content"]
		shoepic = soup.find("meta", {"property":"og:image"})["content"]
		sizes = ["4","4.5","5","5.5","6","6.5","7","7.5","8","8.5","9","9.5","10","10.5","11","11.5","12","12.5"]
		region = ["ch/en","ch/fr","ch/de","ch/it"]
		country = ["gb","fr","de","it"]
		earlylink = []
		for i in range(len(region)):
			for j in range(len(sizes)):
				earlylink.append(str("[US " + str(sizes[j]) + "](" + firstpartlink + str(region[i]) + "/launch/" + secondpartlink + "?productId=" + str(text) + "&size=" + str(sizes[j]) + ")"))
			lenearlylink = len(earlylink)
			n = 6
			embedlistsizes = list(divide_chunks(earlylink, n))

			if region[i] == "ch/en":
				embedlistsizes[0] = "\n".join(embedlistsizes[0])
				embedlistsizes[1] = "\n".join(embedlistsizes[1])
				embedlistsizes[2] = "\n".join(embedlistsizes[2])
				embed=discord.Embed(title="Nike CH - Early Links - " + str.upper(region[i]) + " " + ":flag_" + str(country[i]) + ":", color=setembedcolor)
				embed.add_field(name="Checkout Link", value=embedlistsizes[0], inline=True)
				embed.add_field(name="Checkout Link", value=embedlistsizes[1], inline=True)
				embed.add_field(name="Checkout Link", value=embedlistsizes[2], inline=True)
				embed.set_footer(text=setfootertextnike, icon_url=setfooterimage)
				embed.set_thumbnail(url=shoepic)
				await context.send(embed=embed)
			if region[i] == "ch/fr":
				embedlistsizes[3] = "\n".join(embedlistsizes[3])
				embedlistsizes[4] = "\n".join(embedlistsizes[4])
				embedlistsizes[5] = "\n".join(embedlistsizes[5])
				embed=discord.Embed(title="Nike CH - Early Links - " + str.upper(region[i]) + " " + ":flag_" + str(country[i]) + ":", color=setembedcolor)
				embed.add_field(name="Checkout Link", value=embedlistsizes[3], inline=True)
				embed.add_field(name="Checkout Link", value=embedlistsizes[4], inline=True)
				embed.add_field(name="Checkout Link", value=embedlistsizes[5], inline=True)
				embed.set_footer(text=setfootertextnike, icon_url=setfooterimage)
				embed.set_thumbnail(url=shoepic)
				await context.send(embed=embed)
			if region[i] == "ch/de":
				embedlistsizes[6] = "\n".join(embedlistsizes[6])
				embedlistsizes[7] = "\n".join(embedlistsizes[7])
				embedlistsizes[8] = "\n".join(embedlistsizes[8])
				embed=discord.Embed(title="Nike CH - Early Links - " + str.upper(region[i]) + " " + ":flag_" + str(country[i]) + ":", color=setembedcolor)
				embed.add_field(name="Checkout Link", value=embedlistsizes[6], inline=True)
				embed.add_field(name="Checkout Link", value=embedlistsizes[7], inline=True)
				embed.add_field(name="Checkout Link", value=embedlistsizes[8], inline=True)
				embed.set_footer(text=setfootertextnike, icon_url=setfooterimage)
				embed.set_thumbnail(url=shoepic)
				await context.send(embed=embed)
			if region[i] == "ch/it":
				embedlistsizes[9] = "\n".join(embedlistsizes[9])
				embedlistsizes[10] = "\n".join(embedlistsizes[10])
				embedlistsizes[11] = "\n".join(embedlistsizes[11])
				embed=discord.Embed(title="Nike CH - Early Links - " + str.upper(region[i]) + " " + ":flag_" + str(country[i]) + ":", color=setembedcolor)
				embed.add_field(name="Checkout Link", value=embedlistsizes[9], inline=True)
				embed.add_field(name="Checkout Link", value=embedlistsizes[10], inline=True)
				embed.add_field(name="Checkout Link", value=embedlistsizes[11], inline=True)
				embed.set_footer(text=setfootertextnike, icon_url=setfooterimage)
				embed.set_thumbnail(url=shoepic)
				await context.send(embed=embed)


	elif nikeregion == "au":
		firstpartlink = link.split("au/")[0]
		secondpartlink = link.split("/launch/")[1]

		response = requests.get(link, headers=headers)
		soup = bs(response.content, 'html.parser')
		text = soup.find("meta", {"name":"branch:deeplink:productId"})["content"]
		shoepic = soup.find("meta", {"property":"og:image"})["content"]
		sizes = ["4","4.5","5","5.5","6","6.5","7","7.5","8","8.5","9","9.5","10","10.5","11","11.5","12","12.5"]
		region = ["au"]
		country = ["au"]
		earlylink = []
		for i in range(len(region)):
			for j in range(len(sizes)):
				earlylink.append(str("[US " + str(sizes[j]) + "](" + firstpartlink + str(region[i]) + "/launch/" + secondpartlink + "?productId=" + str(text) + "&size=" + str(sizes[j]) + ")"))
			lenearlylink = len(earlylink)
			n = 6
			embedlistsizes = list(divide_chunks(earlylink, n))

			embedlistsizes[0] = "\n".join(embedlistsizes[0])
			embedlistsizes[1] = "\n".join(embedlistsizes[1])
			embedlistsizes[2] = "\n".join(embedlistsizes[2])
			embed=discord.Embed(title="Nike AU - Early Links - " + str.upper(region[i]) + " " + ":flag_" + str(country[i]) + ":", color=setembedcolor)
			embed.add_field(name="Checkout Link", value=embedlistsizes[0], inline=True)
			embed.add_field(name="Checkout Link", value=embedlistsizes[1], inline=True)
			embed.add_field(name="Checkout Link", value=embedlistsizes[2], inline=True)
			embed.set_footer(text=setfootertextnike, icon_url=setfooterimage)
			embed.set_thumbnail(url=shoepic)
			await context.send(embed=embed)

	elif nikeregion == "ca":
		firstpartlink = link.split("ca/")[0]
		secondpartlink = link.split("/launch/")[1]

		response = requests.get(link, headers=headers)
		soup = bs(response.content, 'html.parser')
		text = soup.find("meta", {"name":"branch:deeplink:productId"})["content"]
		shoepic = soup.find("meta", {"property":"og:image"})["content"]
		sizes = ["4","4.5","5","5.5","6","6.5","7","7.5","8","8.5","9","9.5","10","10.5","11","11.5","12","12.5"]
		region = ["ca","ca/fr"]
		country = ["ca","fr"]
		earlylink = []
		for i in range(len(region)):
			for j in range(len(sizes)):
				earlylink.append(str("[US " + str(sizes[j]) + "](" + firstpartlink + region[i] + "/launch/" + secondpartlink + "?productId=" + str(text) + "&size=" + str(sizes[j]) + ")"))
			lenearlylink = len(earlylink)
			n = 6
			embedlistsizes = list(divide_chunks(earlylink, n))

			if region[i] == "ca":
				embedlistsizes[0] = "\n".join(embedlistsizes[0])
				embedlistsizes[1] = "\n".join(embedlistsizes[1])
				embedlistsizes[2] = "\n".join(embedlistsizes[2])
				embed=discord.Embed(title="Nike CA - Early Links - " + str.upper(region[i]) + " " + ":flag_" + str(country[i]) + ":", color=setembedcolor)
				embed.add_field(name="Checkout Link", value=embedlistsizes[0], inline=True)
				embed.add_field(name="Checkout Link", value=embedlistsizes[1], inline=True)
				embed.add_field(name="Checkout Link", value=embedlistsizes[2], inline=True)
				embed.set_footer(text=setfootertextnike, icon_url=setfooterimage)
				embed.set_thumbnail(url=shoepic)
				await context.send(embed=embed)
			if region[i] == "ca/fr":
				embedlistsizes[3] = "\n".join(embedlistsizes[3])
				embedlistsizes[4] = "\n".join(embedlistsizes[4])
				embedlistsizes[5] = "\n".join(embedlistsizes[5])
				embed=discord.Embed(title="Nike CA - Early Links - " + str.upper(region[i]) + " " + ":flag_" + str(country[i]) + ":", color=setembedcolor)
				embed.add_field(name="Checkout Link", value=embedlistsizes[3], inline=True)
				embed.add_field(name="Checkout Link", value=embedlistsizes[4], inline=True)
				embed.add_field(name="Checkout Link", value=embedlistsizes[5], inline=True)
				embed.set_footer(text=setfootertextnike, icon_url=setfooterimage)
				embed.set_thumbnail(url=shoepic)
				await context.send(embed=embed)

	elif nikeregion == "ru":
		firstpartlink = link.split("ru/")[0]
		secondpartlink = link.split("/launch/")[1]

		response = requests.get(link, headers=headers)
		soup = bs(response.content, 'html.parser')
		text = soup.find("meta", {"name":"branch:deeplink:productId"})["content"]
		shoepic = soup.find("meta", {"property":"og:image"})["content"]
		sizes = ["4","4.5","5","5.5","6","6.5","7","7.5","8","8.5","9","9.5","10","10.5","11","11.5","12","12.5"]
		region = ["ru"]
		country = ["ru"]
		earlylink = []
		for i in range(len(region)):
			for j in range(len(sizes)):
				earlylink.append(str("[US " + str(sizes[j]) + "](" + firstpartlink + str(region[i]) + "/launch/" + secondpartlink + "?productId=" + str(text) + "&size=" + str(sizes[j]) + ")"))
			lenearlylink = len(earlylink)
			n = 6
			embedlistsizes = list(divide_chunks(earlylink, n))

			embedlistsizes[0] = "\n".join(embedlistsizes[0])
			embedlistsizes[1] = "\n".join(embedlistsizes[1])
			embedlistsizes[2] = "\n".join(embedlistsizes[2])
			embed=discord.Embed(title="Nike RU - Early Links - " + str.upper(region[i]) + " " + ":flag_" + str(country[i]) + ":", color=setembedcolor)
			embed.add_field(name="Checkout Link", value=embedlistsizes[0], inline=True)
			embed.add_field(name="Checkout Link", value=embedlistsizes[1], inline=True)
			embed.add_field(name="Checkout Link", value=embedlistsizes[2], inline=True)
			embed.set_footer(text=setfootertextnike, icon_url=setfooterimage)
			embed.set_thumbnail(url=shoepic)
			await context.send(embed=embed)
	elif nikeregion == "sg":
		firstpartlink = link.split("sg/")[0]
		secondpartlink = link.split("/launch/")[1]

		response = requests.get(link, headers=headers)
		soup = bs(response.content, 'html.parser')
		text = soup.find("meta", {"name":"branch:deeplink:productId"})["content"]
		shoepic = soup.find("meta", {"property":"og:image"})["content"]
		sizes = ["4","4.5","5","5.5","6","6.5","7","7.5","8","8.5","9","9.5","10","10.5","11","11.5","12","12.5"]
		region = ["sg"]
		country = ["sg"]
		earlylink = []
		for i in range(len(region)):
			for j in range(len(sizes)):
				earlylink.append(str("[US " + str(sizes[j]) + "](" + firstpartlink + str(region[i]) + "/launch/" + secondpartlink + "?productId=" + str(text) + "&size=" + str(sizes[j]) + ")"))
			lenearlylink = len(earlylink)
			n = 6
			embedlistsizes = list(divide_chunks(earlylink, n))

			embedlistsizes[0] = "\n".join(embedlistsizes[0])
			embedlistsizes[1] = "\n".join(embedlistsizes[1])
			embedlistsizes[2] = "\n".join(embedlistsizes[2])
			embed=discord.Embed(title="Nike SG - Early Links - " + str.upper(region[i]) + " " + ":flag_" + str(country[i]) + ":", color=setembedcolor)
			embed.add_field(name="Checkout Link", value=embedlistsizes[0], inline=True)
			embed.add_field(name="Checkout Link", value=embedlistsizes[1], inline=True)
			embed.add_field(name="Checkout Link", value=embedlistsizes[2], inline=True)
			embed.set_footer(text=setfootertextnike, icon_url=setfooterimage)
			embed.set_thumbnail(url=shoepic)
			await context.send(embed=embed)

##############################################################################################################################################################
##############################################################################################################################################################
############## MESH ORDER TRACKER - MESH ORDER TRACKER - MESH ORDER TRACKER - MESH ORDER TRACKER - MESH ORDER TRACKER - MESH ORDER TRACKER - ORDER TRACKER ###
##############################################################################################################################################################
##############################################################################################################################################################

@bot.command()
async def order(ctx, store, postcode, orderno: int):
	lines = ctx.message.content.splitlines()
	lines.pop(0)
	linescount = len(lines)
	if linescount == 0:
		test1 = discord.Embed(title="Mesh Order Tracker - Error",  colour=setembedcolor)
		test1.add_field(name="Error", value="Make sure Ordernumbers are posted in next line!\nExample:\n```?order jdde 79798\n714151764``")
		test1.set_footer(text=setfootertextorder, icon_url=setfooterimage)
		test1.set_thumbnail(url=setthumbnailorder)
		await ctx.send(embed = test1)
	user_name_id = ctx.author.name + ' ID : ' + str(ctx.author.id)
	log3 = Fore.CYAN + f'[{user_name_id}] '
	log4 = "[ORDER TRACKER]"
	log = log3 + log4
	now = datetime.now()

	if store == "fpgb" or store == "footpatrolgb" or store == "footpatroluk" or store == "fpuk" or store == "fpcom" or store == "footpatrolcom":
		store = "footpatrolcom"
		region = "gb"
	elif store == "fpfr" or store == "footpatrolfr":
		store = "footpatrol"
		region = "fr"
	elif store == "size" or store == "sz" or store == "sizeuk" or store == "sizegb" or store == "szuk" or store == "szgb":
		store = "size"
		region = ""
	elif store == "sizede" or store == "szde":
		store = "size"
		region = "de"
	elif store == "sizefr" or store == "szfr":
		store = "size"
		region = "fr"
	elif store == "sizenl" or store == "sznl":
		store = "size"
		region = "nl"
	elif store == "sizees" or store == "szes":
		store = "size"
		region = "es"
	elif store == "sizedk" or store == "szdk":
		store = "size"
		region = "dk"
	elif store == "sizeie" or store == "szie":
		store = "size"
		region = "ie"
	elif store == "sizese" or store == "szse":
		store = "size"
		region = "se"
	elif store == "jdgb" or store == "jduk" or store == "jdsports" or store == "jdsportsuk" or store == "jdsportsgb":
		store = "jdsports"
		region = "uk"
	elif store == "jdfr" or store == "jdsportsfr":
		store = "jdsports"
		region = "fr"
	elif store == "jdde" or store == "jdsportsde":
		store = "jdsports"
		region = "de"
	elif store == "jdbe" or store == "jdsportsbe":
		store = "jdsports"
		region = "be"
	elif store == "jdnl" or store == "jdsportsnl":
		store = "jdsports"
		region = "nl"
	elif store == "jdes" or store == "jdsportses":
		store = "jdsports"
		region = "es"
	elif store == "jdit" or store == "jdsportsit":
		store = "jdsports"
		region = "it"
	elif store == "jdat" or store == "jdsportsat":
		store = "jdsports"
		region = "at"
	elif store == "jddk" or store == "jdsportsdk":
		store = "jdsports"
		region = "dk"
	elif store == "jdie" or store == "jdsportsie":
		store = "jdsports"
		region = "ie"
	elif store == "jdauf" or store == "jdsportsauf" or store == "jdsportsau" or store == "jdau":
		store = "jdsports"
		region = "auf"
	elif store == "jdsg" or store == "jdsportssg":
		store = "jdsports"
		region = "sg"
	elif store == "jdpt" or store == "jdsportspt":
		store = "jdsports"
		region = "pt"
	elif store == "jdjx" or store == "jdsportsjx" or store == "jdsportsglobal" or store == "jdglobal":
		store = "jdsports"
		region = "jx"
	elif store == "jdmyf" or store == "jdsportsmyf":
		store = "jdsports"
		region = "myf"

	for i in lines:
		try:
			base_url = 'https://data.smartagent.io/v1/jdsports/track-my-order'
			track_url = ''
			track_url = base_url+'?orderNumber='+str(i)+'&fascia='+store+region+'&postcode='+str(postcode)
			r = requests.get(track_url)
			response = r.text
			if 'Order not found' in response:
				test1 = discord.Embed(title="Mesh Order Tracker - Summary",  colour=setembedcolor)
				test1.add_field(name="Order not found!", value="Please check your ordernumber and zip code or use ?orderhelp for more infos")
				test1.set_footer(text=setfootertextorder, icon_url=setfooterimage)
				test1.set_thumbnail(url=setthumbnailorder)
				await ctx.send(embed = test1)
			test = json.loads(response)
			a2 = test['status']['short']
			a4 = test['vendors']
			date = a2[0]['date']
			date = datetime.fromisoformat(date[:-1])
			date.strftime('%Y-%m-%d %H:%M:%S')
			a5 = a4[0]['items']
			sku = a5[0]['sku']
			name = a5[0]['name']
			img = a5[0]['img']
			size = a5[0]['size']
			price_before = a5[0]['price']
			price_number = price_before['amount']
			price_currency = price_before['currency']
			price_final = price_number + ' ' + price_currency
			color = ''
			status = ''
			tracking1 = ''
			tracking2 = ''
			if 'Your order is currently being processed.' in response:
				status = 'Your order is currently being processed.'
				color = '16776960'
			elif 'Your order has been placed.' in response:
				status = 'Your order has been placed.'
				color = '16776960'
			elif 'Your order has been despatched.' in response:
				if '"trackingURL":null' in response:
					tracking2 = 'N/A'
				a12 = test['delivery']
				tracking1 = a12['courier']
				tracking2 = a12['trackingURL']
				status = 'Your order has been despatched.'
				color = '65280'
			elif 'Your order has been delivered.' in response:
				a12 = test['delivery']
				tracking1 = a12['courier']
				tracking2 = a12['trackingURL']
				status = 'Your order has been delivered.'
				color = '65280'
			elif 'It looks like your order has been cancelled.' in response:
				status = 'It looks like your order has been cancelled.'
				color = '16711680'
			elif 'It looks like there was an issue taking payment for this order' in response:
				status = 'It looks like there was an issue taking payment for this order.'
				color = '16711680'
			print(Fore.MAGENTA + f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]"+ log + Fore.GREEN + f"[Tracking Ordernumber - {i}]")
			test1 = discord.Embed(title=name, description=status,  colour=discord.Colour(int(color)))
			test1.set_footer(text='Mesh Order Tracker', icon_url="https://cdn.discordapp.com/attachments/763496861293740102/763512882927108157/67825d35ea85713884df69d5e6f4a9d6.png")
			test1.add_field(name='Size', value=size, inline=True)
			test1.add_field(name='Price', value=price_final, inline=True)
			test1.add_field(name='Order Number', value='||'+str(i)+'||', inline=True)
			test1.add_field(name='Order Date', value=date, inline=False)
			if '"trackingURL":"http' in response:
				test1.add_field(name='Tracking', value='['+tracking1+']('+tracking2+')', inline=True)
			elif '"trackingURL":null' and 'Your order has been despatched.' in response:
				test1.add_field(name='Tracking', value=tracking2, inline=True)
			else:
				print('')
			test1.set_footer(text=setfootertextorder, icon_url=setfooterimage)
			test1.set_thumbnail(url=img)
			print(Fore.MAGENTA + f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]" + log + Fore.GREEN + "[Webhook sent!]")
			print('')
			await ctx.send(embed = test1)
		except KeyError:
			test1 = discord.Embed(title="Mesh Order Tracker - Summary",  colour=setembedcolor)
			test1.add_field(name="Order not found!", value="Please check your ordernumber and zip code or use ?orderhelp for more infos")
			test1.set_footer(text=setfootertextorder, icon_url=setfooterimage)
			test1.set_thumbnail(url=setthumbnailorder)
			await ctx.send(embed = test1)

@bot.command()
async def orderbulk(ctx, store, postcode, orderno: int):
	lines = ctx.message.content.splitlines()
	lines.pop(0)
	linescount = len(lines)
	if linescount == 0:
		test1 = discord.Embed(title="Mesh Order Tracker - Error",  colour=setembedcolor)
		test1.add_field(name="Error", value="Make sure Ordernumbers are posted in next line!\nExample:\n```?orderbulk jdde 79798\n714151769\n714151768``")
		test1.set_footer(text=setfootertextorder, icon_url=setfooterimage)
		test1.set_thumbnail(url=setthumbnailorder)
		await ctx.send(embed = test1)
	orderproc = 0
	orderdel = 0
	orderplaced = 0
	orderdis = 0
	orderproc = 0
	ordercan = 0
	orderpay = 0
	ordernotfound = 0
	user_name_id = ctx.author.name + ' ID : ' + str(ctx.author.id)
	log3 = Fore.CYAN + f'[{user_name_id}] '
	log4 = "[ORDER TRACKER]"
	log = log3 + log4
	now = datetime.now()

	if store == "fpgb" or store == "footpatrolgb" or store == "footpatroluk" or store == "fpuk" or store == "fpcom" or store == "footpatrolcom":
		store = "footpatrolcom"
		region = "gb"
	elif store == "fpfr" or store == "footpatrolfr":
		store = "footpatrol"
		region = "fr"
	elif store == "size" or store == "sz" or store == "sizeuk" or store == "sizegb" or store == "szuk" or store == "szgb":
		store = "size"
		region = ""
	elif store == "sizede" or store == "szde":
		store = "size"
		region = "de"
	elif store == "sizefr" or store == "szfr":
		store = "size"
		region = "fr"
	elif store == "sizenl" or store == "sznl":
		store = "size"
		region = "nl"
	elif store == "sizees" or store == "szes":
		store = "size"
		region = "es"
	elif store == "sizedk" or store == "szdk":
		store = "size"
		region = "dk"
	elif store == "sizeie" or store == "szie":
		store = "size"
		region = "ie"
	elif store == "sizese" or store == "szse":
		store = "size"
		region = "se"
	elif store == "jdgb" or store == "jduk" or store == "jdsports" or store == "jdsportsuk" or store == "jdsportsgb":
		store = "jdsports"
		region = "uk"
	elif store == "jdfr" or store == "jdsportsfr":
		store = "jdsports"
		region = "fr"
	elif store == "jdde" or store == "jdsportsde":
		store = "jdsports"
		region = "de"
	elif store == "jdbe" or store == "jdsportsbe":
		store = "jdsports"
		region = "be"
	elif store == "jdnl" or store == "jdsportsnl":
		store = "jdsports"
		region = "nl"
	elif store == "jdes" or store == "jdsportses":
		store = "jdsports"
		region = "es"
	elif store == "jdit" or store == "jdsportsit":
		store = "jdsports"
		region = "it"
	elif store == "jdat" or store == "jdsportsat":
		store = "jdsports"
		region = "at"
	elif store == "jddk" or store == "jdsportsdk":
		store = "jdsports"
		region = "dk"
	elif store == "jdie" or store == "jdsportsie":
		store = "jdsports"
		region = "ie"
	elif store == "jdauf" or store == "jdsportsauf" or store == "jdsportsau" or store == "jdau":
		store = "jdsports"
		region = "auf"
	elif store == "jdsg" or store == "jdsportssg":
		store = "jdsports"
		region = "sg"
	elif store == "jdpt" or store == "jdsportspt":
		store = "jdsports"
		region = "pt"
	elif store == "jdjx" or store == "jdsportsjx" or store == "jdsportsglobal" or store == "jdglobal":
		store = "jdsports"
		region = "jx"
	elif store == "jdmyf" or store == "jdsportsmyf":
		store = "jdsports"
		region = "myf"

	test1 = discord.Embed(title="Mesh Order Tracker - Summary", description="Tracking " + str(len(lines)) + " orders!",  colour=setembedcolor)
	test1.set_footer(text=setfootertextorder, icon_url=setfooterimage)
	await ctx.send(embed = test1)

	for i in lines:
		try:
			base_url = 'https://data.smartagent.io/v1/jdsports/track-my-order'
			track_url = ''
			track_url = base_url+'?orderNumber='+str(i)+'&fascia='+store+region+'&postcode='+str(postcode)
			r = requests.get(track_url)
			response = r.text
			if 'Order not found' in response:
				ordernotfound = ordernotfound + 1
			test = json.loads(response)
			a2 = test['status']['short']
			a4 = test['vendors']
			date = a2[0]['date']
			date = datetime.fromisoformat(date[:-1])
			date.strftime('%Y-%m-%d %H:%M:%S')
			a5 = a4[0]['items']
			sku = a5[0]['sku']
			name = a5[0]['name']
			img = a5[0]['img']
			size = a5[0]['size']
			price_before = a5[0]['price']
			price_number = price_before['amount']
			price_currency = price_before['currency']
			price_final = price_number + ' ' + price_currency
			color = ''
			status = ''
			tracking1 = ''
			tracking2 = ''
			if 'Your order is currently being processed.' in response:
				status = 'Your order is currently being processed.'
				color = '16776960'
				orderproc = orderproc + 1
			elif 'Your order has been placed.' in response:
				status = 'Your order has been placed.'
				color = '16776960'
				orderplaced = orderplaced + 1
			elif 'Your order has been despatched.' in response:
				if '"trackingURL":null' in response:
					tracking2 = 'N/A'
				a12 = test['delivery']
				tracking1 = a12['courier']
				tracking2 = a12['trackingURL']
				status = 'Your order has been despatched.'
				color = '65280'
				orderdis = orderdis + 1
			elif 'Your order has been delivered.' in response:
				a12 = test['delivery']
				tracking1 = a12['courier']
				tracking2 = a12['trackingURL']
				status = 'Your order has been delivered.'
				color = '65280'
				orderdel = orderdel + 1
			elif 'It looks like your order has been cancelled.' in response:
				status = 'It looks like your order has been cancelled.'
				color = '16711680'
				ordercan = ordercan + 1
			elif 'It looks like there was an issue taking payment for this order' in response:
				status = 'It looks like there was an issue taking payment for this order.'
				color = '16711680'
				orderpay = orderpay + 1
		except (KeyError,UnboundLocalError):
				ordernotfound = ordernotfound + 1
		trackedorders = orderproc + orderplaced + orderdis + orderdel + orderpay + ordercan
		print(Fore.MAGENTA + f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]"+ log + Fore.GREEN + f"[Tracking Ordernumber - {i}]")

	test1 = discord.Embed(title="Mesh Order Tracker - Summary", description="Successfully tracked " + str(trackedorders) + " orders!",  colour=setembedcolor)
	test1.add_field(name=':x:  Order Not Found', value=ordernotfound, inline=False)
	test1.add_field(name=':sleeping: Order Placed', value=orderplaced, inline=False)
	test1.add_field(name=':cold_face: Order Processed', value=orderproc, inline=False)
	test1.add_field(name=':face_with_symbols_over_mouth: Order Canceled', value=ordercan, inline=False)
	test1.add_field(name=':rage: Payment Error', value=orderpay, inline=False)
	test1.add_field(name=':articulated_lorry: Order Dispatched', value=orderdis, inline=False)
	test1.set_footer(text=setfootertextorder, icon_url=setfooterimage)
	test1.set_thumbnail(url=setthumbnailorder)
	print(Fore.MAGENTA + f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]" + log + Fore.GREEN + "[Webhook sent!]")
	print('')
	await ctx.send(embed = test1)

##############################################################################################################################################################
##############################################################################################################################################################
############## RESTOCKS - RESTOCKS - RESTOCKS - RESTOCKS - RESTOCKS - RESTOCKS - RESTOCKS - RESTOCKS - RESTOCKS - RESTOCKS - RESTOCKS - RESTOCKS - RESTOCKS ##
##############################################################################################################################################################
##############################################################################################################################################################

@bot.command()
async def restocks(context, *sku):
	try:
		track_url = 'https://restocks.de/shop/search?q=' + str(sku) + '&page=1&filters[][range][price][gte]=1'
		r = requests.get(track_url)
		response = r.text
		test = json.loads(response)
		test2 = test['data']

		product_name = test2[0]['name']
		slug = test2[0]['slug']
		product_link = 'https://restocks.de' + slug

		headers = {
		"pragma": "no-cache",
		"cache-control": "no-cache",
		"upgrade-insecure-requests": "1",
		"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
		"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
		"sec-fetch-site": "none",
		"sec-fetch-mode": "navigate",
		"sec-fetch-user": "?1",
		"sec-fetch-dest": "document",
		"accept-language": "de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7"
		}

		response = requests.get(product_link, headers=headers)
		soup = bs(response.content, 'html.parser')
		sizelist = soup.find("ul", {"class":"select__size__list"})
		resell = sizelist.find_all("li", {"data-type":"all"})
		newprices = sizelist.find_all("span", {"class":""})
		resaleprice = []
		consignmentprice = []
		sizes = []
		currentprice = []
		currentpricenow = []
		for i in range(len(resell)):
			if "Notify me" in resell[i]:
				continue
			elif resell[i].find("span", {"class":"price__label__value"}) == None:
				continue
			else:
				try:
					value = resell[i].find("span", {"class":"value"})
					pirce = resell[i].find("span", {"class":"price__label__value"})
					pricenow = resell[i].find("span",{"class":"float-right price"}).text
					currentpricenow.append(pricenow.split(" ")[1].split("€")[0])
					if resell[i].find("span", {"class":"sell__method__value"}).text == "consignment":
						sizes.append(str(resell[i].find("span", {"class":"text"}).text))
						consignmentprice.append(str(round(float(pirce.text),2)))
						resellprice = str(round((round(float(pirce.text),2) + 10)/95*100*0.90-10,2))
						resaleprice.append(str(round(float(resellprice),2)))
					if resell[i].find("span", {"class":"sell__method__value"}).text == "resale":
						sizes.append(str(resell[i].find("span", {"class":"text"}).text))
						resaleprice.append(str(round(float(pirce.text),2)))
						resellprice = str(round((round(float(pirce.text),2) + 10)/90*100*0.95-10,2))
						consignmentprice.append(str(round(float(resellprice),2)))
				except(Exception,AttributeError):
					continue
		print(currentpricenow)
		rprices = prepend(resaleprice, "R: € ")
		cprices = prepend(consignmentprice, "C: € ")
		lprices = prepend(currentpricenow, "L: € ")
		data = ",".join("{0}\n{1}\n{2}".format(x,y,z) for x,y,z in zip(lprices,rprices,cprices))
		data = data.split(",")
		data2 = ",".join(sizes)
		data2 = data2.split(",")
		list(data)
		list(data2)
		correctsku = soup.find_all("div", {"class":"product__info__value"})
		shoesku = str(correctsku[2].text).replace("-","")
		skuforembed = str(correctsku[2].text).replace("\n","")
		lenshoesku = len(shoesku)+2
		newembed = list(zip(data2,data))
		shoepic = soup.find("meta", {"property":"og:image"})["content"]
		shoedesc = soup.find("meta", {"property":"og:title"})["content"]
		shoedesc = shoedesc.replace("Restocks","").replace("-","").replace("'","")
		embed=discord.Embed(title=shoedesc[:-lenshoesku],description="> *L - Current List Price*\n> *R - Resale Price Payout*\n> *C - Consignment Price Payout*\n"+"> *SKU - " + skuforembed + "*", url=product_link ,color=setembedcolor)
		for i in range(len(newembed)):
			embed.add_field(name=newembed[i][0],value=newembed[i][1],inline=True)
		embed.set_thumbnail(url=shoepic)
		embed.set_footer(text=setfootertextrestocks, icon_url=setfooterimage)
		await context.send(embed=embed)
	except IndexError:
		embed=discord.Embed(title="Command Error", color=setembedcolor)
		embed.add_field(name="Error", value="Your are missing an argument", inline=True)
		embed.add_field(name="Command Format", value="?restocks <shoe name>\n?restocks <Shoe ID>", inline=False)
		embed.set_footer(text=setfootertextrestocks, icon_url=setfooterimage)
		await context.send(embed=embed)

##############################################################################################################################################################
##############################################################################################################################################################
############## STOCKX - STOCKX - STOCKX - STOCKX - STOCKX - STOCKX - STOCKX - STOCKX - STOCKX - STOCKX - STOCKX - STOCKX - STOCKX - STOCKX - STOCKX - STOCKX #
##############################################################################################################################################################
##############################################################################################################################################################

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

##############################################################################################################################################################
##############################################################################################################################################################
############## UPS TRACKER - UPS TRACKER - UPS TRACKER - UPS TRACKER - UPS TRACKER - UPS TRACKER - UPS TRACKER - UPS TRACKER - UPS TRACKER - UPS TRACKER #####
##############################################################################################################################################################
##############################################################################################################################################################

@bot.command()
async def ups(ctx, TrackingNr):
	ordernotfound = 0
	lines = ctx.message.content.splitlines()
	lines.pop(0)
	linescount = len(lines)

	if linescount == 0:
		test1 = discord.Embed(title="UPS Tracker - Error",  colour=setembedcolor)
		test1.add_field(name="Commad Format - Single View", value="Make sure tracking numbers are on the next line after ?ups```?ups\n<Tracking NR. 1>\n<Tracking NR. 2>\n<Tracking NR. 3>```", inline=True)
		test1.add_field(name="Max. Track Links", value="Cause of Discord Text limit you can track up to **26 Links**", inline=False)
		test1.add_field(name="Max. Track Numbers", value="Cause of Discord Text limit you can track up to **105 Trackingnumbers**", inline=False)
		test1.add_field(name="GMAIL - FTL Ship Mails - How to get Trackingnumbers", value="""Paste following command in your chrome console\nKeep in mind all your mails need to be extended!```js
!(function(){
    var orders = Array.from(document.querySelectorAll('[class^="m_"][class$="fl-email--actions-block--button-container"]')).map(element => {
        var SIZE = element.getElementsByTagName('tr')[0].getElementsByTagName('a')[0]
        return new String(`${SIZE}`).replace("http://www.ups.com/WebTracking/track?track=yes&trackNums=","");
    });
    console.log(orders.join("\\n"));
})()```""")

	test1 = discord.Embed(title="UPS Order Tracker", description="Tracking " + str(len(lines)) + " orders!",  colour=setembedcolor)
	test1.set_footer(text=setfootertextups, icon_url=setfooterimage)
	await ctx.send(embed = test1)

	TrackingNumber = []
	for i in range(len(lines)):
		if len(lines[i]) > 20:
			TrackingNumber.append(lines[i][-18:])
		else:
			TrackingNumber.append(lines[i])

	track_url = 'https://www.ups.com/track/api/Track/GetStatus?loc=en_GB'

	s = requests.Session()

	today = datetime.date.today()
	yesterday2 = today - datetime.timedelta(days=1)
	yesterday = yesterday2.strftime('%d/%m/%Y')

	r1 = s.get('https://www.ups.com/track?loc=en_GB&requester=ST/')

	cookie_xs = s.cookies['X-XSRF-TOKEN-ST']

	headers = {
	"Connection":"keep-alive",
	"Pragma":"no-cache",
	"Cache-Control":"no-cache",
	"Accept":"application/json, text/plain, */*",
	"X-XSRF-TOKEN":cookie_xs,
	"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36",
	"Content-Type":"application/json",
	"Origin":"https://www.ups.com",
	"Sec-Fetch-Site":"same-origin",
	"Sec-Fetch-Mode":"cors",
	"Sec-Fetch-Dest":"empty",
	"Referer":"https://www.ups.com/WebTracking/track?loc=en_GB&requester=ST/",
	"Accept-Language":"de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7",
	}

	payload = []
	country = []
	for i in range(len(TrackingNumber)):
		payload.append('{"Locale":"en_GB","TrackingNumber":["'+TrackingNumber[i]+'"]}')
	for i in range(len(payload)):
		r = s.post(track_url, data=payload[i], headers=headers)
		jsondata = json.loads(r.text)
		try:
			trackDetails = jsondata["trackDetails"]
			print("Order Status of Trackingnumber " + TrackingNumber[i] + " is: " + trackDetails[0]["packageStatus"])
			country1 = trackDetails[0]
			country2 = country1["shipToAddress"]
			country = ":flag_" + str.lower(country2["country"]) + ":"
			packageStatus = trackDetails[0]["packageStatus"]
			packageStatus = packageStatus.replace("Order Processed: ","")
			additionalInformation = trackDetails[0]["additionalInformation"]
			weight = additionalInformation["weight"]
			weightUnit = additionalInformation["weightUnit"]
			TrackLinks = "https://www.ups.com/track?loc=en_GB&tracknum=" + TrackingNumber[i] +""

			if packageStatus == "Ready for UPS":
				setembedcolorstatus = 0xF2872E
			if packageStatus == "Shipment Cleared Customs":
				setembedcolorstatus = 0x0000FF
			if packageStatus == "Delay":
				packageStatus = "Delayed"
				setembedcolorstatus = 0xFFFF00
			if packageStatus == "In Transit":
				setembedcolorstatus = 0x96ee88
			if packageStatus == "Delivered":
				setembedcolorstatus = 0x5be545


			test1 = discord.Embed(title="UPS Order Tracker - " + country, url = TrackLinks, colour=setembedcolorstatus)
			test1.add_field(name=':package:  Order Status', value=packageStatus, inline=False)
			test1.add_field(name='Tracking Number', value="||" + TrackingNumber[i] + "||", inline=True)
			test1.add_field(name=':bricks: Weight', value=weight + " " + weightUnit, inline=True)
			test1.set_footer(text=setfootertextups, icon_url=setfooterimage)
			test1.set_thumbnail(url=setthumbnailups)
			print('')
			await ctx.send(embed=test1)
		except TypeError:
			ordernotfound = ordernotfound + 1
			setembedcolorstatus = 0xFF0000
			TrackLinks = "https://www.ups.com/track?loc=en_GB&tracknum=" + TrackingNumber[i] +""
			print("Order Status of Trackingnumber " + TrackingNumber[i] + " is: " + "Order Not Found")
			test1 = discord.Embed(title="UPS Order Tracker", url = TrackLinks,  colour=setembedcolorstatus)
			test1.add_field(name=':package:  Order Status', value="Order Not Found", inline=False)
			test1.add_field(name='Tracking Number', value="||" + TrackingNumber[i] + "||\n", inline=True)
			test1.add_field(name=':bricks: Weight', value="N/A", inline=True)
			test1.set_footer(text=setfootertextups, icon_url=setfooterimage)
			test1.set_thumbnail(url=setthumbnailups)
			print('')
			await ctx.send(embed=test1)
				
		

@bot.command()
async def upsbulk(ctx, TrackingNr):

	ordernotfound = 0
	if TrackingNr == "text":
		attachment_url = ctx.message.attachments[0].url
		file_request = requests.get(attachment_url)
		newfile = file_request.text.replace("\n",",")
		lines = newfile.split(",")
	else:
		lines = ctx.message.content.splitlines()
		lines.pop(0)
	linescount = len(lines)

	if linescount == 0:
		test1 = discord.Embed(title="UPS Tracker - Error",  colour=setembedcolor)
		test1.add_field(name="Commad Format - Summary", value="Make sure tracking numbers are on the next line after ?ups```?upsbulk\n<Tracking NR. 1>\n<Tracking NR. 2>\n<Tracking NR. 3>```", inline=True)
		test1.add_field(name="Max. Track Links", value="Cause of Discord Text limit you can track up to **26 Links**", inline=False)
		test1.add_field(name="Max. Track Numbers", value="Cause of Discord Text limit you can track up to **105 Trackingnumbers**", inline=False)
		test1.add_field(name="GMAIL - FTL Ship Mails - How to get Trackingnumbers", value="""Paste following command in your chrome console\nKeep in mind all your mails need to be extended!```js
!(function(){
    var orders = Array.from(document.querySelectorAll('[class^="m_"][class$="fl-email--actions-block--button-container"]')).map(element => {
        var SIZE = element.getElementsByTagName('tr')[0].getElementsByTagName('a')[0]
        return new String(`${SIZE}`).replace("http://www.ups.com/WebTracking/track?track=yes&trackNums=","");
    });
    console.log(orders.join("\\n"));
})()```""")

	test1 = discord.Embed(title="UPS Order Tracker - Summary", description="Tracking " + str(len(lines)) + " orders!",  colour=setembedcolor)
	test1.set_footer(text=setfootertextups, icon_url=setfooterimage)
	await ctx.send(embed = test1)

	TrackingNumber = []
	for i in range(len(lines)):
		if len(lines[i]) > 20:
			TrackingNumber.append(lines[i][-18:])
		else:
			TrackingNumber.append(lines[i])

	track_url = 'https://www.ups.com/track/api/Track/GetStatus?loc=en_GB'

	s = requests.Session()

	today = datetime.date.today()
	yesterday2 = today - datetime.timedelta(days=1)
	yesterday = yesterday2.strftime('%d/%m/%Y')

	r1 = s.get('https://www.ups.com/track?loc=en_GB&requester=ST/')

	cookie_xs = s.cookies['X-XSRF-TOKEN-ST']

	headers = {
	"Connection":"keep-alive",
	"Pragma":"no-cache",
	"Cache-Control":"no-cache",
	"Accept":"application/json, text/plain, */*",
	"X-XSRF-TOKEN":cookie_xs,
	"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36",
	"Content-Type":"application/json",
	"Origin":"https://www.ups.com",
	"Sec-Fetch-Site":"same-origin",
	"Sec-Fetch-Mode":"cors",
	"Sec-Fetch-Dest":"empty",
	"Referer":"https://www.ups.com/WebTracking/track?loc=en_GB&requester=ST/",
	"Accept-Language":"de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7",
	}

	payload = []
	country = []
	packageStatus = []
	for i in range(len(TrackingNumber)):
		payload.append('{"Locale":"en_GB","TrackingNumber":["'+TrackingNumber[i]+'"]}')
	for i in range(len(payload)):
		r = s.post(track_url, data=payload[i], headers=headers)
		jsondata = json.loads(r.text)
		try:
			trackDetails = jsondata["trackDetails"]
			print("Order Status of Trackingnumber " + TrackingNumber[i] + " is: " + trackDetails[0]["packageStatus"])
			country1 = trackDetails[0]
			country2 = country1["shipToAddress"]
			country.append(country2["country"])
			packageStatus.append(trackDetails[0]["packageStatus"])
		except TypeError:
			ordernotfound = ordernotfound + 1
			print("Order Status of Trackingnumber " + TrackingNumber[i] + " is: " + "Order Not Found")
		
		orderDelivered = packageStatus.count("Delivered")
		orderInCustoms = packageStatus.count("Shipment Cleared Customs")
		orderReady = packageStatus.count("Order Processed: Ready for UPS")
		orderInTransit = packageStatus.count("In Transit")
		orderDelayed = packageStatus.count("Delay")


	test1 = discord.Embed(title="UPS Order Tracker - Summary", description="Successfully tracked " + str(linescount) + " orders!",  colour=setembedcolor)
	test1.add_field(name=':x:  Order Not Found', value=ordernotfound, inline=False)
	test1.add_field(name=':orange_circle:  Order Ready for UPS', value=orderReady, inline=False)
	test1.add_field(name=':articulated_lorry:  Order In Transit', value=orderInTransit, inline=False)
	test1.add_field(name=':customs:  Order Cleared Customs', value=orderInCustoms, inline=False)
	test1.add_field(name=':clock1:  Order Delayed', value=orderDelayed, inline=False)
	test1.add_field(name=':house_with_garden:  Order Delivered', value=orderDelivered, inline=False)
	test1.set_footer(text=setfootertextups, icon_url=setfooterimage)
	test1.set_thumbnail(url=setthumbnailups)
	print('')
	await ctx.send(embed=test1)

##############################################################################################################################################################
##############################################################################################################################################################
############## ZALANDO - ZALANDO - ZALANDO - ZALANDO - ZALANDO - ZALANDO - ZALANDO - ZALANDO - ZALANDO - ZALANDO - ZALANDO - ZALANDO - ZALANDO - ZALANDO #####
##############################################################################################################################################################
##############################################################################################################################################################

@bot.command()
async def zalando(ctx, link):
	try:
		text = link.split(".html")[0].split("-")[-2]
		text2 = link.split(".html")[0].split("-")[-1]
		productid = text + "-" + text2
		countrycode = str(link.split("zalando.")[1].split("/")[0])
		if countrycode == "co.uk":
			countrycode = "gb"
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

		payload = ""
		headers2 = {
			'authority': "www.zalando.fr",
			'cache-control': "max-age=0",
			'sec-ch-ua': '"Chromium";v="88", "Google Chrome";v="88", ";Not A Brand";v="99"',
			'sec-ch-ua-mobile': "?0",
			'upgrade-insecure-requests': "1",
			'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36",
			'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
			'sec-fetch-site': "none",
			'sec-fetch-mode': "navigate",
			'sec-fetch-user': "?1",
			'sec-fetch-dest': "document",
			'accept-language': "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7",
			'cookie': 'Zalando-Client-Id=6a6ac196-bc7a-44d6-aaad-ffbdcdffe132; _ga=GA1.2.2008705842.1602795231; liveagent_oref=; liveagent_sid=6330a192-441d-424f-9a7c-c5da866c53bd; liveagent_vc=2; liveagent_ptid=6330a192-441d-424f-9a7c-c5da866c53bd; catalog.follow_brand_banner={"count":3,"isClosed":true}; _gcl_aw=GCL.1610462344.Cj0KEQjwmIrJBRCRmJ_x7KDo-9oBEiQAuUPKMmIAxdJo1PlEgeCCRZ-yfl4duzXiTLHVeq-G4J_rmxEaAtow8P8HAQ; _gac_UA-19190613-1=1.1610462345.Cj0KEQjwmIrJBRCRmJ_x7KDo-9oBEiQAuUPKMmIAxdJo1PlEgeCCRZ-yfl4duzXiTLHVeq-G4J_rmxEaAtow8P8HAQ; _gcl_au=1.1.1804205407.1610582121; sqt_cap=1612221258437; bm_sz=ADAF005A7E40C55E20E36A3A03EA3F80~YAAQViIQAvEkVmB3AQAAAS0BawpsCD0dI0m7vuu6e8fSy7uz1faB67zdSMFnHVyNJxsfWEnCy8G+yTuWKjuHFN5bLKZ5uTER00P/gObFM5FIp9lllSmjLRk/nbpoCwUVAqKshcJvdrpV+3/QHjj2jZvJA7n2+IgWyfc4DlDKs8luX6WFXwV1DZ7JXNrUZ2D/bURB57tCV/lANIVTwqqsNUaLktNGbw8Rwi1Nfx8V5S5+OLE5KOXKi2jBAaiYNA3zM9B8XVX9kdK7Z1FTvcx/mIn+Q3uUwg3Q936gYE4a; ak_bmsc=9FA3B641E8B6691B565F627F41EEC7CB02102256D84E0000A7641B605259563B~plC6qSHQ0KYlzdUz69qrU7MLX39kK1NHrvz701NyYEKgVaz1H7yY89fcjgkPSBLSO4jA9oM1kv+L9D3wxQpczRPjbqLfEoLWwcu0B1jS5Xp8w274aagX3wPxmimOp7uo+dugoHEuRwmAAJbxJUl9SoAyhhYq6eQHMcOz+QaOdGGghr5engJBJYKwZITK4ZCdBTsismRLgwjKLgmZhwc3u/+1KDAZmrcokE6igDbBlIV/ZWx13lqrlIVgkqJPLfPuGs; _gid=GA1.2.1450000166.1612407981; frsx=AAAAAIHeF7FCdSeRv1VXUTW-dUIS_wxFlQwSZZpH43zLFrmBu_beUpI3F8ceexWTVVYMycvw5i7MrZTv1Y9xERnOLF003nt47xKQKKfDgobWgWAJuHGgDAfUO4GdqKes5IdWvSjzMR8m3zDViYcml00=; mpulseinject=false; ncx=f; _abck=DFAD29EF196683F82E808987BB788F17~-1~YAAQPYQVAq2SA2R3AQAAlxpNawUN6fm27mUg37dz96g//Cv+/RwDflM1ZzictKMhsgl64LD/u7G3pBAtbXhI6apazI2gdKUtYTAhHIf8SLb9r2IBHoEoc60HpC1KbHytmWltWnKcrttfb/FyHKZu4eLIj/vzsexeFfPEtWY6pLR25rRzsbkxXyJuw2M6MJzAF3Jk4w4H8dk2L4Uuv/5GaoBHUn3kYmS0ysB7G1IA0ipkRW9E8I4zWZ8ULKqvY4rqWpYAzHW2GYPsHZ5VC0JGH3qgWHhlxNdjKgy0JwVP2gfytAX0944N+JoB0BhfzuFCSHgHdmgA0k+WCw2+Neyp1DT7q0Gt73DZp7XlM+9vt4MmU05I4wRyDHQIIMpi69dRhXv8fsuDi09hBo5GM7ibiLPfbeFz/S2ahGMHM6z453UqcAVVhFerAn/GroheBz/NOcyr8as9Z9641noy5h/CYpSIXi9aQMPn~-1~-1~-1; _gat_zalga=1; bm_sv=B3886A9C6914B3F8D73A97CAC7EE98CB~r/m9BM8z1C5r3UUDzWca0CDA6RXHU/OGjNgMX+kSiHMT/wqAYGojulS9WNDq9phCdUwS7mT3hMcDSKnj5MpJ/kcnTebwS3jVsYl4JHnmkxCMajnUZDCGDJSptpvQCrW0d731202q67se0rGaWV9MtcrFMaqRZT+WkKs6YONlLaE='
		}

		print("Getting Stock for " + productid + " on Zalando " + countrycode)
		embed3=discord.Embed(title="Zalando Stock Checker :flag_" + countrycode + ":", description='Checking backend...', color=setembedcolor)
		embed3.set_footer(text=setfootertextzalando, icon_url=setfooterimage)
		test91 = await ctx.send(embed=embed3)
		try:
			response = requests.get(link, headers=headers)
			soup = bs(response.content, 'html.parser')
			text = soup.find("script",{"id":"z-vegas-pdp-props"}).text
			strtext = str(text)
			newtext = strtext.replace("""\xa0€""","€").replace("<![CDATA[","")
			if countrycode == "fr" or countrycode == "es" or countrycode == "se" or countrycode == "fi" or countrycode == "it" or countrycode == "dk":
				newstrtext = newtext.split('"units":')[1].split(',"partnerTncUrl')[0]
			else:
				newstrtext = newtext.split('"units":')[1].split("}]")[0]
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
			allsize2 = ['> '+x for x in size]
			totalstock = sum(Decimal(i) for i in stock)
			discsize = "\n".join(allsize2)
			discstock = "\n".join(stock)
			discsku = "\n".join(sku)

			embed=discord.Embed(title="Zalando Stock Checker :flag_" + countrycode + ":", description='> ['+(shoename)+']('+link+')', color=setembedcolor)
			embed.set_thumbnail(url=shoepic)
			embed.add_field(name=":straight_ruler: Size", value=discsize, inline=True)
			embed.add_field(name=":bar_chart: Stock", value=discstock, inline=True)
			embed.add_field(name=":pushpin: SKUs", value=discsku, inline=True)
			embed.add_field(name="Total Stock", value="`"+str(totalstock)+"`", inline=True)
			embed.add_field(name="Price", value="`" + str(correctprice) + "`", inline=True)
			embed.add_field(name="Release Date", value="`Live`", inline=True)
			embed.set_footer(text=setfootertextzalando, icon_url=setfooterimage)
			if "private" in ctx.channel.type:
				member = ctx.author
				await member.send(embed=embed)
				await test91.delete()
			else:
				await ctx.send(embed=embed)
				await ctx.message.delete()
				await test91.delete()
		except (AttributeError,TypeError):
			try:
				response2 = requests.get(link, data=payload, headers=headers2)
				response2text = response2.text
				soup = bs(response2.content, 'html.parser')
				releasedate = soup.find("h2",{"class":"AKpsL5 ka2E9k uMhVZi z-oVg8 pVrzNP"})
				newtext2 = response2text.split('"simples":')[2].split("null}}}]")[0]
				newtext2 = newtext2 + "null}}}]"
				skucount = newtext2.count("sku")
				jsondata = json.loads(newtext2)
				stock = []
				size = []
				sku = []
				data = jsondata[0]
				for i in range(len(jsondata)):
					newdata = jsondata[i]
					offer = newdata["offer"]
					quantity = offer["stock"]
					stock.append(quantity["quantity"])
					sku.append(str(newdata["sku"]))
					size.append(str(newdata["size"]))
				coloredstock = []
				for i in range(len(stock)):
					#coloredstock.append(stock[i].replace("OUT_OF_STOCK",":red_circle:`OOS`").replace("ONE",":yellow_circle:`ONE`").replace("TWO",":yellow_circle:`TWO`").replace("THREE",":yellow_circle:`THREE`").replace("MANY",":green_circle:`MANY`"))
					coloredstock.append(stock[i].replace("OUT_OF_STOCK","0").replace("ONE","1").replace("TWO","2").replace("THREE","3").replace("MANY","4+"))
				price = data["offer"]
				allprice = price["price"]
				try:
					promoprice = allprice["promotional"]
					correctpromoprice = str(promoprice["amount"])
					currency = promoprice["currency"]
					correctprice = "`" +  correctpromoprice[0:-2] + ',' + correctpromoprice[-2:] + " " + currency + "`"
				except TypeError:
					ogprice = allprice["original"]
					correctogprice = str(ogprice["amount"])
					currency = ogprice["currency"]
					correctprice = "`" + correctogprice[0:-2] + ',' + correctogprice[-2:] + " " + currency + "`"
				shoepic = soup.find("meta", {"property":"og:image"})["content"]
				shoename1 = soup.find("meta", {"property":"og:title"})["content"]
				newtext = shoename1.split("-")[0]
				newtext2 = shoename1.split("-")[1]
				shoename = newtext + newtext2
				allsize2 = ['> '+x for x in size]
				discsize = "\n".join(allsize2)
				discstock = "\n".join(coloredstock)
				discsku = "\n".join(sku)

				countone = coloredstock.count("1")
				counttwo = coloredstock.count("2")
				countthree = coloredstock.count("3")
				countmany = coloredstock.count("4+")
				totalstock = countone + (counttwo * 2) + (countthree * 3) + (countmany * 4)
				if totalstock > 0:
					totalstock = str(totalstock) + "+"
				else:
					totalstock = totalstock

				embed=discord.Embed(title="Zalando Stock Checker :flag_" + countrycode + ":", description='> ['+(shoename)+']('+link+')', color=setembedcolor)
				embed.set_thumbnail(url=shoepic)
				embed.add_field(name=":straight_ruler: Size", value=discsize, inline=True)
				embed.add_field(name=":bar_chart: Stock", value=discstock, inline=True)
				embed.add_field(name=":pushpin: SKUs", value=discsku, inline=True)
				embed.add_field(name="Total Stock", value="`"+str(totalstock)+"`", inline=True)
				embed.add_field(name="Price", value="`"+str(correctprice)+"`", inline=True)
				embed.add_field(name="Release Date", value="`" + releasedate.text + "`", inline=True)
				embed.set_footer(text=setfootertextzalando, icon_url=setfooterimage)
				if "private" in ctx.channel.type:
					member = ctx.author
					await member.send(embed=embed)
					await test91.delete()
				else:
					await ctx.send(embed=embed)
					await ctx.message.delete()
					await test91.delete()
			except Exception:
				embed=discord.Embed(title="Zalando Stock Checker - Error", color=setembedcolor)
				embed.add_field(name="Error", value="An error occured. Please check your command or link!", inline=True)
				embed.set_footer(text=setfootertextzalando, icon_url=setfooterimage)
				await ctx.send(embed=embed)
				await test91.delete()
	except IndexError:
		embed=discord.Embed(title="Zalando Stock Checker - Error", color=setembedcolor)
		embed.add_field(name="Error", value="An error occured. Please check your command or link!", inline=False)
		embed.add_field(name="Command Format",value="?zalando <full link here>", inline=False)
		embed.set_footer(text=setfootertextzalando, icon_url=setfooterimage)
		await ctx.send(embed=embed)

@bot.command()
async def zalandopid(ctx, link):
	try:
		text = link.split(".html")[0].split("-")[-2]
		text2 = link.split(".html")[0].split("-")[-1]
		productid = text + "-" + text2
		countrycode = str(link.split("zalando.")[1].split("/")[0])
		if countrycode == "co.uk":
			countrycode = "gb"
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

		payload = ""
		headers2 = {
			'authority': "www.zalando.fr",
			'cache-control': "max-age=0",
			'sec-ch-ua': '"Chromium";v="88", "Google Chrome";v="88", ";Not A Brand";v="99"',
			'sec-ch-ua-mobile': "?0",
			'upgrade-insecure-requests': "1",
			'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36",
			'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
			'sec-fetch-site': "none",
			'sec-fetch-mode': "navigate",
			'sec-fetch-user': "?1",
			'sec-fetch-dest': "document",
			'accept-language': "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7",
			'cookie': 'Zalando-Client-Id=6a6ac196-bc7a-44d6-aaad-ffbdcdffe132; _ga=GA1.2.2008705842.1602795231; liveagent_oref=; liveagent_sid=6330a192-441d-424f-9a7c-c5da866c53bd; liveagent_vc=2; liveagent_ptid=6330a192-441d-424f-9a7c-c5da866c53bd; catalog.follow_brand_banner={"count":3,"isClosed":true}; _gcl_aw=GCL.1610462344.Cj0KEQjwmIrJBRCRmJ_x7KDo-9oBEiQAuUPKMmIAxdJo1PlEgeCCRZ-yfl4duzXiTLHVeq-G4J_rmxEaAtow8P8HAQ; _gac_UA-19190613-1=1.1610462345.Cj0KEQjwmIrJBRCRmJ_x7KDo-9oBEiQAuUPKMmIAxdJo1PlEgeCCRZ-yfl4duzXiTLHVeq-G4J_rmxEaAtow8P8HAQ; _gcl_au=1.1.1804205407.1610582121; sqt_cap=1612221258437; bm_sz=ADAF005A7E40C55E20E36A3A03EA3F80~YAAQViIQAvEkVmB3AQAAAS0BawpsCD0dI0m7vuu6e8fSy7uz1faB67zdSMFnHVyNJxsfWEnCy8G+yTuWKjuHFN5bLKZ5uTER00P/gObFM5FIp9lllSmjLRk/nbpoCwUVAqKshcJvdrpV+3/QHjj2jZvJA7n2+IgWyfc4DlDKs8luX6WFXwV1DZ7JXNrUZ2D/bURB57tCV/lANIVTwqqsNUaLktNGbw8Rwi1Nfx8V5S5+OLE5KOXKi2jBAaiYNA3zM9B8XVX9kdK7Z1FTvcx/mIn+Q3uUwg3Q936gYE4a; ak_bmsc=9FA3B641E8B6691B565F627F41EEC7CB02102256D84E0000A7641B605259563B~plC6qSHQ0KYlzdUz69qrU7MLX39kK1NHrvz701NyYEKgVaz1H7yY89fcjgkPSBLSO4jA9oM1kv+L9D3wxQpczRPjbqLfEoLWwcu0B1jS5Xp8w274aagX3wPxmimOp7uo+dugoHEuRwmAAJbxJUl9SoAyhhYq6eQHMcOz+QaOdGGghr5engJBJYKwZITK4ZCdBTsismRLgwjKLgmZhwc3u/+1KDAZmrcokE6igDbBlIV/ZWx13lqrlIVgkqJPLfPuGs; _gid=GA1.2.1450000166.1612407981; frsx=AAAAAIHeF7FCdSeRv1VXUTW-dUIS_wxFlQwSZZpH43zLFrmBu_beUpI3F8ceexWTVVYMycvw5i7MrZTv1Y9xERnOLF003nt47xKQKKfDgobWgWAJuHGgDAfUO4GdqKes5IdWvSjzMR8m3zDViYcml00=; mpulseinject=false; ncx=f; _abck=DFAD29EF196683F82E808987BB788F17~-1~YAAQPYQVAq2SA2R3AQAAlxpNawUN6fm27mUg37dz96g//Cv+/RwDflM1ZzictKMhsgl64LD/u7G3pBAtbXhI6apazI2gdKUtYTAhHIf8SLb9r2IBHoEoc60HpC1KbHytmWltWnKcrttfb/FyHKZu4eLIj/vzsexeFfPEtWY6pLR25rRzsbkxXyJuw2M6MJzAF3Jk4w4H8dk2L4Uuv/5GaoBHUn3kYmS0ysB7G1IA0ipkRW9E8I4zWZ8ULKqvY4rqWpYAzHW2GYPsHZ5VC0JGH3qgWHhlxNdjKgy0JwVP2gfytAX0944N+JoB0BhfzuFCSHgHdmgA0k+WCw2+Neyp1DT7q0Gt73DZp7XlM+9vt4MmU05I4wRyDHQIIMpi69dRhXv8fsuDi09hBo5GM7ibiLPfbeFz/S2ahGMHM6z453UqcAVVhFerAn/GroheBz/NOcyr8as9Z9641noy5h/CYpSIXi9aQMPn~-1~-1~-1; _gat_zalga=1; bm_sv=B3886A9C6914B3F8D73A97CAC7EE98CB~r/m9BM8z1C5r3UUDzWca0CDA6RXHU/OGjNgMX+kSiHMT/wqAYGojulS9WNDq9phCdUwS7mT3hMcDSKnj5MpJ/kcnTebwS3jVsYl4JHnmkxCMajnUZDCGDJSptpvQCrW0d731202q67se0rGaWV9MtcrFMaqRZT+WkKs6YONlLaE='
		}

		print("Getting Stock for " + productid + " on Zalando " + countrycode)
		embed3=discord.Embed(title="Zalando Stock Checker :flag_" + countrycode + ":", description='Checking backend...', color=setembedcolor)
		embed3.set_footer(text=setfootertextzalando, icon_url=setfooterimage)
		test91 = await ctx.send(embed=embed3)
		try:
			response = requests.get(link, headers=headers)
			soup = bs(response.content, 'html.parser')
			text = soup.find("script",{"id":"z-vegas-pdp-props"}).text
			strtext = str(text)
			newtext = strtext.replace("""\xa0€""","€").replace("<![CDATA[","")
			if countrycode == "fr" or countrycode == "es" or countrycode == "se" or countrycode == "fi" or countrycode == "it" or countrycode == "dk":
				newstrtext = newtext.split('"units":')[1].split(',"partnerTncUrl')[0]
			else:
				newstrtext = newtext.split('"units":')[1].split("}]")[0]
				newstrtext = newstrtext + "}]"
				count = newstrtext.count("displayPrice")
				valuecount = newstrtext.count("value")
				newvalue2 = newstrtext.split('"percentageDiscount":')[1].split(",")[0]
				legacyPartnerId = []
				newvalue = []

				for i in range(count):
					try:
						legacyPartnerId.append(str(newstrtext.split('"legacyPartnerId":')[i+1].split(",")[0]))
					except IndexError:
						continue
				for i in range(valuecount):
					newvalue.append(newstrtext.split('"value":')[i+1].split(",")[0])
				legacyPartnerId = list(legacyPartnerId)
				legacyPartnerId = list(dict.fromkeys(legacyPartnerId))
				newvalue = list(newvalue)
				newvalue = list(dict.fromkeys(newvalue))
				newstrtext = newstrtext.replace('"percentageDiscount":' + str(newvalue2) + ",",'"percentageDiscount":"' + str(newvalue2) + '",')
				newstrtext = newstrtext.replace("false",'"false"').replace("true",'"true"').replace(',"deliveryPromises":[]',"")
				for i in range(len(legacyPartnerId)):
					try:
						newstrtext = newstrtext.replace('"legacyPartnerId":' + str(legacyPartnerId[i]) + ",",'"legacyPartnerId":"' + str(legacyPartnerId[i]) + '",')
					except IndexError:
						continue
				for i in range(len(newvalue)):
					newstrtext = newstrtext.replace('"value":'+str(newvalue[i])+",",'"value":"'+str(newvalue[i])+'",')
			jsondata = json.loads(newstrtext)
			size = []
			sku = []
			data = jsondata[0]
			displayPrice = data["displayPrice"]
			price = displayPrice["price"]
			correctprice = price["formatted"]
			for i in range(len(jsondata)):
				newdata = jsondata[i]
				manufacturer = newdata["size"]
				sku.append(str(newdata["id"]))
				size.append(str(manufacturer["local"]))

			shoepic = soup.find("meta", {"property":"og:image"})["content"]
			shoename1 = soup.find("meta", {"property":"og:title"})["content"]
			newtext = shoename1.split("-")[0]
			newtext2 = shoename1.split("-")[1]
			mainpid = sku[1][:13]
			shoename = newtext + newtext2
			allsize2 = ['> '+x for x in size]
			discsize = "\n".join(allsize2)
			newsku = ['> '+x for x in sku]
			discsku = "\n".join(sku)
			dischazey = "\n".join(newsku)
			discsizesku = "\n".join("{0} {1}".format(x,y) for x,y in zip(allsize2,sku))
			discfleek = ";".join(sku)
			discrootz = ",".join(sku)
			disclunar = "/".join(sku)

			embed=discord.Embed(title="Zalando Stock Checker :flag_" + countrycode + ":", description='> ['+(shoename)+']('+link+')', color=setembedcolor)
			embed.set_thumbnail(url=shoepic)
			embed.add_field(name=":straight_ruler: Size", value=discsize, inline=True)
			embed.add_field(name=":pushpin: SKUs", value=discsku, inline=True)
			embed.add_field(name="<:hazeyoos:810363526765346836> Hazey", value=dischazey, inline=False)
			embed.add_field(name="<:lunaroos:810363502568013825> Lunar", value="> "+disclunar, inline=False)
			embed.add_field(name="<:rootlabzoos:810363570666733578> RootLabz", value="> "+discrootz, inline=False)
			embed.add_field(name="<:fleekoos:810363547686928384> Fleek", value="> "+discfleek, inline=False)
			embed.add_field(name="PID", value="`" + mainpid + "`", inline=False)
			embed.add_field(name="Price", value="`" + str(correctprice) + "`", inline=True)
			embed.add_field(name="Release Date", value="`Live`", inline=True)
			embed.set_footer(text=setfootertextzalando, icon_url=setfooterimage)
			if "private" in ctx.channel.type:
				member = ctx.author
				await member.send(embed=embed)
				await test91.delete()
			else:
				await ctx.send(embed=embed)
				await ctx.message.delete()
				await test91.delete()
		except (AttributeError,TypeError):
			try:
				response2 = requests.get(link, data=payload, headers=headers2)
				response2text = response2.text
				soup = bs(response2.content, 'html.parser')
				releasedate = soup.find("h2",{"class":"AKpsL5 ka2E9k uMhVZi z-oVg8 pVrzNP"})
				newtext2 = response2text.split('"simples":')[2].split("null}}}]")[0]
				newtext2 = newtext2 + "null}}}]"
				skucount = newtext2.count("sku")
				jsondata = json.loads(newtext2)
				size = []
				sku = []
				data = jsondata[0]
				for i in range(len(jsondata)):
					newdata = jsondata[i]
					offer = newdata["offer"]
					quantity = offer["stock"]
					sku.append(str(newdata["sku"]))
					size.append(str(newdata["size"]))
				price = data["offer"]
				allprice = price["price"]
				try:
					promoprice = allprice["promotional"]
					correctpromoprice = str(promoprice["amount"])
					currency = promoprice["currency"]
					correctprice = "`" +  correctpromoprice[0:-2] + ',' + correctpromoprice[-2:] + " " + currency + "`"
				except TypeError:
					ogprice = allprice["original"]
					correctogprice = str(ogprice["amount"])
					currency = ogprice["currency"]
					correctprice = "`" + correctogprice[0:-2] + ',' + correctogprice[-2:] + " " + currency + "`"
				shoepic = soup.find("meta", {"property":"og:image"})["content"]
				shoename1 = soup.find("meta", {"property":"og:title"})["content"]
				newtext = shoename1.split("-")[0]
				newtext2 = shoename1.split("-")[1]
				mainpid = sku[1][:13]
				shoename = newtext + newtext2
				allsize2 = ['> '+x for x in size]
				discsize = "\n".join(allsize2)
				newsku = ['> '+x for x in sku]
				discsku = "\n".join(sku)
				dischazey = "\n".join(newsku)
				discsizesku = "\n".join("{0} {1}".format(x,y) for x,y in zip(allsize2,sku))
				discfleek = ";".join(sku)
				discrootz = ",".join(sku)
				disclunar = "/".join(sku)

				embed=discord.Embed(title="Zalando Stock Checker :flag_" + countrycode + ":", description='> ['+(shoename)+']('+link+')', color=setembedcolor)
				embed.set_thumbnail(url=shoepic)
				embed.add_field(name=":straight_ruler: Size", value=discsize, inline=True)
				embed.add_field(name=":pushpin: SKUs", value=discsku, inline=True)
				embed.add_field(name="<:hazeyoos:810363526765346836> Hazey", value=dischazey, inline=False)
				embed.add_field(name="<:lunaroos:810363502568013825> Lunar", value="> "+disclunar, inline=False)
				embed.add_field(name="<:rootlabzoos:810363570666733578> RootLabz", value="> "+discrootz, inline=False)
				embed.add_field(name="<:fleekoos:810363547686928384> Fleek", value="> "+discfleek, inline=False)
				embed.add_field(name="PID", value="`" + mainpid + "`", inline=False)
				embed.add_field(name="Price", value="`" + str(correctprice) + "`", inline=True)
				embed.add_field(name="Release Date", value="`Live`", inline=True)
				embed.set_footer(text=setfootertextzalando, icon_url=setfooterimage)
				if "private" in ctx.channel.type:
					member = ctx.author
					await member.send(embed=embed)
					await test91.delete()
				else:
					await ctx.send(embed=embed)
					await ctx.message.delete()
					await test91.delete()
			except Exception:
				embed=discord.Embed(title="Zalando Stock Checker - Error", color=setembedcolor)
				embed.add_field(name="Error", value="An error occured. Please check your command or link!", inline=True)
				embed.set_footer(text=setfootertextzalando, icon_url=setfooterimage)
				await ctx.send(embed=embed)
				await test91.delete()
	except IndexError:
		embed=discord.Embed(title="Zalando PID Scraper - Error", color=setembedcolor)
		embed.add_field(name="Error", value="An error occured. Please check your command or link!", inline=False)
		embed.add_field(name="Command Format",value="?zalandopid <full link here>", inline=False)
		embed.set_footer(text=setfootertextzalando, icon_url=setfooterimage)
		await ctx.send(embed=embed)

##############################################################################################################################################################
##############################################################################################################################################################
############## HELP COMMAND - HELP COMMAND - HELP COMMAND - HELP COMMAND - HELP COMMAND - HELP COMMAND - HELP COMMAND - HELP COMMAND - HELP COMMAND ##########
##############################################################################################################################################################
##############################################################################################################################################################


@bot.command()
async def ftlcountries(context):
	embed=discord.Embed(title="All Support FTL Countries", color=setembedcolor)
	old_region = ['UK','FR','NL','SG','AU','MY','HK','MO']
	old_region_name = ['United Kingdom','France','Netherlands','Singapore','Australia','Malaysia','Hong Kong','Macau']
	old_region_flag = [':flag_gb:',':flag_fr:',':flag_nl:',':flag_sg:',':flag_au:',':flag_my:',':flag_hk:',':flag_mo:']
	new_region = ['AT','BE','DK','HU','IE','IT',"DE",'GR','LU','NO','CZ','PL','PT','ES','SE']
	new_region_name = ['Austria','Belgium','Denmark','Hungary','Ireland','Italy',"Germany",'Greece','Luxembourg','Norway','Czech Republic','Poland','Portugal','Spain','Sweden']
	new_region_flag = [':flag_at:',':flag_be:',':flag_dk:',':flag_hu:',':flag_ie:',':flag_it:',':flag_de:',':flag_gr:',':flag_lu:',':flag_no:',':flag_cz:',':flag_pl:',':flag_pt:',':flag_es:',':flag_se:']
	countriesold = "\n".join("{0} - {1}  {2}".format(x,y,z) for x,y,z in zip(old_region_flag,old_region,old_region_name))
	countriesnew = "\n".join("{0} - {1} {2}".format(x,y,z) for x,y,z in zip(new_region_flag,new_region,new_region_name))
	embed.add_field(name="NEW REGION", value=countriesnew, inline=True)
	embed.add_field(name="OLD REGION", value=countriesold, inline=True)
	embed.set_footer(text=setfootertextftl, icon_url=setfooterimage)
	await context.send(embed=embed)

@bot.command()
async def ftlhelp(context):
	embed=discord.Embed(title="Footlocker Stock Checker Help", color=setembedcolor)
	embed.add_field(name="List of all countries supported by FTL", value='?ftlcountries', inline=False)
	embed.add_field(name="Command Format - FTL", value='?stock <link>', inline=False)
	embed.add_field(name="Command Format - Sidestep", value='?side <link>', inline=False)
	embed.add_field(name="Command Format - FTL New Page Checker", value='?ftlnew <link>', inline=False)
	embed.set_footer(text=setfootertextftl, icon_url=setfooterimage)
	await context.send(embed=embed)

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
async def nikehelp(context):
	embed=discord.Embed(title="Nike Early Links HELP", color=setembedcolor)
	embed.add_field(name="Command Format", value="?nike  <full link here>", inline=False)
	embed.add_field(name="Supported Countries", value=":flag_ch: Switzerand\n:flag_au: Australia\n:flag_ca: Canada\n:flag_ru: Russia\n:flag_sg: Singapore", inline=False)
	embed.set_footer(text=setfootertextnike, icon_url=setfooterimage)
	await context.send(embed=embed)

@bot.command()
async def orderhelp(context):
	embed=discord.Embed(title="Mesh Order Tracker Help", color=setembedcolor)
	embed.add_field(name="How do i track a single order :question:", value="```?order <store> <postcode>\n<ordernr>```\n**Example:**```?order jdde 79798\n302723669```", inline=False)
	embed.add_field(name="How do i track a multiple orders :question:", value="```?order <store> <postcode>\n<ordernr1>\n<ordernr2>\n<ordernr3>\n```\n**Example:**```?order jdde 79798\n302723669\n302723123\n302723456```", inline=False)
	embed.add_field(name="How do i get all order status :question:", value="```?orderbulk <store> <postcode>\n<ordernr1>\n<ordernr2>\n<ordernr3>\n```\n**Example:**```?orderbulk jdsportsde 79798\n302723669\n302723123\n302723456```", inline=False)
	embed.add_field(name="How do i get a store list with its command format :question:", value="Use command `?orderstore to get a full list of all stores supported", inline=False)
	embed.add_field(name="Information",value="You can either use the full name of the store or the given shortcut!\nexample: jdsportsnl -> jdnl", inline=False)
	embed.set_footer(text=setfootertextorder, icon_url=setfooterimage)
	embed.set_thumbnail(url=setthumbnailorder)
	await context.send(embed=embed)

@bot.command()
async def orderstore(context):
	fpregions = ["gb","fr","it","nl","dk","fi","se","ie","de"]
	fpflag = [":flag_gb:",":flag_fr:",":flag_it:",":flag_nl:",":flag_dk:",":flag_fi:",":flag_se:",":flag_ie:",":flag_de:"]
	szregions = ["gb","de","dk","es","fr","ie","it","nl","se"]
	szflag = [":flag_gb:",":flag_de:",":flag_dk:",":flag_es:",":flag_fr:",":flag_ie:",":flag_it:",":flag_nl:",":flag_se:"]
	jdregions = ["gb","at","au","be","de","dk","es","fr","ie","it","my","nl","pt","se","sg","au","my"]
	jdflag = [":flag_gb:",":flag_at:",":flag_au:",":flag_be:",":flag_de:",":flag_dk:",":flag_es:",":flag_fr:",":flag_ie:",":flag_it:",":flag_my:",":flag_nl:",":flag_pt:",":flag_se:",":flag_sg:",":flag_au:",":flag_my:"]
	jdsportsregions = ["jdsports" + i for i in jdregions]
	jdshortregions = ["jd" + i for i in jdregions]
	footpatrolregions = ["footpatrol" + i for i in fpregions]
	fpshortregion = ["fp" + i for i in fpregions]
	sizeregion = ["size" + i for i in szregions]
	sizeshortregion = ["sz" + i for i in szregions]

	
	fpstores = "\n".join("{0} {1} {2}".format(x,y,z) for x,y,z in zip(fpflag,footpatrolregions,fpshortregion))
	szstores = "\n".join("{0} {1} {2}".format(x,y,z) for x,y,z in zip(szflag,sizeregion,sizeshortregion))
	jdstores = "\n".join("{0} {1} {2}".format(x,y,z) for x,y,z in zip(jdflag,jdsportsregions,jdshortregions))
	embed=discord.Embed(title="Mesh Stores Help", color=setembedcolor)
	embed.add_field(name="JDSports", value=jdstores, inline=True)
	embed.add_field(name="Size?", value=szstores, inline=True)
	embed.add_field(name="Footpatrol", value=fpstores, inline=True)
	embed.set_footer(text=setfootertextorder, icon_url=setfooterimage)
	embed.set_thumbnail(url=setthumbnailorder)
	await context.send(embed=embed)

@bot.command()
async def upshelp(context):
		embed=discord.Embed(title="UPS Order Tracker", color=setembedcolor)
		embed.add_field(name="Commad Format - Single View", value="Make sure tracking numbers are on the next line after ?ups```?ups\n<Tracking NR. 1>\n<Tracking NR. 2>\n<Tracking NR. 3>```", inline=True)
		embed.add_field(name="Commad Format - Summary", value="Make sure tracking numbers are on the next line after ?ups```?upsbulk\n<Tracking NR. 1>\n<Tracking NR. 2>\n<Tracking NR. 3>```", inline=True)
		embed.add_field(name="Commad Format - Summary with .txt File - 105+ Orders", value="Make sure to type 'text' on the next line after ?upsbulk```?upsbulk\ntext\n<paste ordernrs here as message.txt file>```", inline=True)
		embed.add_field(name="Max. Track Links", value="Cause of Discord Text limit you can track up to **26 Links**", inline=False)
		embed.add_field(name="Max. Track Numbers", value="Cause of Discord Text limit you can track up to **105 Trackingnumbers**", inline=False)
		embed.add_field(name="GMAIL - FTL Ship Mails - How to get Trackingnumbers", value="""Paste following command in your chrome console\nKeep in mind all your mails need to be extended!```js
!(function(){
    var orders = Array.from(document.querySelectorAll('[class^="m_"][class$="fl-email--actions-block--button-container"]')).map(element => {
        var SIZE = element.getElementsByTagName('tr')[0].getElementsByTagName('a')[0]
        return new String(`${SIZE}`).replace("http://www.ups.com/WebTracking/track?track=yes&trackNums=","");
    });
    console.log(orders.join("\\n"));
})()```""")
		embed.set_footer(text=setfootertextups, icon_url=setfooterimage)
		await context.send(embed=embed)

@bot.command()
async def zalandohelp(context):
	embed=discord.Embed(title="Zalando HELP", color=setembedcolor)
	embed.add_field(name="Stock/SKU Scraper", value="?zalando  <full link here>", inline=False)
	embed.add_field(name="SKU Scraper", value="?zalandopid  <full link here>", inline=False)
	embed.set_footer(text=setfootertextzalando, icon_url=setfooterimage)
	await context.send(embed=embed)

@bot.event
async def on_command_error(ctx, error):
	if isinstance(error, CommandNotFound):
		return
	elif isinstance(error,MissingRequiredArgument):
		embed=discord.Embed(title="Command Error", color=setembedcolor)
		embed.add_field(name="Error", value="Your are missing an argument", inline=True)
		embed.add_field(name="Command Format - FTL", value="?stock <link>", inline=False)
		embed.add_field(name="Command Format - Side Step", value="?side <link>", inline=False)
		embed.set_footer(text=setfootertextftl, icon_url=setfooterimage)
		await ctx.send(embed=embed)
		return
	raise error


@bot.command()
async def clear(ctx, amount=2):
	await ctx.channel.purge(limit=amount)



bot.run(bottoken)
