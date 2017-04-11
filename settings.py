"""This class is used to make CRUD operations on the settings."""

import ConfigParser
import logger

titleKeyURL = ''


def create_settings():
    """Create an empty settings file."""
    settings = ConfigParser.RawConfigParser()
    settings.add_section('Settings')
    settings.set('Settings', 'titleKeyURL', '')
    with open('settings.cfg', 'wb') as settingsfile:
        settings.write(settingsfile)


def read_settings():
    """Load settings from file."""
    settings = ConfigParser.RawConfigParser()
    settings.read('settings.cfg')
    global titleKeyURL
    titleKeyURL = settings.get('Settings', 'titleKeyURL')


def save_settings():
    """Write settings to file."""
    settings = ConfigParser.RawConfigParser()
    settings.add_section('Settings')
    settings.set('Settings', 'titleKeyURL', titleKeyURL)
    with open('settings.cfg', 'wb') as settingsfile:
        settings.write(settingsfile)


def set_title_key_url(url):
    """Set the title key url"""
    global titleKeyURL
    titleKeyURL = url

try:
    with open('settings.cfg') as settingsfile:
        read_settings()
except IOError as e:
    logger.log("No config file, so one is being created")
    logger.log("Please edit the config file and try again")
    create_settings()