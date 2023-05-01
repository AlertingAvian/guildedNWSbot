import requests
from io import BytesIO
from enum import Enum
from PIL import Image

import utilities

NWS_LOGO: str = "https://www.spc.noaa.gov/nwscwi/nwsright.jpg"


class Direction(Enum):
    North = 0
    South = 1


async def aurora_forecast(hemisphere: Direction, ctx):
    """
        Get image of the Aurora forecast.

        Returns
        -------
        Image
            The image sequence as a WEBP gotten from the SWPC.

    """
    match hemisphere:
        case hemisphere.North:
            url = "https://services.swpc.noaa.gov/products/animations/ovation_north_24h.json"
        case hemisphere.South:
            url = "https://services.swpc.noaa.gov/products/animations/ovation_south_24h.json"
        case _:
            url = NWS_LOGO  # this will error, so don't I guess
    response = requests.get(url)
    images = []
    for i in response.json():
        images.append("https://services.swpc.noaa.gov" + i['url'])
    await utilities.image_fetcher_pool(images, ctx, "Aurora Forecast")


def tonight_aurora_viewline() -> BytesIO:
    response = requests.get("https://services.swpc.noaa.gov/experimental/images/aurora_dashboard"
                            "/tonights_static_viewline_forecast.png")
    return BytesIO(response.content)


def tomorrow_aurora_viewline() -> BytesIO:
    """
        Get image of tomorrow's Aurora forecast.

        Returns
        -------
        Image
            The image sequence as a WEBP gotten from the SWPC.

    """
    response = requests.get("https://services.swpc.noaa.gov/experimental/images/aurora_dashboard"
                            "/tomorrow_nights_static_viewline_forecast.png")
    return BytesIO(response.content)


async def cme_gif(ctx):  # in an effort to speed this up i have broken the general flexibility of this
    """
        Get image of the coronal mass ejection.

        Returns
        -------
        Image
            The image sequence as a WEBP gotten from the SWPC.

    """
    response = requests.get("https://services.swpc.noaa.gov/products/animations/lasco-c3.json")
    images = []
    for i in response.json():
        images.append("https://services.swpc.noaa.gov" + i['url'])
    await utilities.image_fetcher_pool(images, ctx, "Coronal Mass Ejections")
