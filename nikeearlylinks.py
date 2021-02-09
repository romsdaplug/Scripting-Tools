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

setfootertext = "@ScriptingTools | <?nikehelp>"
setfooterimage = "https://images-ext-1.discordapp.net/external/atwFnJRaXHB0ebXrVSPjVWDXe5hL2OQ0JBWopjGcVCY/https/images-ext-2.discordapp.net/external/gGrbK8FUkmby_Ao8mmH9dZ4RI1cvfkhpUNBlIB46XQE/https/media.discordapp.net/attachments/460974692073734164/680067025493950474/Wcu7EAAAAASUVORK5CYII.png"
setembedcolor = 0x000000

@bot.event
async def on_ready():
	print('Bot is ready.')
	pass

def check_if_it_is_me(ctx):
	return ctx.message.author.id == 175953718750085121 or ctx.message.author.id == 351639955531104258


def divide_chunks(l, n): 
      
    # looping till length l 
    for i in range(0, len(l), n):  
        yield l[i:i + n] 
  
@bot.command()
async def nike(context, link):
	nikeregion = link.split("www.nike.com/")[1].split("/")[0]
	headers = {
	    'authority': 'www.nike.com',
	    'pragma': 'no-cache',
	    'cache-control': 'no-cache',
	    'upgrade-insecure-requests': '1',
	    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.146 Safari/537.36',
	    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
	    'sec-fetch-site': 'same-origin',
	    'sec-fetch-mode': 'navigate',
	    'sec-fetch-user': '?1',
	    'sec-fetch-dest': 'document',
	    'accept-language': 'de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7',
	}
	if nikeregion == "ch":
		firstpartlink = link.split("ch/")[0]
		secondpartlink = link.split("/launch/")[1]

		response = requests.get(link, headers=headers)
		soup = bs(response.content, 'html.parser')
		text = soup.find("meta", {"name":"branch:deeplink:productId"})["content"]
		shoepic = soup.find("meta", {"property":"og:image"})["content"]
		sizes = ["4","4.5","5","5.5","6","6.5","7","7.5","8","8.5","9","9.5","10","10.5","11","11.5","12","12.5"]
		region = ["ch/en","ch/fr","ch/de","ch/it"]
		country = ["gb","fr","de","it"]
		earlylink = []
		for i in range(len(region)):
			for j in range(len(sizes)):
				earlylink.append(str("[US " + str(sizes[j]) + "](" + firstpartlink + str(region[i]) + "/launch/" + secondpartlink + "?productId=" + str(text) + "&size=" + str(sizes[j]) + ")"))
			lenearlylink = len(earlylink)
			n = 6
			embedlistsizes = list(divide_chunks(earlylink, n))

			if region[i] == "ch/en":
				embedlistsizes[0] = "\n".join(embedlistsizes[0])
				embedlistsizes[1] = "\n".join(embedlistsizes[1])
				embedlistsizes[2] = "\n".join(embedlistsizes[2])
				embed=discord.Embed(title="Nike CH - Early Links - " + str.upper(region[i]) + " " + ":flag_" + str(country[i]) + ":", color=setembedcolor)
				embed.add_field(name="Checkout Link", value=embedlistsizes[0], inline=True)
				embed.add_field(name="Checkout Link", value=embedlistsizes[1], inline=True)
				embed.add_field(name="Checkout Link", value=embedlistsizes[2], inline=True)
				embed.set_footer(text=setfootertext, icon_url=setfooterimage)
				embed.set_thumbnail(url=shoepic)
				await context.send(embed=embed)
			if region[i] == "ch/fr":
				embedlistsizes[3] = "\n".join(embedlistsizes[3])
				embedlistsizes[4] = "\n".join(embedlistsizes[4])
				embedlistsizes[5] = "\n".join(embedlistsizes[5])
				embed=discord.Embed(title="Nike CH - Early Links - " + str.upper(region[i]) + " " + ":flag_" + str(country[i]) + ":", color=setembedcolor)
				embed.add_field(name="Checkout Link", value=embedlistsizes[3], inline=True)
				embed.add_field(name="Checkout Link", value=embedlistsizes[4], inline=True)
				embed.add_field(name="Checkout Link", value=embedlistsizes[5], inline=True)
				embed.set_footer(text=setfootertext, icon_url=setfooterimage)
				embed.set_thumbnail(url=shoepic)
				await context.send(embed=embed)
			if region[i] == "ch/de":
				embedlistsizes[6] = "\n".join(embedlistsizes[6])
				embedlistsizes[7] = "\n".join(embedlistsizes[7])
				embedlistsizes[8] = "\n".join(embedlistsizes[8])
				embed=discord.Embed(title="Nike CH - Early Links - " + str.upper(region[i]) + " " + ":flag_" + str(country[i]) + ":", color=setembedcolor)
				embed.add_field(name="Checkout Link", value=embedlistsizes[6], inline=True)
				embed.add_field(name="Checkout Link", value=embedlistsizes[7], inline=True)
				embed.add_field(name="Checkout Link", value=embedlistsizes[8], inline=True)
				embed.set_footer(text=setfootertext, icon_url=setfooterimage)
				embed.set_thumbnail(url=shoepic)
				await context.send(embed=embed)
			if region[i] == "ch/it":
				embedlistsizes[9] = "\n".join(embedlistsizes[9])
				embedlistsizes[10] = "\n".join(embedlistsizes[10])
				embedlistsizes[11] = "\n".join(embedlistsizes[11])
				embed=discord.Embed(title="Nike CH - Early Links - " + str.upper(region[i]) + " " + ":flag_" + str(country[i]) + ":", color=setembedcolor)
				embed.add_field(name="Checkout Link", value=embedlistsizes[9], inline=True)
				embed.add_field(name="Checkout Link", value=embedlistsizes[10], inline=True)
				embed.add_field(name="Checkout Link", value=embedlistsizes[11], inline=True)
				embed.set_footer(text=setfootertext, icon_url=setfooterimage)
				embed.set_thumbnail(url=shoepic)
				await context.send(embed=embed)


	elif nikeregion == "au":
		firstpartlink = link.split("au/")[0]
		secondpartlink = link.split("/launch/")[1]

		response = requests.get(link, headers=headers)
		soup = bs(response.content, 'html.parser')
		text = soup.find("meta", {"name":"branch:deeplink:productId"})["content"]
		shoepic = soup.find("meta", {"property":"og:image"})["content"]
		sizes = ["4","4.5","5","5.5","6","6.5","7","7.5","8","8.5","9","9.5","10","10.5","11","11.5","12","12.5"]
		region = ["au"]
		country = ["au"]
		earlylink = []
		for i in range(len(region)):
			for j in range(len(sizes)):
				earlylink.append(str("[US " + str(sizes[j]) + "](" + firstpartlink + str(region[i]) + "/launch/" + secondpartlink + "?productId=" + str(text) + "&size=" + str(sizes[j]) + ")"))
			lenearlylink = len(earlylink)
			n = 6
			embedlistsizes = list(divide_chunks(earlylink, n))

			embedlistsizes[0] = "\n".join(embedlistsizes[0])
			embedlistsizes[1] = "\n".join(embedlistsizes[1])
			embedlistsizes[2] = "\n".join(embedlistsizes[2])
			embed=discord.Embed(title="Nike AU - Early Links - " + str.upper(region[i]) + " " + ":flag_" + str(country[i]) + ":", color=setembedcolor)
			embed.add_field(name="Checkout Link", value=embedlistsizes[0], inline=True)
			embed.add_field(name="Checkout Link", value=embedlistsizes[1], inline=True)
			embed.add_field(name="Checkout Link", value=embedlistsizes[2], inline=True)
			embed.set_footer(text=setfootertext, icon_url=setfooterimage)
			embed.set_thumbnail(url=shoepic)
			await context.send(embed=embed)

	elif nikeregion == "ca":
		firstpartlink = link.split("ca/")[0]
		secondpartlink = link.split("/launch/")[1]

		response = requests.get(link, headers=headers)
		soup = bs(response.content, 'html.parser')
		text = soup.find("meta", {"name":"branch:deeplink:productId"})["content"]
		shoepic = soup.find("meta", {"property":"og:image"})["content"]
		sizes = ["4","4.5","5","5.5","6","6.5","7","7.5","8","8.5","9","9.5","10","10.5","11","11.5","12","12.5"]
		region = ["ca","ca/fr"]
		country = ["ca","fr"]
		earlylink = []
		for i in range(len(region)):
			for j in range(len(sizes)):
				earlylink.append(str("[US " + str(sizes[j]) + "](" + firstpartlink + region[i] + "/launch/" + secondpartlink + "?productId=" + str(text) + "&size=" + str(sizes[j]) + ")"))
			lenearlylink = len(earlylink)
			n = 6
			embedlistsizes = list(divide_chunks(earlylink, n))

			if region[i] == "ca":
				embedlistsizes[0] = "\n".join(embedlistsizes[0])
				embedlistsizes[1] = "\n".join(embedlistsizes[1])
				embedlistsizes[2] = "\n".join(embedlistsizes[2])
				embed=discord.Embed(title="Nike CA - Early Links - " + str.upper(region[i]) + " " + ":flag_" + str(country[i]) + ":", color=setembedcolor)
				embed.add_field(name="Checkout Link", value=embedlistsizes[0], inline=True)
				embed.add_field(name="Checkout Link", value=embedlistsizes[1], inline=True)
				embed.add_field(name="Checkout Link", value=embedlistsizes[2], inline=True)
				embed.set_footer(text=setfootertext, icon_url=setfooterimage)
				embed.set_thumbnail(url=shoepic)
				await context.send(embed=embed)
			if region[i] == "ca/fr":
				embedlistsizes[3] = "\n".join(embedlistsizes[3])
				embedlistsizes[4] = "\n".join(embedlistsizes[4])
				embedlistsizes[5] = "\n".join(embedlistsizes[5])
				embed=discord.Embed(title="Nike CA - Early Links - " + str.upper(region[i]) + " " + ":flag_" + str(country[i]) + ":", color=setembedcolor)
				embed.add_field(name="Checkout Link", value=embedlistsizes[3], inline=True)
				embed.add_field(name="Checkout Link", value=embedlistsizes[4], inline=True)
				embed.add_field(name="Checkout Link", value=embedlistsizes[5], inline=True)
				embed.set_footer(text=setfootertext, icon_url=setfooterimage)
				embed.set_thumbnail(url=shoepic)
				await context.send(embed=embed)

	elif nikeregion == "ru":
		firstpartlink = link.split("ru/")[0]
		secondpartlink = link.split("/launch/")[1]

		response = requests.get(link, headers=headers)
		soup = bs(response.content, 'html.parser')
		text = soup.find("meta", {"name":"branch:deeplink:productId"})["content"]
		shoepic = soup.find("meta", {"property":"og:image"})["content"]
		sizes = ["4","4.5","5","5.5","6","6.5","7","7.5","8","8.5","9","9.5","10","10.5","11","11.5","12","12.5"]
		region = ["ru"]
		country = ["ru"]
		earlylink = []
		for i in range(len(region)):
			for j in range(len(sizes)):
				earlylink.append(str("[US " + str(sizes[j]) + "](" + firstpartlink + str(region[i]) + "/launch/" + secondpartlink + "?productId=" + str(text) + "&size=" + str(sizes[j]) + ")"))
			lenearlylink = len(earlylink)
			n = 6
			embedlistsizes = list(divide_chunks(earlylink, n))

			embedlistsizes[0] = "\n".join(embedlistsizes[0])
			embedlistsizes[1] = "\n".join(embedlistsizes[1])
			embedlistsizes[2] = "\n".join(embedlistsizes[2])
			embed=discord.Embed(title="Nike RU - Early Links - " + str.upper(region[i]) + " " + ":flag_" + str(country[i]) + ":", color=setembedcolor)
			embed.add_field(name="Checkout Link", value=embedlistsizes[0], inline=True)
			embed.add_field(name="Checkout Link", value=embedlistsizes[1], inline=True)
			embed.add_field(name="Checkout Link", value=embedlistsizes[2], inline=True)
			embed.set_footer(text=setfootertext, icon_url=setfooterimage)
			embed.set_thumbnail(url=shoepic)
			await context.send(embed=embed)
	elif nikeregion == "sg":
		firstpartlink = link.split("sg/")[0]
		secondpartlink = link.split("/launch/")[1]

		response = requests.get(link, headers=headers)
		soup = bs(response.content, 'html.parser')
		text = soup.find("meta", {"name":"branch:deeplink:productId"})["content"]
		shoepic = soup.find("meta", {"property":"og:image"})["content"]
		sizes = ["4","4.5","5","5.5","6","6.5","7","7.5","8","8.5","9","9.5","10","10.5","11","11.5","12","12.5"]
		region = ["sg"]
		country = ["sg"]
		earlylink = []
		for i in range(len(region)):
			for j in range(len(sizes)):
				earlylink.append(str("[US " + str(sizes[j]) + "](" + firstpartlink + str(region[i]) + "/launch/" + secondpartlink + "?productId=" + str(text) + "&size=" + str(sizes[j]) + ")"))
			lenearlylink = len(earlylink)
			n = 6
			embedlistsizes = list(divide_chunks(earlylink, n))

			embedlistsizes[0] = "\n".join(embedlistsizes[0])
			embedlistsizes[1] = "\n".join(embedlistsizes[1])
			embedlistsizes[2] = "\n".join(embedlistsizes[2])
			embed=discord.Embed(title="Nike SG - Early Links - " + str.upper(region[i]) + " " + ":flag_" + str(country[i]) + ":", color=setembedcolor)
			embed.add_field(name="Checkout Link", value=embedlistsizes[0], inline=True)
			embed.add_field(name="Checkout Link", value=embedlistsizes[1], inline=True)
			embed.add_field(name="Checkout Link", value=embedlistsizes[2], inline=True)
			embed.set_footer(text=setfootertext, icon_url=setfooterimage)
			embed.set_thumbnail(url=shoepic)
			await context.send(embed=embed)

@bot.command()
async def nikehelp(context):
	embed=discord.Embed(title="Nike Early Links HELP", color=setembedcolor)
	embed.add_field(name="Command Format", value="?nike  <full link here>", inline=False)
	embed.set_footer(text=setfootertext, icon_url=setfooterimage)
	await context.send(embed=embed)


@bot.event
async def on_command_error(ctx, error):
	if isinstance(error, CommandNotFound):
		return
	elif isinstance(error,MissingRequiredArgument):
		embed=discord.Embed(title="Command Error", color=setembedcolor)
		embed.add_field(name="Error", value="Your are missing an argument", inline=True)
		embed.add_field(name="Command Format", value="?nike  <full link here>", inline=False)
		embed.set_footer(text=setfootertext, icon_url=setfooterimage)
		await ctx.send(embed=embed)
		return
	raise error


bot.run(bottoken)
