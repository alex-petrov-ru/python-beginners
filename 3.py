import keys
from pubnub import pubnub

PUB_KEY = 'pub-c-bab40884-15d8-42a3-8675-21d381efc60e'
SUB_KEY = 'sub-c-d3ff6da6-faa9-11e5-8180-0619f8945a4f'

pubnub = pubnub(publish_key=keys.PUB_KEY, subscribe_key=keys.SUB_KEY)

def callback(message):
    print(message)

pubnub.publish('my_channel_sf23', 'Hello from PubNub Python SDK!', callback=callback, error=callback)

while True:
    pubnub.publish('my_channel_sf23', input(), callback=callback, error=callback)