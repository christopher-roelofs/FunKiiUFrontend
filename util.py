"""This is a utility class to help with misc tasks"""

import urllib
import settings
from logger import *

def download_titlekeys_json():
    log("Attempting to download titlekey json...")
    try:
        urllib.urlretrieve(settings.titleKeyURL,'titlekeys.json')
    except Exception as error:
        log(error)