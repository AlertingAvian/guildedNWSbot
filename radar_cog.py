import guilded

import utilities
import weather
from guilded.ext import commands
from requests import RequestException


class Radar_Cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.group(name="radar")
    async def radar_group(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.reply(f'Invalid radar subcommand: {ctx.subcommand_passed}')

    @radar_group.group(case_insensitive=True)
    async def nws(self, ctx):
        if ctx.invoked_subcommand is None:
            wfo = str(ctx.subcommand_passed).upper()

            try:
                file = guilded.File(weather.radar.nws_station_radar(wfo), filename="image.gif")
            except RequestException:
                await ctx.reply(f"Invalid WFO: {wfo}")
            else:
                await utilities.send_image_hook(ctx, f"{wfo} Radar, Source: NWS", file)

    @nws.command(name="conus")
    async def conus_radar(self, ctx):
        file = guilded.File(weather.radar.nws_conus_radar(), filename="image.gif")
        await utilities.send_image_hook(ctx, "CONUS Radar, Source: NWS", file)

    @nws.command(name="alaska")
    async def alaska_radar(self, ctx):
        file = guilded.File(weather.radar.nws_alaska_radar(), filename="image.gif")
        await utilities.send_image_hook(ctx, "ALASKA Radar, Source: NWS", file)

    @nws.command(name="hawaii")
    async def hawaii_radar(self, ctx):
        file = guilded.File(weather.radar.nws_hawaii_radar(), filename="image.gif")
        await utilities.send_image_hook(ctx, "HAWAII Radar, Source: NWS", file)

    @nws.command(name="guam")
    async def guam_radar(self, ctx):
        file = guilded.File(weather.radar.nws_guam_radar(), filename="image.gif")
        await utilities.send_image_hook(ctx, "GUAM Radar, Source: NWS", file)

    @radar_group.group(name="wu")
    async def wu_radar(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.reply(f'Invalid WU subcommand: {ctx.subcommand_passed}')

    @wu_radar.command(name="tracked")
    async def wu_tracked_radar(self, ctx, *, arg):
        loc = str(arg).upper()
        try:
            file = guilded.File(weather.radar.wu_radar(loc, tracks=True), filename="image.png")
        except ValueError:
            ctx.reply(f"Invalid location: {loc}")
        else:
            await utilities.send_image_hook(ctx, f"{loc} Radar, Source: Weather Underground", file)

    @wu_radar.command(name="untracked")
    async def wu_untracked_radar(self, ctx, *, arg):
        loc = str(arg).upper()
        try:
            file = guilded.File(weather.radar.wu_radar(loc, tracks=False), filename="image.png")
        except ValueError:
            ctx.reply(f"Invalid location: {loc}")
        else:
            await utilities.send_image_hook(ctx, f"{loc} Radar, Source: Weather Underground", file)
