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
from discord.ext.commands import CommandNotFound
bot = commands.Bot(command_prefix = '?', help_command=None)

@bot.event
async def on_ready():
	print('Bot is ready.')
	pass

bottoken = "Nzk4NTY2ODE4ODEzMDUwOTYw.X_25Tg.Fgr9xvAtE0qkJnmHL_dz4gZ3ofw"

setfootertext = "@ScriptingTools | Stock Checker | <?ftlhelp>"
setfooterimage = "https://images-ext-1.discordapp.net/external/atwFnJRaXHB0ebXrVSPjVWDXe5hL2OQ0JBWopjGcVCY/https/images-ext-2.discordapp.net/external/gGrbK8FUkmby_Ao8mmH9dZ4RI1cvfkhpUNBlIB46XQE/https/media.discordapp.net/attachments/460974692073734164/680067025493950474/Wcu7EAAAAASUVORK5CYII.png"
setembedcolor = 0x00000

euregionhook = ["https://discord.com/api/webhooks/795830345668362262/q6mhcOBrm6JsG6n7RE-J0XFn9arGDFhG9WL-by45-n9qidrKEHjXBywzo__nBu_yWDmo","https://discord.com/api/webhooks/805796056024481823/25pAS0D_v75ADprKf2HHGHYffcqfSpA__2Br6cnVj95hdh1-3V9EXIiHjHCyWVpE3WUf","https://discord.com/api/webhooks/806877294907883540/w30E5dZFEmeFX3VtuWUsrWxyVYW-Gb5GrHcBT_88ilNQjJlHz7FqGm5rJUIz6D6vwvXM"]
asiaregionhook = ["https://discord.com/api/webhooks/795830744110071819/oqo38JTYAl_PDIdFJZtQq-01ILvRtSrQpP4LR_zbzyDthOaEsGV1PEjyD8QWvuryWsHN","https://discord.com/api/webhooks/805796056024481823/25pAS0D_v75ADprKf2HHGHYffcqfSpA__2Br6cnVj95hdh1-3V9EXIiHjHCyWVpE3WUf","https://discord.com/api/webhooks/806877294907883540/w30E5dZFEmeFX3VtuWUsrWxyVYW-Gb5GrHcBT_88ilNQjJlHz7FqGm5rJUIz6D6vwvXM"]
newregionhook = ["https://discord.com/api/webhooks/796527829261090848/36pfX9AeOlz321uMFTwiibnwAwxT_noBgTkt98JgCoh1xzufCn6yQIW8LkPDtc5iv4dt","https://discord.com/api/webhooks/805796056024481823/25pAS0D_v75ADprKf2HHGHYffcqfSpA__2Br6cnVj95hdh1-3V9EXIiHjHCyWVpE3WUf","https://discord.com/api/webhooks/806877294907883540/w30E5dZFEmeFX3VtuWUsrWxyVYW-Gb5GrHcBT_88ilNQjJlHz7FqGm5rJUIz6D6vwvXM"]

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
async def staff(ctx, link):

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
		if region == "nl" or region == "NL":
			response = requests.get(url, headers=headers, params=parameters, verify=False)
		else:
			response = requests.get(url, headers=headers, params=parameters, verify=False)
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
			embed.set_footer(text=setfootertext, icon_url=setfooterimage)
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
			response2 = requests.get(link, headers=headers, verify=False)
			soup2 = BeautifulSoup(response2.content, "html.parser")
			img = soup2.find("meta", {"property":"og:image"})["content"]
			embed.set_thumbnail(url=img)
			embed.add_field(name="Info", value="Product has no stock loaded", inline=False)
			embed.set_footer(text=setfootertext, icon_url=setfooterimage)
			await ctx.send(embed=embed)
		elif getnewpid7 in response.text:
			embed=discord.Embed(title="Footlocker Stock Checker - Failed", color=setembedcolor)
			response2 = requests.get(link, headers=headers, verify=False)
			soup2 = BeautifulSoup(response2.content, "html.parser")
			img = soup2.find("meta", {"property":"og:image"})["content"]
			embed.set_thumbnail(url=img)
			embed.add_field(name="Info", value="Product has no stock loaded", inline=False)
			embed.set_footer(text=setfootertext, icon_url=setfooterimage)
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

	if region == 'DE' or region == 'de' or region == 'IT' or region == 'dk' or region == 'it' or region == 'AT' or region == 'at' or region == 'HU' or region == 'hu' or region == 'PL' or region == 'pl' or region == 'ES' or region == 'es' or region == 'PT' or region == 'pt' or region == 'GR' or region == 'gr' or region == 'NO' or region == 'no' or region == 'BE' or region == 'be' or region == 'IE' or region == 'ie' or region == 'CZ' or region == 'cz' or region == 'SE' or region == 'se':
		pidlink = link[-17:]
		pid = pidlink[:12]
		print("Getting Stock for " + pid + " on FTL " + countrycode)
		embed3=discord.Embed(title="Footlocker Stock Checker :flag_" + countrycode + ":", description='Checking backend...', color=setembedcolor)
		embed3.set_footer(text=setfootertext, icon_url=setfooterimage)
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
	embed.set_footer(text=setfootertext, icon_url=setfooterimage)
	await ctx.message.delete()
	await ctx.send(embed=embed)
	await test91.delete()

@bot.command()
@commands.has_any_role(644574705990238210,644574707475152926,806766600686010432,806855381656928266,790654515899662366,791044154351157328)
async def stock(ctx, link):

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
		if region == "nl" or region == "NL":
			response = requests.get(url, headers=headers, params=parameters)
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
			embed.set_footer(text=setfootertext, icon_url=setfooterimage)
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

	if region == "DE" or region == "de" or region == 'IT' or region == 'it' or region == 'AT' or region == 'at' or region == 'dk' or region == 'HU' or region == 'hu' or region == 'PL' or region == 'pl' or region == 'ES' or region == 'es' or region == 'PT' or region == 'pt' or region == 'GR' or region == 'gr' or region == 'NO' or region == 'no' or region == 'BE' or region == 'be' or region == 'IE' or region == 'ie' or region == 'CZ' or region == 'cz' or region == 'SE' or region == 'se':
		pidlink = link[-17:]
		pid = pidlink[:12]
		print("Getting Stock for " + pid + " on FTL " + countrycode)
		embed3=discord.Embed(title="Footlocker Stock Checker :flag_" + countrycode + ":", description='Checking backend...', color=setembedcolor)
		embed3.set_footer(text=setfootertext, icon_url=setfooterimage)
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
		if region == "nl" or region == "NL":
			response = requests.get(url, headers=headers, params=parameters, verify=False)
		else:
			response = requests.get(url, headers=headers, params=parameters, verify=False)
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
			embed.set_footer(text=setfootertext, icon_url=setfooterimage)
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
			response2 = requests.get(link, headers=headers, verify=False)
			soup2 = BeautifulSoup(response2.content, "html.parser")
			img = soup2.find("meta", {"property":"og:image"})["content"]
			embed.set_thumbnail(url=img)
			embed.add_field(name="Info", value="Product has no stock loaded", inline=False)
			embed.set_footer(text=setfootertext, icon_url=setfooterimage)
			await ctx.send(embed=embed)
		elif getnewpid7 in response.text:
			embed=discord.Embed(title="Footlocker Stock Checker - Failed", color=setembedcolor)
			response2 = requests.get(link, headers=headers, verify=False)
			soup2 = BeautifulSoup(response2.content, "html.parser")
			img = soup2.find("meta", {"property":"og:image"})["content"]
			embed.set_thumbnail(url=img)
			embed.add_field(name="Info", value="Product has no stock loaded", inline=False)
			embed.set_footer(text=setfootertext, icon_url=setfooterimage)
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

	if region == 'DE' or region == 'de' or region == 'IT' or region == 'it' or region == 'dk' or region == 'AT' or region == 'at' or region == 'HU' or region == 'hu' or region == 'PL' or region == 'pl' or region == 'ES' or region == 'es' or region == 'PT' or region == 'pt' or region == 'GR' or region == 'gr' or region == 'NO' or region == 'no' or region == 'BE' or region == 'be' or region == 'IE' or region == 'ie' or region == 'CZ' or region == 'cz' or region == 'SE' or region == 'se':
		pidlink = link[-17:]
		pid = pidlink[:12]
		print("Getting Stock for " + pid + " on FTL " + countrycode)
		embed3=discord.Embed(title="Footlocker Stock Checker :flag_" + countrycode + ":", description='Checking backend...', color=setembedcolor)
		embed3.set_footer(text=setfootertext, icon_url=setfooterimage)
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
		embed3=discord.Embed(title="Side-Step Stock Checker :flag_" + countrycode + ":", description='Checking backend...', color=setembedcolor)
		embed3.set_footer(text=setfootertext, icon_url=setfooterimage)
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
	embed.set_footer(text=setfootertext, icon_url=setfooterimage)
	await ctx.message.delete()
	await ctx.send(embed=embed)
	await test91.delete()


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
	embed.set_footer(text=setfootertext, icon_url=setfooterimage)
	await context.send(embed=embed)

@bot.command()
async def ftlhelp(context):
	embed=discord.Embed(title="All Commands", color=setembedcolor)
	embed.add_field(name="List of all countries supported by FTL", value='?ftlcountries', inline=False)
	embed.add_field(name="Command Format - FTL", value='?stock <link>', inline=False)
	embed.add_field(name="Command Format - Sidestep", value='?side <link>', inline=False)
	embed.set_footer(text=setfootertext, icon_url=setfooterimage)
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
		embed.set_footer(text=setfootertext, icon_url=setfooterimage)
		await ctx.send(embed=embed)
		return
	raise error

@bot.command()
async def clear(ctx, amount=2):
	await ctx.channel.purge(limit=amount)

bot.run(bottoken)
