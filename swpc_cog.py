import guilded
from guilded.ext import commands
import weather
import utilities
from weather.swpc import Direction


class SWPC(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.group()
    async def swpc(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.reply(f'Invalid SWPC subcommand: {ctx.subcommand_passed}')

    @swpc.group(name="aurora-viewline")
    async def aurora_viewline(self, ctx):
        if ctx.invoked_subcommand is None:
            await self.viewline_tonight(ctx)

    @aurora_viewline.command(name="tonight")
    async def viewline_tonight(self, ctx):
        file = guilded.File(weather.swpc.tonight_aurora_viewline(), filename="image.png")
        await utilities.send_image_hook(ctx, "Tonight's Aurora Forecast", file)

    @aurora_viewline.command(name="tomorrow")
    async def viewline_tomorrow(self, ctx):
        file = guilded.File(weather.swpc.tomorrow_aurora_viewline(), filename="image.png")
        await utilities.send_image_hook(ctx, "Tomorrow Night's Aurora Forecast", file)

    @swpc.group(name="aurora-forecast")
    async def aurora_forecast(self, ctx):
        if ctx.invoked_subcommand is None:
            await self.aurora_north(ctx)

    @aurora_forecast.command(name="north")
    async def aurora_north(self, ctx):
        await weather.swpc.aurora_forecast(Direction.North, ctx)

    @aurora_forecast.command(name="south")
    async def aurora_south(self, ctx):
        await weather.swpc.aurora_forecast(Direction.South, ctx)

    @swpc.command(name="cme")
    async def cme_gif(self, ctx):
        await weather.swpc.cme_gif(ctx)
