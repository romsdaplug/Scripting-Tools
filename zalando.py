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
from datetime import datetime
from colorama import Fore, Back, Style, init
from decimal import Decimal
from discord.ext.commands import CommandNotFound,MissingRequiredArgument

bot = commands.Bot(command_prefix = '?', help_command=None)

bottoken ="YOUR_DISCORD_BOT_TOKEN"

setfootertextzalando = "@ScriptingToolsPublic | <?zalandohelp>"
setfooterimage = "https://images-ext-1.discordapp.net/external/atwFnJRaXHB0ebXrVSPjVWDXe5hL2OQ0JBWopjGcVCY/https/images-ext-2.discordapp.net/external/gGrbK8FUkmby_Ao8mmH9dZ4RI1cvfkhpUNBlIB46XQE/https/media.discordapp.net/attachments/460974692073734164/680067025493950474/Wcu7EAAAAASUVORK5CYII.png"
setembedcolor = 0x000000

@bot.event
async def on_ready():
	print('Bot is ready.')
	pass

def check_if_it_is_me(ctx):
	return ctx.message.author.id == 175953718750085121 or ctx.message.author.id == 351639955531104258

def split_list(a_list):
    half = len(a_list)//2
    return a_list[:half], a_list[half:]

@bot.command()
async def zalando(ctx, link):

	user_name_id = ctx.author.name + ' ID : ' + str(ctx.author.id)
	log3 = Fore.CYAN + f'[{user_name_id}] '
	log4 = "[ZALANDO]"
	log = log3 + log4
	now = datetime.now()
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

		print(Fore.MAGENTA + f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]"+ log + Fore.GREEN + f"[PRODUCT ID - {str.upper(productid)}][{str.upper(countrycode)}]")
		try:
			response = requests.get(link, headers=headers)
			soup = bs(response.content, 'html.parser')
			text = soup.find("script",{"id":"z-vegas-pdp-props"}).text
			strtext = str(text)
			newtext = strtext.replace("""\xa0€""","€").replace("<![CDATA[","")
			try:
				newstrtext = newtext.split('"units":')[1].split("}]")[0]
				newstrtext = newstrtext + "}]"
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
			except IndexError:
				newstrtext = newtext.split('"units":')[1].split(',"partnerTncUrl')[0]
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
			allsize2 = ['> '+x for x in size]
			discsize = "\n".join(allsize2)
			newsku = ['> '+x for x in sku]
			discstock = "\n".join(stock)
			discsku = "\n".join(sku)
			discsizesku = "\n".join("{0} {1}".format(x,y) for x,y in zip(allsize2,sku))


			embed=discord.Embed(title="Zalando Stock Checker :flag_" + countrycode + ":", description='> ['+(shoename)+']('+link+')', color=setembedcolor)
			embed.set_thumbnail(url=shoepic)
			embed.add_field(name=":straight_ruler: Size", value=discsize, inline=True)
			embed.add_field(name=":bar_chart: Stock", value=discstock, inline=True)
			embed.add_field(name=":pushpin: SKUs", value=discsku, inline=True)
			embed.add_field(name="Total Stock", value="`"+str(totalstock)+"`", inline=True)
			embed.add_field(name="Price", value="`" + str(correctprice) + "`", inline=True)
			embed.add_field(name="Release Date", value="`Live`", inline=True)
			embed.set_footer(text=setfootertextzalando, icon_url=setfooterimage)
			await ctx.send(embed=embed)
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
				discstock = "\n".join(coloredstock)
				discsize = "\n".join(allsize2)
				newsku = ['> '+x for x in sku]
				discsku = "\n".join(sku)
				discsizesku = "\n".join("{0} {1}".format(x,y) for x,y in zip(allsize2,sku))


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
				await ctx.send(embed=embed)

			except Exception:
				embed=discord.Embed(title="Zalando Stock Checker - Error", color=setembedcolor)
				embed.add_field(name="Error", value="An error occured. Please check your command or link!", inline=True)
				embed.set_footer(text=setfootertextzalando, icon_url=setfooterimage)
				await ctx.send(embed=embed)
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

		try:
			response = requests.get(link, headers=headers)
			soup = bs(response.content, 'html.parser')
			text = soup.find("script",{"id":"z-vegas-pdp-props"}).text
			strtext = str(text)
			newtext = strtext.replace("""\xa0€""","€").replace("<![CDATA[","")				
			try:
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
			except IndexError:
				newstrtext = newtext.split('"units":')[1].split(',"partnerTncUrl')[0]
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
			await ctx.send(embed=embed)
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
				await ctx.send(embed=embed)
			except Exception:
				embed=discord.Embed(title="Zalando Stock Checker - Error", color=setembedcolor)
				embed.add_field(name="Error", value="An error occured. Please check your command or link!", inline=True)
				embed.set_footer(text=setfootertextzalando, icon_url=setfooterimage)
				await ctx.send(embed=embed)
	except IndexError:
		embed=discord.Embed(title="Zalando PID Scraper - Error", color=setembedcolor)
		embed.add_field(name="Error", value="An error occured. Please check your command or link!", inline=False)
		embed.add_field(name="Command Format",value="?zalandopid <full link here>", inline=False)
		embed.set_footer(text=setfootertextzalando, icon_url=setfooterimage)
		await ctx.send(embed=embed)


@bot.command()
async def zalandolink(ctx, link):

	user_name_id = ctx.author.name + ' ID : ' + str(ctx.author.id)
	log3 = Fore.CYAN + f'[{user_name_id}] '
	log4 = "[ZALANDO]"
	log = log3 + log4
	now = datetime.now()

	newlinks = []
	hypedproduct = 0

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

	try:
		response = requests.get(link, headers=headers)
		souplink = bs(response.content, "html.parser")
		testcolorway = souplink.find("meta", {"name":"twitter:data2"})["content"].replace("/","").replace(" ","-")
		testsku = souplink.find("meta", {"property":"al:ios:url"})["content"].split("sku=")[1].split("&")[0]
		colorway = testcolorway+"-"+str.lower(testsku) + ".html"
		
		countryflag = [":flag_de:",":flag_at:",":flag_ch:",":flag_nl:",":flag_be:",":flag_fr:",":flag_it:",":flag_es:",":flag_gb:",":flag_se:",":flag_no:",":flag_dk:",":flag_fi:",":flag_pl:",":flag_cz:"]
		country = ["Germany","Austria","Switzerland","Netherlands","Belgium","France","Italy","Spain","United Kingdom","Sweden","Norway","Denmark","Finnland","Poland","Czech Republic"]

		if "jordan-air-1" in link:
			if "low" in link or "laag" in link or "basses" in link or "basse"  in link or "matalavartiset" in link or "niskie" in link:
				if "-se-" in link:
					if testcolorway in link:
						hypedproduct = 1
						colorwayprint = colorway.replace("-"," ").replace(".html","").replace("?_rfl=en","")
						colorwayprint = colorwayprint.replace(colorwayprint[-13:],"")
						embedcolorway = f"JORDAN 1 LOW SE\n{str.upper(colorwayprint)}"
						print(Fore.MAGENTA + f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]"+ log + Fore.GREEN + f"[ZALANDO][PRODUCT - JORDAN LOW SE {str.upper(colorwayprint)}]")
						jordan1lowse = ["https://www.zalando.de/jordan-air-1-se-sneaker-low-","https://www.zalando.at/jordan-air-1-se-sneaker-low-","https://wwww.zalando.ch/jordan-air-1-se-sneaker-low-","https://www.zalando.nl/jordan-air-1-se-sneakers-laag-","https://www.zalando.be/jordan-air-1-se-sneakers-laag-","https://www.zalando.fr/jordan-air-1-se-baskets-basses-","https://www.zalando.it/jordan-air-1-se-sneakers-basse-","https://www.zalando.es/jordan-air-1-se-zapatillas-","https://www.zalando.co.uk/jordan-air-1-se-trainers-","https://www.zalando.se/jordan-air-1-se-sneakers-","https://www.zalando.no/jordan-air-1-se-joggesko-","https://www.zalando.dk/jordan-air-1-se-sneakers-","https://www.zalando.fi/jordan-air-1-se-matalavartiset-tennarit-","https://www.zalando.pl/jordan-air-1-se-sneakersy-niskie-","https://www.zalando.cz/jordan-air-1-se-tenisky-"]
						for i in range(len(jordan1lowse)):
							newlinks.append(jordan1lowse[i]+colorway)
					else:
						hypedproduct = 1
						colorwayprint = colorway.replace("-"," ").replace(".html","").replace("?_rfl=en","")
						colorwayprint = colorwayprint.replace(colorwayprint[-13:],"")
						embedcolorway = f"JORDAN 1 LOW SE\n{str.upper(colorwayprint)}"
						colorway = link.split(".html")[0][-13:] + ".html"
						print(Fore.MAGENTA + f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]"+ log + Fore.GREEN + f"[ZALANDO][PRODUCT - JORDAN LOW SE {str.upper(colorwayprint)}]")
						jordan1lowse = ["https://www.zalando.de/jordan-air-1-se-sneaker-low-","https://www.zalando.at/jordan-air-1-se-sneaker-low-","https://wwww.zalando.ch/jordan-air-1-se-sneaker-low-","https://www.zalando.nl/jordan-air-1-se-sneakers-laag-","https://www.zalando.be/jordan-air-1-se-sneakers-laag-","https://www.zalando.fr/jordan-air-1-se-baskets-basses-","https://www.zalando.it/jordan-air-1-se-sneakers-basse-","https://www.zalando.es/jordan-air-1-se-zapatillas-","https://www.zalando.co.uk/jordan-air-1-se-trainers-","https://www.zalando.se/jordan-air-1-se-sneakers-","https://www.zalando.no/jordan-air-1-se-joggesko-","https://www.zalando.dk/jordan-air-1-se-sneakers-","https://www.zalando.fi/jordan-air-1-se-matalavartiset-tennarit-","https://www.zalando.pl/jordan-air-1-se-sneakersy-niskie-","https://www.zalando.cz/jordan-air-1-se-tenisky-"]
						for i in range(len(jordan1lowse)):
							newlinks.append(jordan1lowse[i]+colorway)
				else:
					if testcolorway in link:
						hypedproduct = 1
						colorwayprint = colorway.replace("-"," ").replace(".html","").replace("?_rfl=en","")
						colorwayprint = colorwayprint.replace(colorwayprint[-13:],"")
						embedcolorway = f"JORDAN 1 LOW\n{str.upper(colorwayprint)}"
						print(Fore.MAGENTA + f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]"+ log + Fore.GREEN + f"[ZALANDO][PRODUCT - JORDAN LOW {str.upper(colorwayprint)}]")
						jordan1low = ["https://www.zalando.de/jordan-air-1-sneaker-low-","https://www.zalando.at/jordan-air-1-sneaker-low-","https://wwww.zalando.ch/jordan-air-1-sneaker-low-","https://www.zalando.nl/jordan-air-1-sneakers-laag-","https://www.zalando.be/jordan-air-1-sneakers-laag-","https://www.zalando.fr/jordan-air-1-baskets-basses-","https://www.zalando.it/jordan-air-1-sneakers-basse-","https://www.zalando.es/jordan-air-1-zapatillas-","https://www.zalando.co.uk/jordan-air-1-trainers-","https://www.zalando.se/jordan-air-1-sneakers-","https://www.zalando.no/jordan-air-1-joggesko-","https://www.zalando.dk/jordan-air-1-sneakers-","https://www.zalando.fi/jordan-air-1-matalavartiset-tennarit-","https://www.zalando.pl/jordan-air-1-sneakersy-niskie-","https://www.zalando.cz/jordan-air-1-tenisky-"]
						for i in range(len(jordan1low)):
							newlinks.append(jordan1low[i]+colorway)
					else:
						hypedproduct = 1
						colorwayprint = colorway.replace("-"," ").replace(".html","").replace("?_rfl=en","")
						colorwayprint = colorwayprint.replace(colorwayprint[-13:],"")
						embedcolorway = f"JORDAN 1 LOW\n{str.upper(colorwayprint)}"
						colorway = link.split(".html")[0][-13:] + ".html"
						print(Fore.MAGENTA + f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]"+ log + Fore.GREEN + f"[ZALANDO][PRODUCT - JORDAN LOW {str.upper(colorwayprint)}]")
						jordan1low = ["https://www.zalando.de/jordan-air-1-sneaker-low-","https://www.zalando.at/jordan-air-1-sneaker-low-","https://wwww.zalando.ch/jordan-air-1-sneaker-low-","https://www.zalando.nl/jordan-air-1-sneakers-laag-","https://www.zalando.be/jordan-air-1-sneakers-laag-","https://www.zalando.fr/jordan-air-1-baskets-basses-","https://www.zalando.it/jordan-air-1-sneakers-basse-","https://www.zalando.es/jordan-air-1-zapatillas-","https://www.zalando.co.uk/jordan-air-1-trainers-","https://www.zalando.se/jordan-air-1-sneakers-","https://www.zalando.no/jordan-air-1-joggesko-","https://www.zalando.dk/jordan-air-1-sneakers-","https://www.zalando.fi/jordan-air-1-matalavartiset-tennarit-","https://www.zalando.pl/jordan-air-1-sneakersy-niskie-","https://www.zalando.cz/jordan-air-1-tenisky-"]
						for i in range(len(jordan1low)):
							newlinks.append(jordan1low[i]+colorway)

			if "high" in link or "hoog" in link or "montantes" in link or "akte" in link or "altas" in link or "hoega" in link or "hoeye" in link or "hoye" in link or "korkeavartiset" in link:
				if "-retro-" in link:
					if testcolorway in link:
						hypedproduct = 1
						colorwayprint = colorway.replace("-"," ").replace(".html","").replace("?_rfl=en","")
						colorwayprint = colorwayprint.replace(colorwayprint[-13:],"")
						embedcolorway = f"JORDAN 1 HIGH\n{str.upper(colorwayprint)}"
						print(Fore.MAGENTA + f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]"+ log + Fore.GREEN + f"[ZALANDO][PRODUCT - JORDAN 1 HIGH {str.upper(colorwayprint)}]")
						jordan1high = ["https://www.zalando.de/jordan-air-1-retro-sneaker-high-","https://www.zalando.at/jordan-air-1-retro-sneaker-high-","https://wwww.zalando.ch/jordan-air-1-retro-sneaker-high-","https://www.zalando.nl/jordan-air-1-retro-sneakers-hoog-","https://www.zalando.be/jordan-air-1-retro-sneakers-hoog-","https://www.zalando.fr/jordan-air-1-retro-baskets-montantes-","https://www.zalando.it/jordan-air-1-retro-sneakers-alte-","https://www.zalando.es/jordan-air-1-retro-zapatillas-altas-","https://www.zalando.co.uk/jordan-air-1-retro-high-top-trainers-","https://www.zalando.se/jordan-air-1-retro-hoega-sneakers-","https://www.zalando.no/jordan-air-1-retro-hoeye-joggesko-","https://www.zalando.dk/jordan-air-1-retro-sneakers-high-","https://www.zalando.fi/jordan-air-1-retro-korkeavartiset-tennarit-","https://www.zalando.pl/jordan-air-1-retro-sneakersy-wysokie-","https://www.zalando.cz/jordan-air-1-retro-vysoke-tenisky-"]
						for i in range(len(jordan1high)):
							newlinks.append(jordan1high[i]+colorway)
					else:
						hypedproduct = 1
						colorwayprint = colorway.replace("-"," ").replace(".html","").replace("?_rfl=en","")
						colorwayprint = colorwayprint.replace(colorwayprint[-13:],"")
						embedcolorway = f"JORDAN 1 HIGH\n{str.upper(colorwayprint)}"
						colorway = link.split(".html")[0][-13:] + ".html"
						print(Fore.MAGENTA + f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]"+ log + Fore.GREEN + f"[ZALANDO][PRODUCT - JORDAN 1 HIGH {str.upper(colorwayprint)}]")
						jordan1high = ["https://www.zalando.de/jordan-air-1-retro-sneaker-high-","https://www.zalando.at/jordan-air-1-retro-sneaker-high-","https://wwww.zalando.ch/jordan-air-1-retro-sneaker-high-","https://www.zalando.nl/jordan-air-1-retro-sneakers-hoog-","https://www.zalando.be/jordan-air-1-retro-sneakers-hoog-","https://www.zalando.fr/jordan-air-1-retro-baskets-montantes-","https://www.zalando.it/jordan-air-1-retro-sneakers-alte-","https://www.zalando.es/jordan-air-1-retro-zapatillas-altas-","https://www.zalando.co.uk/jordan-air-1-retro-high-top-trainers-","https://www.zalando.se/jordan-air-1-retro-hoega-sneakers-","https://www.zalando.no/jordan-air-1-retro-hoeye-joggesko-","https://www.zalando.dk/jordan-air-1-retro-sneakers-high-","https://www.zalando.fi/jordan-air-1-retro-korkeavartiset-tennarit-","https://www.zalando.pl/jordan-air-1-retro-sneakersy-wysokie-","https://www.zalando.cz/jordan-air-1-retro-vysoke-tenisky-"]
						for i in range(len(jordan1high)):
							newlinks.append(jordan1high[i]+colorway)

			if "-mid-" in link:
				if "-se-" in link:
					if testcolorway in link:
						hypedproduct = 1
						colorwayprint = colorway.replace("-"," ").replace(".html","").replace("?_rfl=en","")
						colorwayprint = colorwayprint.replace(colorwayprint[-13:],"")
						embedcolorway = f"JORDAN 1 MID SE\n{str.upper(colorwayprint)}"
						print(Fore.MAGENTA + f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]"+ log + Fore.GREEN + f"[ZALANDO][PRODUCT - JORDAN 1 MID SE {str.upper(colorwayprint)}]")
						jordan1midse = ["https://www.zalando.de/jordan-air-1-mid-se-sneaker-high-","https://www.zalando.at/jordan-air-1-mid-se-sneaker-high-","https://wwww.zalando.ch/jordan-air-1-mid-se-sneaker-high-","https://www.zalando.nl/jordan-air-1-mid-se-sneakers-hoog-","https://www.zalando.be/jordan-air-1-mid-se-sneakers-hoog-","https://www.zalando.fr/jordan-air-1-mid-se-baskets-montantes-","https://www.zalando.it/jordan-air-1-mid-se-sneakers-alte-","https://www.zalando.es/jordan-air-1-mid-se-zapatillas-altas-","https://www.zalando.co.uk/jordan-air-1-mid-se-high-top-trainers-","https://www.zalando.se/jordan-air-1-mid-se-hoega-sneakers-","https://www.zalando.no/jordan-air-1-mid-se-hoeye-joggesko-","https://www.zalando.dk/jordan-air-1-mid-se-sneakers-high-","https://www.zalando.fi/jordan-air-1-mid-se-korkeavartiset-tennarit-","https://www.zalando.pl/jordan-air-1-mid-se-sneakersy-wysokie-","https://www.zalando.cz/jordan-air-1-mid-se-vysoke-tenisky-"]
						for i in range(len(jordan1midse)):
							newlinks.append(jordan1midse[i]+colorway)
					else:
						hypedproduct = 1
						colorwayprint = colorway.replace("-"," ").replace(".html","").replace("?_rfl=en","")
						colorwayprint = colorwayprint.replace(colorwayprint[-13:],"")
						embedcolorway = f"JORDAN 1 MID SE\n{str.upper(colorwayprint)}"
						colorway = link.split(".html")[0][-13:] + ".html"
						print(Fore.MAGENTA + f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]"+ log + Fore.GREEN + f"[ZALANDO][PRODUCT - JORDAN 1 MID SE {str.upper(colorwayprint)}]")
						jordan1midse = ["https://www.zalando.de/jordan-air-1-mid-se-sneaker-high-","https://www.zalando.at/jordan-air-1-mid-se-sneaker-high-","https://wwww.zalando.ch/jordan-air-1-mid-se-sneaker-high-","https://www.zalando.nl/jordan-air-1-mid-se-sneakers-hoog-","https://www.zalando.be/jordan-air-1-mid-se-sneakers-hoog-","https://www.zalando.fr/jordan-air-1-mid-se-baskets-montantes-","https://www.zalando.it/jordan-air-1-mid-se-sneakers-alte-","https://www.zalando.es/jordan-air-1-mid-se-zapatillas-altas-","https://www.zalando.co.uk/jordan-air-1-mid-se-high-top-trainers-","https://www.zalando.se/jordan-air-1-mid-se-hoega-sneakers-","https://www.zalando.no/jordan-air-1-mid-se-hoeye-joggesko-","https://www.zalando.dk/jordan-air-1-mid-se-sneakers-high-","https://www.zalando.fi/jordan-air-1-mid-se-korkeavartiset-tennarit-","https://www.zalando.pl/jordan-air-1-mid-se-sneakersy-wysokie-","https://www.zalando.cz/jordan-air-1-mid-se-vysoke-tenisky-"]
						for i in range(len(jordan1midse)):
							newlinks.append(jordan1midse[i]+colorway)
				else:
					if testcolorway in link:
						hypedproduct = 1
						colorwayprint = colorway.replace("-"," ").replace(".html","")
						colorwayprint = colorwayprint.replace(colorwayprint[-13:],"")
						embedcolorway = f"JORDAN 1 MID\n{str.upper(colorwayprint)}"
						print(Fore.MAGENTA + f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]"+ log + Fore.GREEN + f"[ZALANDO][PRODUCT - JORDAN 1 MID {str.upper(colorwayprint)}]")
						jordan1mid = ["https://www.zalando.de/jordan-air-1-mid-sneaker-high-","https://www.zalando.at/jordan-air-1-mid-sneaker-high-","https://wwww.zalando.ch/jordan-air-1-mid-sneaker-high-","https://www.zalando.nl/jordan-air-1-mid-sneakers-hoog-","https://www.zalando.be/jordan-air-1-mid-sneakers-hoog-","https://www.zalando.fr/jordan-air-1-mid-baskets-montantes-","https://www.zalando.it/jordan-air-1-mid-sneakers-alte-","https://www.zalando.es/jordan-air-1-mid-zapatillas-altas-","https://www.zalando.co.uk/jordan-air-1-mid-high-top-trainers-","https://www.zalando.se/jordan-air-1-mid-hoega-sneakers-","https://www.zalando.no/jordan-air-1-mid-hoeye-joggesko-","https://www.zalando.dk/jordan-air-1-mid-sneakers-high-","https://www.zalando.fi/jordan-air-1-mid-korkeavartiset-tennarit-","https://www.zalando.pl/jordan-air-1-mid-sneakersy-wysokie-","https://www.zalando.cz/jordan-air-1-mid-vysoke-tenisky-"]
						for i in range(len(jordan1mid)):
							newlinks.append(jordan1mid[i]+colorway)
					else:
						hypedproduct = 1
						colorwayprint = colorway.replace("-"," ").replace(".html","")
						colorwayprint = colorwayprint.replace(colorwayprint[-13:],"")
						embedcolorway = f"JORDAN 1 MID\n{str.upper(colorwayprint)}"
						colorway = link.split(".html")[0][-13:] + ".html"
						print(Fore.MAGENTA + f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]"+ log + Fore.GREEN + f"[ZALANDO][PRODUCT - JORDAN 1 MID {str.upper(colorwayprint)}]")
						jordan1mid = ["https://www.zalando.de/jordan-air-1-mid-sneaker-high-","https://www.zalando.at/jordan-air-1-mid-sneaker-high-","https://wwww.zalando.ch/jordan-air-1-mid-sneaker-high-","https://www.zalando.nl/jordan-air-1-mid-sneakers-hoog-","https://www.zalando.be/jordan-air-1-mid-sneakers-hoog-","https://www.zalando.fr/jordan-air-1-mid-baskets-montantes-","https://www.zalando.it/jordan-air-1-mid-sneakers-alte-","https://www.zalando.es/jordan-air-1-mid-zapatillas-altas-","https://www.zalando.co.uk/jordan-air-1-mid-high-top-trainers-","https://www.zalando.se/jordan-air-1-mid-hoega-sneakers-","https://www.zalando.no/jordan-air-1-mid-hoeye-joggesko-","https://www.zalando.dk/jordan-air-1-mid-sneakers-high-","https://www.zalando.fi/jordan-air-1-mid-korkeavartiset-tennarit-","https://www.zalando.pl/jordan-air-1-mid-sneakersy-wysokie-","https://www.zalando.cz/jordan-air-1-mid-vysoke-tenisky-"]
						for i in range(len(jordan1mid)):
							newlinks.append(jordan1mid[i]+colorway)	

		elif "nike-sportswear-dunk-retro" in link:
			if "high" in link or "hoog" in link or "montantes" in link or "akte" in link or "altas" in link or "hoega" in link or "hoeye" in link or "hoye" in link or "korkeavartiset" in link:
				if testcolorway in link:
					hypedproduct = 1
					colorwayprint = colorway.replace("-"," ").replace(".html","").replace("?_rfl=en","")
					colorwayprint = colorwayprint.replace(colorwayprint[-13:],"")
					embedcolorway = f"DUNK HIGH\n{str.upper(colorwayprint)}"
					print(Fore.MAGENTA + f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]"+ log + Fore.GREEN + f"[ZALANDO][PRODUCT - DUNK HIGH {str.upper(colorwayprint)}]")
					dunkhigh = ["https://www.zalando.de/nike-sportswear-dunk-retro-sneaker-high-","https://www.zalando.at/nike-sportswear-dunk-retro-sneaker-high-","https://www.zalando.ch/nike-sportswear-dunk-retro-sneaker-high-","https://www.zalando.nl/nike-sportswear-dunk-retro-sneakers-hoog-","https://www.zalando.be/nike-sportswear-dunk-retro-sneakers-hoog-","https://www.zalando.fr/nike-sportswear-dunk-retro-baskets-montantes-","https://www.zalando.it/nike-sportswear-dunk-retro-sneakers-alte-","https://www.zalando.es/nike-sportswear-dunk-retro-zapatillas-altas-","https://www.zalando.co.uk/nike-sportswear-dunk-retro-high-top-trainers-","https://www.zalando.se/nike-sportswear-dunk-retro-hoega-sneakers-","https://www.zalando.no/nike-sportswear-dunk-retro-hoeye-joggesko-","https://www.zalando.dk/nike-sportswear-dunk-retro-sneakers-high-","https://www.zalando.fi/nike-sportswear-dunk-retro-korkeavartiset-tennarit-","https://www.zalando.pl/nike-sportswear-dunk-retro-sneakersy-wysokie-","https://www.zalando.cz/nike-sportswear-dunk-retro-vysoke-tenisky-"]
					for i in range(len(dunkhigh)):
						newlinks.append(dunkhigh[i]+colorway)
				else:
					hypedproduct = 1
					colorwayprint = colorway.replace("-"," ").replace(".html","").replace("?_rfl=en","")
					colorwayprint = colorwayprint.replace(colorwayprint[-13:],"")
					embedcolorway = f"DUNK HIGH\n{str.upper(colorwayprint)}"
					colorway = link.split(".html")[0][-13:] + ".html"
					print(Fore.MAGENTA + f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]"+ log + Fore.GREEN + f"[ZALANDO][PRODUCT - DUNK HIGH {str.upper(colorwayprint)}]")
					dunkhigh = ["https://www.zalando.de/nike-sportswear-dunk-retro-sneaker-high-","https://www.zalando.at/nike-sportswear-dunk-retro-sneaker-high-","https://www.zalando.ch/nike-sportswear-dunk-retro-sneaker-high-","https://www.zalando.nl/nike-sportswear-dunk-retro-sneakers-hoog-","https://www.zalando.be/nike-sportswear-dunk-retro-sneakers-hoog-","https://www.zalando.fr/nike-sportswear-dunk-retro-baskets-montantes-","https://www.zalando.it/nike-sportswear-dunk-retro-sneakers-alte-","https://www.zalando.es/nike-sportswear-dunk-retro-zapatillas-altas-","https://www.zalando.co.uk/nike-sportswear-dunk-retro-high-top-trainers-","https://www.zalando.se/nike-sportswear-dunk-retro-hoega-sneakers-","https://www.zalando.no/nike-sportswear-dunk-retro-hoeye-joggesko-","https://www.zalando.dk/nike-sportswear-dunk-retro-sneakers-high-","https://www.zalando.fi/nike-sportswear-dunk-retro-korkeavartiset-tennarit-","https://www.zalando.pl/nike-sportswear-dunk-retro-sneakersy-wysokie-","https://www.zalando.cz/nike-sportswear-dunk-retro-vysoke-tenisky-"]
					for i in range(len(dunkhigh)):
						newlinks.append(dunkhigh[i]+colorway)

			elif "low" in link or "laag" in link or "basses" in link or "basse" in link or "matalavartiset" in link or "niskie" in link:
				if testcolorway in link:
					hypedproduct = 1
					colorwayprint = colorway.replace("-"," ").replace(".html","").replace("?_rfl=en","")
					colorwayprint = colorwayprint.replace(colorwayprint[-13:],"")
					embedcolorway = f"DUNK LOW\n{str.upper(colorwayprint)}"
					print(Fore.MAGENTA + f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]"+ log + Fore.GREEN + f"[ZALANDO][PRODUCT - DUNK LOW {str.upper(colorwayprint)}]")
					dunklow = ["https://www.zalando.de/nike-sportswear-dunk-retro-sneaker-low-","https://www.zalando.at/nike-sportswear-dunk-retro-sneaker-low-","https://www.zalando.ch/nike-sportswear-dunk-retro-sneaker-low-","https://www.zalando.nl/nike-sportswear-dunk-retro-sneakers-laag-","https://www.zalando.be/nike-sportswear-dunk-retro-sneakers-laag-","https://www.zalando.fr/nike-sportswear-dunk-retro-baskets-basses-","https://www.zalando.it/nike-sportswear-dunk-retro-sneakers-basse-","https://www.zalando.es/nike-sportswear-dunk-retro-zapatillas-","https://www.zalando.co.uk/nike-sportswear-dunk-retro-trainers-","https://www.zalando.se/nike-sportswear-dunk-retro-sneakers-","https://www.zalando.no/nike-sportswear-dunk-retro-joggesko-","https://www.zalando.dk/nike-sportswear-dunk-retro-sneakers-","https://www.zalando.fi/nike-sportswear-dunk-retro-matalavartiset-tennarit-","https://www.zalando.pl/nike-sportswear-dunk-retro-sneakersy-niskie-","https://www.zalando.cz/nike-sportswear-dunk-retro-tenisky-"]
					for i in range(len(dunklow)):
						newlinks.append(dunklow[i]+colorway)
				else:
					hypedproduct = 1
					colorwayprint = colorway.replace("-"," ").replace(".html","").replace("?_rfl=en","")
					colorwayprint = colorwayprint.replace(colorwayprint[-13:],"")
					embedcolorway = f"DUNK LOW\n{str.upper(colorwayprint)}"
					colorway = link.split(".html")[0][-13:] + ".html"
					print(Fore.MAGENTA + f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]"+ log + Fore.GREEN + f"[ZALANDO][PRODUCT - DUNK LOW {str.upper(colorwayprint)}]")
					dunklow = ["https://www.zalando.de/nike-sportswear-dunk-retro-sneaker-low-","https://www.zalando.at/nike-sportswear-dunk-retro-sneaker-low-","https://www.zalando.ch/nike-sportswear-dunk-retro-sneaker-low-","https://www.zalando.nl/nike-sportswear-dunk-retro-sneakers-laag-","https://www.zalando.be/nike-sportswear-dunk-retro-sneakers-laag-","https://www.zalando.fr/nike-sportswear-dunk-retro-baskets-basses-","https://www.zalando.it/nike-sportswear-dunk-retro-sneakers-basse-","https://www.zalando.es/nike-sportswear-dunk-retro-zapatillas-","https://www.zalando.co.uk/nike-sportswear-dunk-retro-trainers-","https://www.zalando.se/nike-sportswear-dunk-retro-sneakers-","https://www.zalando.no/nike-sportswear-dunk-retro-joggesko-","https://www.zalando.dk/nike-sportswear-dunk-retro-sneakers-","https://www.zalando.fi/nike-sportswear-dunk-retro-matalavartiset-tennarit-","https://www.zalando.pl/nike-sportswear-dunk-retro-sneakersy-niskie-","https://www.zalando.cz/nike-sportswear-dunk-retro-tenisky-"]
					for i in range(len(dunklow)):
						newlinks.append(dunklow[i]+colorway)

		elif "jordan-air-jordan-1" in link:
			if "mid" in link:
				if "high" in link or "hoog" in link or "montantes" in link or "akte" in link or "altas" in link or "hoega" in link or "hoeye" in link or "hoye" in link or "korkeavartiset" in link:
					if testcolorway in link:
						hypedproduct = 1
						colorwayprint = colorway.replace("-"," ").replace(".html","").replace("?_rfl=en","")
						colorwayprint = colorwayprint.replace(colorwayprint[-13:],"")
						embedcolorway = f"JORDAN 1 MID\n{str.upper(colorwayprint)}"
						print(Fore.MAGENTA + f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]"+ log + Fore.GREEN + f"[ZALANDO][PRODUCT - JORDAN 1 MID {str.upper(colorwayprint)}]")
						aj1mid = ["https://www.zalando.de/jordan-air-jordan-1-mid-sneaker-high-","https://www.zalando.at/jordan-air-jordan-1-mid-sneaker-high-","https://www.zalando.ch/jordan-air-jordan-1-mid-sneaker-high-","https://www.zalando.nl/jordan-air-jordan-1-mid-sneakers-hoog-","https://www.zalando.be/jordan-air-jordan-1-mid-sneakers-hoog-","https://www.zalando.fr/jordan-air-jordan-1-mid-baskets-montantes-","https://www.zalando.it/jordan-air-jordan-1-mid-sneakers-alte-","https://www.zalando.es/jordan-air-jordan-1-mid-zapatillas-altas-","https://www.zalando.co.uk/jordan-air-jordan-1-mid-high-top-trainers-","https://www.zalando.se/jordan-air-jordan-1-mid-hoega-sneakers-","https://www.zalando.no/jordan-air-jordan-1-mid-hoeye-joggesko-","https://www.zalando.dk/jordan-air-jordan-1-mid-sneakers-high-","https://www.zalando.fi/jordan-air-jordan-1-mid-korkeavartiset-tennarit-","https://www.zalando.pl/jordan-air-jordan-1-mid-sneakersy-wysokie-","https://www.zalando.cz/jordan-air-jordan-1-mid-vysoke-tenisky-"]
						for i in range(len(aj1mid)):
							newlinks.append(aj1mid[i]+colorway)
					else:
						hypedproduct = 1
						colorwayprint = colorway.replace("-"," ").replace(".html","").replace("?_rfl=en","")
						colorwayprint = colorwayprint.replace(colorwayprint[-13:],"")
						embedcolorway = f"JORDAN 1 MID\n{str.upper(colorwayprint)}"
						colorway = link.split(".html")[0][-13:] + ".html"
						print(Fore.MAGENTA + f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]"+ log + Fore.GREEN + f"[ZALANDO][PRODUCT - JORDAN 1 MID {str.upper(colorwayprint)}]")
						aj1mid = ["https://www.zalando.de/jordan-air-jordan-1-mid-sneaker-high-","https://www.zalando.at/jordan-air-jordan-1-mid-sneaker-high-","https://www.zalando.ch/jordan-air-jordan-1-mid-sneaker-high-","https://www.zalando.nl/jordan-air-jordan-1-mid-sneakers-hoog-","https://www.zalando.be/jordan-air-jordan-1-mid-sneakers-hoog-","https://www.zalando.fr/jordan-air-jordan-1-mid-baskets-montantes-","https://www.zalando.it/jordan-air-jordan-1-mid-sneakers-alte-","https://www.zalando.es/jordan-air-jordan-1-mid-zapatillas-altas-","https://www.zalando.co.uk/jordan-air-jordan-1-mid-high-top-trainers-","https://www.zalando.se/jordan-air-jordan-1-mid-hoega-sneakers-","https://www.zalando.no/jordan-air-jordan-1-mid-hoeye-joggesko-","https://www.zalando.dk/jordan-air-jordan-1-mid-sneakers-high-","https://www.zalando.fi/jordan-air-jordan-1-mid-korkeavartiset-tennarit-","https://www.zalando.pl/jordan-air-jordan-1-mid-sneakersy-wysokie-","https://www.zalando.cz/jordan-air-jordan-1-mid-vysoke-tenisky-"]
						for i in range(len(aj1mid)):
							newlinks.append(aj1mid[i]+colorway)
			elif "zoom" in link:
				if "high" in link or "hoog" in link or "montantes" in link or "akte" in link or "altas" in link or "hoega" in link or "hoeye" in link or "hoye" in link or "korkeavartiset" in link:
					if testcolorway in link:
						hypedproduct = 1
						colorwayprint = colorway.replace("-"," ").replace(".html","").replace("?_rfl=en","")
						colorwayprint = colorwayprint.replace(colorwayprint[-13:],"")
						embedcolorway = f"JORDAN 1 MID\n{str.upper(colorwayprint)}"
						print(Fore.MAGENTA + f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]"+ log + Fore.GREEN + f"[ZALANDO][PRODUCT - JORDAN 1 MID {str.upper(colorwayprint)}]")
						aj1zoom = ["https://www.zalando.de/jordan-air-jordan-1-zoom-air-comfort-sneaker-high-","https://www.zalando.at/jordan-air-jordan-1-zoom-air-comfort-sneaker-high-","https://www.zalando.ch/jordan-air-jordan-1-zoom-air-comfort-sneaker-high-","https://www.zalando.nl/jordan-air-jordan-1-zoom-air-comfort-sneakers-hoog-","https://www.zalando.be/jordan-air-jordan-1-zoom-air-comfort-sneakers-hoog-","https://www.zalando.fr/jordan-air-jordan-1-zoom-air-comfort-baskets-montantes-","https://www.zalando.it/jordan-air-jordan-1-zoom-air-comfort-sneakers-alte-","https://www.zalando.es/jordan-air-jordan-1-zoom-air-comfort-zapatillas-altas-","https://www.zalando.co.uk/jordan-air-jordan-1-zoom-air-comfort-high-top-trainers-","https://www.zalando.se/jordan-air-jordan-1-zoom-air-comfort-hoega-sneakers-","https://www.zalando.no/jordan-air-jordan-1-zoom-air-comfort-hoeye-joggesko-","https://www.zalando.dk/jordan-air-jordan-1-zoom-air-comfort-sneakers-high-","https://www.zalando.fi/jordan-air-jordan-1-zoom-air-comfort-korkeavartiset-tennarit-","https://www.zalando.pl/jordan-air-jordan-1-zoom-air-comfort-sneakersy-wysokie-","https://www.zalando.cz/jordan-air-jordan-1-zoom-air-comfort-vysoke-tenisky-"]
						for i in range(len(aj1zoom)):
							newlinks.append(aj1zoom[i]+colorway)
					else:
						hypedproduct = 1
						colorwayprint = colorway.replace("-"," ").replace(".html","").replace("?_rfl=en","")
						colorwayprint = colorwayprint.replace(colorwayprint[-13:],"")
						embedcolorway = f"JORDAN 1 MID\n{str.upper(colorwayprint)}"
						colorway = link.split(".html")[0][-13:] + ".html"
						print(Fore.MAGENTA + f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]"+ log + Fore.GREEN + f"[ZALANDO][PRODUCT - JORDAN 1 MID {str.upper(colorwayprint)}]")
						aj1zoom = ["https://www.zalando.de/jordan-air-jordan-1-zoom-air-comfort-sneaker-high-","https://www.zalando.at/jordan-air-jordan-1-zoom-air-comfort-sneaker-high-","https://www.zalando.ch/jordan-air-jordan-1-zoom-air-comfort-sneaker-high-","https://www.zalando.nl/jordan-air-jordan-1-zoom-air-comfort-sneakers-hoog-","https://www.zalando.be/jordan-air-jordan-1-zoom-air-comfort-sneakers-hoog-","https://www.zalando.fr/jordan-air-jordan-1-zoom-air-comfort-baskets-montantes-","https://www.zalando.it/jordan-air-jordan-1-zoom-air-comfort-sneakers-alte-","https://www.zalando.es/jordan-air-jordan-1-zoom-air-comfort-zapatillas-altas-","https://www.zalando.co.uk/jordan-air-jordan-1-zoom-air-comfort-high-top-trainers-","https://www.zalando.se/jordan-air-jordan-1-zoom-air-comfort-hoega-sneakers-","https://www.zalando.no/jordan-air-jordan-1-zoom-air-comfort-hoeye-joggesko-","https://www.zalando.dk/jordan-air-jordan-1-zoom-air-comfort-sneakers-high-","https://www.zalando.fi/jordan-air-jordan-1-zoom-air-comfort-korkeavartiset-tennarit-","https://www.zalando.pl/jordan-air-jordan-1-zoom-air-comfort-sneakersy-wysokie-","https://www.zalando.cz/jordan-air-jordan-1-zoom-air-comfort-vysoke-tenisky-"]
						for i in range(len(aj1zoom)):
							newlinks.append(aj1zoom[i]+colorway)
		else:
			hypedproduct = 0

		if hypedproduct == 1:

			newlinks1, newlinks2 = split_list(newlinks)
			countryflag1, countryflag2 = split_list(countryflag)
			country1, country2 = split_list(country)

			for i in range(len(newlinks1)):
				newlinks1[i] = f"[{country1[i]}]({newlinks1[i]})"

			for i in range(len(newlinks2)):
				newlinks2[i] = f"[{country2[i]}]({newlinks2[i]})"

			embedlinks1 = "\n".join("{0} - {1}".format(x,y) for x,y in zip(countryflag1,newlinks1))
			embedlinks2 = "\n".join("{0} - {1}".format(x,y) for x,y in zip(countryflag2,newlinks2))
			if embedcolorway[-1:] == " ":
				lentext = len(embedcolorway)
				embedcolorway = embedcolorway[:(lentext-1)]

			shoepic = souplink.find("meta", {"property":"og:image"})["content"]

			embed=discord.Embed(title="Zalando Region Links",description= "*"+embedcolorway+"*", color=setembedcolor)
			for i in range(2):
				if i == 0:
					if len(embedlinks1) < 1024:
						embed.add_field(name="Links", value=embedlinks1, inline=False)
					else:
						newlinks5, newlinks6 = split_list(newlinks1)
						countryflag5, countryflag6 = split_list(countryflag1)
						country5, country6 = split_list(country1)

						embedlinks5 = "\n".join("{0} - {1}".format(x,y) for x,y in zip(countryflag5,newlinks5))
						embedlinks6 = "\n".join("{0} - {1}".format(x,y) for x,y in zip(countryflag6,newlinks6))

						for m in range(2):
							if m == 0:
								embed.add_field(name="Links", value=embedlinks5, inline=False)

							if m == 1:
								embed.add_field(name="\xad", value=embedlinks6, inline=False)
			
				if i == 1:
					if len(embedlinks2) < 1024:
						embed.add_field(name="\xad", value=embedlinks2, inline=False)
					else:
						newlinks3, newlinks4 = split_list(newlinks2)
						countryflag3, countryflag4 = split_list(countryflag2)
						country3, country4 = split_list(country2)

						embedlinks3 = "\n".join("{0} - {1}".format(x,y) for x,y in zip(countryflag3,newlinks3))
						embedlinks4 = "\n".join("{0} - {1}".format(x,y) for x,y in zip(countryflag4,newlinks4))

						for j in range(2):
							if j == 0:
								embed.add_field(name="\xad", value=embedlinks3, inline=False)

							if j == 1:
								embed.add_field(name="\xad", value=embedlinks4, inline=False)
			embed.set_thumbnail(url=shoepic)
			embed.set_footer(text=setfootertextzalando, icon_url=setfooterimage)
			await ctx.send(embed=embed)
		else:
			embed=discord.Embed(title="Error Scraping Zalando Links", color=0xFF0000)
			embed.add_field(name="Error", value="Country not supported to scrape from, try another country link!", inline=False)
			embed.add_field(name="Important", value="Only works for AJ1 Mids, AJ1 High, Dunk Low, Dunk High, AJ1 Low, AJ1 Low SE", inline=False)
			embed.set_footer(text=setfootertextzalando, icon_url=setfooterimage)
			await ctx.send(embed=embed)
	except TypeError:
			embed=discord.Embed(title="Error Scraping Zalando Links", color=0xFF0000)
			embed.add_field(name="Error", value="Site is not live!", inline=False)
			embed.set_footer(text=setfootertextzalando, icon_url=setfooterimage)
			await ctx.send(embed=embed)


@bot.command()
async def zalandohelp(context):
	embed=discord.Embed(title="Zalando HELP", color=setembedcolor)
	embed.add_field(name="Stock/SKU Scraper", value="?zalando  <full link here>", inline=False)
	embed.add_field(name="SKU Scraper", value="?zalandopid  <full link here>", inline=False)
	embed.add_field(name="Link Scraper", value="?zalandolink  <full link here>", inline=False)
	embed.set_footer(text=setfootertextzalando, icon_url=setfooterimage)
	await context.send(embed=embed)


@bot.event
async def on_command_error(ctx, error):
	if isinstance(error, CommandNotFound):
		return
	elif isinstance(error,MissingRequiredArgument):
		embed=discord.Embed(title="Command Error", color=setembedcolor)
		embed.add_field(name="Error", value="Your are missing an argument", inline=True)
		embed.add_field(name="Command - Stock Checker", value="?zalando <link>\n?zalando <zalando main pid>", inline=False)
		embed.add_field(name="Command - PID Scraper", value="?zalandopid <link>\n?zalandopid <zalando main pid>", inline=False)
		embed.set_footer(text=setfootertextzalando, icon_url=setfooterimage)
		await ctx.send(embed=embed)
		return
	raise error


bot.run(bottoken)
