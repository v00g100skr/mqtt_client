import paho.mqtt.client as mqtt

import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("../src/debug.log"),
        logging.StreamHandler()
    ]
)

# This is the Subscriber


def on_connect(client, userdata, flags, rc):
    logging.info("Connected with result code " + str(rc))
    client.subscribe("zigbee2mqtt_lan/geiger_counter")


def on_message(client, userdata, msg):
    data = str(msg.payload.decode("utf-8"))
    logging.info("received message: %s" % data)


logging.info('start main')
client = mqtt.Client()
client.username_pw_set("zigstar", "zigstar")
client.connect("10.2.0.40", 1883, 60)

client.on_connect = on_connect
client.on_message = on_message
client.loop_forever()