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

def split_list(a_list):
    half = len(a_list)//2
    return a_list[:half], a_list[half:]

def check_if_it_is_me(ctx):
	return ctx.message.author.id == 175953718750085121 or ctx.message.author.id == 351639955531104258 or ctx.message.author.id == 243519195529084939 or ctx.message.author.id == 272815177659842561 or ctx.message.author.id == 418649205494775820

proxies = []

setembedcolor = 0x000000
setfooterimage = "https://media.discordapp.net/attachments/460974692073734164/680067025493950474/Wcu7EAAAAASUVORK5CYII.png"
setfootertext = "@ScriptingTools | Demandware"

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
    asd = 0
    nopidfound = 0
    data = {}
    data["Snipes"] = []
    y = data["Snipes"]
    testpid = ["00000001","00000002","00000003","00000004","00000005","00000006","00000007","00000008","00000009","00000010","00000011","00000012","00000013","00000014","00000015","00000016","00000017","00000018","00000019","00000020","00000021","00000022","00000023","00000024","00000025","00000026","00000027","00000028","00000029","00000030","00000031","Null"]
    correcttestpid = []

    now = datetime.now()
    try:
    	server_name = context.guild.name
    except AttributeError:
    	server_name = "DM"

    user_name_id = context.author.name + ' ID : ' + str(context.author.id)
    log2 = Fore.CYAN +f'[{server_name}]'
    log3 = Fore.CYAN + f'[{user_name_id}] '
    log = log2 + ' ' + log3

    bb = pid.isdigit()
    if bb == False:
        pid3 = pid.split('000')[1].split('.html')[0]
        url1 = pid.split('000')[0]
        pid2 = pid3.replace(pid3, '000'+pid3)
        pid = pid2
    elif bb == True:
        pid5 = len(str(pid))
        if pid5 == 14:
            pid = pid
        elif pid5 == 22:
            pid2 = pid.split("000000")
            pid3 = pid2[0]
            pid = pid3
        else:
            print('Wrong PID')

    for i in range(len(testpid)):
        correcttestpid.append(pid + testpid[i])
    data = {}
    data["Snipes"] = []

    with open('snipes.json') as json_file:
        data = json.load(json_file)
        for i in range(len(data["Snipes"])):            
            for R in range(len(data["Snipes"][i])):
                try:
                    for w in range(len(correcttestpid)):
                        if correcttestpid[w] in data["Snipes"][i][R]:
                            nopidfound = 1
                except (TypeError,KeyError,IndexError) as e:
                	continue

    if nopidfound == 1:
        print(Fore.MAGENTA + f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] " + log + Fore.GREEN + f"[FOUND PID]")
        embedpid = []
        embedsize = []

        with open('snipes.json') as json_file: 
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
        variantId2 = ['N/A' if x==pid+"Null" else x for x in embedpid]
        allsize = ['> '+x for x in embedsize]
        sizelist = "\n".join(allsize)
        variantIdlist = "\n".join(variantId2)

        embed=discord.Embed(title="Snipes - "+productName, description="> SKU: "+sku+"\n> Price: "+price, color=setembedcolor)
        embed.add_field(name=":straight_ruler: Size", value=sizelist, inline=True)
        embed.add_field(name=":pushpin: SKUs", value=variantIdlist, inline=True)
        embed.set_thumbnail(url=image)
        embed.set_footer(text=setfootertext + ' Snipes Scraper', icon_url=setfooterimage)
        await context.send(embed=embed)
        print(Fore.MAGENTA + f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] " + log + Fore.GREEN + f"[Webhook sent!]")
        json_file.close()

    else:
        session = aiohttp.ClientSession()
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


        bb = pid.isdigit()
        if bb == False:
            pid3 = pid.split('000')[1].split('.html')[0]
            url1 = pid.split('000')[0]
            pid2 = pid3.replace(pid3, '000'+pid3)
            url2 = pid+'?dwvar_'+pid2+'_212&format=ajax'
            url3 = url1+pid2+'.html'+'?dwvar_'+pid2+'_212&format=ajax'
            producturl = url3
            pid = pid2
            print(Fore.MAGENTA + f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] " + log + Fore.YELLOW + f"[DIDNT FIND PID][Getting SKUs - {pid}]")
            await session.close()
        elif bb == True:
            pid5 = len(str(pid))
            if pid5 == 14:
                pid = pid
            elif pid5 == 22:
                pid2 = pid.split("000000")
                pid3 = pid2[0]
                pid = pid3
            else:
                print(Fore.MAGENTA + f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] " + log + Fore.RED + f"[WRONG PID]")
            print(Fore.MAGENTA + f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] " + log + Fore.YELLOW + f"[DIDNT FIND PID][Getting SKUs - {pid}]")
            url = "https://www.snipes.com/p/jordan-air_jordan_1_mid_-black%2Fchile_red%2Fwhite-"+pid+".html"
            proxy = getRandomProxy()
            proxy2 = getRandomProxy()
            proxy3 = proxy2['http'] 
            proxy4 = proxy3.replace('7000/', '7000')
            firstresponse = await session.get(url, headers=headers2, proxy=proxy4, allow_redirects=False)
            link3 = firstresponse.headers['Location']
            producturl = link3+'?dwvar_'+pid+'_212&format=ajax'
            print(producturl)
            await session.close()
        else:
            embed=discord.Embed(title="Snipes - PID Scraper", color=setembedcolor)
            embed.add_field(name="Error", value="Make sure your PID / Link is correct.", inline=True)
            embed.set_footer(text=setfootertext + ' Snipes Scraper', icon_url=setfooterimage)
            await context.send(embed=embed)
        session = aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False))
        proxy = getRandomProxy()
        proxy2 = getRandomProxy()
        proxy3 = proxy2['http'] 
        proxy4 = proxy3.replace('7000/', '7000')
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
            variantId = []
            size = []
            for i in range(len(values)):
                variantId.append(values[i]["variantId"])
                size.append(values[i]["displayValue"])
            variantId2 = ['N/A' if x==None else x for x in variantId]
            variantId3 = [pid+"Null" if x==None else x for x in variantId]
            allsize = ['> '+x for x in size]
            variantIdlist = "\n".join(variantId2)
            sizelist = "\n".join(allsize)
            pidimage = pid[7:]
            embedproductlink = "[" + sku + "](" + producturl + ")"
            print(Fore.MAGENTA + f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] " + log + Fore.GREEN + f"[Succesfully got SKUs of - {pid}]")

            for j in range(len(variantId3)):
                name = str(variantId3[j])
                y.append({
                    name:[{
                        "SKU": sku,
                        "Size": size[j],
                        "price": price,
                        "name": productName,
                        "image": image
                    }]
                })

            def write_json(data, filename='snipes.json'): 
                with open(filename,'w') as f: 
                    json.dump(data, f, indent=2)

            with open('snipes.json') as json_file: 
                data = json.load(json_file)
                temp = data["Snipes"]
                temp.append(y) 

            write_json(data) 
            json_file.close()

            embed=discord.Embed(title="Snipes - "+productName, description="> SKU: "+sku+"\n> Price: "+price, color=setembedcolor)
            embed.add_field(name=":straight_ruler: Size", value=sizelist, inline=True)
            embed.add_field(name=":pushpin: SKUs", value=variantIdlist, inline=True)
            embed.set_thumbnail(url=image)
            embed.set_footer(text=setfootertext + ' Snipes Scraper', icon_url=setfooterimage)
            await context.send(embed=embed)
            await session.close()
            print(Fore.MAGENTA + f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] " + log + Fore.GREEN + f"[Webhook sent!]")
        except (ValueError,UnboundLocalError,TypeError) as e:
            print("An Error occured", e, producturl)
            embed=discord.Embed(title="Snipes - PID Scraper", color=setembedcolor)
            embed.add_field(name="Error", value="An error occured, try later", inline=True)
            embed.set_footer(text=setfootertext + ' Snipes Scraper', icon_url=setfooterimage)
            await context.send(embed=embed)
            await session.close()

@bot.command()
@commands.check(check_if_it_is_me)
async def snipesstock(context, pid):
	
	now = datetime.now()
	try:
		server_name = context.guild.name
	except AttributeError:
		server_name = "DM"

	user_name_id = context.author.name + ' ID : ' + str(context.author.id)

	log2 = Fore.CYAN +f'[{server_name}]'
	log3 = Fore.CYAN + f'[{user_name_id}] '

	log = log2 + ' ' + log3

	print(Fore.MAGENTA + f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] " + log + Fore.YELLOW + f"[Getting stock of - {pid}]")

	asd = 0
	nopidfound = 0
	data = {}
	data["Snipes"] = []
	y = data["Snipes"]
	testpid = ["00000001","00000002","00000003","00000004","00000005","00000006","00000007","00000008","00000009","00000010","00000011","00000012","00000013","00000014","00000015","00000016","00000017","00000018","00000019","00000020","00000021","00000022","00000023","00000024","00000025","00000026","00000027","00000028","00000029","00000030","00000031","Null"]
	correcttestpid = []

	now = datetime.now()
	try:
		server_name = context.guild.name
	except AttributeError:
		server_name = "DM"

	user_name_id = context.author.name + ' ID : ' + str(context.author.id)
	log2 = Fore.CYAN +f'[{server_name}]'
	log3 = Fore.CYAN + f'[{user_name_id}] '
	log = log2 + ' ' + log3

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

	bb = pid.isdigit()
	if bb == False:
		pid3 = pid.split('000')[1].split('.html')[0]
		url1 = pid.split('000')[0]
		pid2 = pid3.replace(pid3, '000'+pid3)
		pid = pid2
	elif bb == True:
		pid5 = len(str(pid))
		if pid5 == 14:
			pid = pid
		elif pid5 == 22:
			pid2 = pid.split("000000")
			pid3 = pid2[0]
			pid = pid3
		else:
			print(Fore.MAGENTA + f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] " + log + Fore.RED + f"[WRONG PID]")

	for i in range(len(testpid)):
	    correcttestpid.append(pid + testpid[i])
	data = {}
	data["Snipes"] = []

	with open('snipes.json') as json_file:
	    data = json.load(json_file)
	    for i in range(len(data["Snipes"])):            
	        for R in range(len(data["Snipes"][i])):
	            try:
	                for w in range(len(correcttestpid)):
	                    if correcttestpid[w] in data["Snipes"][i][R]:
	                        nopidfound = 1
	            except (TypeError,KeyError,IndexError) as e:
	            	continue
	if nopidfound == 1:
		print(Fore.MAGENTA + f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] " + log + Fore.GREEN + f"[FOUND PID]")
		embedpid = []
		embedsize = []
		pidlist = []

		with open('snipes.json') as json_file: 
			data = json.load(json_file)
			for i in range(len(data["Snipes"])):            
				for R in range(len(data["Snipes"][i])):
					try:
						for w in range(len(correcttestpid)):
							if correcttestpid[w] in data["Snipes"][i][R]:
								key, value = list(data["Snipes"][i][R].items())[0]
								embedpid.append(key)
					except (TypeError,KeyError,IndexError) as e:
						continue
			pidlist = embedpid
		json_file.close()

	else:
		session = aiohttp.ClientSession()
		headers3 = {
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
		headers4 = {
		"Upgrade-Insecure-Requests": "1",
		"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36",
		}


		bb = pid.isdigit()
		if bb == False:
			pid3 = pid.split('000')[1].split('.html')[0]
			url1 = pid.split('000')[0]
			pid2 = pid3.replace(pid3, '000'+pid3)
			url2 = pid+'?dwvar_'+pid2+'_212&format=ajax'
			url3 = url1+pid2+'.html'+'?dwvar_'+pid2+'_212&format=ajax'
			producturl = url3
			pid = pid2
			print(Fore.MAGENTA + f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] " + log + Fore.YELLOW + f"[DIDNT FIND PID][Getting SKUs - {pid}]")
			await session.close()
		elif bb == True:
			pid5 = len(str(pid))
			if pid5 == 14:
			    pid = pid
			elif pid5 == 22:
				pid2 = pid.split("000000")
				pid3 = pid2[0]
				pid = pid3
			else:
				print(Fore.MAGENTA + f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] " + log + Fore.RED + f"[WRONG PID]")
			print(Fore.MAGENTA + f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] " + log + Fore.YELLOW + f"[DIDNT FIND PID][Getting SKUs - {pid}]")
			url = "https://www.snipes.com/p/jordan-air_jordan_1_mid_-black%2Fchile_red%2Fwhite-"+pid+".html"
			proxy = getRandomProxy()
			proxy2 = getRandomProxy()
			proxy3 = proxy2['http'] 
			proxy4 = proxy3.replace('7000/', '7000')
			firstresponse = await session.get(url, headers=headers4, proxy=proxy4, allow_redirects=False)
			link3 = firstresponse.headers['Location']
			producturl = link3+'?dwvar_'+pid+'_212&format=ajax'
			print(producturl)
			await session.close()
		else:
			embed=discord.Embed(title="Snipes - PID Scraper", color=setembedcolor)
			embed.add_field(name="Error", value="Make sure your PID / Link is correct.", inline=True)
			embed.set_footer(text=setfootertext + ' Snipes Scraper', icon_url=setfooterimage)
			await context.send(embed=embed)
		session = aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False))
		proxy = getRandomProxy()
		proxy2 = getRandomProxy()
		proxy3 = proxy2['http'] 
		proxy4 = proxy3.replace('7000/', '7000')
		session = aiohttp.ClientSession()
		response = await session.get(producturl, headers=headers3, proxy=proxy4)
		text = await response.text()
		if 'https://collector-pxszbf5p84.perimeterx.net' in text:
			while asd > 5:
				await session.close()
				proxy = getRandomProxy()
				proxy2 = getRandomProxy()
				proxy3 = proxy2['http'] 
				proxy4 = proxy3.replace('7000/', '7000')
				session = aiohttp.ClientSession()
				response = await session.get(producturl, headers=headers3, proxy=proxy4)
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
			variantId = []
			size = []
			for i in range(len(values)):
				variantId.append(values[i]["variantId"])
				size.append(values[i]["displayValue"])
			pidlist = variantId
			variantId2 = ['N/A' if x==None else x for x in variantId]
			variantId3 = [pid+"Null" if x==None else x for x in variantId]
			allsize = ['> '+x for x in size]
			variantIdlist = "\n".join(variantId2)
			sizelist = "\n".join(allsize)
			pidimage = pid[7:]
			embedproductlink = "[" + sku + "](" + producturl + ")"
			print(Fore.MAGENTA + f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] " + log + Fore.GREEN + f"[Succesfully got SKUs of - {pid}]")

			for j in range(len(variantId3)):
				name = str(variantId3[j])
				y.append({
					name:[{
						"SKU": sku,
						"Size": size[j],
						"price": price,
						"name": productName,
						"image": image
					}]
				})

			def write_json(data, filename='snipes.json'): 
				with open(filename,'w') as f: 
					json.dump(data, f, indent=2)

			with open('snipes.json') as json_file: 
				data = json.load(json_file)
				temp = data["Snipes"]
				temp.append(y)

			write_json(data)
			json_file.close()
		except (ValueError,UnboundLocalError,TypeError) as e:
			print("An Error occured", e, producturl)
			embed=discord.Embed(title="Snipes - PID Scraper", color=setembedcolor)
			embed.add_field(name="Error", value="An error occured, try later", inline=True)
			embed.set_footer(text=setfootertext + ' Snipes Scraper', icon_url=setfooterimage)
			await context.send(embed=embed)
			await session.close()

	embedstock = []
	embedsize = []
	sizelinks = []
	sku = ""
	releasedate = ""
	count = ''

	
	for i in range(len(pidlist)):
		proxy2 = getRandomProxy()
		proxy3 = proxy2['http'] 
		proxy4 = proxy3.replace('7000/', '7000')
		url = "https://www.snipes.com/p/jordan-air_jordan_1_mid__%28gs%29-white%2Funiversity_gold%2Fblack-"+str(pidlist[i])+".html?chosen=size&dwvar_"+str(pidlist[i])+"_212="+str(pidlist[i])+"&format=ajax"
		link = "https://www.snipes.com/p/"+str(pidlist[i])+".html"
		pidimage = pid[7:]
		image = "https://images.weserv.nl/?url=https://www.snipes.com/on/demandware.static/-/Sites-snse-master-eu/default/dw24f55347/"+pidimage+"_P.png"
		exception = True
		session = aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False))
		response = await session.get(url, headers=headers, proxy=proxy4)
		text = await response.text()
		await session.close()
		print(Fore.MAGENTA + f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] " + log + Fore.YELLOW + f"[Checking stock for size - {str(pidlist[i])}]")
		if 'https://collector-pxszbf5p84.perimeterx.net' in text:
			proxy = getRandomProxy()
			proxy2 = getRandomProxy()
			proxy3 = proxy2['http'] 
			proxy4 = proxy3.replace('7000/', '7000')
			session = aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False))
			response = await session.get(url, headers=headers, proxy=proxy4)
			text = await response.text()
			await session.close()
		elif 'The owner of this website (www.snipes.com) has banned you temporarily from accessing this website.' in text:
			proxy = getRandomProxy()
			proxy2 = getRandomProxy()
			proxy3 = proxy2['http'] 
			proxy4 = proxy3.replace('7000/', '7000')
			session = aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False))
			response = await session.get(url, headers=headers, proxy=proxy4)
			text = await response.text()
			await session.close()
		elif response.status == 403:
			proxy = getRandomProxy()
			proxy2 = getRandomProxy()
			proxy3 = proxy2['http'] 
			proxy4 = proxy3.replace('7000/', '7000')
			session = aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False))
			response = await session.get(url, headers=headers, proxy=proxy4)
			text = await response.text()
			await session.close()
		elif response.status == 404 or response.status == 410:
			print(Fore.MAGENTA + f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] " + log + Fore.YELLOW + f"[No stock found - {str(pidlist[i])}]")
			continue
			await session.close()
		else:
			session = aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False))
			info = json.loads(text)
			availability = info["product"]
			pidid = availability["id"]
			productname = availability["productName"]
			print(Fore.MAGENTA + f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] " + log + Fore.GREEN + f"[Succesfully got stock of - {str(pidlist[i])}]")
			await session.close()
			if len(pidid) > 15:
				stocknr = availability["lineItemAvailability"]
				custom = availability["custom"]
				embedsize.append(custom["size"])
				embedstock.append(stocknr["available"])
				sizelinks.append("https://www.snipes.com/p/scriptintools-"+availability["id"])
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


				allsize5 = ['https://www.snipes.com/p/scriptintools-'+x for x in allsize10]
				sizelinks_final = [f"> [{i}]({e})" for i, e in zip(allsize, allsize5)]
				discsize = "\n".join(sizelinks_final)
				discstock = "\n".join(map(str, allsize2))
				discpids = "\n".join(map(str, allsize3))
				totalstock = sum(newlist10)
			await session.close()
			getsku = availability["facts"]
			custom = availability["custom"]
			for url in getsku:
				if url["ID"] == "manufacturerSKU":
					sku = url["value"]
				if url["ID"] == "releaseDate":
					releasedate = custom["releaseDateUTC"]
				else:
					releasedate = "Live"
	embed=discord.Embed(title="Snipes - "+productname, description='> Snipes sizes early links, use them on drop / restock.\n\n> '+str(sku), color=0)
	embed.add_field(name=":link: Sizes & Links", value=discsize, inline=True)
	embed.add_field(name=":bar_chart: Stock", value=discstock, inline=True)
	embed.add_field(name=":pushpin: SKUs", value=discpids, inline=True)
	embed.add_field(name="Total Stock", value="`"+str(totalstock)+"`", inline=True)
	embed.add_field(name="Release Date", value="`"+str(releasedate)+"`", inline=True)

	embed.set_thumbnail(url=image)
	embed.set_footer(text=setfootertext, icon_url=setfooterimage)
	await context.send(embed=embed)
	await session.close()
	print(Fore.MAGENTA + f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] " + log + Fore.GREEN + "[Webhook sent!]")

@bot.command()
@commands.check(check_if_it_is_me)
async def snipesadd(context, info):
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

	def write_json(data, filename='snipes.json'): 
		with open(filename,'w') as f: 
			json.dump(data, f, indent=2)

	with open('snipes.json') as json_file: 
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
	data["Snipes"] = []
	y = data["Snipes"]
	lines = context.message.content.splitlines()
	lines.pop(0)



	with open('snipes.json', 'r') as data_file:
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

	with open('snipes.json', 'w') as data_file:
		data = json.dump(data, data_file, indent=2)

	variantIdlist = "\n".join(lines)

	embed=discord.Embed(title="Succesfully deleted from Snipes", color=setembedcolor)
	embed.add_field(name=":pushpin: SKUs", value=variantIdlist, inline=True)
	embed.set_footer(text=setfootertext + ' Snipes Scraper', icon_url=setfooterimage)
	await context.send(embed=embed)

@bot.command()
@commands.check(check_if_it_is_me)
async def checksnipes(context, info):

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
	data["Snipes"] = []
	y = data["Snipes"]
	lines = context.message.content.splitlines()
	lines.pop(0)
	foundpids = []


	with open('snipes.json', 'r') as data_file:
		data = json.load(data_file)

		for i in range(len(data["Snipes"])):            
			for R in range(len(data["Snipes"][i])):
				try:
					for w in range(len(lines)):
						if lines[w] in data["Snipes"][i][R]:
							foundpids.append(str(data["Snipes"][i][R].keys()))

				except (TypeError,KeyError,IndexError) as e:
					continue

	with open('snipes.json', 'w') as data_file:
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

################################################################################################################################################
################################################################################################################################################
################################################################################################################################################
################################################################################################################################################
#									   #####  #####  #      ######  ######  #####  #    #
#									   #      #   #  #      #       #    #  #   #   #  #
#									   #####  #   #  #      ###     # ###   #   #    ##
#									       #  #   #  #      #       #    #  #   #   #  #
#									   #####  #####  #####  ######  ######  #####  #    #
################################################################################################################################################
################################################################################################################################################
################################################################################################################################################
################################################################################################################################################

@bot.command()
async def soleboxpid(context, pid):

	now = datetime.now()
	try:
		server_name = context.guild.name
	except AttributeError:
		server_name = "DM"

	user_name_id = context.author.name + ' ID : ' + str(context.author.id)

	log2 = Fore.CYAN +f'[{server_name}]'
	log3 = Fore.CYAN + f'[{user_name_id}] '

	log = log2 + ' ' + log3

	asd = 0
	nopidfound = 0
	data = {}
	data["Solebox"] = []
	y = data["Solebox"]
	testpid = ["00000001","00000002","00000003","00000004","00000005","00000006","00000007","00000008","00000009","00000010","00000011","00000012","00000013","00000014","00000015","00000016","00000017","00000018","00000019","00000020","00000021","00000022","00000023","00000024","00000025","00000026","00000027","00000028","00000029","00000030","00000031","Null"]
	correcttestpid = []

	bb = pid.isdigit()
	if bb == False:
		pidlink = pid.replace(".html","")
		pid2 = pidlink[-8:]
		url1 = pid.split('01')[0]
		pid = pid2
	elif bb == True:
		if len(pid) > 10:
			pid = pid[:8]
		else:
			pid = pid

	for i in range(len(testpid)):
		correcttestpid.append(pid + testpid[i])
	data = {}
	data["Solebox"] = []

	with open('solebox.json') as json_file:
		data = json.load(json_file)
		for i in range(len(data["Solebox"])):            
			for R in range(len(data["Solebox"][i])):
				try:
					for w in range(len(correcttestpid)):
						if correcttestpid[w] in data["Solebox"][i][R]:
							nopidfound = 1
				except (TypeError,KeyError,IndexError) as e:
					continue

	if nopidfound == 1:
		print(Fore.MAGENTA + f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] " + log + Fore.GREEN + f"[FOUND PID]")
		embedpid = []
		embedsize = []
	    
		with open('solebox.json') as json_file: 
			data = json.load(json_file)
			for i in range(len(data["Solebox"])):            
				for R in range(len(data["Solebox"][i])):
					try:
						for w in range(len(correcttestpid)):
							if correcttestpid[w] in data["Solebox"][i][R]:
								key, value = list(data["Solebox"][i][R].items())[0]
								embedpid.append(key)
								embedsize.append(value[0]["Size"])
								price = value[0]["price"]
								sku = value[0]["SKU"]
								productName = value[0]["name"]
								image = value[0]["image"]
					except (TypeError,KeyError,IndexError) as e:
						continue

		variantId2 = ['N/A' if x==pid+"Null" else x for x in embedpid]
		allsize = ['> '+x for x in embedsize]
		sizelist = "\n".join(allsize)
		variantIdlist = "\n".join(variantId2)

		embed=discord.Embed(title="Solebox - "+productName, description="> SKU: "+sku+"\n> Price: "+price, color=setembedcolor)
		embed.add_field(name=":straight_ruler: Size", value=sizelist, inline=True)
		embed.add_field(name=":pushpin: SKUs", value=variantIdlist, inline=True)
		embed.set_thumbnail(url=image)
		embed.set_footer(text=setfootertext + ' Solebox Scraper', icon_url=setfooterimage)
		await context.send(embed=embed)
		print(Fore.MAGENTA + f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] " + log + Fore.GREEN + f"[Webhook sent!]")
		json_file.close()

	else:
		session = aiohttp.ClientSession()
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


		bb = pid.isdigit()
		if bb == False:
			pidlink = pid.replace(".html","")
			pid2 = pidlink[-8:]
			url1 = pid.split('01')[0]
			pid = pid2
			url2 = pid+'?dwvar_'+pid2+'_212&format=ajax'
			url3 = url1+pid2+'.html'+'?dwvar_'+pid2+'_212&format=ajax'
			producturl = url3
			pid = pid2
			print(Fore.MAGENTA + f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] " + log + Fore.YELLOW + f"[DIDNT FIND PID][Getting SKUs - {pid}]")
			await session.close()
		elif bb == True:
			if len(pid) > 10:
				pid = pid[:8]
			else:
				pid = pid
			url = "https://www.solebox.com/en_DE/p/nike-air_force_1_%2707_lv8_%22raygun%22-white%2Fblack-orange_flash-"+pid+".html"
			proxy = getRandomProxy()
			proxy2 = getRandomProxy()
			proxy3 = proxy2['http'] 
			proxy4 = proxy3.replace('7000/', '7000')
			firstresponse = await session.get(url, headers=headers2, proxy=proxy4, allow_redirects=False)
			link3 = firstresponse.headers['Location']
			producturl = link3+'?dwvar_'+pid+'_212&format=ajax'
			print(Fore.MAGENTA + f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] " + log + Fore.YELLOW + f"[DIDNT FIND PID][Getting SKUs - {pid}]")
			await session.close()
		else:
			embed=discord.Embed(title="Solebox - PID Scraper", color=setembedcolor)
			embed.add_field(name="Error", value="Make sure your PID / Link is correct.", inline=True)
			embed.set_footer(text=setfootertext + ' Solebox Scraper', icon_url=setfooterimage)
			await context.send(embed=embed)
		session = aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False))
		proxy = getRandomProxy()
		proxy2 = getRandomProxy()
		proxy3 = proxy2['http'] 
		proxy4 = proxy3.replace('7000/', '7000')
		session = aiohttp.ClientSession()
		response = await session.get(producturl, headers=headers, proxy=proxy4)
		text = await response.text()
		if 'https://collector-pxur63h57z.perimeterx.net' in text:
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
				if 'https://collector-pxur63h57z.perimeterx.net' in text:
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
			variantId = []
			size = []
			for i in range(len(values)):
				variantId.append(values[i]["variantId"])
				size.append(values[i]["displayValue"])
			variantId2 = ['N/A' if x==None else x for x in variantId]
			variantId3 = [pid+"Null" if x==None else x for x in variantId]
			allsize = ['> '+x for x in size]
			variantIdlist = "\n".join(variantId2)
			sizelist = "\n".join(allsize)
			pidimage = pid[7:]
			embedproductlink = "[" + sku + "](" + producturl + ")"
			print(Fore.MAGENTA + f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] " + log + Fore.GREEN + f"[Succesfully got SKUs of - {pid}]")

			for j in range(len(variantId3)):
				name = str(variantId3[j])
				y.append({
					name:[{
						"SKU": sku,
						"Size": size[j],
						"price": price,
						"name": productName,
						"image": image
					}]
				})

			def write_json(data, filename='solebox.json'): 
				with open(filename,'w') as f: 
					json.dump(data, f, indent=2)

			with open('solebox.json') as json_file: 
				data = json.load(json_file)
				temp = data["Solebox"]
				temp.append(y) 

			write_json(data) 
			json_file.close()

			embed=discord.Embed(title="Solebox - "+productName, description="> SKU: "+sku+"\n> Price: "+price, color=setembedcolor)
			embed.add_field(name=":straight_ruler: Size", value=sizelist, inline=True)
			embed.add_field(name=":pushpin: SKUs", value=variantIdlist, inline=True)
			embed.set_thumbnail(url=image)
			embed.set_footer(text=setfootertext + ' Solebox Scraper', icon_url=setfooterimage)
			await context.send(embed=embed)
			print(Fore.MAGENTA + f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] " + log + Fore.GREEN + f"[Webhook sent!]")
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
async def soleboxstock(context, pid):
	now = datetime.now()

	try:
		server_name = context.guild.name
	except AttributeError:
		server_name = "DM"

	user_name_id = context.author.name + ' ID : ' + str(context.author.id)

	log2 = Fore.CYAN +f'[{server_name}]'
	log3 = Fore.CYAN + f'[{user_name_id}] '

	log = log2 + ' ' + log3

	asd = 0
	nopidfound = 0
	data = {}
	data["Solebox"] = []
	pidlist = []
	y = data["Solebox"]
	testpid = ["00000001","00000002","00000003","00000004","00000005","00000006","00000007","00000008","00000009","00000010","00000011","00000012","00000013","00000014","00000015","00000016","00000017","00000018","00000019","00000020","00000021","00000022","00000023","00000024","00000025","00000026","00000027","00000028","00000029","00000030","00000031","Null"]
	correcttestpid = []

	bb = pid.isdigit()
	if bb == False:
		pid3 = pid.split('01')[1].split('.html')[0]
		url1 = pid.split('01')[0]
		pid2 = pid3.replace(pid3, '01'+pid3)
		pid = pid2
	elif bb == True:
		if len(pid) > 10:
			pid = pid[:8]
		else:
			pid = pid

	for i in range(len(testpid)):
		correcttestpid.append(pid + testpid[i])
	data = {}
	data["Solebox"] = []

	with open('solebox.json') as json_file:
		data = json.load(json_file)
		for i in range(len(data["Solebox"])):            
			for R in range(len(data["Solebox"][i])):
				try:
					for w in range(len(correcttestpid)):
						if correcttestpid[w] in data["Solebox"][i][R]:
							nopidfound = 1
				except (TypeError,KeyError,IndexError) as e:
					continue
 
	if nopidfound == 1:
		print(Fore.MAGENTA + f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] " + log + Fore.GREEN + f"[FOUND PID]")
		embedpid = []
		embedsize = []

		with open('solebox.json') as json_file: 
			data = json.load(json_file)
			for i in range(len(data["Solebox"])):            
				for R in range(len(data["Solebox"][i])):
					try:
						for w in range(len(correcttestpid)):
							if correcttestpid[w] in data["Solebox"][i][R]:
								key, value = list(data["Solebox"][i][R].items())[0]
								embedpid.append(key)
					except (TypeError,KeyError,IndexError) as e:
						continue
		pidlist = embedpid
		json_file.close()

	else:
		session = aiohttp.ClientSession()

		headers3 = {
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
		headers4 = {
		"Upgrade-Insecure-Requests": "1",
		"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36",
		}


		bb = pid.isdigit()
		if bb == False:
			pid3 = pid.split('01')[1].split('.html')[0]
			url1 = pid.split('01')[0]
			pid2 = pid3.replace(pid3, '01'+pid3)
			url2 = pid+'?dwvar_'+pid2+'_212&format=ajax'
			url3 = url1+pid2+'.html'+'?dwvar_'+pid2+'_212&format=ajax'
			producturl = url3
			pid = pid2
			print(Fore.MAGENTA + f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] " + log + Fore.YELLOW + f"[DIDNT FIND PID][Getting SKUs - {pid}]")
			await session.close()
		elif bb == True:
			if len(pid) > 10:
				pid = pid[:8]
			else:
				pid = pid
			url = "https://www.solebox.com/en_DE/p/nike-air_force_1_%2707_lv8_%22raygun%22-white%2Fblack-orange_flash-"+pid+".html"
			proxy = getRandomProxy()
			proxy2 = getRandomProxy()
			proxy3 = proxy2['http'] 
			proxy4 = proxy3.replace('7000/', '7000')
			firstresponse = await session.get(url, headers=headers4, proxy=proxy4, allow_redirects=False)
			link3 = firstresponse.headers['Location']
			producturl = link3+'?dwvar_'+pid+'_212&format=ajax'
			print(Fore.MAGENTA + f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] " + log + Fore.YELLOW + f"[DIDNT FIND PID][Getting SKUs - {pid}]")
			await session.close()
		else:
			embed=discord.Embed(title="Solebox - PID Scraper", color=setembedcolor)
			embed.add_field(name="Error", value="Make sure your PID / Link is correct.", inline=True)
			embed.set_footer(text=setfootertext + ' Solebox Scraper', icon_url=setfooterimage)
			await context.send(embed=embed)
		session = aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False))
		proxy = getRandomProxy()
		proxy2 = getRandomProxy()
		proxy3 = proxy2['http'] 
		proxy4 = proxy3.replace('7000/', '7000')
		session = aiohttp.ClientSession()
		response = await session.get(producturl, headers=headers3, proxy=proxy4)
		text = await response.text()
		if 'https://collector-pxur63h57z.perimeterx.net' in text:
			while asd > 5:
				await session.close()
				proxy = getRandomProxy()
				proxy2 = getRandomProxy()
				proxy3 = proxy2['http'] 
				proxy4 = proxy3.replace('7000/', '7000')
				session = aiohttp.ClientSession()
				response = await session.get(producturl, headers=headers3, proxy=proxy4)
				text = await response.text()
				asd = asd + 1
				print("PX banned - Retry Nr. " + str(asd))
				if 'https://collector-pxur63h57z.perimeterx.net' in text:
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
			variantId = []
			size = []
			for i in range(len(values)):
				variantId.append(values[i]["variantId"])
				size.append(values[i]["displayValue"])
			pidlist = variantId
			variantId2 = ['N/A' if x==None else x for x in variantId]
			variantId3 = [pid+"Null" if x==None else x for x in variantId]
			allsize = ['> '+x for x in size]
			variantIdlist = "\n".join(variantId2)
			sizelist = "\n".join(allsize)
			pidimage = pid[7:]
			print(Fore.MAGENTA + f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] " + log + Fore.GREEN + f"[Succesfully got SKUs of - {pid}]")

			for j in range(len(variantId3)):
				name = str(variantId3[j])
				y.append({
					name:[{
						"SKU": sku,
						"Size": size[j],
						"price": price,
						"name": productName,
						"image": image
					}]
				})

			def write_json(data, filename='solebox.json'): 
				with open(filename,'w') as f: 
					json.dump(data, f, indent=2)

			with open('solebox.json') as json_file: 
				data = json.load(json_file)
				temp = data["Solebox"]
				temp.append(y) 

			write_json(data) 
			json_file.close()

			await session.close()
		except (ValueError,UnboundLocalError,TypeError) as e:
			print("An Error occured", e, producturl)
			embed=discord.Embed(title="Solebox - PID Scraper", color=setembedcolor)
			embed.add_field(name="Error", value="An error occured, try later", inline=True)
			embed.set_footer(text=setfootertext + ' Solebox Scraper', icon_url=setfooterimage)
			await context.send(embed=embed)
			await session.close()

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
	count = ''
	
	for i in range(len(pidlist)):
		proxy2 = getRandomProxy()
		proxy3 = proxy2['http'] 
		proxy4 = proxy3.replace('7000/', '7000')
		url = 'https://www.solebox.com/en_DE/p/nike-air_force_1_%2707_"coconut_milk"-sail%2Fsummit_white-white-'+str(pidlist[i])+".html?chosen=size&dwvar_"+str(pidlist[i])+"_212="+str(pidlist[i])+"&format=ajax"
		pidimage = pid[1:]
		image = "https://www.solebox.com/on/demandware.static/-/Sites-solebox-master-de/default/dw4d286efa/"+pidimage+"_PS.png"
		exception = True
		session = aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False))
		response = await session.get(url, headers=headers, proxy=proxy4)
		text = await response.text()
		await session.close()
		print(Fore.MAGENTA + f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] " + log + Fore.YELLOW + f"[Checking stock for size - {str(pidlist[i])}]")
		if 'https://collector-pxur63h57z.perimeterx.net' in text:
			proxy = getRandomProxy()
			proxy2 = getRandomProxy()
			proxy3 = proxy2['http'] 
			proxy4 = proxy3.replace('7000/', '7000')
			session = aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False))
			response = await session.get(url, headers=headers, proxy=proxy4)
			text = await response.text()
			await session.close()
		elif 'The owner of this website (www.solebox.com) has banned you temporarily from accessing this website.' in text:
			proxy = getRandomProxy()
			proxy2 = getRandomProxy()
			proxy3 = proxy2['http'] 
			proxy4 = proxy3.replace('7000/', '7000')
			session = aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False))
			response = await session.get(url, headers=headers, proxy=proxy4)
			text = await response.text()
			await session.close()
		elif response.status == 403:
			proxy = getRandomProxy()
			proxy2 = getRandomProxy()
			proxy3 = proxy2['http'] 
			proxy4 = proxy3.replace('7000/', '7000')
			session = aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False))
			response = await session.get(url, headers=headers, proxy=proxy4)
			text = await response.text()
			await session.close()
		elif response.status == 404 or response.status == 410:
			print(Fore.MAGENTA + f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] " + log + Fore.YELLOW + f"[No stock found - {str(pidlist[i])}]")
			continue
			await session.close()
		else:
			session = aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False))
			info = json.loads(text)
			availability = info["product"]
			pidid = availability["id"]
			productname = availability["productName"]
			print(Fore.MAGENTA + f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] " + log + Fore.GREEN + f"[Succesfully got stock of - {str(pidlist[i])}]")
			await session.close()
			if len(pidid) > 15:
				stocknr = availability["lineItemAvailability"]
				custom = availability["custom"]
				embedsize.append(custom["size"])
				embedstock.append(stocknr["available"])
				sizelinks.append("https://www.solebox.com/en_DE/p/scriptintools-"+availability["id"])
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


				allsize5 = ['https://www.solebox.com/en_DE/p/scriptintools-'+x+'.html' for x in allsize10]
				sizelinks_final = [f"> [{i}]({e})" for i, e in zip(allsize, allsize5)]
				discsize = "\n".join(sizelinks_final)
				discstock = "\n".join(map(str, allsize2))
				discpids = "\n".join(map(str, allsize3))
				totalstock = sum(newlist10)
			await session.close()
			getsku = availability["facts"]
			custom = availability["custom"]
			for url in getsku:
				if url["ID"] == "manufacturerSKU":
					sku = url["value"]
				if url["ID"] == "releaseDate":
					releasedate = custom["releaseDateUTC"]
				else:
					releasedate = "Live"

	embed=discord.Embed(title="Solebox - "+productname, description='> Solebox sizes early links, use them on drop / restock.\n\n> '+str(sku), color=0)
	embed.add_field(name=":link: Sizes & Links", value=discsize, inline=True)
	embed.add_field(name=":bar_chart: Stock", value=discstock, inline=True)
	embed.add_field(name=":pushpin: SKUs", value=discpids, inline=True)
	embed.add_field(name="Total Stock", value="`"+str(totalstock)+"`", inline=True)
	embed.add_field(name="Release Date", value="`"+str(releasedate)+"`", inline=True)

	embed.set_thumbnail(url=image)
	embed.set_footer(text=setfootertext, icon_url=setfooterimage)
	await context.send(embed=embed)
	await session.close()
	print(Fore.MAGENTA + f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] " + log + Fore.GREEN + "[Webhook sent!]")

@bot.command()
@commands.check(check_if_it_is_me)
async def soleboxadd(context, info):

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
	data["Solebox"] = []
	y = data["Solebox"]
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

	def write_json(data, filename='solebox.json'): 
		with open(filename,'w') as f: 
			json.dump(data, f, indent=2)

	with open('solebox.json') as json_file: 
		data = json.load(json_file)
		temp = data["Solebox"]
		temp.append(y) 

	sizelist = "\n".join(size)
	variantIdlist = "\n".join(variantId)
	write_json(data) 
	json_file.close()

	embed=discord.Embed(title="Added to Solebox - "+productName, description="> SKU: "+sku+"\n> Price: "+price, color=setembedcolor)
	embed.add_field(name=":straight_ruler: Size", value=sizelist, inline=True)
	embed.add_field(name=":pushpin: SKUs", value=variantIdlist, inline=True)
	embed.set_thumbnail(url=image)
	embed.set_footer(text=setfootertext + ' Solebox Scraper', icon_url=setfooterimage)
	await context.send(embed=embed)

@bot.command()
@commands.check(check_if_it_is_me)
async def soleboxdelete(context, info):

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
	data["Solebox"] = []
	y = data["Solebox"]
	lines = context.message.content.splitlines()
	lines.pop(0)



	with open('solebox.json', 'r') as data_file:
		data = json.load(data_file)

		for i in range(len(data["Solebox"])):            
			for R in range(len(data["Solebox"][i])):
				try:
					for w in range(len(lines)):
						if lines[w] in data["Solebox"][i][R]:
							data["Solebox"][i][R].pop(lines[w])
							print(Fore.MAGENTA + f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] " + log + Fore.GREEN + f"[Succesfully deleted PID - {lines[w]}]")
							break;
				except (TypeError,KeyError,IndexError) as e:
					continue

	with open('solebox.json', 'w') as data_file:
		data = json.dump(data, data_file, indent=2)

	variantIdlist = "\n".join(lines)

	embed=discord.Embed(title="Succesfully deleted from Solebox", color=setembedcolor)
	embed.add_field(name=":pushpin: SKUs", value=variantIdlist, inline=True)
	embed.set_footer(text=setfootertext + ' Solebox Scraper', icon_url=setfooterimage)
	await context.send(embed=embed)

@bot.command()
@commands.check(check_if_it_is_me)
async def checksolebox(context, info):

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
	data["Solebox"] = []
	y = data["Solebox"]
	lines = context.message.content.splitlines()
	lines.pop(0)
	foundpids = []


	with open('solebox.json', 'r') as data_file:
		data = json.load(data_file)

		for i in range(len(data["Solebox"])):            
			for R in range(len(data["Solebox"][i])):
				try:
					for w in range(len(lines)):
						if lines[w] in data["Solebox"][i][R]:
							foundpids.append(str(data["Solebox"][i][R].keys()))

				except (TypeError,KeyError,IndexError) as e:
					continue

	with open('solebox.json', 'w') as data_file:
		data = json.dump(data, data_file, indent=2)

	if not foundpids:
		embed=discord.Embed(title="Solebox - No Product found", color=setembedcolor)
		embed.set_footer(text=setfootertext + ' Solebox Scraper', icon_url=setfooterimage)
		await context.send(embed=embed)
	else:
		variantIdlist = "\n".join(foundpids)
		embed=discord.Embed(title="Found Pids in Solebox.json", color=setembedcolor)
		embed.add_field(name=":pushpin: SKUs", value=variantIdlist, inline=True)
		embed.set_footer(text=setfootertext + ' Solebox Scraper', icon_url=setfooterimage)
		await context.send(embed=embed)

################################################################################################################################################
################################################################################################################################################
################################################################################################################################################
################################################################################################################################################
#									   #####   ##    #  #    #   #######  ######														
#									   #   #   # #   #   #  #    #        #    # 
#									   #   #   #  #  #    ##     #   ###  #    #
#									   #   #   #   # #    ##     #     #  #    # 
#									   #####   #    ##    ##     #######  ###### 
################################################################################################################################################
################################################################################################################################################
################################################################################################################################################
################################################################################################################################################

@bot.command()
async def onygopid(context, pid):
    
    now = datetime.now()
    
    try:
        server_name = context.guild.name
    except AttributeError:
        server_name = "DM"

    user_name_id = context.author.name + ' ID : ' + str(context.author.id)

    log2 = Fore.CYAN +f'[{server_name}]'
    log3 = Fore.CYAN + f'[{user_name_id}] '

    log = log2 + ' ' + log3


    asd = 0
    nopidfound = 0
    data = {}
    data["Onygo"] = []
    y = data["Onygo"]
    testpid = ["00000001","00000002","00000003","00000004","00000005","00000006","00000007","00000008","00000009","00000010","00000011","00000012","00000013","00000014","00000015","00000016","00000017","00000018","00000019","00000020","00000021","00000022","00000023","00000024","00000025","00000026","00000027","00000028","00000029","00000030","00000031","Null"]
    correcttestpid = []

    bb = pid.isdigit()
    if bb == False:
        pid3 = pid.split('000')[1].split('.html')[0]
        url1 = pid.split('000')[0]
        pid2 = pid3.replace(pid3, '000'+pid3)
        pid = pid2
    elif bb == True:
        pid5 = len(str(pid))
        if pid5 == 14:
            pid = pid
        elif pid5 == 22:
            pid2 = pid.split("000000")
            pid3 = pid2[0]
            pid = pid3
        else:
            print('Wrong PID')

    for i in range(len(testpid)):
        correcttestpid.append(pid + testpid[i])
    data = {}
    data["Onygo"] = []

    with open('onygo.json') as json_file:
        data = json.load(json_file)
        for i in range(len(data["Onygo"])):            
            for R in range(len(data["Onygo"][i])):
                try:
                    for w in range(len(correcttestpid)):
                        if correcttestpid[w] in data["Onygo"][i][R]:
                            nopidfound = 1
                except (TypeError,KeyError,IndexError) as e:
                    continue
 
    if nopidfound == 1:
        print(Fore.MAGENTA + f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] " + log + Fore.GREEN + f"[FOUND PID]")
        embedpid = []
        embedsize = []
        
        with open('onygo.json') as json_file: 
            data = json.load(json_file)
            for i in range(len(data["Onygo"])):            
                for R in range(len(data["Onygo"][i])):
                    try:
                        for w in range(len(correcttestpid)):
                            if correcttestpid[w] in data["Onygo"][i][R]:
                                key, value = list(data["Onygo"][i][R].items())[0]
                                embedpid.append(key)
                                embedsize.append(value[0]["Size"])
                                price = value[0]["price"]
                                sku = value[0]["SKU"]
                                productName = value[0]["name"]
                                image = value[0]["image"]
                    except (TypeError,KeyError,IndexError) as e:
                        continue
        variantId2 = ['N/A' if x==pid+"Null" else x for x in embedpid]
        allsize = ['> '+x for x in embedsize]
        sizelist = "\n".join(allsize)
        variantIdlist = "\n".join(variantId2)

        embed=discord.Embed(title="Onygo - "+productName, description="> SKU: "+sku+"\n> Price: "+price, color=setembedcolor)
        embed.add_field(name=":straight_ruler: Size", value=sizelist, inline=True)
        embed.add_field(name=":pushpin: SKUs", value=variantIdlist, inline=True)
        embed.set_thumbnail(url=image)
        embed.set_footer(text=setfootertext, icon_url=setfooterimage)
        await context.send(embed=embed)
        print(Fore.MAGENTA + f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] " + log + Fore.GREEN + f"[Webhook sent!]")
        json_file.close()

    else:
        session = aiohttp.ClientSession()

        headers3 = {
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
        headers4 = {
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36",
        }


        bb = pid.isdigit()
        if bb == False:
            pid3 = pid.split('000')[1].split('.html')[0]
            url1 = pid.split('000')[0]
            pid2 = pid3.replace(pid3, '000'+pid3)
            url2 = pid+'?dwvar_'+pid2+'_212&format=ajax'
            url3 = url1+pid2+'.html'+'?dwvar_'+pid2+'_size='+pid2+'&format=ajax'
            producturl = url3
            pid = pid2
            print(Fore.MAGENTA + f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] " + log + Fore.YELLOW + f"[DIDNT FIND PID][Getting stock of - {pid}]")
            await session.close()
        elif bb == True:
            pid5 = len(str(pid))
            if pid5 == 14:
                pid = pid
                print(Fore.MAGENTA + f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] " + log + Fore.YELLOW + f"[DIDNT FIND PID][Getting stock of - {pid}]")
            elif pid5 == 22:
                pid2 = pid.split("000000")
                pid3 = pid2[0]
                pid = pid3
                print(Fore.MAGENTA + f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] " + log + Fore.YELLOW + f"[DIDNT FIND PID][Getting stock of - {pid}]")
            else:
                print(Fore.MAGENTA + f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] " + log + Fore.RED + f"[WRONG PID]")
            url = "https://www.onygo.com/p/nike-blazer_mid_%2777_vintage-white%2Fblack-"+pid+".html"
            proxy = getRandomProxy()
            proxy2 = getRandomProxy()
            proxy3 = proxy2['http'] 
            proxy4 = proxy3.replace('7000/', '7000')
            firstresponse = await session.get(url, headers=headers4, proxy=proxy4, allow_redirects=False)
            link3 = firstresponse.headers['Location']
            producturl = link3+'?dwvar_'+pid+'_size='+pid+'&format=ajax'
            await session.close()
        else:
            embed=discord.Embed(title="Onygo - PID Scraper", color=setembedcolor)
            embed.add_field(name="Error", value="Make sure your PID / Link is correct.", inline=True)
            embed.set_footer(text=setfootertext + ' Onygo Scraper', icon_url=setfooterimage)
            await context.send(embed=embed)
        session = aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False))
        proxy = getRandomProxy()
        proxy2 = getRandomProxy()
        proxy3 = proxy2['http'] 
        proxy4 = proxy3.replace('7000/', '7000')
        session = aiohttp.ClientSession()
        response = await session.get(producturl, headers=headers3, proxy=proxy4)
        text = await response.text()
        if 'https://collector-pxj1n025xg.perimeterx.net' in text:
            while asd > 5:
                await session.close()
                proxy = getRandomProxy()
                proxy2 = getRandomProxy()
                proxy3 = proxy2['http'] 
                proxy4 = proxy3.replace('7000/', '7000')
                session = aiohttp.ClientSession()
                response = await session.get(producturl, headers=headers3, proxy=proxy4)
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
                image = "https://www.onygo.com/dw/image/v2/BDCB_PRD/on/demandware.static/-/Sites-ong-master-de/default/dw3e361af2/"+pid[-7:]+"_P.jpg?sw=1560&sh=1560&sm=fit&sfrm=png"
                print(pid)
            except:
                image = ''
            try:
                sku = product["facts"][1]["value"]
            except:
                sku = 'N/A'
            values = product["variationAttributes"][1]["values"]
            variantId = []
            size = []
            for i in range(len(values)):
                variantId.append(values[i]["variantId"])
                size.append(values[i]["displayValue"])
            variantId2 = ['N/A' if x==None else x for x in variantId]
            variantId3 = [pid+"Null" if x==None else x for x in variantId]
            allsize = ['> '+x for x in size]
            variantIdlist = "\n".join(variantId2)
            sizelist = "\n".join(allsize)
            pidimage = pid[7:]
            embedproductlink = "[" + sku + "](" + producturl + ")"
            print(Fore.MAGENTA + f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] " + log + Fore.GREEN + f"[Succesfully got SKUs]")

            for j in range(len(variantId3)):
                name = str(variantId3[j])
                y.append({
                    name:[{
                        "SKU": sku,
                        "Size": size[j],
                        "price": price,
                        "name": productName,
                        "image": image
                    }]
                })
            def write_json(data, filename='onygo.json'): 
                with open(filename,'w') as f: 
                    json.dump(data, f, indent=2)

            with open('onygo.json') as json_file: 
                data = json.load(json_file)
                temp = data["Onygo"]
                temp.append(y) 

            write_json(data) 
            json_file.close()

            embed=discord.Embed(title="Onygo - "+productName, description="> SKU: "+sku+"\n> Price: "+price, color=setembedcolor)
            embed.add_field(name=":straight_ruler: Size", value=sizelist, inline=True)
            embed.add_field(name=":pushpin: SKUs", value=variantIdlist, inline=True)
            embed.set_thumbnail(url=image)
            embed.set_footer(text=setfootertext, icon_url=setfooterimage)
            await context.send(embed=embed)
            print(Fore.MAGENTA + f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] " + log + Fore.YELLOW + f"[Webhook sent!]")
            await session.close()
        except (ValueError,UnboundLocalError,TypeError) as e:
            print("An Error occured", e, producturl)
            embed=discord.Embed(title="Onygo - PID Scraper", color=setembedcolor)
            embed.add_field(name="Error", value="An error occured, try later", inline=True)
            embed.set_footer(text=setfootertext, icon_url=setfooterimage)
            await context.send(embed=embed)
            await session.close()

@bot.command()
@commands.check(check_if_it_is_me)
async def onygostock(context, pid):

	now = datetime.now()

	try:
		server_name = context.guild.name
	except AttributeError:
		server_name = "DM"

	user_name_id = context.author.name + ' ID : ' + str(context.author.id)

	log2 = Fore.CYAN +f'[{server_name}]'
	log3 = Fore.CYAN + f'[{user_name_id}] '

	log = log2 + ' ' + log3
	asd = 0
	nopidfound = 0
	data = {}
	data["Onygo"] = []
	y = data["Onygo"]
	testpid = ["00000001","00000002","00000003","00000004","00000005","00000006","00000007","00000008","00000009","00000010","00000011","00000012","00000013","00000014","00000015","00000016","00000017","00000018","00000019","00000020","00000021","00000022","00000023","00000024","00000025","00000026","00000027","00000028","00000029","00000030","00000031","Null"]
	correcttestpid = []

	bb = pid.isdigit()
	if bb == False:
		pid3 = pid.split('000')[1].split('.html')[0]
		url1 = pid.split('000')[0]
		pid2 = pid3.replace(pid3, '000'+pid3)
		pid = pid2
	elif bb == True:
		pid5 = len(str(pid))
		if pid5 == 14:
			pid = pid
		elif pid5 == 22:
			pid2 = pid.split("000000")
			pid3 = pid2[0]
			pid = pid3
		else:
			print('Wrong PID')

	for i in range(len(testpid)):
		correcttestpid.append(pid + testpid[i])
	data = {}
	data["Onygo"] = []

	with open('onygo.json') as json_file:
		data = json.load(json_file)
		for i in range(len(data["Onygo"])):            
			for R in range(len(data["Onygo"][i])):
				try:
					for w in range(len(correcttestpid)):
						if correcttestpid[w] in data["Onygo"][i][R]:
							nopidfound = 1
				except (TypeError,KeyError,IndexError) as e:
					continue

	if nopidfound == 1:
		print(Fore.MAGENTA + f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] " + log + Fore.GREEN + f"[FOUND PID]")
		embedpid = []
		embedsize = []

		with open('onygo.json') as json_file: 
			data = json.load(json_file)
			for i in range(len(data["Onygo"])):            
				for R in range(len(data["Onygo"][i])):
					try:
						for w in range(len(correcttestpid)):
							if correcttestpid[w] in data["Onygo"][i][R]:
								key, value = list(data["Onygo"][i][R].items())[0]
								embedpid.append(key)
					except (TypeError,KeyError,IndexError) as e:
						continue
		pidlist = embedpid
		json_file.close()

	else:
		session = aiohttp.ClientSession()

		headers3 = {
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
		headers4 = {
		"Upgrade-Insecure-Requests": "1",
		"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36",
		}


		bb = pid.isdigit()
		if bb == False:
			pid3 = pid.split('000')[1].split('.html')[0]
			url1 = pid.split('000')[0]
			pid2 = pid3.replace(pid3, '000'+pid3)
			url2 = pid+'?dwvar_'+pid2+'_212&format=ajax'
			url3 = url1+pid2+'.html'+'?dwvar_'+pid2+'_size='+pid2+'&format=ajax'
			producturl = url3
			pid = pid2
			print(Fore.MAGENTA + f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] " + log + Fore.YELLOW + f"[DIDNT FIND PID][Getting stock of - {pid}]")
			await session.close()
		elif bb == True:
			pid5 = len(str(pid))
			if pid5 == 14:
				pid = pid
				print(Fore.MAGENTA + f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] " + log + Fore.YELLOW + f"[DIDNT FIND PID][Getting stock of - {pid}]")
			elif pid5 == 22:
				pid2 = pid.split("000000")
				pid3 = pid2[0]
				pid = pid3
				print(Fore.MAGENTA + f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] " + log + Fore.YELLOW + f"[DIDNT FIND PID][Getting stock of - {pid}]")
			else:
				print(Fore.MAGENTA + f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] " + log + Fore.RED + f"[WRONG PID]")
			url = "https://www.onygo.com/p/nike-blazer_mid_%2777_vintage-white%2Fblack-"+pid+".html"
			proxy = getRandomProxy()
			proxy2 = getRandomProxy()
			proxy3 = proxy2['http'] 
			proxy4 = proxy3.replace('7000/', '7000')
			firstresponse = await session.get(url, headers=headers4, proxy=proxy4, allow_redirects=False)
			link3 = firstresponse.headers['Location']
			producturl = link3+'?dwvar_'+pid+'_size='+pid+'&format=ajax'
			await session.close()
		else:
			embed=discord.Embed(title="Onygo - PID Scraper", color=setembedcolor)
			embed.add_field(name="Error", value="Make sure your PID / Link is correct.", inline=True)
			embed.set_footer(text=setfootertext + ' Onygo Scraper', icon_url=setfooterimage)
			await context.send(embed=embed)
		session = aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False))
		proxy = getRandomProxy()
		proxy2 = getRandomProxy()
		proxy3 = proxy2['http'] 
		proxy4 = proxy3.replace('7000/', '7000')
		session = aiohttp.ClientSession()
		response = await session.get(producturl, headers=headers3, proxy=proxy4)
		text = await response.text()
		if 'https://collector-pxj1n025xg.perimeterx.net' in text:
			while asd > 5:
				await session.close()
				proxy = getRandomProxy()
				proxy2 = getRandomProxy()
				proxy3 = proxy2['http'] 
				proxy4 = proxy3.replace('7000/', '7000')
				session = aiohttp.ClientSession()
				response = await session.get(producturl, headers=headers3, proxy=proxy4)
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
				image = "https://www.onygo.com/dw/image/v2/BDCB_PRD/on/demandware.static/-/Sites-ong-master-de/default/dw3e361af2/"+pid[-7:]+"_P.jpg?sw=1560&sh=1560&sm=fit&sfrm=png"
			except:
				image = ''
			try:
				sku = product["facts"][1]["value"]
			except:
				sku = 'N/A'
			values = product["variationAttributes"][1]["values"]
			variantId = []
			size = []
			for i in range(len(values)):
				variantId.append(values[i]["variantId"])
				size.append(values[i]["displayValue"])
			pidlist = variantId
			variantId2 = ['N/A' if x==None else x for x in variantId]
			variantId3 = [pid+"Null" if x==None else x for x in variantId]
			allsize = ['> '+x for x in size]
			variantIdlist = "\n".join(variantId2)
			sizelist = "\n".join(allsize)
			pidimage = pid[7:]
			embedproductlink = "[" + sku + "](" + producturl + ")"
			print(Fore.MAGENTA + f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] " + log + Fore.GREEN + f"[Succesfully got SKUs]")

			for j in range(len(variantId3)):
				name = str(variantId3[j])
				y.append({
					name:[{
						"SKU": sku,
						"Size": size[j],
						"price": price,
						"name": productName,
						"image": image
					}]
				})
			def write_json(data, filename='onygo.json'): 
				with open(filename,'w') as f: 
					json.dump(data, f, indent=2)

			with open('onygo.json') as json_file: 
				data = json.load(json_file)
				temp = data["Onygo"]
				temp.append(y) 

			write_json(data) 
			json_file.close()
			await session.close()
		except (ValueError,UnboundLocalError,TypeError) as e:
			print("An Error occured", e, producturl)
			embed=discord.Embed(title="Onygo - PID Scraper", color=setembedcolor)
			embed.add_field(name="Error", value="An error occured, try later", inline=True)
			embed.set_footer(text=setfootertext, icon_url=setfooterimage)
			await context.send(embed=embed)
			await session.close()

	print(Fore.MAGENTA + f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] " + log + Fore.YELLOW + f"[Getting stock of - {pid}]")
	headers = {
	'authority': "www.onygo.com",
	'pragma': 'no-cache',
	'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36",
	'accept': "application/json, text/javascript, */*; q=0.01",
	'content-type': 'application/json',
	'sec-fetch-site': "same-origin",
	'sec-fetch-mode': "cors",
	'sec-fetch-dest': "empty",
	'referer': "https://www.onygo.com/p/"+pid+".html",
	'accept-language': "de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7",
	}

	embedstock = []
	embedsize = []
	sizelinks = []
	sku = ""
	releasedate = ""
	count = ''

	for i in range(len(pidlist)):
		proxy2 = getRandomProxy()
		proxy3 = proxy2['http'] 
		proxy4 = proxy3.replace('7000/', '7000')
		url = "https://www.onygo.com/p/jordan-air_jordan_1_retro_high_og_-black%2Fblack-metallic_silver_white-"+str(pidlist[i])+".html?chosen=size&dwvar_"+str(pidlist[i])+"_size="+str(pidlist[i])+"&format=ajax"
		pidimage = pid[7:]
		image = "https://www.onygo.com/on/demandware.static/-/Sites-ong-master-de/default/dw6812d605/"+pidimage+"_P.png"
		exception = True
		session = aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False))
		response = await session.get(url, headers=headers, proxy=proxy4)
		text = await response.text()
		await session.close()
		print(Fore.MAGENTA + f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] " + log + Fore.YELLOW + f"[Checking stock for size - {str(pidlist[i])}]")
		if 'https://collector-pxj1n025xg.perimeterx.net' in text:
			proxy = getRandomProxy()
			proxy2 = getRandomProxy()
			proxy3 = proxy2['http'] 
			proxy4 = proxy3.replace('7000/', '7000')
			session = aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False))
			response = await session.get(url, headers=headers, proxy=proxy4)
			text = await response.text()
			await session.close()
		elif 'The owner of this website (www.onygo.com) has banned you temporarily from accessing this website.' in text:
			proxy = getRandomProxy()
			proxy2 = getRandomProxy()
			proxy3 = proxy2['http'] 
			proxy4 = proxy3.replace('7000/', '7000')
			session = aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False))
			response = await session.get(url, headers=headers, proxy=proxy4)
			text = await response.text()
			await session.close()
		elif response.status == 403:
			proxy = getRandomProxy()
			proxy2 = getRandomProxy()
			proxy3 = proxy2['http'] 
			proxy4 = proxy3.replace('7000/', '7000')
			session = aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False))
			response = await session.get(url, headers=headers, proxy=proxy4)
			text = await response.text()
			await session.close()
		elif response.status == 404 or response.status == 410:
			print(Fore.MAGENTA + f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] " + log + Fore.YELLOW + f"[No stock found - {str(pidlist[i])}]")
			continue
			await session.close()
		else:
			session = aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False))
			info = json.loads(text)
			availability = info["product"]
			pidid = availability["id"]
			productname = availability["productName"]
			print(Fore.MAGENTA + f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] " + log + Fore.GREEN + f"[Succesfully got stock of - {str(pidlist[i])}]")
			await session.close()
			if len(pidid) > 15:
				stocknr = availability["lineItemAvailability"]
				custom = availability["custom"]
				embedsize.append(custom["size"])
				embedstock.append(stocknr["available"])
				sizelinks.append("https://www.onygo.com/p/scriptintools-"+availability["id"])
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


				allsize5 = ['https://www.onygo.com/p/scriptintools-'+x+'.html' for x in allsize10]
				sizelinks_final = [f"> [{i}]({e})" for i, e in zip(allsize, allsize5)]
				discsize = "\n".join(sizelinks_final)
				discstock = "\n".join(map(str, allsize2))
				discpids = "\n".join(map(str, allsize3))
				totalstock = sum(newlist10)
			await session.close()
			getsku = availability["facts"]
			custom = availability["custom"]
			for url in getsku:
				if url["ID"] == "manufacturerSKU":
					sku = url["value"]
				if url["ID"] == "releaseDate":
					releasedate = custom["releaseDateUTC"]
				else:
					releasedate = "Live"

	embed=discord.Embed(title="Onygo - "+productname, description='> Onygo sizes early links, use them on drop / restock.\n\n> '+str(sku), color=0)
	embed.add_field(name=":link: Sizes & Links", value=discsize, inline=True)
	embed.add_field(name=":bar_chart: Stock", value=discstock, inline=True)
	embed.add_field(name=":pushpin: SKUs", value=discpids, inline=True)
	embed.add_field(name="Total Stock", value="`"+str(totalstock)+"`", inline=True)
	embed.add_field(name="Release Date", value="`"+str(releasedate)+"`", inline=True)

	embed.set_thumbnail(url=image)
	embed.set_footer(text="@ScriptingTools | Onygo Stock Checker", icon_url="https://images-ext-2.discordapp.net/external/CaKgsPyNTamwDBmdhLjtuI36MuDiqIm7woXUcYVopw8/https/images-ext-1.discordapp.net/external/atwFnJRaXHB0ebXrVSPjVWDXe5hL2OQ0JBWopjGcVCY/https/images-ext-2.discordapp.net/external/gGrbK8FUkmby_Ao8mmH9dZ4RI1cvfkhpUNBlIB46XQE/https/media.discordapp.net/attachments/460974692073734164/680067025493950474/Wcu7EAAAAASUVORK5CYII.png")
	await context.send(embed=embed)
	await session.close()
	print(Fore.MAGENTA + f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] " + log + Fore.GREEN + "[Webhook sent!]")

@bot.command()
@commands.check(check_if_it_is_me)
async def onygoadd(context, info):

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
	data["Onygo"] = []
	y = data["Onygo"]
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
		print(Fore.MAGENTA + f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] " + log + Fore.GREEN + f"[Succesfully added - {str(variantId[j])}]")

	def write_json(data, filename='onygo.json'): 
		with open(filename,'w') as f: 
			json.dump(data, f, indent=2)

	with open('onygo.json') as json_file: 
		data = json.load(json_file)
		temp = data["Onygo"]
		temp.append(y) 

	sizelist = "\n".join(size)
	variantIdlist = "\n".join(variantId)
	write_json(data) 
	json_file.close()

	embed=discord.Embed(title="Added to Onygo - "+productName, description="> SKU: "+sku+"\n> Price: "+price, color=setembedcolor)
	embed.add_field(name=":straight_ruler: Size", value=sizelist, inline=True)
	embed.add_field(name=":pushpin: SKUs", value=variantIdlist, inline=True)
	embed.set_thumbnail(url=image)
	embed.set_footer(text=setfootertext + ' Onygo Scraper', icon_url=setfooterimage)
	await context.send(embed=embed)

@bot.command()
@commands.check(check_if_it_is_me)
async def onygodelete(context, info):

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
	data["Onygo"] = []
	y = data["Onygo"]
	lines = context.message.content.splitlines()
	lines.pop(0)



	with open('onygo.json', 'r') as data_file:
		data = json.load(data_file)

		for i in range(len(data["Onygo"])):            
			for R in range(len(data["Onygo"][i])):
				try:
					for w in range(len(lines)):
						if lines[w] in data["Onygo"][i][R]:
							data["Onygo"][i][R].pop(lines[w])
							print(Fore.MAGENTA + f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] " + log + Fore.GREEN + f"[Succesfully deleted - {lines[w]}]")
							break;
				except (TypeError,KeyError,IndexError) as e:
					continue

	with open('onygo.json', 'w') as data_file:
		data = json.dump(data, data_file, indent=2)

	variantIdlist = "\n".join(lines)

	embed=discord.Embed(title="Succesfully deleted from Onygo", color=setembedcolor)
	embed.add_field(name=":pushpin: SKUs", value=variantIdlist, inline=True)
	embed.set_footer(text=setfootertext + ' Onygo Scraper', icon_url=setfooterimage)
	await context.send(embed=embed)

@bot.command()
@commands.check(check_if_it_is_me)
async def checkonygo(context, info):

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
	data["Onygo"] = []
	y = data["Onygo"]
	lines = context.message.content.splitlines()
	lines.pop(0)
	foundpids = []


	with open('onygo.json', 'r') as data_file:
		data = json.load(data_file)

		for i in range(len(data["Onygo"])):            
			for R in range(len(data["Onygo"][i])):
				try:
					for w in range(len(lines)):
						if lines[w] in data["Onygo"][i][R]:
							foundpids.append(str(data["Onygo"][i][R].keys()))

				except (TypeError,KeyError,IndexError) as e:
					continue

	with open('onygo.json', 'w') as data_file:
		data = json.dump(data, data_file, indent=2)

	if not foundpids:
		embed=discord.Embed(title="Onygo - No Product found", color=setembedcolor)
		embed.set_footer(text=setfootertext + ' Onygo Scraper', icon_url=setfooterimage)
		await context.send(embed=embed)
	else:
		variantIdlist = "\n".join(foundpids)
		embed=discord.Embed(title="Found Pids in Onygo.json", color=setembedcolor)
		embed.add_field(name=":pushpin: SKUs", value=variantIdlist, inline=True)
		embed.set_footer(text=setfootertext + ' Onygo Scraper', icon_url=setfooterimage)
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


bot.run(bottoken)
