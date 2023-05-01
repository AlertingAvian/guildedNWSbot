from io import BytesIO
import requests

WU_LOCATIONS = {("CONUS", "US"): "conus",
                ("ALASKA", "AK"): "alask",
                ("ARKANSAS", "AR"): "uslit",
                ("ARIZONA", "AZ"): "usprc",
                ("CALIFORNIA", "CA"): "usbfl",
                ("COLORADO", "CO"): "usden",
                ("CONNECTICUT", "CT"): "ushfd",
                ("FLORIDA SOUTH", "FL S"): "useyw",
                ("FLORIDA", "FL"): "uspie",
                ("GEORGIA", "GA"): "uscgs",
                ("HAWAII", "HI"): "hawai",
                ("IOWA", "IA"): "usdsm",
                ("IDAHO", "ID"): "usmyl",
                ("ILLINOIS", "IL"): "usspi",
                ("KANSAS", "KS"): "ussln",
                ("KENTUCKY", "KY"): "usbwg",
                ("LOUISIANA", "LA"): "usmsy",
                ("MICHIGAN", "MI"): "uscad",
                ("MINNESOTA", "MN"): "usstc",
                ("MISSOURI", "MO"): "usjef",
                ("MISSISSIPPI", "MS"): "ustvr",
                ("MONTANA", "MT"): "uslwt",
                ("NORTH CAROLINA", "NC"): "usclt",
                ("NORTH DAKOTA", "ND"): "usbis",
                ("NEBRASKA", "NE"): "uslbf",
                ("NEW HAMPSHIRE", "NH"): "usbml",
                ("NEW MEXICO", "NM"): "usrow",
                ("NEVADA", "NV"): "usrno",
                ("NEW YORK", "NY"): "usbgm",
                ("OHIO", "OH"): "usday",
                ("OKLAHOMA", "OK"): "uslaw",
                ("OREGON", "OR"): "usrdm",
                ("PUERTO RICO", "PR"): "prico",
                ("SOUTH DAKOTA", "SD"): "uspir",
                ("TEXAS SOUTH", "TX S"): "usbro",
                ("TEXAS", "TX"): "ussat",
                ("UTAH", "UT"): "uspvu",
                ("VIRGINIA EAST", "VA E"): "usfcx",
                ("VIRGINIA", "VA"): "usshd",
                ("WASHINGTON", "WA"): "ustiw",
                ("WYOMING", "WY"): "usriw"}


def nws_conus_radar() -> BytesIO:
    """
        Get image of the CONUS base reflectivity.

        Returns
        -------
        Image
            The image gotten from the NWS.

    """
    response = requests.get("https://radar.weather.gov/ridge/standard/CONUS_loop.gif")
    return BytesIO(response.content)


def nws_alaska_radar() -> BytesIO:
    """
        Get image of the ALASKA base reflectivity.

        Returns
        -------
        Image
            The image gotten from the NWS.

    """
    response = requests.get("https://radar.weather.gov/ridge/standard/ALASKA_loop.gif")
    return BytesIO(response.content)


def nws_hawaii_radar() -> BytesIO:
    """
        Get image of the HAWAII base reflectivity.

        Returns
        -------
        Image
            The image gotten from the NWS.

    """
    response = requests.get("https://radar.weather.gov/ridge/standard/HAWAII_loop.gif")
    return BytesIO(response.content)


def nws_guam_radar() -> BytesIO:
    """
        Get image of the GUAM base reflectivity.

        Returns
        -------
        Image
            The image gotten from the NWS.

    """
    response = requests.get("https://radar.weather.gov/ridge/standard/GUAM_loop.gif")
    return BytesIO(response.content)


def nws_station_radar(wfo: str) -> BytesIO:
    """
        Get image of the WFO's base reflectivity.

        Parameters
        ----------
        wfo : str
            The weather forecast office to fetch the base reflectivity image from.

        Returns
        -------
        Image
            The image gotten from the SPC. Is the NWS logo when an error is encountered.

        Raises
        ------
        requests.RequestException
            Raised when an invalid wfo is passed and the lookup 404s.
    """
    if wfo in ("CONUS", "HAWAII", "GUAM", "ALASKA"):
        print(f"functions available for wfo {wfo} -> nws_{wfo.lower()}_radar()")
    response = requests.get(f"https://radar.weather.gov/ridge/standard/{wfo}_loop.gif")
    if response.status_code != 200:
        raise requests.RequestException(f'The wfo: {wfo} was invalid and returned status code 404')
    return BytesIO(response.content)


def wu_radar(loc: str, tracks: bool = False) -> BytesIO:
    """
        Get image of the radar from Weather Underground.

        Parameters
        ----------
        loc : str
            The state (or CONUS) to grab the image from.

        tracks: bool, optional
            Whether of not to show storm tracks. Default False.

        Returns
        -------
        Image
            The image gotten from the SPC. Is the NWS logo when an error is encountered.

        Raises
        ------
        ValueError
            Raised when an invalid loc is passed.
    """
    wu_loc = ""
    for key, value in WU_LOCATIONS.items():
        if loc.upper() in key:
            wu_loc = value
            break
    if not wu_loc:
        raise ValueError(f"loc provided: '{loc}' did not match any available locations")
    else:
        if tracks:
            response = requests.get(f"https://s.w-x.co/staticmaps/wu/wu/radsum1200_cur/{wu_loc}/animate.png")
            return BytesIO(response.content)
        else:
            response = requests.get(f"https://s.w-x.co/staticmaps/wu/wu/wxtype1200_cur/{wu_loc}/animate.png")
            return BytesIO(response.content)
