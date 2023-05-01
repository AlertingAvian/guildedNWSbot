import requests
from io import BytesIO
from enum import Enum
from PIL import Image


NWS_LOGO: str = "https://www.spc.noaa.gov/nwscwi/nwsright.jpg"


class Direction(Enum):
    North = 0
    South = 1


def aurora_forcast(hemisphere: Direction) -> BytesIO:
    """
    Get image of the Aurora forcast.

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
        images.append(Image.open(BytesIO(requests.get("https://services.swpc.noaa.gov" + i['url']).content),
                                 formats=('JPEG', 'PNG')))
    seq_bytes = BytesIO()
    images[0].save(seq_bytes, save_all=True, append_images=images[1::], format='WEBP')
    return BytesIO(seq_bytes.getvalue())


def tonight_aurora_viewline() -> BytesIO:
    response = requests.get("https://services.swpc.noaa.gov/experimental/images/aurora_dashboard"
                            "/tonights_static_viewline_forecast.png")
    return BytesIO(response.content)


def tomorrow_aurora_viewline() -> BytesIO:
    response = requests.get("https://services.swpc.noaa.gov/experimental/images/aurora_dashboard"
                            "/tomorrow_nights_static_viewline_forecast.png")
    return BytesIO(response.content)


def cme_gif() -> BytesIO:
    response = requests.get("https://services.swpc.noaa.gov/products/animations/lasco-c3.json")
    images = []
    for i in response.json():
        images.append(Image.open(BytesIO(requests.get("https://services.swpc.noaa.gov" + i['url']).content),
                                 formats=('JPEG',)))
    seq_bytes = BytesIO()
    images[0].save(seq_bytes, save_all=True, append_images=images[1::], format='WEBP')
    return BytesIO(seq_bytes.getvalue())

