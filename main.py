import requests
import discord
from discord.ext import commands
from bs4 import BeautifulSoup
import json
bot = commands.Bot(command_prefix="*")


@bot.command()
async def stats(ctx, *, username):
    parsedUsername = username.replace(" ", "%20")
    playerStats = requests.get(f"https://www.wof.gg/stats/{parsedUsername}/")
    soup = BeautifulSoup(playerStats.text, "html.parser")
    hoursPlayed = soup.select("#time-hours")
    final = hoursPlayed[0].text
    await ctx.send(final)


@bot.command()
async def fuckyou(ctx):
    await ctx.send("everybody in here is a nigger")

@bot.command()
async def fuckyouray(ctx):
    await ctx.send("ray has a vagina")


@bot.command()
async def clear(ctx, amount=10230):
    await ctx.channel.purge(limit=amount)


@bot.command()
async def weather(ctx, *, zip_code):
    url = f"http://api.openweathermap.org/data/2.5/weather?zip={zip_code}&appid=fc5169ad2b9a42e269cea4914a158dff"
    res = requests.get(url)
    data = res.json()
    temp = data['main']['temp']
    temp = 1.8 * (temp - 273) + 32
    temp = round(temp, 1)
    name = data['name']
    feels = data['main']['feels_like']
    feels = 1.8 * (feels - 273) + 32
    feels = round(feels, 1)
    message = f'Currently it is {temp} degrees in {name} and feels like {feels} degrees'
    await ctx.send(message)
bot.run("Njc1NTYwNjkzODg5NjMwMjA4.Xj5Hgw.Y_DoUv2QqhmnbTFceWvor-X8wW0")