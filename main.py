import asyncio
from rocket_cores.fetch_data import fetch_data_automatically, present_data

async def main():
    result = await fetch_data_automatically(False, True, 5)
    present_data(result)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
