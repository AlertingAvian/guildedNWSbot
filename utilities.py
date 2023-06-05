import guilded
from guilded.ext import commands
from datetime import datetime
from dotenv import load_dotenv
import os
import concurrent
import requests
from io import BytesIO
from PIL import Image

load_dotenv()
avatar_url = os.environ['AVATAR']

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


MAX_WORKERS = os.cpu_count()


async def image_fetcher_pool(image_urls: list, ctx, title: str) -> None:
    images_bytes = {}
    with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        futures = {executor.submit(get_image, url[1], url[0]): url for url in enumerate(image_urls)}
        for future in concurrent.futures.as_completed(futures):
            url = futures[future]
            try:
                result = future.result()
            except Exception as exc:
                print(f'{url} generated an exception: {exc}')
            else:
                images_bytes[result[0]] = result[1]
    seq_bytes = BytesIO()
    images = []
    for i in range(len(image_urls)):
        images.append(images_bytes[i])
    images[0].save(seq_bytes, save_all=True, append_images=images[1::], format='WEBP')
    await send_image_hook(ctx, title, guilded.File(BytesIO(seq_bytes.getvalue()), filename="image.webp"))


def get_image(url: str, item_id: int) -> (int, Image):
    response = requests.get(url)
    return item_id, Image.open(BytesIO(response.content))


# def test():
#     response = requests.get("https://services.swpc.noaa.gov/products/animations/lasco-c3.json")
#     images = []
#     for i in response.json():
#         images.append(Image.open(BytesIO(requests.get("https://services.swpc.noaa.gov" + i['url']).content),
#                                  formats=('JPEG',)))
#     seq_bytes = BytesIO()
#     images[0].save(seq_bytes, save_all=True, append_images=images[1::], format='WEBP')
#     return BytesIO(seq_bytes.getvalue())
