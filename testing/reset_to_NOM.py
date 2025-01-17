import asyncio
from config import * # Hide your secrets!
from sessypy.devices import SessyDevice, SessyP1Meter, SessyBattery, get_sessy_device, SessyPowerStrategy
import pprint

async def run():
    battery = await get_sessy_device(SESSY_BATTERY_HOST, SESSY_BATTERY_USERNAME, SESSY_BATTERY_PASSWORD)

    # First, try to get the power status:
    res = await battery.get_power_status()
    print("Power status:")
    pprint.pprint(res)

    # Set power stratergy to API
    res = await battery.set_power_strategy(SessyPowerStrategy.NOM)
    print('Result set power strategy:')
    pprint.pprint(res)


    # Now get power strategy
    res = await battery.get_power_strategy()
    print('Power strategy:')
    pprint.pprint(res)

    # Close and go
    await battery.close()

asyncio.run(run())

