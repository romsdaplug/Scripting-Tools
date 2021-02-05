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


bot = commands.Bot(command_prefix = '?', help_command=None)
bottoken ="Nzk4NTY2ODE4ODEzMDUwOTYw.X_25Tg.Fgr9xvAtE0qkJnmHL_dz4gZ3ofw"

init(autoreset=True)

@bot.event
async def on_ready():
	print('Bot is ready.')
	pass

def check_if_it_is_me(ctx):
	return ctx.message.author.id == 175953718750085121 or ctx.message.author.id == 351639955531104258 or ctx.message.author.id == 243519195529084939 or ctx.message.author.id == 272815177659842561 or ctx.message.author.id == 418649205494775820

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
  		}
  	else:
  		proxyDict = {
  		"http": "http://" + proxySplit[2] + ":" + proxySplit[3] + "@" + proxySplit[0] + ":" + proxySplit[1] + "/",
  		}          
  		return proxyDict
  else:
  	proxyDict = {}
  	proxyDict = {
  	"http": "http://",
  	}             
  return proxyDict

@bot.command()
async def snipespid(context, pid):
	session = aiohttp.ClientSession()
	asd = 0
	headers = {
	    'authority': "www.snipes.com",
	    'cache-control': "no-cache",
	    "pragma": "no-cache",
	    'upgrade-insecure-requests': "1",
	    'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36",
	    'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
	    'sec-fetch-site': "none",
	    'sec-fetch-mode': "navigate",
	    'sec-fetch-user': "?1",
	    'sec-fetch-dest': "document",
	    'accept-language': "de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7",
	    }
	headers2 = {
	"Upgrade-Insecure-Requests": "1",
	"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36",
	}


	url = "https://www.snipes.com/p/jordan-air_jordan_1_mid_-black%2Fchile_red%2Fwhite-"+pid+".html?variantId&dwvar_"+pid+"_212&format=ajax"
	proxy = getRandomProxy()
	proxy2 = getRandomProxy()
	proxy3 = proxy2['http'] 
	proxy4 = proxy3.replace('7000/', '7000')
	firstresponse = await session.get(url, headers=headers2, proxy=proxy4)
	await session.close()
	newlink = str(firstresponse.url)
	urlshoename = newlink.split("https://www.snipes.com/p/")[1].split(pid)[0]
	newurl2 = "https://www.snipes.com/p/" + urlshoename + pid + ".html?dwvar_"+pid+"_212"+"&format=ajax"
	newurl = "https://www.snipes.com/p/nike-air_force_1_react_-white%2Fblack%2Funiversity_red-00013801786856.html?dwvar_00013801786856_212&format=ajax&pid=00013801786856"
	producturl = "https://www.snipes.com/p/" + urlshoename + pid + ".html"
	session = aiohttp.ClientSession()
	response = await session.get(newurl, headers=headers, proxy=proxy4)
	text = await response.text()
	pprint(newurl)
	pprint(newurl2)
	if 'https://collector-pxszbf5p84.perimeterx.net' in text:
		while asd > 5:
			await session.close()
			proxy = getRandomProxy()
			proxy2 = getRandomProxy()
			proxy3 = proxy2['http'] 
			proxy4 = proxy3.replace('7000/', '7000')
			session = aiohttp.ClientSession()
			response = await session.get(newurl, headers=headers, proxy=proxy4)
			text = await response.text()
			asd = asd + 1
			print("PX banned - Retry Nr. " + str(asd))
			if 'https://collector-pxszbf5p84.perimeterx.net' in text:
				continue
			else:
				break
	try:
		jsondata = json.loads(text)
		product = jsondata["product"]
		productName = product["productName"]
		values = product["variationAttributes"][0]["values"]
		releasedate = product["custom"]["releaseDateUTC"]
		if releasedate == "":
			releasedate = "Live"
		sku = product["facts"][1]["value"]
		variantId = []
		size = []
		for i in range(len(values)):
			variantId.append(values[i]["variantId"])
			size.append(values[i]["displayValue"])
		getvariantIdlist = len(variantId)
		variantIdlist = "\n".join(variantId)
		sizelist = "\n".join(size)
		pidimage = pid[7:]
		embedproductlink = "[" + sku + "](" + producturl + ")"
		image = "https://images.weserv.nl/?url=https://www.snipes.com/on/demandware.static/-/Sites-snse-master-eu/default/dw24f55347/"+pidimage+"_P.png"
		embed=discord.Embed(title="Snipes - "+productName, description='> '+"SKU: "+embedproductlink, color=3743743)
		embed.add_field(name=":bar_chart: Size", value=sizelist, inline=True)
		embed.add_field(name=":pushpin: SKUs", value=variantIdlist, inline=True)
		embed.add_field(name="Release Date", value="`"+str(releasedate)+"`", inline=False)
		embed.set_thumbnail(url=image)
		embed.set_footer(text="ACOM | @ACOMonitor", icon_url="https://cdn.discordapp.com/icons/449269002317987860/21178bb74135a510f015a21a6afe24c1.png")
		await context.send(embed=embed)
		await session.close()
	except (ValueError,UnboundLocalError):
		print("An Error occured")
		embed=discord.Embed(title="Snipes - PID Scraper", color=3743743)
		embed.add_field(name="Error", value="Please try again", inline=True)
		embed.set_footer(text="ACOM | @ACOMonitor", icon_url="https://cdn.discordapp.com/icons/449269002317987860/21178bb74135a510f015a21a6afe24c1.png")
		await context.send(embed=embed)
		await session.close()
@bot.command()
@commands.check(check_if_it_is_me)
async def snipes(context, pid):
	
	now = datetime.now()

	server_name = context.guild.name

	user_name_id = context.author.name + ' ID : ' + str(context.author.id)

	log2 = Fore.CYAN +f'[{server_name}]'
	log3 = Fore.CYAN + f'[{user_name_id}] '

	log = log2 + ' ' + log3

	print(Fore.MAGENTA + f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] " + log + Fore.YELLOW + f"[Getting stock of - {pid}]")

	headers = {
    'authority': "www.snipes.com",
    'cache-control': "no-cache",
    "pragma": "no-cache",
    'upgrade-insecure-requests': "1",
    'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36",
    'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    'sec-fetch-site': "none",
    'sec-fetch-mode': "navigate",
    'sec-fetch-user': "?1",
    'sec-fetch-dest': "document",
    'accept-language': "de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7",
    }

	headers2 = {
	    'authority': "www.snipes.com",
	    'cache-control': "no-cache",
	    "pragma": "no-cache",
	    'upgrade-insecure-requests': "1",
	    'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36",
	    'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
	    'sec-fetch-site': "none",
	    'sec-fetch-mode': "navigate",
	    'sec-fetch-user': "?1",
	    'sec-fetch-dest': "document",
	    'accept-language': "de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7",
	    }

	headers3 = {
	"Upgrade-Insecure-Requests": "1",
	"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36",
	}

	embedstock = []
	embedsize = []
	sizelinks = []
	sku = ""
	releasedate = ""
	pidlist = []
	count = ''

	session = aiohttp.ClientSession()

	embed3=discord.Embed(title="Snipes Stock Checker", description='Checking backend...', color=3743743)
	embed3.set_footer(text='ACOM Snipes Stock Checker', icon_url="https://cdn.discordapp.com/icons/449269002317987860/21178bb74135a510f015a21a6afe24c1.png")
	message = await context.send(embed=embed3)

	proxy = getRandomProxy()

	url = "https://www.snipes.com/p/jordan-air_jordan_1_mid_-black%2Fchile_red%2Fwhite-"+pid+".html?variantId&dwvar_"+pid+"_212&format=ajax"
	proxy = getRandomProxy()
	proxy2 = getRandomProxy()
	proxy3 = proxy2['http'] 
	proxy4 = proxy3.replace('7000/', '7000')
	firstresponse = await session.get(url, headers=headers3, proxy=proxy4)
	await session.close()
	newlink = str(firstresponse.url)
	urlshoename = newlink.split("https://www.snipes.com/p/")[1].split(pid)[0]
	newurl = "https://www.snipes.com/p/" + urlshoename + pid + ".html?variantId&dwvar_"+pid+"_212&format=ajax"
	producturl = "https://www.snipes.com/p/" + urlshoename + pid + ".html"
	session = aiohttp.ClientSession()
	pidresponse = await session.get(newurl, headers=headers2, proxy=proxy4)
	pidtext = await pidresponse.text()
	await session.close()
	while 'https://collector-pxszbf5p84.perimeterx.net' in pidtext:
		await session.close()
		proxy = getRandomProxy()
		proxy2 = getRandomProxy()
		proxy3 = proxy2['http'] 
		proxy4 = proxy3.replace('7000/', '7000')
		session = aiohttp.ClientSession()
		pidresponse = await session.get(newurl, headers=headers2, proxy=proxy4)
		pidtext = await pidresponse.text()
		await session.close()
		print(proxy4)
		if 'https://collector-pxszbf5p84.perimeterx.net' in pidtext:
			continue
		else:
			break
	try:
		jsondata = json.loads(pidtext)
	except (ValueError,UnboundLocalError):
		embed=discord.Embed(title="Snipes - Stock Checker", color=3743743)
		embed.add_field(name="Error", value="Please try again", inline=True)
		embed.set_footer(text="ACOM | @ACOMonitor", icon_url="https://cdn.discordapp.com/icons/449269002317987860/21178bb74135a510f015a21a6afe24c1.png")
		await context.send(embed=embed)
		await session.close()
	product = jsondata["product"]
	productName = product["productName"]
	values = product["variationAttributes"][0]["values"]
	releasedate = product["custom"]["releaseDateUTC"]
	if releasedate == "":
		releasedate = "Live"
	sku = product["facts"][1]["value"]
	variantId = []
	size = []
	for i in range(len(values)):
		variantId.append(values[i]["variantId"])
		size.append(values[i]["displayValue"])
	discpids = "\n".join(variantId)
	getvariantIdlist = len(variantId)
	sizelinks = ['https://www.snipes.fr/p/acom-'+x+'.html' for x in variantId]
	sizelinks_final = [f"> [{i}]({e})" for i, e in zip(size, sizelinks)]
	discsize = "\n".join(sizelinks_final)

	for i in range(len(variantId)):
		session = aiohttp.ClientSession()
		proxy2 = getRandomProxy()
		proxy3 = proxy2['http'] 
		proxy4 = proxy3.replace('7000/', '7000')
		url = "https://www.snipes.com/p/" + urlshoename + str(variantId[i]) + ".html?chosen=size&dwvar_" + pid + "_212=" + str(variantId[i]) + "&format=ajax"
		link = "https://www.snipes.com/p/"+str(variantId[i])+".html"
		pidimage = pid[7:]
		image = "https://images.weserv.nl/?url=https://www.snipes.com/on/demandware.static/-/Sites-snse-master-eu/default/dw24f55347/"+pidimage+"_P.png"
		exception = True
		session = aiohttp.ClientSession()
		response = await session.get(url, headers=headers, proxy=proxy4)
		text = await response.text()
		await session.close()
		print(Fore.MAGENTA + f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] " + log + Fore.YELLOW + f"[Checking stock for size - {str(variantId[i])}]")
		if 'https://collector-pxszbf5p84.perimeterx.net' in text:
			proxy = getRandomProxy()
			proxy2 = getRandomProxy()
			proxy3 = proxy2['http'] 
			proxy4 = proxy3.replace('7000/', '7000')
			session = aiohttp.ClientSession()
			response = await session.get(url, headers=headers, proxy=proxy4)
			text = await response.text()
			await session.close()
		elif 'The owner of this website (www.snipes.com) has banned you temporarily from accessing this website.' in text:
			proxy = getRandomProxy()
			proxy2 = getRandomProxy()
			proxy3 = proxy2['http'] 
			proxy4 = proxy3.replace('7000/', '7000')
			session = aiohttp.ClientSession()
			response = await session.get(url, headers=headers, proxy=proxy4)
			text = await response.text()
			await session.close()
		elif response.status == 403:
			proxy = getRandomProxy()
			proxy2 = getRandomProxy()
			proxy3 = proxy2['http'] 
			proxy4 = proxy3.replace('7000/', '7000')
			session = aiohttp.ClientSession()
			response = await session.get(url, headers=headers, proxy=proxy4)
			text = await response.text()
			await session.close()
		else:
			session = aiohttp.ClientSession()
			info = json.loads(text)
			availability = info["product"]
			pidid = availability["id"]
			productname = availability["productName"]
			print(Fore.MAGENTA + f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] " + log + Fore.GREEN + f"[Succesfully got stock of - {str(variantId[i])}]")
			stocknr = availability["lineItemAvailability"]
			custom = availability["custom"]
			embedsize.append(custom["size"])
			embedstock.append(stocknr["available"])
			sizelinks.append("https://www.snipes.fr/p/acom-"+availability["id"])
			pidlist.append(availability["id"])
			newlist1 = list(embedsize)
			newlist2 = list(embedstock)
			newlist10 = list(embedstock)
			newlist3 = list(pidlist)
			newlist4 = list(sizelinks)

			test = list(zip(newlist1, newlist2, newlist3))
			allsize = []
			allsize2 = []
			allsize3 = []
			allsize10 = []

			sortedtest = sorted(test)

			for n in range(len(sortedtest)):
				allsize2.append(sortedtest[n][1])

			for n in range(len(sortedtest)):
				allsize10.append(sortedtest[n][2])

			discstock = "\n".join(map(str, allsize2))
			totalstock = sum(newlist10)
			await session.close()
	embed=discord.Embed(title="Snipes - "+productname, description='> Snipes sizes early links, use them on drop / restock.\n> SKU: '+str(sku), url=producturl,color=3743743)
	embed.add_field(name=":link: Sizes", value=discsize, inline=True)
	embed.add_field(name=":bar_chart: Stock", value=discstock, inline=True)
	embed.add_field(name=":pushpin: SKUs", value=discpids, inline=True)
	embed.add_field(name="Total Stock", value="`"+str(totalstock)+"`", inline=True)
	embed.add_field(name="Release Date", value="`"+str(releasedate)+"`", inline=True)
	embed.set_thumbnail(url=image)
	embed.set_footer(text="ACOM | @ACOMonitor", icon_url="https://cdn.discordapp.com/icons/449269002317987860/21178bb74135a510f015a21a6afe24c1.png")
	await context.send(embed=embed)
	await message.delete()
	await session.close()
	await context.message.delete()
	print(Fore.MAGENTA + f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] " + log + Fore.GREEN + "[Webhook sent!]")
	print('')

@bot.command()
@commands.check(check_if_it_is_me)
async def solebox(context, pid):
	now = datetime.now()

	server_name = context.guild.name

	user_name_id = context.author.name + ' ID : ' + str(context.author.id)

	log2 = Fore.CYAN +f'[{server_name}]'
	log3 = Fore.CYAN + f'[{user_name_id}] '

	log = log2 + ' ' + log3

	print(Fore.MAGENTA + f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] " + log + Fore.YELLOW + f"[Getting stock of - {pid}]")
	headers = {
    'authority': "www.solebox.com",
    'pragma': 'no-cache',
    'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36",
    'accept': "application/json, text/javascript, */*; q=0.01",
    'content-type': 'application/json',
    'sec-fetch-site': "same-origin",
    'sec-fetch-mode': "cors",
    'sec-fetch-dest': "empty",
    'referer': "https://www.solebox.com/de_DE/p/"+pid+".html",
    'accept-language': "de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7",
    }

	embedstock = []
	embedsize = []
	sizelinks = []
	sku = ""
	releasedate = ""
	pidlist = []
	lastcharpid = ["00000001","00000002","00000004","00000005","00000006","00000007","00000008","00000009","00000010","00000011","00000012","00000013","00000014","00000015","00000016","00000017","00000020"]

	embed3=discord.Embed(title="Solebox Stock Checker", description='Checking backend...', color=3743743)
	embed3.set_footer(text='ACOM Solebox Stock Checker', icon_url="https://cdn.discordapp.com/icons/449269002317987860/21178bb74135a510f015a21a6afe24c1.png")
	message = await context.send(embed=embed3)

	newpid = pid + "00000001"

	session = aiohttp.ClientSession()


	url = "https://www.snipes.com/p/"+str(newpid)+".html"

	pidimage = pid[1:]
	image = "https://www.solebox.com/on/demandware.static/-/Sites-solebox-master-de/default/dw4d286efa/"+pidimage+"_PS.png"
	link2 = "https://www.solebox.com/p/"+str(pid)+".html"


	for i in range(len(lastcharpid)):
		proxy2 = getRandomProxy()
		proxy3 = proxy2['http'] 
		proxy4 = proxy3.replace('7000/', '7000')
		newpid = pid + lastcharpid[i]
		url = "https://www.solebox.com/p/"+str(newpid)+".html?chosen=size&dwvar_calix_212="+str(newpid)+"&format=ajax"
		link = "https://www.solebox.com/p/"+str(newpid)+".html"
		exception = True
		while (exception):
			exception = False
			try:
				response = await session.get(url, headers=headers, proxy=proxy4)
				text = await response.text()
			except Exception as e:
				print(Fore.MAGENTA + f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] " + log + Fore.RED + "[Proxy error - Retrying!]")
				proxy = getRandomProxy()
				exception = True
		print(Fore.MAGENTA + f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] " + log + Fore.YELLOW + f"[Checking stock for size - {newpid}]")
		if '//client.perimeterx.net/PXuR63h57Z/main.min.js' in text:
			exception = True
			while (exception):
				exception = False
				try:
					response = await session.get(url, headers=headers, proxy=proxy4)
					text = await response.text()
				except Exception as e:
					print(Fore.MAGENTA + f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] " + log + Fore.RED + "[Proxy error - Retrying!]")
					proxy = getRandomProxy()
					exception = True
		
		elif response.status == 410 or response.status == 404:
			continue

		elif response.status == 403:
			proxy = getRandomProxy()
			url = "https://www.solebox.com/p/"+str(newpid)+".html?chosen=size&dwvar_calix_212="+str(newpid)+"&format=ajax"
			exception = True
			while (exception):
				exception = False
				try:
					response = await session.get(url, headers=headers, proxy=proxy4)
					text = await response.text()
				except Exception:
					print(Fore.MAGENTA + f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] " + log + Fore.RED + "[Proxy error - Retrying!]")
					proxy = getRandomProxy()
					print("rate")
					exception = True

		else:
			info = json.loads(text)
			availability = info["product"]
			pidid = availability["id"]
			productname = availability["productName"]
			print(Fore.MAGENTA + f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] " + log + Fore.GREEN + f"[Succesfully got stock of - {newpid}]")
			if len(pidid) > 15:
				stocknr = availability["lineItemAvailability"]
				custom = availability["custom"]
				embedsize.append(custom["size"])
				embedstock.append(stocknr["available"])
				sizelinks.append("https://www.solebox.com/en_DE/p/acom-"+availability["id"])
				pidlist.append(availability["id"])
				newlist1 = list(embedsize)
				newlist2 = list(embedstock)
				newlist10 = list(embedstock)
				newlist3 = list(pidlist)
				newlist4 = list(sizelinks)

				test = list(zip(newlist1, newlist2, newlist3))
				allsize = []
				allsize2 = []
				allsize3 = []
				allsize10 = []

				sortedtest = sorted(test)
				for i in range(len(sortedtest)):
					allsize.append(sortedtest[i][0])

				for n in range(len(sortedtest)):
					allsize2.append(sortedtest[n][1])

				for n in range(len(sortedtest)):
					allsize3.append(sortedtest[n][2])
					allsize10.append(sortedtest[n][2])


				allsize5 = ['https://www.solebox.com/en_DE/p/acom-'+x for x in allsize10]
				sizelinks_final = [f"> [{i}]({e})" for i, e in zip(allsize, allsize5)]
				discsize = "\n".join(sizelinks_final)
				discstock = "\n".join(map(str, allsize2))
				discpids = "\n".join(map(str, allsize3))
				totalstock = sum(newlist10)
			getsku = availability["facts"]
			custom = availability["custom"]
			for url in getsku:
				if url["ID"] == "manufacturerSKU":
					sku = url["value"]
				if url["ID"] == "releaseDate":
					releasedate = custom["releaseDateUTC"]
				else:
					releasedate = "Live"

	embed=discord.Embed(title="Solebox - "+productname, description='> Solebox sizes early links, use them on drop / restock.\n\n> '+str(sku), color=3743743)
	embed.add_field(name=":link: Sizes & Links", value=discsize, inline=True)
	embed.add_field(name=":bar_chart: Stock", value=discstock, inline=True)
	embed.add_field(name=":pushpin: SKUs", value=discpids, inline=True)
	embed.add_field(name="Total Stock", value="`"+str(totalstock)+"`", inline=True)
	embed.add_field(name="Release Date", value="`"+str(releasedate)+"`", inline=True)

	embed.set_thumbnail(url=image)
	embed.set_footer(text="ACOM | @ACOMonitor", icon_url="https://cdn.discordapp.com/icons/449269002317987860/21178bb74135a510f015a21a6afe24c1.png")
	await context.send(embed=embed)
	await message.delete()
	await session.close()
	await context.message.delete()
	print(Fore.MAGENTA + f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] " + log + Fore.GREEN + "[Webhook sent!]")
	print('')


@bot.command()
@commands.check(check_if_it_is_me)
async def onygo(context, pid):
	
	now = datetime.now()

	server_name = context.guild.name

	user_name_id = context.author.name + ' ID : ' + str(context.author.id)

	log2 = Fore.CYAN +f'[{server_name}]'
	log3 = Fore.CYAN + f'[{user_name_id}] '

	log = log2 + ' ' + log3

	print(Fore.MAGENTA + f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] " + log + Fore.YELLOW + f"[Getting stock of - {pid}]")


	headers = {
    'authority': "www.onygo.com",
    'cache-control': "max-age=0",
    'upgrade-insecure-requests': "1",
    'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.3",
    'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    'sec-fetch-site': "none",
    'sec-fetch-mode': "navigate",
    'sec-fetch-user': "?1",
    'sec-fetch-dest': "document",
    'accept-language': "en-US,en;q=0.9",
    }

	embedstock = []
	embedsize = []
	sizelinks = []
	sku = ""
	releasedate = ""
	pidlist = []
	lastcharpid = ["00000001","00000002","00000004","00000005","00000006","00000007","00000008","00000009","00000010","00000011","00000012","00000013","00000014"]

	count = ''

	embed3=discord.Embed(title="Onygo Stock Checker", description='Checking backend...', color=3743743)
	embed3.set_footer(text='ACOM Onygo Stock Checker', icon_url="https://cdn.discordapp.com/icons/449269002317987860/21178bb74135a510f015a21a6afe24c1.png")
	message = await context.send(embed=embed3)

	newpid = pid + "00000001"

	url = "https://www.onygo.com/p/"+str(newpid)+".html"

	proxy = getRandomProxy()


	for i in range(len(lastcharpid)):
		proxy2 = getRandomProxy()
		proxy3 = proxy2['http'] 
		proxy4 = proxy3.replace('7000/', '7000')
		session = aiohttp.ClientSession()
		newpid = pid + lastcharpid[i]
		url = "https://www.onygo.com/p/"+str(newpid)+".html?chosen=size&dwvar_calix_212="+str(newpid)+"&format=ajax"
		link = "https://www.onygo.com/p/"+str(newpid)+".html"
		pidimage = pid[7:]
		image = "https://images.weserv.nl/?url=https://www.onygo.com/on/demandware.static/-/Sites-ong-master-de/default/dw6812d605/"+pidimage+"_P.png"
		exception = True
		while (exception):
			exception = False
			try:
				response = await session.get(url, headers=headers, proxy=proxy4)
				text = await response.text()
			except Exception as e:
				print(Fore.MAGENTA + f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] " + log + Fore.RED + "[Proxy error - Retrying!]")
				proxy = getRandomProxy()
				session = aiohttp.ClientSession()
				exception = True
		print(Fore.MAGENTA + f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] " + log + Fore.YELLOW + f"[Checking stock for size - {newpid}]")
		if 'https://collector-pxj1n025xg.perimeterx.net' in text:
			await session.close()
			proxy2 = getRandomProxy()
			proxy3 = proxy2['http'] 
			proxy4 = proxy3.replace('7000/', '7000')
			session = aiohttp.ClientSession()
			url = "https://www.onygo.com/p/"+str(newpid)+".html?chosen=size&dwvar_calix_212="+str(newpid)+"&format=ajax"
			print(Fore.MAGENTA + f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] " + log + Fore.RED + "[PX (Collector) - Proxy error - Retrying!]")
			print(url)
			exception = True
			while (exception):
				exception = False
				try:
					response = await session.get(url, headers=headers, proxy=proxy4)
					text = await response.text()
					print(url)
				except Exception as e:
					print(Fore.MAGENTA + f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] " + log + Fore.RED + "[Proxy error - Retrying!]")
					await session.close()
					proxy2 = getRandomProxy()
					proxy3 = proxy2['http'] 
					proxy4 = proxy3.replace('7000/', '7000')
					session = aiohttp.ClientSession()
					exception = True
		elif 'The owner of this website (www.onygo.com) has banned you temporarily from accessing this website.' in text:
			await session.close()
			proxy2 = getRandomProxy()
			proxy3 = proxy2['http'] 
			proxy4 = proxy3.replace('7000/', '7000')
			session = aiohttp.ClientSession()
			url = "https://www.onygo.com/p/"+str(newpid)+".html?chosen=size&dwvar_calix_212="+str(newpid)+"&format=ajax"
			print(Fore.MAGENTA + f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] " + log + Fore.RED + "[PX (Owner) - Proxy error - Retrying!]")
			exception = True
			while (exception):
				exception = False
				try:
					response = await session.get(url, headers=headers, proxy=proxy4)
					text = await response.text()
				except Exception as e:
					print(Fore.MAGENTA + f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] " + log + Fore.RED + "[Proxy error - Retrying!]")
					await session.close()
					proxy = getRandomProxy()
					session = aiohttp.ClientSession()
					exception = True

		elif response.status == 410 or response.status == 404:
			print(Fore.MAGENTA + f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] " + log + Fore.YELLOW + "[404 or 410 Page - Continue!]")
			await session.close()
			continue

		elif response.status == 403:
			await session.close()
			proxy2 = getRandomProxy()
			proxy3 = proxy2['http'] 
			proxy4 = proxy3.replace('7000/', '7000')
			session = aiohttp.ClientSession()
			print(Fore.MAGENTA + f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] " + log + Fore.RED + "[403 Forbidden - Proxy error - Retrying!]")
			url = "https://www.onygo.com/p/"+str(newpid)+".html?chosen=size&dwvar_calix_212="+str(newpid)+"&format=ajax"
			exception = True
			while (exception):
				exception = False
				try:
					response = await session.get(url, headers=headers, proxy=proxy4)
					text = await response.text()
				except Exception:
					print(Fore.MAGENTA + f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] " + log + Fore.RED + "[Proxy error - Retrying!]")
					await session.close()
					proxy2 = getRandomProxy()
					proxy3 = proxy2['http'] 
					proxy4 = proxy3.replace('7000/', '7000')
					session = aiohttp.ClientSession()
					exception = True


		else:
			info = json.loads(text)
			availability = info["product"]
			pidid = availability["id"]
			productname = availability["productName"]
			print(Fore.MAGENTA + f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] " + log + Fore.GREEN + f"[Succesfully got stock of - {newpid}]")
			await session.close()
			if len(pidid) > 15:
				stocknr = availability["lineItemAvailability"]
				custom = availability["custom"]
				embedsize.append(custom["size"])
				embedstock.append(stocknr["available"])
				sizelinks.append("https://www.onygo.com/en_DE/p/acom-"+availability["id"])
				pidlist.append(availability["id"])
				newlist1 = list(embedsize)
				newlist2 = list(embedstock)
				newlist10 = list(embedstock)
				newlist3 = list(pidlist)
				newlist4 = list(sizelinks)

				test = list(zip(newlist1, newlist2, newlist3))
				allsize = []
				allsize2 = []
				allsize3 = []
				allsize10 = []

				sortedtest = sorted(test)
				for i in range(len(sortedtest)):
					allsize.append(sortedtest[i][0])

				for n in range(len(sortedtest)):
					allsize2.append(sortedtest[n][1])

				for n in range(len(sortedtest)):
					allsize3.append(sortedtest[n][2])
					allsize10.append(sortedtest[n][2])


				allsize5 = ['https://www.onygo.com/en_DE/p/acom-'+x for x in allsize10]
				sizelinks_final = [f"> [{i}]({e})" for i, e in zip(allsize, allsize5)]
				discsize = "\n".join(sizelinks_final)
				discstock = "\n".join(map(str, allsize2))
				discpids = "\n".join(map(str, allsize3))
				totalstock = sum(newlist10)
			getsku = availability["facts"]
			custom = availability["custom"]
			for url in getsku:
				if url["ID"] == "manufacturerSKU":
					sku = url["value"]
				if url["ID"] == "releaseDate":
					releasedate = custom["releaseDateUTC"]
				else:
					releasedate = "Live"
	embed=discord.Embed(title="Onygo - "+productname, description='> Onygo sizes early links, use them on drop / restock.\n\n> '+str(sku), color=3743743)
	embed.add_field(name=":link: Sizes & Links", value=discsize, inline=True)
	embed.add_field(name=":bar_chart: Stock", value=discstock, inline=True)
	embed.add_field(name=":pushpin: SKUs", value=discpids, inline=True)
	embed.add_field(name="Total Stock", value="`"+str(totalstock)+"`", inline=True)
	embed.add_field(name="Release Date", value="`"+str(releasedate)+"`", inline=True)

	embed.set_thumbnail(url=image)
	embed.set_footer(text="ACOM | @ACOMonitor", icon_url="https://cdn.discordapp.com/icons/449269002317987860/21178bb74135a510f015a21a6afe24c1.png")
	await context.send(embed=embed)
	await message.delete()
	await session.close()
	await context.message.delete()
	print(Fore.MAGENTA + f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] " + log + Fore.GREEN + "[Webhook sent!]")
	print('')


bot.run(bottoken)