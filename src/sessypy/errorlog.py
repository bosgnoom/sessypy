# Import modules
# import asyncio
from sessypy.devices import SessyDevice
from bs4 import BeautifulSoup
from datetime import datetime
import logging


async def parse_error_line(line:str):
    """
        Take one error message, parse datetime, and
        split between error_type and error message

        returns: [datetime, error_type, message]
    """
    date, _, remaining = line.partition(' E (')
    time, _, remaining = remaining.partition(') ')
    error_type, _, message = remaining.partition(': ')

    try:
        date_obj = datetime.strptime(date + ' ' + time, '%Y/%m/%d %H:%M:%S.%f')
    except ValueError:
        logging.error(f'Could not convert "{line}"')

    return date_obj, error_type, message


async def get_error_log(device: SessyDevice) -> list:
    response = await device.get_error_log()
    
    soup = BeautifulSoup(response, 'html.parser')
    errors = soup.find('p', id='errors').contents[0]

    return [ await parse_error_line(err) for err in errors.split('\n') if len(err) ]

