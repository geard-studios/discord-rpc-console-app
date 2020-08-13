from pypresence import Presence
import time

clientid = input('Client ID: ')
print()
print('Connecting...')
time.sleep(3)
RPC = Presence(clientid)
RPC.connect()
print('Connected!')
print()
state = input('State: ')
details = input('Details: ')
print()
print('Changing Rich Presence...')
time.sleep(3)
RPC.update(state=state, details=details)
print()
print('Changed Presence to:')
print(f'State: {state}')
print(f'Details: {details}')

while True:
    time.sleep(15)