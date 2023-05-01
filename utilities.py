import guilded
from guilded.ext import commands
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()
avatar_url = os.environ['avatar']

async def send_image_hook(ctx, title: str, file):
    embed = guilded.Embed(title=title,
                          colour=0x071f66,
                          timestamp=datetime.now())
    hook = await ctx.channel.create_webhook(name=title)
    if isinstance(list(), type(file)):
        await hook.send(embed=embed, files=file, avatar_url=avatar_url)
    else:
        await hook.send(embed=embed, file=file, avatar_url=avatar_url)
    await hook.delete()
