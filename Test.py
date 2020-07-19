import wmi
import paho.mqtt.publish as publish
from time import sleep
#remember to add the ca-cert.pem file when using. This is not included as it would make my IP public
# run the temp of two cores and return the two temps every 30 seconds.

#define a method that takes in the two paramaters and prints them out with a retunr type
def sendMessage(mes1, mes2):
    publish.single("ArransAssignment/topic", mes1, hostname="127.0.0.1", port=8883, tls={"ca_certs": "ca-cert.pem"}) # This method publishes the topic so it can be subscribed to
    publish.single("ArransAssignment/topic", mes2, hostname="127.0.0.1", port=8883, tls={"ca_certs": "ca-cert.pem"}) # change it to local host as im using mosqitto locally


w = wmi.WMI(namespace="root\OpenHardwareMonitor", privileges=["Security"])
temperature_infos = w.Sensor()
while True:
    for sensor in temperature_infos:
        if sensor.SensorType==u'Load':
            if(sensor.name == "CPU Core #1" or sensor.name == "CPU Core #2"):
                nameOfCore = (sensor.Name)
                valueOfCore = (str(sensor.Value) + "%\n") # assign the name and load to variables that are pased into the method v
                print(nameOfCore)
                print(valueOfCore)
                sendMessage(nameOfCore, valueOfCore)
    sleep(30)





