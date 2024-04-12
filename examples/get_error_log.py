# Hide your secrets in config.py
from config import * 

# Import modules
import asyncio
from sessypy.devices import SessyDevice, get_sessy_device
from sessypy.errorlog import get_error_log
import pprint

import logging
# While debugging
logging.basicConfig(level=logging.DEBUG)


async def run():
    devices = list()

    devices.append(
        await get_sessy_device(SESSY_BATTERY_HOST, SESSY_BATTERY_USERNAME, SESSY_BATTERY_PASSWORD)
    )
    devices.append(
        await get_sessy_device(SESSY_P1_HOST, SESSY_P1_USERNAME, SESSY_P1_PASSWORD)
    )
    device: SessyDevice

    for device in devices:
        # Show for which device 
        logging.info(f"=== Sessy Device at { device.host } ===")
        logging.info(f"S/N: {device.serial_number}")
        
        # Get errors from sessypy
        errors = await get_error_log(device)

        pprint.pprint(errors, width=150)
        
        await device.close()

asyncio.run(run())