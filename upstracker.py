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
from discord.ext.commands import CommandNotFound,MissingRequiredArgument
import time
import datetime

token = 'YOUR_DISCORD_BOT_TOKEN'

bot = commands.Bot(command_prefix = '?', help_command=None)


@bot.event
async def on_ready():
	print('Bot is ready.')
	pass


setfootertext = "@ScriptingToolsPublic | UPS Order Tracker | <?upshelp>"
setfooterimage = "https://images-ext-1.discordapp.net/external/atwFnJRaXHB0ebXrVSPjVWDXe5hL2OQ0JBWopjGcVCY/https/images-ext-2.discordapp.net/external/gGrbK8FUkmby_Ao8mmH9dZ4RI1cvfkhpUNBlIB46XQE/https/media.discordapp.net/attachments/460974692073734164/680067025493950474/Wcu7EAAAAASUVORK5CYII.png"
setembedcolor = 0x00000
setthumbnail = setfooterimage

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
	test1.set_footer(text=setfootertext, icon_url=setfooterimage)
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
			test1.set_footer(text=setfootertext, icon_url=setfooterimage)
			test1.set_thumbnail(url=setthumbnail)
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
			test1.set_footer(text=setfootertext, icon_url=setfooterimage)
			test1.set_thumbnail(url=setthumbnail)
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
	test1.set_footer(text=setfootertext, icon_url=setfooterimage)
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
	test1.set_footer(text=setfootertext, icon_url=setfooterimage)
	test1.set_thumbnail(url=setthumbnail)
	print('')
	await ctx.send(embed=test1)

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
		embed.set_footer(text=setfootertext, icon_url=setfooterimage)
		await context.send(embed=embed)


@bot.event
async def on_command_error(ctx, error):
	if isinstance(error, CommandNotFound):
		return
	elif isinstance(error,MissingRequiredArgument):
		embed=discord.Embed(title="Command Error", color=setembedcolor)
		embed.add_field(name="Error", value="Your are missing an argument", inline=False)
		embed.add_field(name="Commad Format", value="Make sure tracking numbers are on the next line after ?ups```?ups\n<Tracking NR. 1>\n<Tracking NR. 2>\n<Tracking NR. 3>```", inline=False)
		embed.add_field(name="Max. Track Links", value="Cause of Discord Text limit you can track up to **26 Links**", inline=False)
		embed.add_field(name="Max. Track Numbers", value="Cause of Discord Text limit you can track up to **105 Trackingnumbers**", inline=False)
		embed.set_footer(text=setfootertext, icon_url=setfooterimage)
		await ctx.send(embed=embed)
		return
	raise error

bot.run(token)
