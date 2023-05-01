from PIL import Image
import requests
from io import BytesIO
from enum import Enum


NWS_LOGO: str = "https://www.spc.noaa.gov/nwscwi/nwsright.jpg"


class ConvOutlookType(Enum):
    """
        Outlook type:
        Categorical = 0
        Tornado = 1
        Wind = 2
        Hail = 3
        Probabilistic = 4
    """
    Categorical = 0
    Tornado = 1
    Wind = 2
    Hail = 3
    Probabilistic = 4


class FireOutlookType(Enum):
    """
        Outlook type:
        Categorical = 0
        DryT/LowRH/Wind = 1
    """
    Categorical = 0
    DryT = 1  # DryT/LowRH/Wind


def day1_conv_otlk(outlook_type: ConvOutlookType = ConvOutlookType.Categorical) -> BytesIO:
    """
        Get gif of the Day 1 Convective Outlook.

        Parameters
        ----------
        outlook_type : ConvOutlookType, optional
            The outlook type to get. Only valid options are: Categorical, Tornado, Wind, and Hail.
            The default is ConvOutlookType.Categorical.

        Returns
        -------
        Image
            The image gotten from the SPC. Is the NWS logo when an error is encountered.

    """
    match outlook_type:
        case outlook_type.Categorical:
            response = requests.get("https://www.spc.noaa.gov/products/outlook/day1otlk.gif")
        case outlook_type.Tornado:
            response = requests.get("https://www.spc.noaa.gov/products/outlook/day1probotlk_torn.gif")
        case outlook_type.Wind:
            response = requests.get("https://www.spc.noaa.gov/products/outlook/day1probotlk_wind.gif")
        case outlook_type.Hail:
            response = requests.get("https://www.spc.noaa.gov/products/outlook/day1probotlk_hail.gif")
        case _:
            response = requests.get(NWS_LOGO)

    return BytesIO(response.content)


def day2_conv_otlk(outlook_type: ConvOutlookType = ConvOutlookType.Categorical) -> BytesIO:
    """
        Get gif of the Day 2 Convective Outlook.

        Parameters
        ----------
        outlook_type : ConvOutlookType, optional
            The outlook type to get. Only valid options are: Categorical, Tornado, Wind, and Hail.
            The default is ConvOutlookType.Categorical.

        Returns
        -------
        Image
            The image gotten from the SPC. Is the NWS logo when an error is encountered.

    """
    match outlook_type:
        case outlook_type.Categorical:
            response = requests.get("https://www.spc.noaa.gov/products/outlook/day2otlk.gif")
        case outlook_type.Tornado:
            response = requests.get("https://www.spc.noaa.gov/products/outlook/day2probotlk_torn.gif")
        case outlook_type.Wind:
            response = requests.get("https://www.spc.noaa.gov/products/outlook/day2probotlk_wind.gif")
        case outlook_type.Hail:
            response = requests.get("https://www.spc.noaa.gov/products/outlook/day2probotlk_hail.gif")
        case _:
            response = requests.get(NWS_LOGO)

    return BytesIO(response.content)


def day3_conv_otlk(outlook_type: ConvOutlookType = ConvOutlookType.Categorical) -> BytesIO:
    """
        Get gif of the Day 3 Convective Outlook.

        Parameters
        ----------
        outlook_type : ConvOutlookType, optional
            The outlook type to get. Only valid options are: Categorical, and Probabilistic.
            The default is ConvOutlookType.Categorical.

        Returns
        -------
        Image
            The image gotten from the SPC. Is the NWS logo when an error is encountered.

    """
    match outlook_type:
        case outlook_type.Categorical:
            response = requests.get("https://www.spc.noaa.gov/products/outlook/day3otlk.gif")
        case outlook_type.Probabilistic:
            response = requests.get("https://www.spc.noaa.gov/products/outlook/day3prob.gif")

        case _:
            response = requests.get(NWS_LOGO)

    return BytesIO(response.content)


def day48_conv_otlk() -> BytesIO:
    """
        Get gif of the Day 4-8 Convective Outlook.

        Returns
        -------
        Image
            The image gotten from the SPC.

    """
    response = requests.get("https://www.spc.noaa.gov/products/exper/day4-8/day48prob.gif")
    return BytesIO(response.content)


def day1_fire_otlk() -> BytesIO:
    """
        Get gif of the Day 1 Fire Outlook.

        Returns
        -------
        Image
            The image gotten from the SPC.

    """
    response = requests.get("https://www.spc.noaa.gov/products/fire_wx/day1otlk_fire.gif")
    return BytesIO(response.content)


def day2_fire_otlk() -> BytesIO:
    """
        Get gif of the Day 2 Fire Outlook.

        Returns
        -------
        Image
            The image gotten from the SPC.

    """
    response = requests.get("https://www.spc.noaa.gov/products/fire_wx/day2otlk_fire.gif")
    return BytesIO(response.content)


def day38_fire_otlk(outlook_type: FireOutlookType = FireOutlookType.Categorical) -> BytesIO:
    """
        Get gif of the Day 3-8 Fire Outlook.

        Parameters
        ----------
        outlook_type : ConvOutlookType, optional
            The outlook type to get. Only valid options are: Categorical, and DryT.
            The default is ConvOutlookType.Categorical.

        Returns
        -------
        Image
            The image gotten from the SPC. Is the NWS logo when an error is encountered.

    """
    match outlook_type:
        case outlook_type.Categorical:
            response = requests.get("https://www.spc.noaa.gov/products/exper/fire_wx/imgs/day38otlk_fire.gif")
        case outlook_type.DryT:
            response = requests.get("https://www.spc.noaa.gov/products/exper/fire_wx/imgs/day38fireprob.gif")
        case _:
            response = requests.get(NWS_LOGO)

    return BytesIO(response.content)
