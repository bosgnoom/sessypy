# Hide your secrets in config.py
from config import * 

# Import modules
import asyncio
from sessypy.devices import SessyDevice, get_sessy_device
from sessypy.errorlog import get_error_log

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
        
        # Get errors from sessypi
        errors = await get_error_log(device)

        # Convert into InfluxDB's line protocol
        # myMeasurement,tag1=value1,tag2=value2 fieldKey="fieldValue" 1556813561098000000 (unix timestamp in ns)
        for err in errors:
            date_obj, error_type, message = err
            # print(f'errors,device={device.serial_number} {error_type}={message} {int(date_obj.timestamp()*10**9)}')
        
        await device.close()

asyncio.run(run())