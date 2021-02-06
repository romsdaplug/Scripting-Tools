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
from requests_html import HTML, HTMLSession
import numpy as np

bot = commands.Bot(command_prefix = '?', help_command=None)
bottoken = "NzkyODU1MjY5MjQzMjI0MTQ1.X-jyAg.CD0xNJ37E5n_xt8x96TxCCEb_EY"

@bot.event
async def on_ready():
	print('Bot is ready.')
	pass

def prepend(list, str): 
    # Using format() 
    str += '{0}'
    list = [str.format(i) for i in list] 
    return(list)

def divide_chunks(l, n): 
     
    # looping till length l 
    for i in range(0, len(l), n):  
        yield l[i:i + n] 

@bot.command()
async def restocks(context, *sku):
	track_url = 'https://restocks.de/shop/search?q=' + str(sku) + '&page=1&filters[][range][price][gte]=1'
	r = requests.get(track_url)
	response = r.text
	test = json.loads(response)
	test2 = test['data']

	product_name = test2[0]['name']
	product_id = test2[0]['id']
	product_sku = test2[0]['sku']
	slug = test2[0]['slug']
	product_link = 'https://restocks.de' + slug
	product_price = test2[0]['price']

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
	for i in range(len(resell)):
		if "Notify me" in resell[i]:
			continue
		elif resell[i].find("span", {"class":"price__label__value"}) == None:
			continue
		else:
			try:
				value = resell[i].find("span", {"class":"value"})
				pirce = resell[i].find("span", {"class":"price__label__value"})
				sell = resell[i].find("span", {"class":"sell__method__value"})
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
	rprices = prepend(resaleprice, "R: € ")
	cprices = prepend(consignmentprice, "C: € ")
	data = ",".join("{0}\n{1}".format(x,y) for x,y in zip(rprices,cprices))
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
	embed=discord.Embed(title=shoedesc[:-lenshoesku],description="> *R - Resale Price Payout*\n> *C - Consignment Price Payout*\n"+"> *SKU - " + skuforembed + "*", url=product_link ,color=0x66ffff)
	#embed.add_field(name="SKU",value=str(correctsku[2].text), inline=False)
	for i in range(len(newembed)):
		embed.add_field(name=newembed[i][0],value=newembed[i][1],inline=True)
	embed.set_thumbnail(url=shoepic)
	embed.set_footer(text="Pigeon Helper made by OOS#4315", icon_url="https://cdn.discordapp.com/attachments/797052521582952468/797231957951643668/Pigeon_Proxies3.png")
	await context.send(embed=embed)
	

bot.run(bottoken)











