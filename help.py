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

# @bot.event
# async def on_command_error(ctx, error):
#     if isinstance(error, CommandNotFound):
#         return
#     raise error

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

def split_list(a_list):
    half = len(a_list)//2
    return a_list[:half], a_list[half:]

@bot.command()
@commands.check(check_if_it_is_me)
async def snipesadd(context, info):
	data = {}
	data["Snipes"] = []
	y = data["Snipes"]
	lines = context.message.content.splitlines()
	lines.pop(0)
	price = lines[0]
	productName = lines[1]
	image = lines[2]
	sku = lines[3]
	lines.pop(0)
	lines.pop(0)
	lines.pop(0)
	lines.pop(0)

	variantId,size = split_list(lines)

	for j in range(len(variantId)):
		name = str(variantId[j])
		y.append({
			name:[{
				"SKU": sku,
				"Size": size[j],
				"price": price,
				"name": productName,
				"image": image
			}]
		})

	def write_json(data, filename='demo.json'): 
		with open(filename,'w') as f: 
			json.dump(data, f, indent=2)

	with open('demo.json') as json_file: 
		data = json.load(json_file)
		temp = data["Snipes"]
		temp.append(y) 

	sizelist = "\n".join(size)
	variantIdlist = "\n".join(variantId)
	write_json(data) 
	json_file.close()

	embed=discord.Embed(title="Added to Snipes - "+productName, description="> SKU: "+sku+"\n> Price: "+price, color=setembedcolor)
	embed.add_field(name=":straight_ruler: Size", value=sizelist, inline=True)
	embed.add_field(name=":pushpin: SKUs", value=variantIdlist, inline=True)
	embed.set_thumbnail(url=image)
	embed.set_footer(text=setfootertext + ' Snipes Scraper', icon_url=setfooterimage)
	await context.send(embed=embed)

@bot.command()
@commands.check(check_if_it_is_me)
async def snipesdelete(context, info):
	data = {}
	data["Snipes"] = []
	y = data["Snipes"]
	lines = context.message.content.splitlines()
	lines.pop(0)



	with open('demo.json', 'r') as data_file:
		data = json.load(data_file)

		for i in range(len(data["Snipes"])):			
			for R in range(len(data["Snipes"][i])):
				try:
					for w in range(len(lines)):
						if lines[w] in data["Snipes"][i][R]:
							data["Snipes"][i][R].pop(lines[w])
							print("deleted")
							break;
				except (TypeError,KeyError,IndexError) as e:
					continue

	with open('demo.json', 'w') as data_file:
	    data = json.dump(data, data_file, indent=2)

	variantIdlist = "\n".join(lines)

	embed=discord.Embed(title="Succesfully deleted from Snipes", color=setembedcolor)
	embed.add_field(name=":pushpin: SKUs", value=variantIdlist, inline=True)
	embed.set_footer(text=setfootertext + ' Snipes Scraper', icon_url=setfooterimage)
	await context.send(embed=embed)

@bot.command()
@commands.check(check_if_it_is_me)
async def checksnipes(context, info):
	data = {}
	data["Snipes"] = []
	y = data["Snipes"]
	lines = context.message.content.splitlines()
	lines.pop(0)
	foundpids = []


	with open('demo.json', 'r') as data_file:
		data = json.load(data_file)

		for i in range(len(data["Snipes"])):			
			for R in range(len(data["Snipes"][i])):
				try:
					for w in range(len(lines)):
						if lines[w] in data["Snipes"][i][R]:
							foundpids.append(str(data["Snipes"][i][R].keys()))

				except (TypeError,KeyError,IndexError) as e:
					continue

	with open('demo.json', 'w') as data_file:
	    data = json.dump(data, data_file, indent=2)

	if not foundpids:
		embed=discord.Embed(title="Snipes - No Product found", color=setembedcolor)
		embed.set_footer(text=setfootertext + ' Snipes Scraper', icon_url=setfooterimage)
		await context.send(embed=embed)
	else:
		variantIdlist = "\n".join(foundpids)
		embed=discord.Embed(title="Found Pids in Snipes.json", color=setembedcolor)
		embed.add_field(name=":pushpin: SKUs", value=variantIdlist, inline=True)
		embed.set_footer(text=setfootertext + ' Snipes Scraper', icon_url=setfooterimage)
		await context.send(embed=embed)



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
	embed.add_field(name="Information", value="""*Change "snipes" with solebox or onygo to use the other commands for selected store*""" , inline=False)
	embed.set_footer(text=setfootertext + ' Snipes Scraper', icon_url=setfooterimage)
	await context.send(embed=embed)

@bot.command()
async def help(context):
	embed=discord.Embed(title="All commands", color=setembedcolor)
	embed.add_field(name="Mesh Tracker  <:hawkoos:807792754260181023> <:mbotoos:807792807326253077>", value="?orderhelp\n?order <store> <postcode>\n<ordernr>\n\n?orderbulk <store> <postcode>\n<ordernr>\n<ordernr>", inline=False)
	embed.add_field(name="Mesh QT / Scraper  <:hawkoos:807792754260181023> <:mbotoos:807792807326253077>", value="?meshhelp\n?mesh <full link here>\n?mesh <meshpid>\n?qt <store> <PIDs/SKUs>\n?meshcountries", inline=False)
	embed.add_field(name="UPS Tracker  <:UPS:808299085496713257>", value="?upshelp\n?orderstore\n?ups\n<Tracking NR. 1>\n<Tracking NR. 2>\n<Tracking NR. 3>\n\n?upsbulk\n<Tracking NR. 1>\n<Tracking NR. 2>\n<Tracking NR. 3>", inline=False)
	embed.add_field(name="Footlocker / Side-Step Stock Checker  <:ftl:809892922387595314> <:sidestep:809894025636216902>", value="?ftlhelp\n?stock <link>\n?side <link>\n?ftlcountries\n", inline=False)
	embed.add_field(name="Zalando Stock / PID Scraper  <:zalando:809893400718737508>", value="?zalandohelp\n?zalando <full link here>\n?zalandopid <full link here>", inline=False)
	embed.add_field(name="Restocks Price Checker  <:restocks:809892862400921640>", value="?restocks <shoename>", inline=False)
	embed.add_field(name="StockX Price Checker  <:stockx:810352884608532531>", value="?stockx <shoename>", inline=False)
	embed.add_field(name="Nike Early Link <:nike:809892892654305300>", value="?nikehelp\nSupported Countries: CH, CA, AU, RU, SG\n?nike <full link here>", inline=False)
	embed.set_thumbnail(url=setfooterimage)
	embed.set_footer(text=setfootertext + ' All Commands', icon_url=setfooterimage)
	await context.send(embed=embed)


@bot.command()
async def snipes(context, pid):
	asd = 0
	nopidfound = 0
	data = {}
	data["Snipes"] = []
	y = data["Snipes"]
	testpid = ["00000001","00000002","00000003","00000004","00000005","00000006","00000007","00000008","00000009","00000010","00000011","00000012","00000013","00000014","00000015","00000016","00000017","00000018","00000019","00000020","00000021","00000022","00000023","00000024","00000025","00000026","00000027","00000028","00000029","00000030","00000031"]
	correcttestpid = []
	for i in range(len(testpid)):
		correcttestpid.append(pid + testpid[i])
	data = {}
	data["Snipes"] = []

	with open('demo.json') as json_file:
		data = json.load(json_file)
		for i in range(len(data["Snipes"])):			
			for R in range(len(data["Snipes"][i])):
				try:
					for w in range(len(correcttestpid)):
						if correcttestpid[w] in data["Snipes"][i][R]:
							nopidfound = 1
							break;
				except (TypeError,KeyError,IndexError) as e:
					continue
 
	if nopidfound == 1:
		print("found pid")
		embedpid = []
		embedsize = []
		
		with open('demo.json') as json_file: 
			data = json.load(json_file)
			for i in range(len(data["Snipes"])):			
				for R in range(len(data["Snipes"][i])):
					try:
						for w in range(len(correcttestpid)):
							if correcttestpid[w] in data["Snipes"][i][R]:
								key, value = list(data["Snipes"][i][R].items())[0]
								embedpid.append(key)
								embedsize.append(value[0]["Size"])
								price = value[0]["price"]
								sku = value[0]["SKU"]
								productName = value[0]["name"]
								image = value[0]["image"]
					except (TypeError,KeyError,IndexError) as e:
						continue
		sizelist = "\n".join(embedsize)
		variantIdlist = "\n".join(embedpid)

		embed=discord.Embed(title="Snipes - "+productName, description="> SKU: "+sku+"\n> Price: "+price, color=setembedcolor)
		embed.add_field(name=":straight_ruler: Size", value=sizelist, inline=True)
		embed.add_field(name=":pushpin: SKUs", value=variantIdlist, inline=True)
		embed.set_thumbnail(url=image)
		embed.set_footer(text=setfootertext + ' Snipes Scraper', icon_url=setfooterimage)
		await context.send(embed=embed)
		json_file.close()

	elif nopidfound == 0:
		session = aiohttp.ClientSession()
		print("did not found any pid")

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
		producturl = "https://www.snipes.com/p/" + urlshoename + pid + ".html?dwvar_"+pid+"_212&format=ajax"
		bb = pid.isdigit()
		if bb == False:
			pid3 = pid.split('000')[1].split('.html')[0]
			url1 = pid.split('000')[0]
			pid2 = pid3.replace(pid3, '000'+pid3+'00000004')
			url2 = pid+'?dwvar_'+pid2+'_212&format=ajax'
			url3 = url1+pid2+'.html'+'?dwvar_'+pid2+'_212&format=ajax'
			producturl = url3
			pid = pid2
		elif bb == True:
			pid = pid
			producturl = producturl
			print(producturl)
		else:
			embed=discord.Embed(title="Snipes - PID Scraper", color=setembedcolor)
			embed.add_field(name="Error", value="Make sure your PID / Link is correct.", inline=True)
			embed.set_footer(text=setfootertext + ' Snipes Scraper', icon_url=setfooterimage)
			await context.send(embed=embed)
		session = aiohttp.ClientSession()
		response = await session.get(producturl, headers=headers, proxy=proxy4)
		text = await response.text()
		if 'https://collector-pxszbf5p84.perimeterx.net' in text:
			while asd > 5:
				await session.close()
				proxy = getRandomProxy()
				proxy2 = getRandomProxy()
				proxy3 = proxy2['http'] 
				proxy4 = proxy3.replace('7000/', '7000')
				session = aiohttp.ClientSession()
				response = await session.get(producturl, headers=headers, proxy=proxy4)
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
			try:
				price1 = product["price"]
				price2 = price1["sales"]
				price = price2["formatted"]
			except:
				price = 'N/A'
			try:
				image1 = product["images"]
				image2 = image1[0]
				image3 = image2["pdp"]
				image = image3["srcM"]
				image = image.replace("jpg?sw=450&sh=450&sm=fit&sfrm=png", "png")
			except:
				image = ''
			try:
				sku = product["facts"][1]["value"]
			except:
				sku = 'N/A'
			values = product["variationAttributes"][0]["values"]
			releasedate = product["custom"]["releaseDateUTC"]
			if releasedate == "":
				releasedate = "Live"
			variantId = []
			size = []
			for i in range(len(values)):
				variantId.append(values[i]["variantId"])
				size.append(values[i]["displayValue"])
			variantId2 = ['N/A' if x==None else x for x in variantId]
			allsize = ['> '+x for x in size]
			variantIdlist = "\n".join(variantId2)
			sizelist = "\n".join(allsize)
			pidimage = pid[7:]
			embedproductlink = "[" + sku + "](" + producturl + ")"

			for j in range(len(variantId)):
				name = str(variantId[j])
				y.append({
					name:[{
						"SKU": sku,
						"Size": size[j],
						"date": releasedate,
						"price": price,
						"name": productName,
						"image": image
					}]
				})

			def write_json(data, filename='demo.json'): 
				with open(filename,'w') as f: 
					json.dump(data, f, indent=2)

			with open('demo.json') as json_file: 
				data = json.load(json_file)
				temp = data["Snipes"]
				temp.append(y) 

			write_json(data) 
			json_file.close()

			embed=discord.Embed(title="Snipes - "+productName, description="> SKU: "+sku+"\n> Price: "+price, color=setembedcolor)
			embed.add_field(name=":straight_ruler: Size", value=sizelist, inline=True)
			embed.add_field(name=":pushpin: SKUs", value=variantIdlist, inline=True)
			embed.add_field(name="Release Date", value="`"+str(releasedate)+"`", inline=False)
			embed.set_thumbnail(url=image)
			embed.set_footer(text=setfootertext + ' Snipes Scraper', icon_url=setfooterimage)
			await context.send(embed=embed)
			await session.close()
		except (ValueError,UnboundLocalError,TypeError) as e:
			print("An Error occured", e, producturl)
			embed=discord.Embed(title="Snipes - PID Scraper", color=setembedcolor)
			embed.add_field(name="Error", value="An error occured, try later", inline=True)
			embed.set_footer(text=setfootertext + ' Snipes Scraper', icon_url=setfooterimage)
			await context.send(embed=embed)
			await session.close()

@bot.command()
@commands.check(check_if_it_is_me)
async def solebox(context, pid):
	session = aiohttp.ClientSession()
	asd = 0
	headers = {
	    'authority': "www.solebox.com",
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


	url = "https://www.solebox.com/en_DE/p/medicom-bearbrick_series_40_-_100%25-multi-"+pid+".html?variantId&dwvar_"+pid+"_212&format=ajax"
	proxy = getRandomProxy()
	proxy2 = getRandomProxy()
	proxy3 = proxy2['http'] 
	proxy4 = proxy3.replace('7000/', '7000')
	firstresponse = await session.get(url, headers=headers2, proxy=proxy4)
	await session.close()
	newlink = str(firstresponse.url)
	urlshoename = newlink.split("https://www.solebox.com/en_DE/p/")[1].split(pid)[0]
	newurl2 = "https://www.solebox.com/en_DE/p/" + urlshoename + pid + ".html?dwvar_"+pid+"_212"+"&format=ajax"
	producturl = "https://www.solebox.com/en_DE/p/" + urlshoename + pid + ".html?dwvar_"+pid+"_212&format=ajax"
	bb = pid.isdigit()
	if bb == False:
		pid2 = pid.split(".")[-2].split("-")[3]
		url2 = pid+'?dwvar_'+pid2+'_212&format=ajax'
		producturl = url2
		pid = pid2
	elif bb == True:
		pid = pid
		producturl = producturl
	else:
		embed=discord.Embed(title="Solebox - PID Scraper", color=setembedcolor)
		embed.add_field(name="Error", value="Make sure your PID / Link is correct.", inline=True)
		embed.set_footer(text=setfootertext + ' Solebox Scraper', icon_url=setfooterimage)
		await context.send(embed=embed)
	session = aiohttp.ClientSession()
	response = await session.get(producturl, headers=headers, proxy=proxy4)
	text = await response.text()
	if '//client.perimeterx.net/PXuR63h57Z/main.min.js' in text:
		while asd > 5:
			await session.close()
			proxy = getRandomProxy()
			proxy2 = getRandomProxy()
			proxy3 = proxy2['http'] 
			proxy4 = proxy3.replace('7000/', '7000')
			session = aiohttp.ClientSession()
			response = await session.get(producturl, headers=headers, proxy=proxy4)
			text = await response.text()
			asd = asd + 1
			print("PX banned - Retry Nr. " + str(asd))
			if '//client.perimeterx.net/PXuR63h57Z/main.min.js' in text:
				continue
			else:
				break

	try:
		jsondata = json.loads(text)
		product = jsondata["product"]
		productName = product["productName"]
		try:
			price1 = product["price"]
			price2 = price1["sales"]
			price = price2["formatted"]
		except:
			price = 'N/A'
		try:
			image1 = product["images"]
			image2 = image1[0]
			image3 = image2["pdp"]
			image = image3["srcM"]
			image = image.replace("jpg?sw=450&sh=450&sm=fit&sfrm=png", "png")
		except:
			image = ''
		try:
			sku = product["facts"][1]["value"]
		except:
			sku = 'N/A'
		values = product["variationAttributes"][0]["values"]
		releasedate = product["custom"]["releaseDateUTC"]
		if releasedate == "":
			releasedate = "Live"
		variantId = []
		size = []
		for i in range(len(values)):
			variantId.append(values[i]["variantId"])
			size.append(values[i]["displayValue"])
		variantId2 = ['N/A' if x==None else x for x in variantId]
		allsize = ['> '+x for x in size]
		variantIdlist = "\n".join(variantId2)
		sizelist = "\n".join(allsize)
		pidimage = pid[1:]
		embedproductlink = "[" + sku + "](" + producturl + ")"
		image = "https://www.solebox.com/on/demandware.static/-/Sites-solebox-master-de/default/dw4d286efa/"+pidimage+"_PS.png"
		embed=discord.Embed(title="Solebox - "+productName, description="> SKU: "+sku+"\n> Price: "+price, color=setembedcolor)
		embed.add_field(name=":straight_ruler: Size", value=sizelist, inline=True)
		embed.add_field(name=":pushpin: SKUs", value=variantIdlist, inline=True)
		embed.add_field(name="Release Date", value="`"+str(releasedate)+"`", inline=False)
		embed.set_thumbnail(url=image)
		embed.set_footer(text=setfootertext + ' Solebox Scraper', icon_url=setfooterimage)
		await context.send(embed=embed)
		await session.close()
	except (ValueError,UnboundLocalError,TypeError) as e:
		print("An Error occured", e, producturl)
		embed=discord.Embed(title="Solebox - PID Scraper", color=setembedcolor)
		embed.add_field(name="Error", value="An error occured, try later", inline=True)
		embed.set_footer(text=setfootertext + ' Solebox Scraper', icon_url=setfooterimage)
		await context.send(embed=embed)
		await session.close()


@bot.command()
@commands.check(check_if_it_is_me)
async def onygo(context, pid):
	
	session = aiohttp.ClientSession()
	asd = 0
	headers = {
	    'authority': "www.onygo.com",
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


	url = "https://www.onygo.com/p/nike-air_force_1_shadow-shadow_white%2Fwhite-white-"+pid+".html?variantId&dwvar_"+pid+"_212&format=ajax"
	proxy = getRandomProxy()
	proxy2 = getRandomProxy()
	proxy3 = proxy2['http'] 
	proxy4 = proxy3.replace('7000/', '7000')
	firstresponse = await session.get(url, headers=headers2, proxy=proxy4)
	await session.close()
	newlink = str(firstresponse.url)
	urlshoename = newlink.split("https://www.onygo.com/p/")[1].split(pid)[0]
	newurl2 = "https://www.onygo.com/p/" + urlshoename + pid + ".html?dwvar_"+pid+"_212"+"&format=ajax"
	producturl = "https://www.onygo.com/p/" + urlshoename + pid + ".html?dwvar_"+pid+"_212&format=ajax"
	bb = pid.isdigit()
	if bb == False:
		pid2 = pid.split(".")[-2].split("-")[4]
		url2 = pid+'?dwvar_'+pid2+'_212&format=ajax'
		producturl = url2
		pid = pid2
	elif bb == True:
		pid = pid
		producturl = producturl
	else:
		embed=discord.Embed(title="Onygo - PID Scraper", color=setembedcolor)
		embed.add_field(name="Error", value="Make sure your PID / Link is correct.", inline=True)
		embed.set_footer(text=setfootertext + ' Onygo Scraper', icon_url=setfooterimage)
		await context.send(embed=embed)
	session = aiohttp.ClientSession()
	response = await session.get(producturl, headers=headers, proxy=proxy4)
	text = await response.text()
	if 'https://collector-pxj1n025xg.perimeterx.net' in text:
		while asd > 5:
			await session.close()
			proxy = getRandomProxy()
			proxy2 = getRandomProxy()
			proxy3 = proxy2['http'] 
			proxy4 = proxy3.replace('7000/', '7000')
			session = aiohttp.ClientSession()
			response = await session.get(producturl, headers=headers, proxy=proxy4)
			text = await response.text()
			asd = asd + 1
			print("PX banned - Retry Nr. " + str(asd))
			if 'https://collector-pxj1n025xg.perimeterx.net' in text:
				continue
			else:
				break

	try:
		jsondata = json.loads(text)
		product = jsondata["product"]
		productName = product["productName"]
		try:
			price1 = product["price"]
			price2 = price1["sales"]
			price = price2["formatted"]
		except:
			price = 'N/A'
		try:
			image1 = product["images"]
			image2 = image1[0]
			image3 = image2["pdp"]
			image = image3["srcM"]
			image = image.replace("jpg?sw=450&sh=450&sm=fit&sfrm=png", "png")
		except:
			image = ''
		try:
			sku = product["facts"][1]["value"]
		except:
			sku = 'N/A'
		values = product["variationAttributes"][0]["values"]
		releasedate = product["custom"]["releaseDateUTC"]
		if releasedate == "":
			releasedate = "Live"
		variantId = []
		size = []
		for i in range(len(values)):
			variantId.append(values[i]["variantId"])
			size.append(values[i]["displayValue"])
		variantId2 = ['N/A' if x==None else x for x in variantId]
		allsize = ['> '+x for x in size]
		variantIdlist = "\n".join(variantId2)
		sizelist = "\n".join(allsize)
		pidimage = pid[7:]
		embedproductlink = "[" + sku + "](" + producturl + ")"
		image = "https://images.weserv.nl/?url=https://www.onygo.com/on/demandware.static/-/Sites-ong-master-de/default/dw6812d605/"+pidimage+"_P.png"
		embed=discord.Embed(title="Onygo - "+productName, description="> SKU: "+sku+"\n> Price: "+price, color=setembedcolor)
		embed.add_field(name=":straight_ruler: Size", value=sizelist, inline=True)
		embed.add_field(name=":pushpin: SKUs", value=variantIdlist, inline=True)
		embed.add_field(name="Release Date", value="`"+str(releasedate)+"`", inline=False)
		embed.set_thumbnail(url=image)
		embed.set_footer(text=setfootertext + ' Onygo Scraper', icon_url=setfooterimage)
		await context.send(embed=embed)
		await session.close()
	except (ValueError,UnboundLocalError,TypeError) as e:
		print("An Error occured", e, producturl)
		embed=discord.Embed(title="Onygo - PID Scraper", color=setembedcolor)
		embed.add_field(name="Error", value="An error occured, try later", inline=True)
		embed.set_footer(text=setfootertext + ' Onygo Scraper', icon_url=setfooterimage)
		await context.send(embed=embed)
		await session.close()


bot.run(bottoken)
