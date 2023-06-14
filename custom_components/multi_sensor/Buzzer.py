import json

import paho.mqtt.client as mqtt
import time

# HOST = "test.mosquitto.org"
HOST = "192.168.1.223"
PORT = 1883
USER = 'vtec-ls-nl'
PASSWORD = 'vtec123'

payload = {"unique_id": "Buzzer",
            "name": "Buzzer switch",
            "state_topic": "home/bedroom/Buzzer_switch",
            "command_topic": "/multisensor/MS-IPe0e2e6742eff/peripherals/sound/POST",
            "availability_topic": "home/bedroom/Buzzer_switch/available",
            "payload_on": '{"mode" : "ON", "duration" : 1000}',
            "payload_off": '{"mode" : "OFF", "duration" : 1000}',
            "state_on": "ON",
            "state_off": "OFF",
            "optimistic": False,
            "qos": 0,
            "retain": True
            }
payload = json.dumps(payload)  # convert to JSON
config_topic = 'homeassistant/switch/Buzzer_switch/config'

topic = 'home/bedroom/Buzzer_switch/available'


def on_message_callback(client, userdata, message):
    print(message.topic + " " + ":" + str(message.payload))


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    if (str(rc) == '0'):
        print("start")
        client.publish(config_topic, payload, qos=1, retain=True)
        res = client.publish(topic, "online", qos=1)
        if res[0] == 0:
            print('set online success')


def regester_control_service(host, port, username, password):
    client = mqtt.Client()
    client.connect(host, port, 60)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.on_message = on_message_callback
    client.loop_start()
    while True:
        # break
        time.sleep(3)
        break


if __name__ == '__main__':
    regester_control_service(HOST, PORT, USER, PASSWORD)
