'''
Created on 27-May-2016
@author: TERAMATRIX/siddhika.nag

Script to connect to IoTHub and publish data over MQTT
'''
import paho.mqtt.client as mqtt
from datetime import datetime
import time
from logger import log_function
import os
import sys
file_name = os.path.basename(__file__).split('.')[0]
logger = log_function(file_name)
"""
    on_publish(client, userdata, mid)
	Callback function for when a PUBLISH message is received from the server.
	Parameters : the client instance for this callback,
		the private user data as set in Client(),
		mid variable returned from the corresponding publish() call, to allow outgoing messages to be tracked.
        Returns : None
"""
def on_publish(client, userdata, mid):
    pass
    #print("mid: "+str(mid))

def on_connect(client, userdata, flags, result_code):
    print "On connect",client, userdata, flags, result_code
    print mqtt.connack_string(result_code)

"""
    connect_to_IoTHub(IoTHub_IP,IoTHub_port)
	Function to connect to Iot Hub MQTT client
	Parameters : IoTHub IP,IoTHub port
        Returns : MQTT Client object
"""
def connect_to_IoTHub(IoTHub_IP,IoTHub_port):
    # create MQTT client object

    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_publish = on_publish
    client.on_disconnect = on_disconnect
    try :
        # connect to MQTT broker on specified BROKER_IP, PORT, Maximum period in seconds between communications with the broker
        client.connect(IoTHub_IP,int(IoTHub_port))
        #client.connect_async(IoTHub_IP,int(IoTHub_port),10)
        client.loop_start()
    except Exception, exp :
        #return none when doesn't connect to IOT Hub MQTT client
        print 'Error in client connection: %s' %( exp )
        logger.error('Error in client connection: %s'%( exp ))
        return None
    return client  

"""
    on_disconnect(self, client, userdata, rc)
        Function to connect to reconnect MQTT client on disconnection
        Parameters : MQTT client object,the private user data as set in Client()
		and connection result
        Returns : None
"""
def on_disconnect(client, userdata, rc):
    if rc != 0:
        pass

"""
    publish_to_IoTHub(client, deviceID, content, IoTHub_IP, IoTHub_port)
        Function to create MQTT gateway message and publish it to IoT hub
        Parameters : MQTT client object, deviceID, content, IoTHub IP, IoTHub port
        Returns : None
"""     
def publish_to_IoTHub(client, deviceID, content, IoTHub_IP, IoTHub_port):
    # Gateway message with fields DeviceID, ENQUEUED_TIME, ENCRYPTED_CONTENT
    message = {"deviceId" : deviceID ,"enqueued_time" : str(datetime.now()),"encrypted_content" : content}
    #Convert message to BYTE as MQTT supports payload publish in BYTE
    #print message
    byteArray = bytes(message)
    #print "byteArray Size" ,sys.getsizeof(byteArray)
    # Publish to IoT Hub with topic MQTT
    topic_name = '%s-%s-%s' % (IoTHub_IP.replace('.','-'),str(IoTHub_port),'MQTT') #TO-DO : Fetch protocol
    #print topic_name
    logger.debug("Topic name : %s"%(topic_name))
    try :
        result = client.publish(topic_name, payload=byteArray, qos=2, retain=False)
        time.sleep(1)
        print "Pub resp %s"%str(result)
        logger.debug("Pub resp %s"%str(result))
    except Exception, exp :
        print 'Error in client publish: %s'%( exp )
        logger.debug('Error in client publish: %s'%( exp ))

