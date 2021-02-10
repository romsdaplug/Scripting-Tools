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
from discord.ext.commands import CommandNotFound,MissingRequiredArgument

bot = commands.Bot(command_prefix = '?', help_command=None)

bottoken ="Nzk4NTY2ODE4ODEzMDUwOTYw.X_25Tg.Fgr9xvAtE0qkJnmHL_dz4gZ3ofw"

setfootertext = "@ScriptingTools | <?zalandohelp>"
setfooterimage = "https://images-ext-1.discordapp.net/external/atwFnJRaXHB0ebXrVSPjVWDXe5hL2OQ0JBWopjGcVCY/https/images-ext-2.discordapp.net/external/gGrbK8FUkmby_Ao8mmH9dZ4RI1cvfkhpUNBlIB46XQE/https/media.discordapp.net/attachments/460974692073734164/680067025493950474/Wcu7EAAAAASUVORK5CYII.png"
setembedcolor = 0x000000

@bot.event
async def on_ready():
	print('Bot is ready.')
	pass

def check_if_it_is_me(ctx):
	return ctx.message.author.id == 175953718750085121 or ctx.message.author.id == 351639955531104258


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
		embed3.set_footer(text=setfootertext, icon_url=setfooterimage)
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
			embed.set_footer(text=setfootertext, icon_url=setfooterimage)
			if "private" in ctx.channel.type:
				member = ctx.author
				await member.send(embed=embed)
				await test91.delete()
			else:
				await ctx.send(embed=embed
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
				embed.set_footer(text=setfootertext, icon_url=setfooterimage)
				if "private" in ctx.channel.type:
					member = ctx.author
					await member.send(embed=embed)
					await test91.delete()
				else:
					await ctx.send(embed=embed)
					await test91.delete()
			except Exception:
				embed=discord.Embed(title="Zalando Stock Checker - Error", color=setembedcolor)
				embed.add_field(name="Error", value="An error occured. Please check your command or link!", inline=True)
				embed.set_footer(text=setfootertext, icon_url=setfooterimage)
				await ctx.send(embed=embed)
				await test91.delete()
	except IndexError:
		embed=discord.Embed(title="Zalando Stock Checker - Error", color=setembedcolor)
		embed.add_field(name="Error", value="An error occured. Please check your command or link!", inline=False)
		embed.add_field(name="Command Format",value="?zalando <full link here>", inline=False)
		embed.set_footer(text=setfootertext, icon_url=setfooterimage)
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
		embed3.set_footer(text=setfootertext, icon_url=setfooterimage)
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
			discsku = "\n".join(sku)

			embed=discord.Embed(title="Zalando Stock Checker :flag_" + countrycode + ":", description='> ['+(shoename)+']('+link+')', color=setembedcolor)
			embed.set_thumbnail(url=shoepic)
			embed.add_field(name=":straight_ruler: Size", value=discsize, inline=True)
			embed.add_field(name=":pushpin: SKUs", value=discsku, inline=True)
			embed.add_field(name="PID", value="`" + mainpid + "`", inline=False)
			embed.add_field(name="Price", value="`" + str(correctprice) + "`", inline=True)
			embed.add_field(name="Release Date", value="`Live`", inline=True)
			embed.set_footer(text=setfootertext, icon_url=setfooterimage)
			if "private" in ctx.channel.type:
				member = ctx.author
				await member.send(embed=embed)
				await test91.delete()
			else:
				await ctx.send(embed=embed
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
				discsku = "\n".join(sku)

				embed=discord.Embed(title="Zalando Stock Checker :flag_" + countrycode + ":", description='> ['+(shoename)+']('+link+')', color=setembedcolor)
				embed.set_thumbnail(url=shoepic)
				embed.add_field(name=":straight_ruler: Size", value=discsize, inline=True)
				embed.add_field(name=":pushpin: SKUs", value=discsku, inline=True)
				embed.add_field(name="PID", value="`" + mainpid + "`", inline=False)
				embed.add_field(name="Price", value="`"+str(correctprice)+"`", inline=True)
				embed.add_field(name="Release Date", value="`" + releasedate.text + "`", inline=True)
				embed.set_footer(text=setfootertext, icon_url=setfooterimage)
				if "private" in ctx.channel.type:
					member = ctx.author
					await member.send(embed=embed)
					await test91.delete()
				else:
					await ctx.send(embed=embed)
					await test91.delete()
			except Exception:
				embed=discord.Embed(title="Zalando Stock Checker - Error", color=setembedcolor)
				embed.add_field(name="Error", value="An error occured. Please check your command or link!", inline=True)
				embed.set_footer(text=setfootertext, icon_url=setfooterimage)
				await ctx.send(embed=embed)
				await test91.delete()
	except IndexError:
		embed=discord.Embed(title="Zalando PID Scraper - Error", color=setembedcolor)
		embed.add_field(name="Error", value="An error occured. Please check your command or link!", inline=False)
		embed.add_field(name="Command Format",value="?zalandopid <full link here>", inline=False)
		embed.set_footer(text=setfootertext, icon_url=setfooterimage)
		await ctx.send(embed=embed)


@bot.command()
async def zalandohelp(context):
	embed=discord.Embed(title="Zalando HELP", color=setembedcolor)
	embed.add_field(name="Stock/SKU Scraper", value="?zalando  <full link here>", inline=False)
	embed.add_field(name="SKU Scraper", value="?zalandopid  <full link here>", inline=False)
	embed.set_footer(text=setfootertext, icon_url=setfooterimage)
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
		embed.set_footer(text=setfootertext, icon_url=setfooterimage)
		await ctx.send(embed=embed)
		return
	raise error


bot.run(bottoken)
