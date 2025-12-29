import paho.mqtt.client as mqtt
import ssl
import json
import time
import random
from datetime import datetime

# ===================== AWS IOT DETAILS =====================
AWS_ENDPOINT = "aqu49n5t7o5zg-ats.iot.eu-north-1.amazonaws.com"

PORT = 8883
TOPIC = "agriculture/sensors"

CA_PATH = "certs/rootCA.pem"
CERT_PATH = "certs/device.pem.crt"
KEY_PATH = "certs/private.pem.key"

# ===================== MQTT CLIENT SETUP =====================
client = mqtt.Client(client_id="SmartAgriSimulator")

client.tls_set(
    ca_certs=CA_PATH,
    certfile=CERT_PATH,
    keyfile=KEY_PATH,
    tls_version=ssl.PROTOCOL_TLSv1_2
)

client.connect(AWS_ENDPOINT, PORT)
client.loop_start()

print("Connected to AWS IoT Core")
print("Publishing simulated sensor data...\n")

# ===================== SENSOR SIMULATION FUNCTION =====================
def generate_sensor_data():
    temperature = round(random.uniform(20.0, 40.0), 2)      # °C
    humidity = round(random.uniform(40.0, 90.0), 2)         # %
    soil_moisture = round(random.uniform(10.0, 80.0), 2)    # %

    return {
        "temperature": temperature,
        "humidity": humidity,
        "soil_moisture": soil_moisture,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

# ===================== PUBLISH LOOP =====================
try:
    while True:
        data = generate_sensor_data()
        payload = json.dumps(data)

        client.publish(TOPIC, payload)
        print(payload)

        time.sleep(10)   # publish every 10 seconds

except KeyboardInterrupt:
    print("\nSimulation stopped by user")

finally:
    client.loop_stop()
    client.disconnect()
