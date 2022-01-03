# -- Importing Packages -- #
import os, random
import discord
from discord import Client, Intents, Embed
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_commands import create_option
from googleapiclient.discovery import build


# -- Logs "IMAGE BOT" Text in Console -- #
from pyfiglet import figlet_format

banner = figlet_format('IMAGE\n BOT')
print(banner)


# -- Webserver to host it you can host it uptimerobot.com or remove it if you dont want to use -- #
from webserver import keep_alive


# -- Bot Setup -- #
client = Client(intents=Intents.default())
slash = SlashCommand(client)
api_key = 'AIzaSyABKQ8N0zoh3JSz0PM6QrhG-jbmh-Tw9d4'


# -- Messages In Console When Bot Get's Logged In + Bot Status -- #
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(
        type=discord.ActivityType.watching,
        name='Image Bot || Made by RLX'))
    print('Bot Is Online')


# -- Command -- #
@slash.slash(name='image',
             description='shows a specific image',
             options=[
                 create_option(name='search',
                               description='search an image',
                               required=True,
                               option_type=3)
             ])
async def image(ctx: SlashContext, *, search: str):
    ran = random.randint(0, 9)
    resource = build('customsearch', 'v1', developerKey=api_key).cse()
    result = resource.list(q=f'{search}',
                           cx='013d682ac094eda30',
                           searchType="image").execute()
    url = result['items'][ran]['link']
    embed = Embed(
        title=f'Here's Your Search Result For **({search.title()})**')
    embed.set_image(url=url)
    await ctx.send(search, embed=embed)


# -- Webserver -- #
keep_alive()


# -- Client/Bot Login -- #
TOKEN = os.environ.get('TOKEN')
client.run(TOKEN)
