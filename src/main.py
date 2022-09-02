import paho.mqtt.client as mqtt

# This is the Subscriber


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe("zigbee2mqtt_lan/geiger_counter")


def on_message(client, userdata, msg):
    data = str(msg.payload.decode("utf-8"))
    print("received message: ", data)

print("start")
client = mqtt.Client()
client.username_pw_set("zigstar", "zigstar")
client.connect("10.2.0.40", 1883, 60)

client.on_connect = on_connect
client.on_message = on_message
client.loop_forever()