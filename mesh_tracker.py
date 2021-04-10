import discord
from discord.ext import commands
from datetime import datetime
from colorama import Fore, Back, Style, init
import requests
import json
from pprint import pprint
from discord.ext.commands import CommandNotFound,MissingRequiredArgument
import threading
import time
from collections import Counter
import math

bottoken = "Nzk4NTY2ODE4ODEzMDUwOTYw.X_25Tg.Fgr9xvAtE0qkJnmHL_dz4gZ3ofw"

bot = commands.Bot(command_prefix = '?', help_command=None)


@bot.event
async def on_ready():
	print('Bot is ready.')
	pass

setfootertextorder = "@ScriptingTools | Mesh Order Tracker | <?orderhelp>"
setfooterimage = "https://images-ext-1.discordapp.net/external/atwFnJRaXHB0ebXrVSPjVWDXe5hL2OQ0JBWopjGcVCY/https/images-ext-2.discordapp.net/external/gGrbK8FUkmby_Ao8mmH9dZ4RI1cvfkhpUNBlIB46XQE/https/media.discordapp.net/attachments/460974692073734164/680067025493950474/Wcu7EAAAAASUVORK5CYII.png"
setembedcolor = 0x00000
setthumbnailorder = setfooterimage

def check_if_it_is_me(ctx):
    return ctx.message.author.id == 351639955531104258 or ctx.message.author.id == 272815177659842561 or ctx.message.author.id == 175953718750085121

statusrunning = ["notrunning"]
statusbulkrunning = ["notrunning"]
statusbulkrunningsize = ["notrunning"]


orderstatus = []
tracknrplaced = []
tracknrproc = []
tracknrdes = []
tracknrdel = []
tracknrcan = []
tracknrpostcode = []
tracknronly = []
tracklink = []
trackordernumberdelay = []
trackordernumberdelivered = []
trackordernumberontheway = []
trackordernumbernottrackable = []
trackordernumberreadytopickup = []
tracknrandlink = []

countdelivered = []
countdelay = []
countontheway = []
countnottrackable = []
countreadytopickup = []

getallshoenames = []
shoenameandsize = []
noinfos = []


@bot.command()
@commands.check(check_if_it_is_me)
async def meshreset(ctx):
	orderstatus.clear()
	tracknrdes.clear()
	countdelivered.clear()
	countdelay.clear()
	countontheway.clear()
	countnottrackable.clear()
	countreadytopickup.clear()
	tracknrdel.clear()
	tracknrproc.clear()
	tracknrplaced.clear()
	tracknrpostcode.clear()
	tracknrcan.clear()
	tracknronly.clear()
	tracklink.clear()
	trackordernumberdelay.clear()
	trackordernumberdelivered.clear()
	trackordernumberontheway.clear()
	trackordernumbernottrackable.clear()
	trackordernumberreadytopickup.clear()
	tracknrandlink.clear()
	statusbulkrunning[0] = "notrunning"
	statusrunning[0] = "notrunning"
	statusbulkrunningsize[0] = "notrunning"
	embed=discord.Embed(title="Reset Command", color=setembedcolor)
	embed.add_field(name="Reset", value="Successfully resetted all MESH commands", inline=True)
	embed.set_footer(text=setfootertextorder, icon_url=setfooterimage)
	await ctx.send(embed=embed)

def divide_chunks(l, n): 
      
    for i in range(0, len(l), n):  
        yield l[i:i + n]

def bulk(order,track):

	r = requests.get(order)
	response = r.text
	jsondata = json.loads(response)
	try:
		message = jsondata["message"]
		text = message["text"]
	except:
		text = "nada"

	if 'Your order has been placed.' in text:
		orderstatus.append("placed")
		tracknrplaced.append(track)

	elif 'Order not found' in response:
		orderstatus.append("not found")

	elif 'Your order is currently being processed.' in text:
		orderstatus.append("processed")
		tracknrproc.append(track)

	elif 'Your order has been despatched.' in text or "Your order is out for delivery" in text or "It looks like your order has been delayed by the courier." in text:
		orderstatus.append("despatched")
		if '"trackingURL":null' in response:
			tracking2 = 'N/A'
			tracknrdes.append(track)
		else:
			test = json.loads(response)
			a12 = test['delivery']
			tracking1 = a12['courier']
			tracking2 = a12['trackingURL']
			tracknrdes.append(f"[{track}]({tracking2})")
			if "hermes" in tracking2:
				tracklink.append(tracking2)
				tem = [tracking2.split("https://www.myhermes.co.uk/track.html#/parcel/")[1],track]
				tracknrandlink.append(tem)
		tracknronly.append(track)
		
	elif 'Your order has been delivered' in text:
		orderstatus.append("delivered")
		tracknrdel.append(track)

	elif 'It looks like your order has been cancelled.' in text:
		orderstatus.append("cancelled")
		tracknrcan.append(track)

	elif 'It looks like there was an issue taking payment for this order' in text:
		orderstatus.append("issue")

	elif "Postcode does not match" in response:
		tracknrpostcode.append(track)

def amount(order,track):

	r = requests.get(order)
	response = r.text
	jsondata = json.loads(response)
	try:
		vendors = jsondata["vendors"]
		items = vendors[0]["items"]
		shoesize = items[0]["size"]
		shoename = items[0]["name"]
		allinfos = shoename,shoesize
		getallshoenames.append(shoename)
		shoenameandsize.append(allinfos)
	except KeyError:
		noinfos.append("N/A")


def hermes(tracklink,eppis):

	tracklink = tracklink.split("https://www.myhermes.co.uk/track.html#/parcel/")[1]

	headersbarcode = {
	    'Connection': 'keep-alive',
	    'Pragma': 'no-cache',
	    'Cache-Control': 'no-cache',
	    'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
	    'Accept': 'application/json, text/plain, */*',
	    'apiKey': 'R6xkX4kqK4U7UxqTNraxmXrnPi8cFPZ6',
	    'sec-ch-ua-mobile': '?0',
	    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
	    'Origin': 'https://www.myhermes.co.uk',
	    'Sec-Fetch-Site': 'cross-site',
	    'Sec-Fetch-Mode': 'cors',
	    'Sec-Fetch-Dest': 'empty',
	    'Referer': 'https://www.myhermes.co.uk/',
	    'Accept-Language': 'de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7',
	}

	responsebarcode = requests.get('https://api.hermesworld.co.uk/enterprise-tracking-api/v1/parcels/search/'+tracklink, headers=headersbarcode)
	try:
		barcode = json.loads(responsebarcode.text)
		

		headersinfo = {
		    'Connection': 'keep-alive',
		    'Pragma': 'no-cache',
		    'Cache-Control': 'no-cache',
		    'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
		    'Accept': 'application/json, text/plain, */*',
		    'apiKey': 'R6xkX4kqK4U7UxqTNraxmXrnPi8cFPZ6',
		    'sec-ch-ua-mobile': '?0',
		    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
		    'Origin': 'https://www.myhermes.co.uk',
		    'Sec-Fetch-Site': 'cross-site',
		    'Sec-Fetch-Mode': 'cors',
		    'Sec-Fetch-Dest': 'empty',
		    'Referer': 'https://www.myhermes.co.uk/',
		    'Accept-Language': 'de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7',
		}

		paramsinfo = (
		    ('uniqueIds', barcode[0]),
		)

		responseinfo = requests.get('https://api.hermesworld.co.uk/enterprise-tracking-api/v1/parcels/', headers=headersinfo, params=paramsinfo)
		responseinfojson = json.loads(responseinfo.text)
		results = responseinfojson["results"]
		trackingEvents = results[0]["trackingEvents"]
		trackingStage = trackingEvents[0]["trackingStage"]
		description = trackingStage["description"]

		if description == "Delivered":
			countdelivered.append(tracklink)
		elif description == "Info Exception":
			countdelay.append(tracklink)
		elif description == "On it's way" or description == "We got it" or description == "Courier has it":
			countontheway.append(tracklink)
		elif description == "We've not got it":
			countreadytopickup.append(tracklink)
	except IndexError:
		countnottrackable.append(tracklink)

@bot.command()
async def order(ctx, store, postcode, orderno: int):
	lines = ctx.message.content.splitlines()
	if len(lines) > 1:
		lines.pop(0)
	if "ORDER" in lines[0]:
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
		store = "footpatrol"
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
	elif store == "jdmy" or store == "jdsportsmy":
		store = "jdsports"
		region = "my"

	if statusrunning[0] == "notrunning":
		for i in lines:
			statusrunning[0] = "running"
			try:
				base_url = 'https://data.smartagent.io/v1/jdsports/track-my-order'
				track_url = ''
				correctordernr = str(i).replace(" ","")
				track_url = base_url+'?orderNumber='+correctordernr+'&fascia='+store+region+'&postcode='+str(postcode)
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
				color = 0x000000
				if 'Your order is currently being processed.' in response:
					status = 'Your order is currently being processed.'
					color = 0xFFFF00
				elif 'Your order has been placed.' in response:
					status = 'Your order has been placed.'
					color = 0xFFFF00
				elif 'Your order has been despatched.' in response or "Your order is out for delivery" in response:
					if '"trackingURL":null' in response:
						tracking2 = 'N/A'
					a12 = test['delivery']
					tracking1 = a12['courier']
					tracking2 = a12['trackingURL']
					status = 'Your order has been despatched.'
					color = 0x00FF00
				elif 'Your order has been delivered.' in response:
					a12 = test['delivery']
					tracking1 = a12['courier']
					tracking2 = a12['trackingURL']
					status = 'Your order has been delivered.'
					color = 0x00FF00
				elif 'It looks like your order has been cancelled.' in response:
					status = 'It looks like your order has been cancelled.'
					color = 0xFF0000
				elif 'It looks like there was an issue taking payment for this order' in response:
					status = 'It looks like there was an issue taking payment for this order.'
					color = 0xFF0000
				elif "It looks like your order has been delayed by the courier." in response:
					status = "It looks like your order has been delayed by the courier."
					color = 0x00FF00
				print(Fore.MAGENTA + f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]"+ log + Fore.GREEN + f"[Tracking Ordernumber - {i}]")
				test1 = discord.Embed(title=name, description=status,  colour=color)
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
				await ctx.send(embed = test1)
			except KeyError:
				test1 = discord.Embed(title="Mesh Order Tracker - Summary",  colour=setembedcolor)
				test1.add_field(name="Order not found!", value="Please check your ordernumber and zip code or use ?orderhelp for more infos")
				test1.set_footer(text=setfootertextorder, icon_url=setfooterimage)
				test1.set_thumbnail(url=setthumbnailorder)
				await ctx.send(embed = test1)
				statusrunning[0] = "notrunning"
		statusrunning[0] = "notrunning"
	elif statusrunning[0] == "running":
		test1 = discord.Embed(title="Mesh Order Tracker - Summary",  colour=setembedcolor)
		test1.add_field(name="Error", value="Someone else is tracking their orders right now!\n Please try again later")
		test1.set_footer(text=setfootertextorder, icon_url=setfooterimage)
		test1.set_thumbnail(url=setthumbnailorder)
		await ctx.send(embed = test1)


@bot.command()
async def orderbulk(ctx, store, postcode, orderno):
	user_name_id = ctx.author.name + ' ID : ' + str(ctx.author.id)
	log3 = Fore.CYAN + f'[{user_name_id}] '
	log4 = "[ORDER TRACKER]"
	log = log3 + log4
	now = datetime.now()
	if statusbulkrunning[0] == "notrunning":
		statusbulkrunning[0] = "running"

		first = ctx.message.content.splitlines()
		if len(first) > 2:

			embeddes = []
			embeddes1 = []
			embeddes2 = []
			embedlistdes = []

			embedplaced = []
			embedplaced1 = []
			embedplaced2 = []
			embedlistplaced = []

			embedlistproc = []
			embedpro1 = []
			embedpro2 = []
			embedpro = []

			embeddel = []
			embeddel1 = []
			embeddel2 = []
			embedlistdel = []

			embedpost = []
			embedpost1 = []
			embedpost2 = []
			embedlistpost = []

			embedcan = []
			embedcan1 = []
			embedcan2 = []
			embedlistcan = []

			if first[1] == "text":
				attachment_url = ctx.message.attachments[0].url
				file_request = requests.get(attachment_url)
				newfile = file_request.text.replace("\n",",")
				lines = newfile.split(",")
			else:
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

			if store == "fpgb" or store == "footpatrolgb" or store == "footpatroluk" or store == "fpuk" or store == "fpcom" or store == "footpatrolcom":
				store = "footpatrol"
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
			elif store == "jdmy" or store == "jdsportsmy":
				store = "jdsports"
				region = "my"

			test1 = discord.Embed(title="Mesh Order Tracker - Summary", description="Tracking " + str(len(lines)) + " orders!",  colour=setembedcolor)
			test1.set_footer(text=setfootertextorder, icon_url=setfooterimage)
			await ctx.send(embed = test1)

			for i in lines:
				base_url = 'https://data.smartagent.io/v1/jdsports/track-my-order'
				track_url = ''
				correctordernr = str(i).replace(" ","")
				track_url = base_url+'?orderNumber='+correctordernr+'&fascia='+store+region+'&postcode='+str(postcode)
				print(Fore.MAGENTA + f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]"+ log + Fore.GREEN + f"[Tracking Ordernumber - {i}]")
				x = threading.Thread(target=bulk, args=(track_url,f"{i}"))
				time.sleep(0.05)
				x.start()
			x.join()
			while threading.active_count() > 3:
				time.sleep(0.1)

			for i in range(len(orderstatus)):
				if orderstatus[i] == "placed":
					color = '16776960'
					orderplaced = orderplaced + 1

				elif orderstatus[i] == "processed":
						color = '16776960'
						orderproc = orderproc + 1

				elif orderstatus[i] == "despatched":
					color = '65280'
					orderdis = orderdis + 1

				elif orderstatus[i] == "delivered":
					color = '65280'
					orderdel = orderdel + 1

				elif orderstatus[i] == "cancelled":
					color = '16711680'
					ordercan = ordercan + 1

				elif orderstatus[i] == "issue":
					color = '16711680'
					orderpay = orderpay + 1

				elif orderstatus[i] == "not found":
					ordernotfound = ordernotfound + 1

			
			trackedorders = str(len(orderstatus))

			for i in range(7):
				if i == 0:
					test1 = discord.Embed(title="Mesh Order Tracker - Summary", description="Successfully tracked " + str(trackedorders) + " orders!",  colour=setembedcolor)
					test1.add_field(name=':x:  Order Not Found', value=ordernotfound, inline=False)
					test1.add_field(name=':sleeping: Order Placed', value=orderplaced, inline=False)
					test1.add_field(name=':cold_face: Order Processed', value=orderproc, inline=False)
					test1.add_field(name=':face_with_symbols_over_mouth: Order Canceled', value=ordercan, inline=False)
					test1.add_field(name=':rage: Payment Error', value=orderpay, inline=False)
					test1.add_field(name=':articulated_lorry: Order Despatched', value=orderdis, inline=False)
					test1.add_field(name=':house: Order delivered', value=orderdel, inline=False)
					test1.set_footer(text=setfootertextorder, icon_url=setfooterimage)
					test1.set_thumbnail(url=setthumbnailorder)
					print(Fore.MAGENTA + f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]" + log + Fore.GREEN + "[Webhook sent - Ordernumbers!]")
					await ctx.send(embed = test1)

				if i == 1:
					if len(tracknrplaced) > 0:
						test1 = discord.Embed(title="Mesh Order Tracker - Summary", description = str(len(tracknrplaced)) + " placed Orders!",  colour=setembedcolor)
						embedplaced = list(divide_chunks(tracknrplaced, 100))
						for i in range(len(embedplaced)):
							embedplacedonly = []
							embedplacedonly = "\n".join(embedplaced[i])
							if i == 0:
								test1.add_field(name=':sleeping: Order Placed', value=embedplacedonly, inline=False)
							else:
								test1.add_field(name='\xad', value=embedplacedonly, inline=False)
						test1.set_footer(text=setfootertextorder, icon_url=setfooterimage)
						test1.set_thumbnail(url=setthumbnailorder)
						await ctx.send(embed = test1)
						embedplaced.clear()

				if i == 2:
					if len(tracknrproc) > 0:
						test1 = discord.Embed(title="Mesh Order Tracker - Summary", description = str(len(tracknrproc)) + " processed Orders!",  colour=setembedcolor)
						embedpro = list(divide_chunks(tracknrproc, 100))
						for i in range(len(embedpro)):
							embedproonly = []
							embedproonly = "\n".join(embedpro[i])
							if i == 0:
								test1.add_field(name=':cold_face: Order Processed', value=embedproonly, inline=False)
							else:
								test1.add_field(name='\xad', value=embedproonly, inline=False)
						test1.set_footer(text=setfootertextorder, icon_url=setfooterimage)
						test1.set_thumbnail(url=setthumbnailorder)
						await ctx.send(embed = test1)
						embedpro.clear()

				if i == 3:
					if len(tracknrdes) > 0:
						test1 = discord.Embed(title="Mesh Order Tracker - Summary", description = str(len(tracknrdes)) + " despatched Orders!",  colour=setembedcolor)
						if len(tracknrdes) < 76:
							embedlistdes = list(divide_chunks(tracknrdes, 12))
							for i in range(len(embedlistdes)):
								embeddes = []
								embeddes = "\n".join(embedlistdes[i])
								if i == 0:
									test1.add_field(name=':articulated_lorry: Order Despatched', value=embeddes, inline=False)
								else:
									test1.add_field(name='\xad', value=embeddes, inline=False)
							test1.set_footer(text=setfootertextorder, icon_url=setfooterimage)
							test1.set_thumbnail(url=setthumbnailorder)
							await ctx.send(embed = test1)
							embedlistdes.clear()
						else:
							embedlisttrackonly = list(divide_chunks(tracknronly, 100))
							for i in range(len(embedlisttrackonly)):
								embedtrackonly = []
								embedtrackonly = "\n".join(embedlisttrackonly[i])
								if i == 0:
									test1.add_field(name=':articulated_lorry: Order Despatched', value=embedtrackonly, inline=False)
								else:
									test1.add_field(name='\xad', value=embedtrackonly, inline=False)
							test1.set_footer(text=setfootertextorder, icon_url=setfooterimage)
							test1.set_thumbnail(url=setthumbnailorder)
							await ctx.send(embed = test1)
							embedlisttrackonly.clear()

				if i == 4:
					if len(tracknrdel) > 0:
						test1 = discord.Embed(title="Mesh Order Tracker - Summary", description = str(len(tracknrdel)) + " delivered Orders!",  colour=setembedcolor)
						embeddelivered = list(divide_chunks(tracknrdel, 100))
						for i in range(len(embeddelivered)):
							embeddeliveredonly = []
							embeddeliveredonly = "\n".join(embeddelivered[i])
							if i == 0:
								test1.add_field(name=':house: Order Delivered', value=embeddeliveredonly, inline=False)
							else:
								test1.add_field(name='\xad', value=embeddeliveredonly, inline=False)
						test1.set_footer(text=setfootertextorder, icon_url=setfooterimage)
						test1.set_thumbnail(url=setthumbnailorder)
						await ctx.send(embed = test1)
						embeddelivered.clear()

				if i == 5:
					if len(tracknrpostcode) > 0:
						test1 = discord.Embed(title="Mesh Order Tracker - Summary", description = str(len(tracknrpostcode)) + " wrong postcode Orders!",  colour=setembedcolor)
						embedpostcode = list(divide_chunks(tracknrpostcode, 100))
						for i in range(len(embedpostcode)):
							embedpostcodeonly = []
							embedpostcodeonly = "\n".join(embedpostcode[i])
							if i == 0:
								test1.add_field(name=':warning: Postcode does not match', value=embedpostcodeonly, inline=False)
							else:
								test1.add_field(name='\xad', value=embedpostcodeonly, inline=False)
						test1.set_footer(text=setfootertextorder, icon_url=setfooterimage)
						test1.set_thumbnail(url=setthumbnailorder)
						await ctx.send(embed = test1)
						embedpostcode.clear()

				if i == 6:
					if len(tracknrcan) > 0:
						test1 = discord.Embed(title="Mesh Order Tracker - Summary", description = str(len(tracknrcan)) + " canceled Orders!",  colour=setembedcolor)
						embedcancel = list(divide_chunks(tracknrcan, 100))
						for i in range(len(embedcancel)):
							embedcannedonly = []
							embedcannedonly = "\n".join(embedcancel[i])
							if i == 0:
								test1.add_field(name=':face_with_symbols_over_mouth: Order Canceled', value=embedcannedonly, inline=False)
							else:
								test1.add_field(name='\xad', value=embedcannedonly, inline=False)
						test1.set_footer(text=setfootertextorder, icon_url=setfooterimage)
						test1.set_thumbnail(url=setthumbnailorder)
						await ctx.send(embed = test1)
						embedcancel.clear()	
			
			if len(tracklink) > 0:	
				for i in range(len(tracklink)):
					print(Fore.MAGENTA + f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]" + log + Fore.YELLOW + f"[Tracking Hermes Link - {tracklink[i]}]")
					test = str(tracklink[i])
					m = threading.Thread(target=hermes, args=(tracklink[i],"hi"))
					time.sleep(0.05)
					m.start()

				m.join()
				while threading.active_count() > 3:
					time.sleep(0.5)

				for i in range(len(countdelay)):
					for j in range(len(tracknrandlink)):
						if tracknrandlink[j][0] == countdelay[i]:
							trackordernumberdelay.append(f"[{tracknrandlink[j][1]}](https://www.myhermes.co.uk/track.html#/parcel/{tracknrandlink[j][0]})")

				for i in range(len(countdelivered)):
					for j in range(len(tracknrandlink)):
						if tracknrandlink[j][0] == countdelivered[i]:
							trackordernumberdelivered.append(tracknrandlink[j][1])

				for i in range(len(countontheway)):
					for j in range(len(tracknrandlink)):
						if tracknrandlink[j][0] == countontheway[i]:
							trackordernumberontheway.append(tracknrandlink[j][1])

				for i in range(len(countnottrackable)):
					for j in range(len(tracknrandlink)):
						if tracknrandlink[j][0] == countnottrackable[i]:
							trackordernumbernottrackable.append(tracknrandlink[j][1])

				for i in range(len(countreadytopickup)):
					for j in range(len(tracknrandlink)):
						if tracknrandlink[j][0] == countreadytopickup[i]:
							trackordernumberreadytopickup.append(tracknrandlink[j][1])

				test1 = discord.Embed(title="Hermes Order Tracker - Summary", description = str(len(countdelivered)+len(countdelay) + len(countontheway) + len(countnottrackable) + len(countreadytopickup)) + " tracked Orders!",  colour=setembedcolor)
				test1.add_field(name=":orange_circle: Order Not Trackable ATM", value=str(len(countnottrackable)), inline=False)
				test1.add_field(name=":yellow_circle: Order Ready To Pick Up", value=str(len(countreadytopickup)), inline=False)
				test1.add_field(name=":green_circle: Order On It's Way", value=str(len(countontheway)), inline=False)
				test1.add_field(name=':warning: Order Delayed', value=str(len(countdelay)), inline=False)
				test1.add_field(name=':house: Order Delivered', value=str(len(countdelivered)), inline=False)
				test1.set_footer(text=setfootertextorder, icon_url=setfooterimage)
				test1.set_thumbnail(url=setthumbnailorder)
				await ctx.send(embed = test1)

				if len(countnottrackable) > 0 :
					test1 = discord.Embed(title="Hermes Order Tracker - Summary", description = str(len(countnottrackable)) + " not trackable Orders!",  colour=setembedcolor)
					embednottrackable1 = list(divide_chunks(trackordernumbernottrackable, 100))
					for i in range(len(embednottrackable1)):
						embednottrackableonly = []
						embednottrackableonly = "\n".join(embednottrackable1[i])
						if i == 0:
							test1.add_field(name=":orange_circle: Order Not Trackable ATM", value=embednottrackableonly, inline=False)
						else:
							test1.add_field(name='\xad', value=embednottrackableonly, inline=False)
					test1.set_footer(text=setfootertextorder, icon_url=setfooterimage)
					test1.set_thumbnail(url=setthumbnailorder)
					await ctx.send(embed = test1)
					embednottrackable1.clear()

				if len(countreadytopickup) > 0 :
					test1 = discord.Embed(title="Hermes Order Tracker - Summary", description = str(len(countreadytopickup)) + " ready to be picked up Orders!",  colour=setembedcolor)
					embedreadytopickup1 = list(divide_chunks(trackordernumberreadytopickup, 100))
					for i in range(len(embedreadytopickup1)):
						embedreadytopickuponly = []
						embedreadytopickuponly = "\n".join(embedreadytopickup1[i])
						if i == 0:
							test1.add_field(name=":yellow_circle: Order Ready To Pick Up", value=embedreadytopickuponly, inline=False)
						else:
							test1.add_field(name='\xad', value=embedreadytopickuponly, inline=False)
					test1.set_footer(text=setfootertextorder, icon_url=setfooterimage)
					test1.set_thumbnail(url=setthumbnailorder)
					await ctx.send(embed = test1)
					embedreadytopickup1.clear()

				if len(countontheway) > 0 :
					test1 = discord.Embed(title="Hermes Order Tracker - Summary", description = str(len(countontheway)) + " shipped Orders!",  colour=setembedcolor)
					embedontheway1 = list(divide_chunks(trackordernumberontheway, 100))
					for i in range(len(embedontheway1)):
						embedonthewayonly = []
						embedonthewayonly = "\n".join(embedontheway1[i])
						if i == 0:
							test1.add_field(name=":green_circle: Order On It's Way", value=embedonthewayonly, inline=False)
						else:
							test1.add_field(name='\xad', value=embedonthewayonly, inline=False)
					test1.set_footer(text=setfootertextorder, icon_url=setfooterimage)
					test1.set_thumbnail(url=setthumbnailorder)
					await ctx.send(embed = test1)
					embedontheway1.clear()

				if len(countdelay) > 0 :
					test1 = discord.Embed(title="Hermes Order Tracker - Summary", description = str(len(countdelay)) + " delayed Orders!",  colour=setembedcolor)
					embeddelay1 = list(divide_chunks(trackordernumberdelay, 100))
					for i in range(len(embeddelay1)):
						embeddelayonly = []
						embeddelayonly = "\n".join(embeddelay1[i])
						if i == 0:
							test1.add_field(name=':warning: Order Delayed', value=embeddelayonly, inline=False)
						else:
							test1.add_field(name='\xad', value=embeddelayonly, inline=False)
					test1.set_footer(text=setfootertextorder, icon_url=setfooterimage)
					test1.set_thumbnail(url=setthumbnailorder)
					await ctx.send(embed = test1)
					embeddelay1.clear()

				if len(countdelivered) > 0 :
					test1 = discord.Embed(title="Hermes Order Tracker - Summary", description = str(len(countdelivered)) + " delivered Orders!",  colour=setembedcolor)
					embeddeliverd1 = list(divide_chunks(trackordernumberdelivered, 100))
					for i in range(len(embeddeliverd1)):
						embeddeliverdonly = []
						embeddeliverdonly = "\n".join(embeddeliverd1[i])
						if i == 0:
							test1.add_field(name=':house: Order Delivered', value=embeddeliverdonly, inline=False)
						else:
							test1.add_field(name='\xad', value=embeddeliverdonly, inline=False)
					test1.set_footer(text=setfootertextorder, icon_url=setfooterimage)
					test1.set_thumbnail(url=setthumbnailorder)
					await ctx.send(embed = test1)
					embeddeliverd1.clear()
				print(Fore.MAGENTA + f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]" + log + Fore.GREEN + "[Webhook sent - Hermes!]")
		else:
			test1 = discord.Embed(title="MESH Order Tracker - Summary",  colour=setembedcolor)
			test1.add_field(name='Error', value="Make sure to use more than 1 ordernumber!", inline=False)
			test1.set_footer(text=setfootertextorder, icon_url=setfooterimage)
			test1.set_thumbnail(url=setthumbnailorder)
			statusbulkrunning[0] = "notrunning"
			await ctx.send(embed = test1)

		print(Fore.MAGENTA + f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]" + log + Fore.GREEN + "[ALL WEBHOOKS SENT!]")
		orderstatus.clear()
		tracknrdes.clear()
		countdelivered.clear()
		countdelay.clear()
		countontheway.clear()
		countnottrackable.clear()
		countreadytopickup.clear()
		tracknrdel.clear()
		tracknrproc.clear()
		tracknrplaced.clear()
		tracknrpostcode.clear()
		tracknrcan.clear()
		tracknronly.clear()
		tracklink.clear()
		trackordernumberdelay.clear()
		trackordernumberdelivered.clear()
		trackordernumberontheway.clear()
		trackordernumbernottrackable.clear()
		trackordernumberreadytopickup.clear()
		tracknrandlink.clear()
		statusbulkrunning[0] = "notrunning"
	elif statusbulkrunning[0] == "running":
		test1 = discord.Embed(title="Mesh Order Tracker - Summary",  colour=setembedcolor)
		test1.add_field(name="Error", value="Someone else is tracking their orders right now!\n Try again!")
		test1.set_footer(text=setfootertextorder, icon_url=setfooterimage)
		test1.set_thumbnail(url=setthumbnailorder)
		await ctx.send(embed = test1)

@bot.command()
async def ordersize(ctx, store, postcode, orderno):
	if statusbulkrunningsize[0] == "notrunning":
		statusbulkrunningsize[0] = "running"

		first = ctx.message.content.splitlines()

		if first[1] == "text":
			attachment_url = ctx.message.attachments[0].url
			file_request = requests.get(attachment_url)
			newfile = file_request.text.replace("\n",",")
			lines = newfile.split(",")
		else:
			lines = ctx.message.content.splitlines()
			lines.pop(0)
		linescount = len(lines)
		if linescount == 0:
			test1 = discord.Embed(title="Mesh Order Tracker - Error",  colour=setembedcolor)
			test1.add_field(name="Error", value="Make sure Ordernumbers are posted in next line!\nExample:\n```?orderbulk jdde 79798\n714151769\n714151768``")
			test1.set_footer(text=setfootertextorder, icon_url=setfooterimage)
			test1.set_thumbnail(url=setthumbnailorder)
			await ctx.send(embed = test1)

		user_name_id = ctx.author.name + ' ID : ' + str(ctx.author.id)
		log3 = Fore.CYAN + f'[{user_name_id}] '
		log4 = "[ORDER TRACKER]"
		log = log3 + log4
		now = datetime.now()

		if store == "fpgb" or store == "footpatrolgb" or store == "footpatroluk" or store == "fpuk" or store == "fpcom" or store == "footpatrolcom":
			store = "footpatrol"
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
		elif store == "jdmy" or store == "jdsportsmy":
			store = "jdsports"
			region = "my"

		test1 = discord.Embed(title="Mesh Order Tracker - Summary", description="Tracking " + str(len(lines)) + " orders!",  colour=setembedcolor)
		test1.set_footer(text=setfootertextorder, icon_url=setfooterimage)
		await ctx.send(embed = test1)

		for i in lines:
			base_url = 'https://data.smartagent.io/v1/jdsports/track-my-order'
			track_url = ''
			correctordernr = str(i).replace(" ","")
			track_url = base_url+'?orderNumber='+correctordernr+'&fascia='+store+region+'&postcode='+str(postcode)
			print(Fore.MAGENTA + f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]"+ log + Fore.GREEN + f"[Tracking Ordernumber - {i}]")
			x = threading.Thread(target=amount, args=(track_url,f"{i}"))
			time.sleep(0.05)
			x.start()
		x.join()
		while threading.active_count() > 3:
			time.sleep(0.1)


		finalshoelist = list(dict.fromkeys(getallshoenames))
		myDict = {}

		for i in range(len(finalshoelist)):
			myDict[finalshoelist[i]] = []

		for i in range(len(finalshoelist)):
			for m in range(len(shoenameandsize)):
				if finalshoelist[i] == shoenameandsize[m][0]:
					myDict[finalshoelist[i]].append(shoenameandsize[m][1])

		allamountspersize = []
		for i in range(len(myDict)):
			finalcountpersize = list(dict.fromkeys(myDict[finalshoelist[i]]))
			for m in range(len(finalcountpersize)):
				countpersize = []
				for k in range(len(myDict[finalshoelist[i]])):
					if finalcountpersize[m] == myDict[finalshoelist[i]][k]:
						countpersize.append(myDict[finalshoelist[i]][k])
				tem = finalshoelist[i],finalcountpersize[m],str(len(countpersize))
				allamountspersize.append(tem)
		totalamountpershoe = 0
		test1 = discord.Embed(title="Mesh Order Tracker Sizes - Summary",  colour=setembedcolor)
		for r in range(len(finalshoelist)):
			for l in range(len(allamountspersize)):
				totalamountpershoe = totalamountpershoe + int(allamountspersize[l][2])
			test1.add_field(name=finalshoelist[r], value=f"*Total Amount: {str(totalamountpershoe)}*",inline=False)
			for h in range(len(allamountspersize)):
				if finalshoelist[r] == allamountspersize[h][0]:
					test1.add_field(name="Size " + allamountspersize[h][1], value=f"Count: {allamountspersize[h][2]}",inline=False)
		if noinfos:
			test1.add_field(name="No Information to those order numbers", value=f"Count: {str(len(noinfos))}",inline=False)
		test1.set_footer(text=setfootertextorder, icon_url=setfooterimage)
		test1.set_thumbnail(url=setthumbnailorder)
		await ctx.send(embed = test1)
		print(Fore.MAGENTA + f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]"+ log + Fore.GREEN + f"[Webhook Order Size Sent]")
		getallshoenames.clear()
		shoenameandsize.clear()
		noinfos.clear()

		statusbulkrunningsize[0] = "notrunning"
	elif statusbulkrunningsize[0] == "running":
		test1 = discord.Embed(title="Mesh Order Tracker - Summary",  colour=setembedcolor)
		test1.add_field(name="Error", value="Someone else is tracking their orders right now!\n Try again!")
		test1.set_footer(text=setfootertextorder, icon_url=setfooterimage)
		test1.set_thumbnail(url=setthumbnailorder)
		await ctx.send(embed = test1)


@bot.command()
async def orderhelp(context):
	embed=discord.Embed(title="Mesh Order Tracker Help", color=setembedcolor)
	embed.add_field(name="How do i track a single order :question:", value="```?order <store> <postcode>\n<ordernr>```\n**Example:**```?order jdde 79798\n302723669```", inline=False)
	embed.add_field(name="How do i track a multiple orders :question:", value="```?order <store> <postcode>\n<ordernr1>\n<ordernr2>\n<ordernr3>\n```\n**Example:**```?order jdde 79798\n302723669\n302723123\n302723456```", inline=False)
	embed.add_field(name="How do i get all order status :question:", value="```?orderbulk <store> <postcode>\n<ordernr1>\n<ordernr2>\n<ordernr3>\n```\n**Example:**```?orderbulk jdsportsde 79798\n302723669\n302723123\n302723456```", inline=False)
	embed.add_field(name="How do i get a store list with its command format :question:", value="Use command `?orderstore to get a full list of all stores supported", inline=False)
	embed.add_field(name="How do i get all order status 150+ orders :question:", value="```?orderbulk <store> <postcode>\ntext```\n**Example:**```?orderbulk jdsportsde 79798\n302723669\n<message.txt>```", inline=False)
	embed.add_field(name="Orderbulk with message.txt",value="write: \n?orderbulk <store> <zipcode>\n<paste here all orders numbers discord creates message.txt it self>")
	embed.add_field(name="How do i get a size count of each size from each shoe?",value="write: \n?ordersize <store> <zipcode>\n<paste here all orders numbers>")
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

@bot.event
async def on_command_error(ctx, error):
	if isinstance(error, CommandNotFound):
		return
	elif isinstance(error,MissingRequiredArgument):
		embed=discord.Embed(title="Command Error", color=setembedcolor)
		embed.add_field(name="Error", value="Your are missing an argument", inline=True)
		embed.add_field(name="Commad - Mesh Tracker", value="```?order jdde 79798\n714151769\n714151768```", inline=False)
		embed.add_field(name="Commad - Mesh Bulk Tracker", value="```?orderbulk jdde 79798\n714151769\n714151768```", inline=False)
		embed.add_field(name="Commad - Mesh Bulk Tracker - OrderNrs in a file", value="```?orderbulk jdde 79798\ntext\n714151769\n714151768```", inline=False)
		embed.add_field(name="Commad - Mesh Bulk Track Shoe Size", value="```?ordersize jdde 79798\n714151769\n714151768```", inline=False)
		embed.set_footer(text=setfootertextorder, icon_url=setfooterimage)
		await ctx.send(embed=embed)
		return
	raise error


bot.run(bottoken)
