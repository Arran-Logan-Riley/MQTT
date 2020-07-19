import paho.mqtt.client as mqtt



# setting up the message receiver
def on_connect(client, userdata, flags, rc):
    print("Connected with results Code-" + str(rc))

    client.subscribe("ArransAssignment/test")
    client.subscribe("ArransAssignment/topic") # subscribe to a topic

def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.tls_set("ca-cert.pem")

client.connect("localhost", 8883, 60)  # this sets up theprotocol and keepalive for the mqtt
client.loop_forever()