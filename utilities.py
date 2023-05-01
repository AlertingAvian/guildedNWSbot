import guilded
from guilded.ext import commands
from datetime import datetime

# todo: doc string


async def send_image_hook(ctx, title: str, file):
    embed = guilded.Embed(title=title,
                          colour=0x071f66,
                          timestamp=datetime.now())
    hook = await ctx.channel.create_webhook(name=title)
    if isinstance(list(), type(file)):
        await hook.send(embed=embed, files=file, avatar_url="https://www.dropbox.com/s/to6e6xqv4ycvb8x/US"
                                                            "-NationalWeatherService-Logo.png?dl=1")
    else:
        await hook.send(embed=embed, file=file, avatar_url="https://www.dropbox.com/s/to6e6xqv4ycvb8x/US"
                                                           "-NationalWeatherService-Logo.png?dl=1")
    await hook.delete()
