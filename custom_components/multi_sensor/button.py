"Multisensor button entity"

import json

import paho.mqtt.client as mqtt

import time
HOST =

payload = {"unique_id": "multisensor_alarm_switch",
           "name": "Multisensor alarm switch",
           "state_topic": "home/bedroom/bedroom_socket_switch",
           "command_topic": "/multisensor/MS-IPe0e2e6742eff/peripherals/sound/POST",
           "availability_topic": "home/bedroom/bedroom_socket_switch/available",
           "payload_on": '{"mode" : "ON", "duration" : 1000}',
           "payload_off": '{"mode" : "OFF", "duration" : 1000}',
           "state_on": "ON",
           "state_off": "OFF",
           "optimistic": False,
           "qos": 0,
           "retain": True
           }

payload = json.dumps(payload)  # convert to JSON
config_topic = 'homeassistant/switch/bedroom_socket_switch/config'

topic = 'home/bedroom/bedroom_socket_switch/available'

def on_message_callback(client, userdata, message):
    print(message.topic + " " + ":" + str(message.payload))


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    if (str(rc) == '0'):
        print("start")
        client.publish(config_topic, payload, qos=1, retain=True)
        client.publish(topic, "online", qos=1)


client = mqtt.Client()
client.connect(HOST, PORT, 60)
client.username_pw_set('mqtt-user', 'vtec123')
client.on_connect = on_connect
client.on_message = on_message_callback
client.loop_start()

command_topic = '/multisensor/MS-IPe0e2e6742eff/peripherals/sound/POST'
while True:
    client.publish(command_topic, "online", qos=1)
    time.sleep(1)
