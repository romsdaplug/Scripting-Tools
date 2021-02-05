import discord
from discord.ext import commands, tasks
from discord_webhook import DiscordEmbed, DiscordWebhook
from itertools import cycle
import json
import os
from pprint import pprint
from bs4 import BeautifulSoup
import requests
import platform
import sys
import random, ast
import xml.etree.ElementTree as ET
from urllib.request import urlopen
import xmltodict
bot = commands.Bot(command_prefix = '?', help_command=None)

@bot.event
async def on_ready():
	print('Bot is ready.')
	pass

setfootertext = "@PigeonHelpbox | Stock Checker"
setfooterimage = "https://media.discordapp.net/attachments/791440600301961246/797258002159239298/Pigeon_Proxies_DiscordBot.png?width=1274&height=1274"
setembedcolor = 0x66FFFF

euregionhook = ["https://discord.com/api/webhooks/795830345668362262/q6mhcOBrm6JsG6n7RE-J0XFn9arGDFhG9WL-by45-n9qidrKEHjXBywzo__nBu_yWDmo","https://discord.com/api/webhooks/805796056024481823/25pAS0D_v75ADprKf2HHGHYffcqfSpA__2Br6cnVj95hdh1-3V9EXIiHjHCyWVpE3WUf"]
asiaregionhook = ["https://discord.com/api/webhooks/795830744110071819/oqo38JTYAl_PDIdFJZtQq-01ILvRtSrQpP4LR_zbzyDthOaEsGV1PEjyD8QWvuryWsHN","https://discord.com/api/webhooks/805796056024481823/25pAS0D_v75ADprKf2HHGHYffcqfSpA__2Br6cnVj95hdh1-3V9EXIiHjHCyWVpE3WUf"]
newregionhook = ["https://discord.com/api/webhooks/796527829261090848/36pfX9AeOlz321uMFTwiibnwAwxT_noBgTkt98JgCoh1xzufCn6yQIW8LkPDtc5iv4dt","https://discord.com/api/webhooks/805796056024481823/25pAS0D_v75ADprKf2HHGHYffcqfSpA__2Br6cnVj95hdh1-3V9EXIiHjHCyWVpE3WUf"]

proxies = []

try:
	proxies = open("proxies.txt").read().splitlines()
	print(" [Succesfully loaded " + str(len(proxies)) + " proxies]")  
except Exception as e:
	print(e)
	print(" [Could not load proxies]")

def getRandomProxy():
  if (len(proxies) != 0):
  	proxyDict = {}
  	proxy = random.choice(proxies)
  	proxySplit = proxy.split(":")
  	if (len(proxySplit) != 4):
  		proxyDict = {
  		"http": "http://" + proxySplit[0] + ":" + proxySplit[1] + "/",
  		"https": "https://" + proxySplit[0] + ":" + proxySplit[1] + "/"
  		}
  	else:
  		proxyDict = {
  		"http": "http://" + proxySplit[2] + ":" + proxySplit[3] + "@" + proxySplit[0] + ":" + proxySplit[1] + "/",
  		"https": "https://" + proxySplit[2] + ":" + proxySplit[3] + "@" + proxySplit[0] + ":" + proxySplit[1] + "/"
  		}          
  		return proxyDict
  else:
  	proxyDict = {}
  	proxyDict = {
  	"http": "http://",
  	"https": "https://"
  	}             
  return proxyDict

def check_if_it_is_me(ctx):
	return ctx.message.author.id == 175953718750085121 or ctx.message.author.id == 351639955531104258

@bot.command()
@commands.check(check_if_it_is_me)
async def stock(ctx, link):

	headers = ''
	url = ''
	pid = ''
	shoename = ''
	countrycode = ''
	region = str(link.split("footlocker.")[1].split("/")[0]).replace(".","")
	if region == 'DE' or region == 'de':
		url = ("https://www.footlocker.de/api/products/pdp/")
		countrycode = 'de'
		regioncountry = 'Germany'

	elif region == 'FR' or region == 'fr':
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
		"authority": "www.footlocker.nl",
		'pragma': "no-cache",
		'cache-control': "no-cache",
		'accept': "application/json, text/javascript, */*; q=0.01",
		'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36",
		'x-requested-with': "XMLHttpRequest",
		'sec-fetch-site': "same-origin",
		'sec-fetch-mode': "cors",
		'sec-fetch-dest': "empty",
		'referer': link,
		'accept-language': "de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7"
		}

		url = ("https://www.footlocker.nl/INTERSHOP/web/FLE/Footlocker-Footlocker_NL-Site/en_GB/-/EUR/ViewProduct-ProductVariationSelect")
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
	else:
		await ctx.send('This region is not supported by our stock checker.')

	if region == 'FR' or region == 'fr' or region == 'NL' or region == 'nl' or region == 'UK' or region == 'couk' or region == 'GB' or region == 'gb' or region == 'SG' or region == 'sg' or region == 'MY' or region == 'my' or region == 'HK' or region == 'hk' or region == 'MO' or region == 'mo' or region == 'AU' or region == 'comau':
		pid = link[-12:]
		print("Getting Stock for " + pid + " on FTL " + countrycode)
		embed3=discord.Embed(title="Footlocker Stock Checker :flag_" + countrycode + ":", description='Checking backend...', color=setembedcolor)
		embed3.set_footer(text=setfootertext, icon_url=setfooterimage)
		test91 = await ctx.send(embed=embed3)
		parameters = {
		"BaseSKU": pid,
		"InventoryServerity": "ProductDetail",
		}
		proxy = getRandomProxy()
		getpid7 = pid + "070"
		getnewpid7 = "Quantity_" + pid + "070"
		print(region)
		if region == "NL" or region == "nl" or region == "AU" or region == "au":
			print(proxy)
			response = requests.get(url, headers=headers, params=parameters, proxy=proxy)
			pprint(response)
		else:
			response = requests.get(url, headers=headers, params=parameters)
		if 'Foot Locker - Please Stand By' in response.text:
			embed=discord.Embed(title="Footlocker Stock Checker - Failed", color=setembedcolor)
			img = 'https://images.footlocker.com/is/image/FLEU/' + pid + '_01?wid=763&hei=538&fmt=png-alpha'
			embed.set_thumbnail(url=img)
			embed.add_field(name="Info", value="Queue is up, we can't check stock!", inline=False)
			embed.set_footer(text=setfootertext, icon_url=setfooterimage)
			await ctx.send(embed=embed)
		elif 'Foot Locker - Sold Out!' in response.text:
			embed=discord.Embed(title="Footlocker Stock Checker - Failed", color=setembedcolor)
			img = 'https://images.footlocker.com/is/image/FLEU/' + pid + '_01?wid=763&hei=538&fmt=png-alpha'
			embed.set_thumbnail(url=img)
			embed.add_field(name="Info", value="Product is loaded as Sold out!", inline=False)
			embed.set_footer(text='OOS#4315 STOCK CHECKER', icon_url="https://cdn.discordapp.com/attachments/797052521582952468/797231957951643668/Pigeon_Proxies3.png")
			await ctx.send(embed=embed)
		elif 'Please enable JS and disable any ad' in response.text:
			embed=discord.Embed(title="Footlocker Stock Checker - Failed", color=setembedcolor)
			img = 'https://images.footlocker.com/is/image/FLEU/' + pid + '_01?wid=763&hei=538&fmt=png-alpha'
			embed.set_thumbnail(url=img)
			embed.add_field(name="Info", value="Datadome is up - Please try later", inline=False)
			embed.set_footer(text=setfootertext, icon_url=setfooterimage)
			await ctx.send(embed=embed)
		elif not getpid7 in response.text:
			embed=discord.Embed(title="Footlocker Stock Checker - Failed", color=setembedcolor)
			response2 = requests.get(link)
			soup2 = BeautifulSoup(response2.content, "html.parser")
			img = soup2.find("meta", {"property":"og:image"})["content"]
			embed.set_thumbnail(url=img)
			embed.add_field(name="Info", value="Product has no stock loaded", inline=False)
			embed.set_footer(text=setfootertext, icon_url=setfooterimage)
			await ctx.send(embed=embed)
		elif getnewpid7 in response.text:
			embed=discord.Embed(title="Footlocker Stock Checker - Failed", color=setembedcolor)
			response2 = requests.get(link)
			soup2 = BeautifulSoup(response2.content, "html.parser")
			img = soup2.find("meta", {"property":"og:image"})["content"]
			embed.set_thumbnail(url=img)
			embed.add_field(name="Info", value="Product has no stock loaded", inline=False)
			embed.set_footer(text=setfootertext, icon_url=setfooterimage)
			await ctx.send(embed=embed)
		response.raise_for_status()
		soup = BeautifulSoup(response.json()["content"], "html.parser")
		response2 = requests.get(link)
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
				embed.set_footer(text=setfootertext, icon_url=setfooterimage)
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
		if not date:
			date = "Live"
		stockinfo = ":green_square:  -  More than 6 stock\n:yellow_square:  -  6 or less stock\n:red_square:  -  Out of Stock"

	if region == 'DE' or region == 'de' or region == 'IT' or region == 'it' or region == 'AT' or region == 'at' or region == 'HU' or region == 'hu' or region == 'PL' or region == 'pl' or region == 'ES' or region == 'es' or region == 'PT' or region == 'pt' or region == 'GR' or region == 'gr' or region == 'NO' or region == 'no' or region == 'BE' or region == 'be' or region == 'IE' or region == 'ie' or region == 'CZ' or region == 'cz' or region == 'SE' or region == 'se':
		pidlink = link[-17:]
		pid = pidlink[:12]
		print("Getting Stock for " + pid + " on FTL " + countrycode)
		embed3=discord.Embed(title="Footlocker Stock Checker :flag_" + countrycode + ":", description='Checking backend...', color=setembedcolor)
		embed3.set_footer(text='OOS#4315 STOCK CHECKER', icon_url="https://cdn.discordapp.com/attachments/797052521582952468/797231957951643668/Pigeon_Proxies3.png")
		test91 = await ctx.send(embed=embed3)
		urllink = url + pid
		proxy = getRandomProxy()
		response = requests.get(urllink)
		response2 = requests.get(link)
		if 'Please enable JS and disable any ad' in response.text:
			embed=discord.Embed(title="Footlocker Stock Checker - Failed", color=setembedcolor)
			img = 'https://images.footlocker.com/is/image/FLEU/' + pid + '_01?wid=763&hei=538&fmt=png-alpha'
			embed.set_thumbnail(url=img)
			embed.add_field(name="Info", value="Datadome is up - Please try later", inline=False)
			embed.set_footer(text=setfootertext, icon_url=setfooterimage)
			await ctx.send(embed=embed)
		elif 'FlBusinessErrorWebServiceException' in response.text:
			embed=discord.Embed(title="Footlocker Stock Checker - Failed", color=setembedcolor)
			img = 'https://images.footlocker.com/is/image/FLEU/' + pid + '_01?wid=763&hei=538&fmt=png-alpha'
			embed.set_thumbnail(url=img)
			embed.add_field(name="Info", value="An error occured, product might be pulled or sold out", inline=False)
			embed.set_footer(text=setfootertext, icon_url=setfooterimage)
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

		for i in sizelist: 
			if i not in sizelistwithoutdups: 
				sizelistwithoutdups.append(i)
		
		allsizepids = [*map(str, allsizepids)]
		allcoorectsizepids = []
		for i in allsizepids:
			if pid in i:
				allcoorectsizepids.append(i)
		
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
	embed.set_footer(text=setfootertext, icon_url=setfooterimage)
	await ctx.message.delete()
	await ctx.send(embed=embed)
	await test91.delete()

@bot.command()
@commands.has_any_role(791044154351157328,790654515899662366,644574707475152926,644574705990238210)
async def staff(ctx, link):

	headers = ''
	url = ''
	pid = ''
	shoename = ''
	countrycode = ''
	region = str(link.split("footlocker.")[1].split("/")[0]).replace(".","")
	if region == 'DE' or region == 'de':
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
		"https://www.footlocker.de/INTERSHOP/web/FLE"
		"/Footlocker-Footlocker_DE-Site/de_DE/-/EUR"
		"/ViewProduct-ProductVariationSelect"
		)
		countrycode = 'de'
		regioncountry = 'Germany'

	elif region == 'FR' or region == 'fr':
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
			"https://www.footlocker.nl/INTERSHOP/web/FLE"
			"/Footlocker-Footlocker_NL-Site/nl_NL/-/EUR"
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
	else:
		await ctx.send('This region is not supported by our stock checker.')

	if region == 'DE' or region == 'de' or region == 'FR' or region == 'fr' or region == 'NL' or region == 'nl' or region == 'UK' or region == 'couk' or region == 'GB' or region == 'gb' or region == 'SG' or region == 'sg' or region == 'MY' or region == 'my' or region == 'HK' or region == 'hk' or region == 'MO' or region == 'mo' or region == 'AU' or region == 'comau':
		pid = link[-12:]
		print("Getting Stock for " + pid + " on FTL " + countrycode)
		embed3=discord.Embed(title="Footlocker Stock Checker :flag_" + countrycode + ":", description='Checking backend...', color=setembedcolor)
		embed3.set_footer(text=setfootertext, icon_url=setfooterimage)
		test91 = await ctx.send(embed=embed3)
		parameters = {
		"BaseSKU": pid,
		"InventoryServerity": "ProductDetail",
		}
		proxy = getRandomProxy()
		getpid7 = pid + "070"
		getnewpid7 = "Quantity_" + pid + "070"
		if region == "nl" or region == "NL" or region == "AU" or region == "au":
			response = requests.get(url, headers=headers, params=parameters, proxy=proxy)
		else:
			response = requests.get(url, headers=headers, params=parameters)
		if 'Foot Locker - Please Stand By' in response.text:
			embed=discord.Embed(title="Footlocker Stock Checker - Failed", color=setembedcolor)
			img = 'https://images.footlocker.com/is/image/FLEU/' + pid + '_01?wid=763&hei=538&fmt=png-alpha'
			embed.set_thumbnail(url=img)
			embed.add_field(name="Info", value="Queue is up, we can't check stock!", inline=False)
			embed.set_footer(text=setfootertext, icon_url=setfooterimage)
			await ctx.send(embed=embed)
		elif 'Foot Locker - Sold Out!' in response.text:
			embed=discord.Embed(title="Footlocker Stock Checker - Failed", color=setembedcolor)
			img = 'https://images.footlocker.com/is/image/FLEU/' + pid + '_01?wid=763&hei=538&fmt=png-alpha'
			embed.set_thumbnail(url=img)
			embed.add_field(name="Info", value="Product is loaded as Sold out!", inline=False)
			embed.set_footer(text='OOS#4315 STOCK CHECKER', icon_url="https://cdn.discordapp.com/attachments/797052521582952468/797231957951643668/Pigeon_Proxies3.png")
			await ctx.send(embed=embed)
		elif 'Please enable JS and disable any ad' in response.text:
			embed=discord.Embed(title="Footlocker Stock Checker - Failed", color=setembedcolor)
			img = 'https://images.footlocker.com/is/image/FLEU/' + pid + '_01?wid=763&hei=538&fmt=png-alpha'
			embed.set_thumbnail(url=img)
			embed.add_field(name="Info", value="Datadome is up - Please try later", inline=False)
			embed.set_footer(text=setfootertext, icon_url=setfooterimage)
			await ctx.send(embed=embed)
		elif not getpid7 in response.text:
			embed=discord.Embed(title="Footlocker Stock Checker - Failed", color=setembedcolor)
			response2 = requests.get(link)
			soup2 = BeautifulSoup(response2.content, "html.parser")
			img = soup2.find("meta", {"property":"og:image"})["content"]
			embed.set_thumbnail(url=img)
			embed.add_field(name="Info", value="Product has no stock loaded", inline=False)
			embed.set_footer(text=setfootertext, icon_url=setfooterimage)
			await ctx.send(embed=embed)
		elif getnewpid7 in response.text:
			embed=discord.Embed(title="Footlocker Stock Checker - Failed", color=setembedcolor)
			response2 = requests.get(link)
			soup2 = BeautifulSoup(response2.content, "html.parser")
			img = soup2.find("meta", {"property":"og:image"})["content"]
			embed.set_thumbnail(url=img)
			embed.add_field(name="Info", value="Product has no stock loaded", inline=False)
			embed.set_footer(text=setfootertext, icon_url=setfooterimage)
			await ctx.send(embed=embed)
		response.raise_for_status()
		soup = BeautifulSoup(response.json()["content"], "html.parser")
		response2 = requests.get(link)
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
				embed.set_footer(text=setfootertext, icon_url=setfooterimage)
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
		if not date:
			date = "Live"
		stockinfo = ":green_square:  -  More than 6 stock\n:yellow_square:  -  6 or less stock\n:red_square:  -  Out of Stock"

	if region == 'IT' or region == 'it' or region == 'AT' or region == 'at' or region == 'HU' or region == 'hu' or region == 'PL' or region == 'pl' or region == 'ES' or region == 'es' or region == 'PT' or region == 'pt' or region == 'GR' or region == 'gr' or region == 'NO' or region == 'no' or region == 'BE' or region == 'be' or region == 'IE' or region == 'ie' or region == 'CZ' or region == 'cz' or region == 'SE' or region == 'se':
		pidlink = link[-17:]
		pid = pidlink[:12]
		print("Getting Stock for " + pid + " on FTL " + countrycode)
		embed3=discord.Embed(title="Footlocker Stock Checker :flag_" + countrycode + ":", description='Checking backend...', color=setembedcolor)
		embed3.set_footer(text='OOS#4315 STOCK CHECKER', icon_url="https://cdn.discordapp.com/attachments/797052521582952468/797231957951643668/Pigeon_Proxies3.png")
		test91 = await ctx.send(embed=embed3)
		urllink = url + pid
		proxy = getRandomProxy()
		response = requests.get(urllink)
		response2 = requests.get(link)
		if 'Please enable JS and disable any ad' in response.text:
			embed=discord.Embed(title="Footlocker Stock Checker - Failed", color=setembedcolor)
			img = 'https://images.footlocker.com/is/image/FLEU/' + pid + '_01?wid=763&hei=538&fmt=png-alpha'
			embed.set_thumbnail(url=img)
			embed.add_field(name="Info", value="Datadome is up - Please try later", inline=False)
			embed.set_footer(text=setfootertext, icon_url=setfooterimage)
			await ctx.send(embed=embed)
		elif 'FlBusinessErrorWebServiceException' in response.text:
			embed=discord.Embed(title="Footlocker Stock Checker - Failed", color=setembedcolor)
			img = 'https://images.footlocker.com/is/image/FLEU/' + pid + '_01?wid=763&hei=538&fmt=png-alpha'
			embed.set_thumbnail(url=img)
			embed.add_field(name="Info", value="An error occured, product might be pulled or sold out", inline=False)
			embed.set_footer(text=setfootertext, icon_url=setfooterimage)
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

		for i in sizelist: 
			if i not in sizelistwithoutdups: 
				sizelistwithoutdups.append(i)
		
		allsizepids = [*map(str, allsizepids)]
		allcoorectsizepids = []
		for i in allsizepids:
			if pid in i:
				allcoorectsizepids.append(i)
		
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
	embed.set_footer(text=setfootertext, icon_url=setfooterimage)
	await ctx.message.delete()
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
	if region == 'DE' or region == 'de':
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
		"https://www.footlocker.de/INTERSHOP/web/FLE"
		"/Footlocker-Footlocker_DE-Site/de_DE/-/EUR"
		"/ViewProduct-ProductVariationSelect"
		)
		countrycode = 'de'
		regioncountry = 'Germany'
		setwebhook = euregionhook

	elif region == 'FR' or region == 'fr':
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
			"https://www.footlocker.nl/INTERSHOP/web/FLE"
			"/Footlocker-Footlocker_NL-Site/nl_NL/-/EUR"
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
	else:
		await ctx.send('This region is not supported by our stock checker.')

	if region == 'DE' or region == 'de' or region == 'FR' or region == 'fr' or region == 'NL' or region == 'nl' or region == 'UK' or region == 'couk' or region == 'GB' or region == 'gb' or region == 'SG' or region == 'sg' or region == 'MY' or region == 'my' or region == 'HK' or region == 'hk' or region == 'MO' or region == 'mo' or region == 'AU' or region == 'comau':
		pid = link[-12:]
		print("Getting Stock for " + pid + " on FTL " + countrycode)
		embed3=discord.Embed(title="Footlocker Stock Checker :flag_" + countrycode + ":", description='Checking backend...', color=setembedcolor)
		embed3.set_footer(text=setfootertext, icon_url=setfooterimage)
		test91 = await ctx.send(embed=embed3)
		parameters = {
		"BaseSKU": pid,
		"InventoryServerity": "ProductDetail",
		}
		proxy = getRandomProxy()
		getpid7 = pid + "070"
		getnewpid7 = "Quantity_" + pid + "070"
		if region == "nl" or region == "NL" or region == "AU" or region == "au":
			response = requests.get(url, headers=headers, params=parameters, proxy=proxy)
		else:
			response = requests.get(url, headers=headers, params=parameters)
		if 'Foot Locker - Please Stand By' in response.text:
			embed=discord.Embed(title="Footlocker Stock Checker - Failed", color=setembedcolor)
			img = 'https://images.footlocker.com/is/image/FLEU/' + pid + '_01?wid=763&hei=538&fmt=png-alpha'
			embed.set_thumbnail(url=img)
			embed.add_field(name="Info", value="Queue is up, we can't check stock!", inline=False)
			embed.set_footer(text=setfootertext, icon_url=setfooterimage)
			await ctx.send(embed=embed)
		elif 'Foot Locker - Sold Out!' in response.text:
			embed=discord.Embed(title="Footlocker Stock Checker - Failed", color=setembedcolor)
			img = 'https://images.footlocker.com/is/image/FLEU/' + pid + '_01?wid=763&hei=538&fmt=png-alpha'
			embed.set_thumbnail(url=img)
			embed.add_field(name="Info", value="Product is loaded as Sold out!", inline=False)
			embed.set_footer(text='OOS#4315 STOCK CHECKER', icon_url="https://cdn.discordapp.com/attachments/797052521582952468/797231957951643668/Pigeon_Proxies3.png")
			await ctx.send(embed=embed)
		elif 'Please enable JS and disable any ad' in response.text:
			embed=discord.Embed(title="Footlocker Stock Checker - Failed", color=setembedcolor)
			img = 'https://images.footlocker.com/is/image/FLEU/' + pid + '_01?wid=763&hei=538&fmt=png-alpha'
			embed.set_thumbnail(url=img)
			embed.add_field(name="Info", value="Datadome is up - Please try later", inline=False)
			embed.set_footer(text=setfootertext, icon_url=setfooterimage)
			await ctx.send(embed=embed)
		elif not getpid7 in response.text:
			embed=discord.Embed(title="Footlocker Stock Checker - Failed", color=setembedcolor)
			response2 = requests.get(link)
			soup2 = BeautifulSoup(response2.content, "html.parser")
			img = soup2.find("meta", {"property":"og:image"})["content"]
			embed.set_thumbnail(url=img)
			embed.add_field(name="Info", value="Product has no stock loaded", inline=False)
			embed.set_footer(text=setfootertext, icon_url=setfooterimage)
			await ctx.send(embed=embed)
		elif getnewpid7 in response.text:
			embed=discord.Embed(title="Footlocker Stock Checker - Failed", color=setembedcolor)
			response2 = requests.get(link)
			soup2 = BeautifulSoup(response2.content, "html.parser")
			img = soup2.find("meta", {"property":"og:image"})["content"]
			embed.set_thumbnail(url=img)
			embed.add_field(name="Info", value="Product has no stock loaded", inline=False)
			embed.set_footer(text=setfootertext, icon_url=setfooterimage)
			await ctx.send(embed=embed)
		response.raise_for_status()
		soup = BeautifulSoup(response.json()["content"], "html.parser")
		response2 = requests.get(link)
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
				embed.set_footer(text=setfootertext, icon_url=setfooterimage)
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
		if not date:
			date = "Live"
		stockinfo = ":green_square:  -  More than 6 stock\n:yellow_square:  -  6 or less stock\n:red_square:  -  Out of Stock"

	if region == 'IT' or region == 'it' or region == 'AT' or region == 'at' or region == 'HU' or region == 'hu' or region == 'PL' or region == 'pl' or region == 'ES' or region == 'es' or region == 'PT' or region == 'pt' or region == 'GR' or region == 'gr' or region == 'NO' or region == 'no' or region == 'BE' or region == 'be' or region == 'IE' or region == 'ie' or region == 'CZ' or region == 'cz' or region == 'SE' or region == 'se':
		pidlink = link[-17:]
		pid = pidlink[:12]
		print("Getting Stock for " + pid + " on FTL " + countrycode)
		embed3=discord.Embed(title="Footlocker Stock Checker :flag_" + countrycode + ":", description='Checking backend...', color=setembedcolor)
		embed3.set_footer(text='OOS#4315 STOCK CHECKER', icon_url="https://cdn.discordapp.com/attachments/797052521582952468/797231957951643668/Pigeon_Proxies3.png")
		test91 = await ctx.send(embed=embed3)
		urllink = url + pid
		proxy = getRandomProxy()
		response = requests.get(urllink)
		response2 = requests.get(link)
		if 'Please enable JS and disable any ad' in response.text:
			embed=discord.Embed(title="Footlocker Stock Checker - Failed", color=setembedcolor)
			img = 'https://images.footlocker.com/is/image/FLEU/' + pid + '_01?wid=763&hei=538&fmt=png-alpha'
			embed.set_thumbnail(url=img)
			embed.add_field(name="Info", value="Datadome is up - Please try later", inline=False)
			embed.set_footer(text=setfootertext, icon_url=setfooterimage)
			await ctx.send(embed=embed)
		elif 'FlBusinessErrorWebServiceException' in response.text:
			embed=discord.Embed(title="Footlocker Stock Checker - Failed", color=setembedcolor)
			img = 'https://images.footlocker.com/is/image/FLEU/' + pid + '_01?wid=763&hei=538&fmt=png-alpha'
			embed.set_thumbnail(url=img)
			embed.add_field(name="Info", value="An error occured, product might be pulled or sold out", inline=False)
			embed.set_footer(text=setfootertext, icon_url=setfooterimage)
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

		for i in sizelist: 
			if i not in sizelistwithoutdups: 
				sizelistwithoutdups.append(i)
		
		allsizepids = [*map(str, allsizepids)]
		allcoorectsizepids = []
		for i in allsizepids:
			if pid in i:
				allcoorectsizepids.append(i)
		
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
	for i in range(len(setwebhook)):
		webhook = DiscordWebhook(url=setwebhook[i])
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
		embed.set_footer(text=setfootertext, icon_url=setfooterimage)
		embed.set_thumbnail(url=shoepic)
		webhook.add_embed(embed)
		webhook.execute()
		await ctx.message.delete()
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
		embed3=discord.Embed(title="Footlocker Stock Checker :flag_" + countrycode + ":", description='Checking backend...', color=setembedcolor)
		embed3.set_footer(text=setfootertext, icon_url=setfooterimage)
		test91 = await ctx.send(embed=embed3)
		regioncountry = 'Germany'
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
		"https://www.sidestep-shoes.nl/INTERSHOP/web/WFS"
		"/Sidestep-Sidestep_NL-Site/nl_NL/-/EUR"
		"/ViewProduct-ProductVariationSelect"
		)
		pid = link[-12:]
		countrycode = 'nl'
		print("Getting Stock for " + pid + " on Sidestep " + countrycode)
		embed3=discord.Embed(title="Footlocker Stock Checker :flag_" + countrycode + ":", description='Checking backend...', color=setembedcolor)
		embed3.set_footer(text=setfootertext, icon_url=setfooterimage)
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
		response.raise_for_status()
		soup = BeautifulSoup(response.json()["content"], "html.parser")
		response2 = requests.get(link)
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
		print(mojisizerange)
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
	embed.set_footer(text=setfootertext, icon_url=setfooterimage)
	await ctx.message.delete()
	await ctx.send(embed=embed)
	await test91.delete()


@bot.command()
async def countries(context):
	embed=discord.Embed(title="All Support FTL Countries", color=setembedcolor)
	old_region = ['GB','FR','DE','NL','SG','AU','MY','HK','MO']
	old_region_flag = [':flag_gb:',':flag_fr:',':flag_de:',':flag_nl:',':flag_sg:',':flag_au:',':flag_my:',':flag_hk:',':flag_mo:']
	new_region = ['AT','BE','DK','HU','IE','IT','GR','LU','NO','CZ','PL','PT','ES','SE']
	new_region_flag = [':flag_at:',':flag_be:',':flag_dk:',':flag_hu:',':flag_ie:',':flag_it:',':flag_gr:',':flag_lu:',':flag_no:',':flag_cz:',':flag_pl:',':flag_pt:',':flag_es:',':flag_se:']
	countriesold = "\n".join("{0} {1}".format(x,y) for x,y in zip(old_region,old_region_flag))
	countriesnew = "\n".join("{0} {1}".format(x,y) for x,y in zip(new_region,new_region_flag))
	embed.add_field(name="OLD REGION", value=countriesold, inline=True)
	embed.add_field(name="NEW REGION", value=countriesnew, inline=True)
	embed.set_footer(text=setfootertext, icon_url=setfooterimage)
	await context.send(embed=embed)

@bot.command()
async def help(context):
	embed=discord.Embed(title="All Commands", color=setembedcolor)
	embed.add_field(name="?help", value='Shows you this command', inline=False)
	embed.add_field(name="?countries", value='Sends out an embed with a list of all supported FTL regions', inline=False)
	embed.add_field(name="?release (region) (link)", value='Sends out the an embed with checked stock to a release channel', inline=False)
	embed.add_field(name="?pigeon (region) (link)", value='STAFF ONLY! Can only be used by pigeon proxies team \nSends out the an embed with checked stock to to a staff channel', inline=False)
	embed.add_field(name="?stock (region) (link)", value='Can only be used by <@351639955531104258> & <@175953718750085121>', inline=False)
	embed.add_field(name="?side de (link)", value='Sends out an embed with checked stock for DE region', inline=False)
	embed.set_footer(text='OOS#4315 STOCK CHECKER', icon_url="https://cdn.discordapp.com/attachments/797052521582952468/797231957951643668/Pigeon_Proxies3.png")
	await context.send(embed=embed)

@bot.event
async def on_command_error(ctx, error):
	if isinstance(error, commands.CheckFailure):
			embed = discord.Embed(title="Something went wrong", color=setembedcolor)
			embed.add_field(name="Error", value="Either your command is wrong or you arent allowed to use this command \n Contact <@175953718750085121> or <@351639955531104258> for any issues!", inline=False)
			embed.set_footer(text=setfootertext, icon_url=setfooterimage)
			await ctx.send(embed=embed)

@bot.command()
async def clear(ctx, amount=2):
	await ctx.channel.purge(limit=amount)

@bot.command()
async def load(ctx, extension):
	bot.load_extension(f'cogs.{extension}')

@bot.command()
async def unload(ctx, extension):
	bot.unload_extension(f'cogs.{extension}')

bot.run('NzkyODU1MjY5MjQzMjI0MTQ1.X-jyAg.CD0xNJ37E5n_xt8x96TxCCEb_EY')