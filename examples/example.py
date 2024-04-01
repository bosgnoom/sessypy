import asyncio
from config import * # Hide your secrets in example.py
from sessypy.devices import SessyDevice, SessyP1Meter, SessyBattery, get_sessy_device
import pprint

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
        print(f"=== Sessy Device at { device.host } ===")
        print(f"S/N: {device.serial_number}")
        print("- Network status -")
        result = await device.get_network_status()
        pprint.pprint(result)
        print("")

        print("- Software update status -")
        ota_result = await device.get_ota_status()
        pprint.pprint(ota_result)
        print("")

        if isinstance(device, SessyBattery):
            print("- Power Status -")
            result = await device.get_power_status()
            pprint.pprint(result)
            print("")

            print("- Power Strategy -")
            result = await device.get_power_strategy()
            pprint.pprint(result)
            print("")

            print("- System settings -")
            result = await device.get_system_settings()
            pprint.pprint(result)
            print("")

            if ota_result['self']['installed_firmware']['version'] >= '1.6.5':
                # Dynamic mode from 1.6.5 and up
                print("- Dynamic mode schedule -")
                result = await device.get_dynamic_schedule()
                pprint.pprint(result)
                print("")

        elif isinstance(device, SessyP1Meter):
            print("- P1 Status -")
            result = await device.get_p1_status()
            pprint.pprint(result)
            print("")

        await device.close()

asyncio.run(run())