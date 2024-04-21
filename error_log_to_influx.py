# Hide your secrets in config.py
from config import * 

# Import modules
import asyncio
from sessypy.devices import SessyDevice, get_sessy_device
from sessypy.errorlog import get_error_log
import requests

import logging
# While debugging
logging.basicConfig(level=logging.DEBUG)


async def run():
    devices = [
        await get_sessy_device(SESSY_BATTERY_HOST, SESSY_BATTERY_USERNAME, SESSY_BATTERY_PASSWORD),
        await get_sessy_device(SESSY_P1_HOST, SESSY_P1_USERNAME, SESSY_P1_PASSWORD)
    ]

    payload = []

    for device in devices:
        # Show for which device 
        logging.info(f"=== Sessy Device at { device.host } ===")
        logging.info(f"S/N: {device.serial_number}")
        
        # Get errors from sessypy
        errors = await get_error_log(device)

        # Convert into InfluxDB's line protocol:
        # myMeasurement,tag1=value1,tag2=value2 fieldKey="fieldValue" 1556813561098000000 (unix timestamp in ns)
        for err in errors:
            date_obj, error_type, message = err
            payload.append(f'errors,device={device.serial_number} {error_type.replace(" ", "_")}="{message}" {int(date_obj.timestamp())}')
        
        await device.close()

    return payload
    

payload = asyncio.run(run())

# Prepare request, BUCKET, ORG, URL and TOKEN from config.py
params = { 'bucket': BUCKET, 'org': ORG, 'precision': 's' }
headers = {'Authorization': f'Token {TOKEN}'}

# Write data into influxdb
try:
    # Send request to influx server
    r = requests.post(URL, headers=headers, params=params, data='\n'.join(payload))

    # Check response
    if r.status_code != 204:
        print(f'Influx returned status {r.status_code}\n{r.text}')
except Exception as e:
    print(f'Error: {e}')
