import discord
import configparser
import time
from discord.ext import commands
from plugins import rand_joke, cryptoPrice, saucenao, translater, image, dice, youtube as yt, helper
import os

description = '''A simple discord bot using discord.py'''
client = discord.Client()
bot = commands.Bot(command_prefix='/', description=description)


start = time.time()

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command(name='yt', description='Returns the first video result from youtube')
async def youtube(*args : str, ctx):
    query = ' '.join(args)
    url = yt.getVideo(query, config['DEFAULT']['GOOGLE_KEY'])

    if url is None:
        await bot.say('Unable to retrieve information ... ')
        return

    await ctx.send(url)


@bot.command(name='translate', description='Translates english to japanese or vice versa')
async def translate(target : str, *args : str, ctx):
    message = ' '.join(args)

    if target == 'ja':
        result = translater.getTranslation(target, message, config['DEFAULT']['GOOGLE_KEY'])
        embed = discord.Embed(title='Japanese translation', description=result, color=0x7289da)
    else:
        result = translater.getTranslation(target, message, config['DEFAULT']['GOOGLE_KEY'])
        embed = discord.Embed(title='English translation', description=result, color=0x7289da)

    await ctx.send(embed=embed)


@bot.command(name='price', description='Retrieves the price of a cryptocurrency.')
async def price(name : str, ctx ):
    coin = cryptoPrice.getPrice(name,)

    if coin is None:
        await ctx.send('Unable to retrieve information ... ')
        return

    message = '$ {}  |  ({}%) 24h'.format(coin['price_usd'], coin['percent_change_24h'])
    embed = discord.Embed(title=name, description=message, color=0x7289da)

    await ctx.send(embed=embed)

@bot.command(name='joke', description='Returns a random joke to the user.')
async def joke(ctx):
    result = rand_joke.getJoke()
    embed = discord.Embed(title='Joke', description=result, color=0x7289da)

    await ctx.send(embed=embed)


@bot.command(name='status', description='Returns the status of the bot.')
async def status(ctx):
    day, hour, minutes, seconds = helper.getElapsedTime((time.time() - start))
    message = '{}d, {}h, {}m, {}s'.format(day, hour, minutes, seconds)

    embed = discord.Embed(title=' ', description=' ', color=0x7289da)
    embed.add_field(name='Online', value=message)
    embed.add_field(name='Servers', value=str(len(bot.guilds)))

    await ctx.send(embed=embed)


bot.run(os.getenv('token'))
