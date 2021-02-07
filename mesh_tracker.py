import discord
from discord.ext import commands
from datetime import datetime
from colorama import Fore, Back, Style, init
import requests
import json
from discord.ext.commands import CommandNotFound

bottoken = "Nzk4NTY2ODE4ODEzMDUwOTYw.X_25Tg.Fgr9xvAtE0qkJnmHL_dz4gZ3ofw"

bot = commands.Bot(command_prefix = '?', help_command=None)


@bot.event
async def on_ready():
	print('Bot is ready.')
	pass

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        return
    raise error

setfooter = "@ScriptingTools | Mesh Order Tracker | <?orderhelp>"
setfooterimage = "https://images-ext-1.discordapp.net/external/atwFnJRaXHB0ebXrVSPjVWDXe5hL2OQ0JBWopjGcVCY/https/images-ext-2.discordapp.net/external/gGrbK8FUkmby_Ao8mmH9dZ4RI1cvfkhpUNBlIB46XQE/https/media.discordapp.net/attachments/460974692073734164/680067025493950474/Wcu7EAAAAASUVORK5CYII.png"
setembedcolor = 0x00000
setthumbnail = setfooterimage


@bot.command()
async def order(ctx, store, postcode, orderno: int):
	lines = ctx.message.content.splitlines()
	lines.pop(0)
	linescount = len(lines)
	if linescount == 0:
		test1 = discord.Embed(title="Mesh Order Tracker - Error",  colour=setembedcolor)
		test1.add_field(name="Error", value="Make sure Ordernumbers are posted in next line!\nExample:\n```?order jdde 79798\n714151764``")
		test1.set_footer(text=setfooter, icon_url=setfooterimage)
		test1.set_thumbnail(url=setthumbnail)
		await ctx.send(embed = test1)
	server_name = ctx.guild.name
	user_name_id = ctx.author.name + ' ID : ' + str(ctx.author.id)
	log2 = Fore.CYAN +f'[{server_name}]'
	log3 = Fore.CYAN + f'[{user_name_id}] '
	log4 = "[ORDER TRACKER]"
	log = log2 + ' ' + log3 + log4
	now = datetime.now()

	if store == "fpgb" or store == "footpatrolgb" or store == "footpatroluk" or store == "fpuk" or store == "fpcom" or store == "footpatrolcom":
		store = "footpatrolcom"
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
	elif store == "jdmyf" or store == "jdsportsmyf":
		store = "jdsports"
		region = "myf"

	for i in lines:
		try:
			base_url = 'https://data.smartagent.io/v1/jdsports/track-my-order'
			track_url = ''
			track_url = base_url+'?orderNumber='+str(i)+'&fascia='+store+region+'&postcode='+str(postcode)
			r = requests.get(track_url)
			response = r.text
			if 'Order not found' in response:
				test1 = discord.Embed(title="Mesh Order Tracker - Summary",  colour=setembedcolor)
				test1.add_field(name="Order not found!", value="Please check your ordernumber and zip code or use ?orderhelp for more infos")
				test1.set_footer(text=setfooter, icon_url=setfooterimage)
				test1.set_thumbnail(url=setthumbnail)
				await ctx.message.delete()
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
			if 'Your order is currently being processed.' in response:
				status = 'Your order is currently being processed.'
				color = '16776960'
			elif 'Your order has been placed.' in response:
				status = 'Your order has been placed.'
				color = '16776960'
			elif 'Your order has been despatched.' in response:
				if '"trackingURL":null' in response:
					tracking2 = 'N/A'
				a12 = test['delivery']
				tracking1 = a12['courier']
				tracking2 = a12['trackingURL']
				status = 'Your order has been despatched.'
				color = '65280'
			elif 'Your order has been delivered.' in response:
				a12 = test['delivery']
				tracking1 = a12['courier']
				tracking2 = a12['trackingURL']
				status = 'Your order has been delivered.'
				color = '65280'
			elif 'It looks like your order has been cancelled.' in response:
				status = 'It looks like your order has been cancelled.'
				color = '16711680'
			elif 'It looks like there was an issue taking payment for this order' in response:
				status = 'It looks like there was an issue taking payment for this order.'
				color = '16711680'
			print(Fore.MAGENTA + f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]"+ log + Fore.GREEN + f"[Tracking Ordernumber - {i}]")
			test1 = discord.Embed(title=name, description=status,  colour=discord.Colour(int(color)))
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
			test1.set_footer(text=setfooter, icon_url=setfooterimage)
			test1.set_thumbnail(url=img)
			print(Fore.MAGENTA + f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]" + log + Fore.GREEN + "[Webhook sent!]")
			print('')
			await ctx.send(embed = test1)
		except KeyError:
			test1 = discord.Embed(title="Mesh Order Tracker - Summary",  colour=setembedcolor)
			test1.add_field(name="Order not found!", value="Please check your ordernumber and zip code or use ?orderhelp for more infos")
			test1.set_footer(text=setfooter, icon_url=setfooterimage)
			test1.set_thumbnail(url=setthumbnail)
			await ctx.message.delete()
			await ctx.send(embed = test1)

@bot.command()
async def orderbulk(ctx, store, postcode, orderno: int):
	lines = ctx.message.content.splitlines()
	lines.pop(0)
	linescount = len(lines)
	if linescount == 0:
		test1 = discord.Embed(title="Mesh Order Tracker - Error",  colour=setembedcolor)
		test1.add_field(name="Error", value="Make sure Ordernumbers are posted in next line!\nExample:\n```?orderbulk jdde 79798\n714151764``")
		test1.set_footer(text=setfooter, icon_url=setfooterimage)
		test1.set_thumbnail(url=setthumbnail)
		await ctx.send(embed = test1)
	orderproc = 0
	orderdel = 0
	orderplaced = 0
	orderdis = 0
	orderproc = 0
	ordercan = 0
	orderpay = 0
	ordernotfound = 0
	server_name = ctx.guild.name
	user_name_id = ctx.author.name + ' ID : ' + str(ctx.author.id)
	log2 = Fore.CYAN +f'[{server_name}]'
	log3 = Fore.CYAN + f'[{user_name_id}] '
	log4 = "[ORDER TRACKER]"
	log = log2 + ' ' + log3 + log4
	now = datetime.now()

	if store == "fpgb" or store == "footpatrolgb" or store == "footpatroluk" or store == "fpuk" or store == "fpcom" or store == "footpatrolcom":
		store = "footpatrolcom"
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
	elif store == "jdmyf" or store == "jdsportsmyf":
		store = "jdsports"
		region = "myf"

	test1 = discord.Embed(title="Mesh Order Tracker - Summary", description="Tracking " + str(len(lines)) + " orders!",  colour=setembedcolor)
	test1.set_footer(text=setfooter, icon_url=setfooterimage)
	await ctx.send(embed = test1)

	for i in lines:
		try:
			base_url = 'https://data.smartagent.io/v1/jdsports/track-my-order'
			track_url = ''
			track_url = base_url+'?orderNumber='+str(i)+'&fascia='+store+region+'&postcode='+str(postcode)
			r = requests.get(track_url)
			response = r.text
			if 'Order not found' in response:
				ordernotfound = ordernotfound + 1
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
			if 'Your order is currently being processed.' in response:
				status = 'Your order is currently being processed.'
				color = '16776960'
				orderproc = orderproc + 1
			elif 'Your order has been placed.' in response:
				status = 'Your order has been placed.'
				color = '16776960'
				orderplaced = orderplaced + 1
			elif 'Your order has been despatched.' in response:
				if '"trackingURL":null' in response:
					tracking2 = 'N/A'
				a12 = test['delivery']
				tracking1 = a12['courier']
				tracking2 = a12['trackingURL']
				status = 'Your order has been despatched.'
				color = '65280'
				orderdis = orderdis + 1
			elif 'Your order has been delivered.' in response:
				a12 = test['delivery']
				tracking1 = a12['courier']
				tracking2 = a12['trackingURL']
				status = 'Your order has been delivered.'
				color = '65280'
				orderdel = orderdel + 1
			elif 'It looks like your order has been cancelled.' in response:
				status = 'It looks like your order has been cancelled.'
				color = '16711680'
				ordercan = ordercan + 1
			elif 'It looks like there was an issue taking payment for this order' in response:
				status = 'It looks like there was an issue taking payment for this order.'
				color = '16711680'
				orderpay = orderpay + 1
		except (KeyError,UnboundLocalError):
				ordernotfound = ordernotfound + 1
		trackedorders = orderproc + orderplaced + orderdis + orderdel + orderpay + ordercan
		print(Fore.MAGENTA + f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]"+ log + Fore.GREEN + f"[Tracking Ordernumber - {i}]")

	test1 = discord.Embed(title="Mesh Order Tracker - Summary", description="Successfully tracked " + str(trackedorders) + " orders!",  colour=setembedcolor)
	test1.add_field(name=':x:  Order Not Found', value=ordernotfound, inline=False)
	test1.add_field(name=':sleeping: Order Placed', value=orderplaced, inline=False)
	test1.add_field(name=':cold_face: Order Processed', value=orderproc, inline=False)
	test1.add_field(name=':face_with_symbols_over_mouth: Order Canceled', value=ordercan, inline=False)
	test1.add_field(name=':rage: Payment Error', value=orderpay, inline=False)
	test1.add_field(name=':articulated_lorry: Order Dispatched', value=orderdis, inline=False)
	test1.set_footer(text=setfooter, icon_url=setfooterimage)
	test1.set_thumbnail(url=setthumbnail)
	print(Fore.MAGENTA + f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]" + log + Fore.GREEN + "[Webhook sent!]")
	print('')
	await ctx.send(embed = test1)

@bot.command()
async def orderhelp(context):
	embed=discord.Embed(title="Scripting Tools", description="Mesh Order Tracker", color=setembedcolor)
	embed.add_field(name="How do i track a single order :question:", value="```?order <store> <postcode>\n<ordernr>```\n**Example:**```?order jdde 79798\n302723669```", inline=False)
	embed.add_field(name="How do i track a multiple orders :question:", value="```?order <store> <postcode>\n<ordernr1>\n<ordernr2>\n<ordernr3>\n```\n**Example:**```?order jdde 79798\n302723669\n302723123\n302723456```", inline=False)
	embed.add_field(name="How do i get all order status :question:", value="```?orderbulk <store> <postcode>\n<ordernr1>\n<ordernr2>\n<ordernr3>\n```\n**Example:**```?orderbulk jdsportsde 79798\n302723669\n302723123\n302723456```", inline=False)
	embed.add_field(name="How do i get a store list with its command format :question:", value="Use command `?orderstore to get a full list of all stores supported", inline=False)
	embed.add_field(name="Information",value="You can either use the full name of the store or the given shortcut!\nexample: jdsportsnl -> jdnl", inline=False)
	embed.set_footer(text=setfooter, icon_url=setfooterimage)
	embed.set_thumbnail(url=setthumbnail)
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
	embed=discord.Embed(title="Scripting Tools", description="Mesh Stores", color=setembedcolor)
	embed.add_field(name="JDSports", value=jdstores, inline=True)
	embed.add_field(name="Size?", value=szstores, inline=True)
	embed.add_field(name="Footpatrol", value=fpstores, inline=True)
	embed.set_footer(text=setfooter, icon_url=setfooterimage)
	embed.set_thumbnail(url=setthumbnail)
	await context.send(embed=embed)


bot.run(bottoken)
