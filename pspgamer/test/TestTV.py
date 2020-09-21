import samsungctl

import samsungctl
import time

config = {
    "name": "samsungctl",
    "description": "PC",
    "id": "",
    "host": "192.168.0.10",
    "port": 55000,
    "method": "legacy",
    "timeout": 0,
}

with samsungctl.Remote(config) as remote:
    for i in range(10):
        remote.control("KEY_MENU")
        time.sleep(0.5)
