"""This is a utility class to help with misc tasks"""

import urllib
import settings
from logger import *
import binascii
import os

funkiiu_url = "https://raw.githubusercontent.com/llakssz/FunKiiU/master/FunKiiU.py"

try:
    import FunKiiU as fnk
except Exception as e:
    pass

def download_titlekeys_json():
    log("Attempting to download titlekey json...")
    try:
        urllib.urlretrieve(settings.titleKeyURL + "json", "titlekeys.json")
        log("titlekeys.json successfully downloaded.")
    except Exception as error:
        log(error)

def decode_titleid(titleid):
    if titleid[4:8] == '0000':
        content_type = 'GAME'
    elif titleid[4:8] == '000c':
        content_type = 'DLC'
    elif titleid[4:8] == '000e':
        content_type = 'UPDATE'
    elif titleid[4:8] == '0002':
        content_type = 'DEMO'
    return content_type

def get_title_size(titleid):
    baseurl = 'http://ccs.cdn.c.shop.nintendowifi.net/ccs/download/{}'.format(titleid)
    TK = fnk.TK
    if not fnk.download_file(baseurl + '/tmd', 'title.tmd', 1):
        print('ERROR: Could not download TMD...')
    else:
        with open('title.tmd', 'rb') as f:
            tmd = f.read()
        content_count = int(binascii.hexlify(tmd[TK + 0x9E:TK + 0xA0]), 16)

        total_size = 0
        for i in range(content_count):
            c_offs = 0xB04 + (0x30 * i)
            c_id = binascii.hexlify(tmd[c_offs:c_offs + 0x04]).decode()
            total_size += int(binascii.hexlify(tmd[c_offs + 0x08:c_offs + 0x10]), 16)
    os.remove('title.tmd')
    return fnk.bytes2human(total_size)

def download_funkiiu():
    try:
        urllib.urlretrieve(funkiiu_url, "FunKiiU.py")
        log("FunKiiU successfully downloaded.")
    except Exception as error:
        log(error)