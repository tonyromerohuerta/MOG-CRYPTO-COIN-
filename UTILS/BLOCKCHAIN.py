from web3 import Web3
import asyncio

w3 = Web3(Web3.HTTPProvider("https://sepolia.infura.io/v3/YOUR_KEY"))

def monitor_events():
    # Listen to FusionCompleted events
    factory_abi = [...]  # ABI of FusionFactory
    factory_address = "0xYourFactoryAddress"
    contract = w3.eth.contract(address=factory_address, abi=factory_abi)

    def handle_event(event):
        # Update DB with new card details
        pass

    async def log_loop(event_filter, poll_interval):
        while True:
            for event in event_filter.get_new_entries():
                handle_event(event)
            await asyncio.sleep(poll_interval)

    event_filter = contract.events.FusionCompleted.createFilter(fromBlock='latest')
    asyncio.run(log_loop(event_filter, 2))

from web3 import Web3
import asyncio

w3 = Web3(Web3.HTTPProvider("https://sepolia.infura.io/v3/YOUR_KEY"))

def monitor_events():
    # Listen to FusionCompleted events
    factory_abi = [...]  # ABI of FusionFactory
    factory_address = "0xYourFactoryAddress"
    contract = w3.eth.contract(address=factory_address, abi=factory_abi)

    def handle_event(event):
        # Update DB with new card details
        pass

    async def log_loop(event_filter, poll_interval):
        while True:
            for event in event_filter.get_new_entries():
                handle_event(event)
            await asyncio.sleep(poll_interval)

    event_filter = contract.events.FusionCompleted.createFilter(fromBlock='latest')
    asyncio.run(log_loop(event_filter, 2))