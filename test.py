from somecomfort import *
from somecomfort.client import *
import time
import logging
import urllib3
import json

urllib3.disable_warnings()

_LOGGER = logging.getLogger(__name__)


def main():
    password = "YourPassword"
    username = "YourUserName"
    session = requests.Session()
    session.verify = False
    try:
        client = SomeComfort(username, password, session=session)
    except AuthError as ex:
        print(str(ex))
        return 1

    devices = [
        device
        for location in client.locations_by_id.values()
        for device in location.devices_by_id.values()
    ]

    while 1:
        value = devices[0].current_temperature
        fan = devices[0].fan_running
        print(f"The Temp: {value}, Fan Status: {fan}")
        time.sleep(5)
        devices[0].refresh()


main()
