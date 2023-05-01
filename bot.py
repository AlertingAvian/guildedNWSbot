import guilded
from guilded.ext import commands
from dotenv import load_dotenv
import radar_cog
import spc_cog
import swpc_cog
import os

description = 'A bot to get information from NOAA/NWS'

bot = commands.Bot(command_prefix=["!nws ", "!noaa "], description=description)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')
    print('Loading Cogs')
    bot.add_cog(spc_cog.SPC(bot))
    print('Loaded SPC cog')
    bot.add_cog(swpc_cog.SWPC(bot))
    print('Loaded SWPC cog')
    bot.add_cog(radar_cog.Radar_Cog(bot))
    print('Loaded Radar cog')
    print('Cog loading complete')
    print('------')


@bot.command(name="ping")
async def ping(ctx):
    await ctx.reply('Pong.')

load_dotenv()
bot.run(os.environ['TOKEN'])
