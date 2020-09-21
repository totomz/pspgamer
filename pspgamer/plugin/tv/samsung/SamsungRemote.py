import logging
import socket
import sys
import time

logging.basicConfig(level=logging.DEBUG, handlers=[logging.StreamHandler(sys.stdout)])

import samsungctl
config = {
    "name": "samsungctl",
    "description": "PC",
    "id": "",
    "host": "192.168.10.108",
    "port": 55000,
    "method": "legacy",
    "timeout": 0,
}


class SamsungRemote:

    def __init__(self):
        print("Looking for a TV")

    def power_off(self):
        with samsungctl.Remote(config) as remote:
            for i in range(10):
                remote.control("KEY_VOLUP")
                time.sleep(0.5)


print("mah")
samsung = SamsungRemote()
samsung.power_off()
print("dio")
