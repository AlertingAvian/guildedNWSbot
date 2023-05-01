import guilded

import utilities
import weather
from weather.spc import FireOutlookType, ConvOutlookType
from guilded.ext import commands


class SPC(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.group(name="spc")
    async def spc(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.reply(f'Invalid SPC subcommand: {ctx.subcommand_passed}')

    @spc.group()
    async def day1conv(self, ctx):
        if ctx.invoked_subcommand is None:
            await self.d1c_categorical(ctx)

    @day1conv.command(name="categorical")
    async def d1c_categorical(self, ctx):
        file = guilded.File(weather.spc.day1_conv_otlk(ConvOutlookType.Categorical), filename="image.gif")
        await utilities.send_image_hook(ctx, "Day 1 Convective Outlook: Categorical", file)

    @day1conv.command(name="tornado")
    async def d1c_tornado(self, ctx):
        file = guilded.File(weather.spc.day1_conv_otlk(ConvOutlookType.Tornado), filename="image.gif")
        await utilities.send_image_hook(ctx, "Day 1 Convective Outlook: Tornado", file)

    @day1conv.command(name="wind")
    async def d1c_wind(self, ctx):
        file = guilded.File(weather.spc.day1_conv_otlk(ConvOutlookType.Wind), filename="image.gif")
        await utilities.send_image_hook(ctx, "Day 1 Convective Outlook: Wind", file)

    @day1conv.command(name="hail")
    async def d1c_hail(ctx):
        file = guilded.File(weather.spc.day1_conv_otlk(ConvOutlookType.Hail), filename="image.gif")
        await utilities.send_image_hook(ctx, "Day 1 Convective Outlook: Hail", file)

    @spc.group()
    async def day2conv(self, ctx):
        if ctx.invoked_subcommand is None:
            await self.d2c_categorical(ctx)

    @day2conv.command(name="categorical")
    async def d2c_categorical(self, ctx):
        file = guilded.File(weather.spc.day2_conv_otlk(ConvOutlookType.Categorical), filename="image.gif")
        await utilities.send_image_hook(ctx, "Day 2 Convective Outlook: Categorical", file)

    @day2conv.command(name="tornado")
    async def d2c_tornado(self, ctx):
        file = guilded.File(weather.spc.day2_conv_otlk(ConvOutlookType.Tornado), filename="image.gif")
        await utilities.send_image_hook(ctx, "Day 2 Convective Outlook: Tornado", file)

    @day2conv.command(name="wind")
    async def d2c_wind(self, ctx):
        file = guilded.File(weather.spc.day2_conv_otlk(ConvOutlookType.Wind), filename="image.gif")
        await utilities.send_image_hook(ctx, "Day 2 Convective Outlook: Wind", file)

    @day2conv.command(name="hail")
    async def d2c_hail(self, ctx):
        file = guilded.File(weather.spc.day2_conv_otlk(ConvOutlookType.Hail), filename="image.gif")
        await utilities.send_image_hook(ctx, "Day 2 Convective Outlook: Hail", file)

    @spc.group()
    async def day3conv(self, ctx):
        if ctx.invoked_subcommand is None:
            await self.d3c_categorical(ctx)

    @day3conv.command(name="categorical")
    async def d3c_categorical(self, ctx):
        file = guilded.File(weather.spc.day3_conv_otlk(ConvOutlookType.Categorical), filename="image.gif")
        await utilities.send_image_hook(ctx, "Day 3 Convective Outlook: Categorical", file)

    @day3conv.command(name="probabilistic")
    async def d3c_probabilistic(self, ctx):
        file = guilded.File(weather.spc.day3_conv_otlk(ConvOutlookType.Probabilistic), filename="image.gif")
        await utilities.send_image_hook(ctx, "Day 3 Convective Outlook: Probabilistic", file)

    @spc.command(name="day48conv")
    async def day48_conv(self, ctx):
        file = guilded.File(weather.spc.day48_conv_otlk(), filename="image.gif")
        await utilities.send_image_hook(ctx, "Day 4-8 Convective Outlook", file)

    @spc.command(name="day1fire")
    async def day1_fire(self, ctx):
        file = guilded.File(weather.spc.day1_fire_otlk(), filename="image.gif")
        await utilities.send_image_hook(ctx, "Day 1 Fire Outlook", file)

    @spc.command(name="day2fire")
    async def day2_fire(self, ctx):
        file = guilded.File(weather.spc.day2_fire_otlk(), filename="image.gif")
        await utilities.send_image_hook(ctx, "Day 2 Fire Outlook", file)

    @spc.group()
    async def day38fire(self, ctx):
        if ctx.invoked_subcommand is None:
            await self.d3cf_categorical(ctx)

    @day38fire.command(name="categorical")
    async def d3cf_categorical(self, ctx):
        file = guilded.File(weather.spc.day38_fire_otlk(FireOutlookType.Categorical), filename="image.gif")
        await utilities.send_image_hook(ctx, "Day 3-8 Fire Outlook: Categorical", file)

    @day38fire.command(name="dryt")
    async def d3cf_dryt(self, ctx):
        file = guilded.File(weather.spc.day38_fire_otlk(FireOutlookType.DryT), filename="image.gif")
        await utilities.send_image_hook(ctx, "Day 3-8 Fire Outlook: DryT/LowRH/Wind", file)