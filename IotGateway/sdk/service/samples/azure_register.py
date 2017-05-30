import sys
import iothub_service_client
from iothub_service_client import IoTHubRegistryManager, IoTHubRegistryManagerAuthMethod
from iothub_service_client import IoTHubDeviceStatus, IoTHubError
from iothub_service_client_args import get_iothub_opt, OptionError
from pymongo.read_preferences import Primary
CONNECTION_STRING = "[IoTHub Connection String]"
DEVICE_ID = "MyFirstPythonDevice"
#HostName=ttpliot.azure-devices.net

#register device on azure 
def iothub_create_device(DEVICE_ID,primary_key,secondary_key):
    try:
        print "i am here"
        CONNECTION_STRING="HostName=ttpliot.azure-devices.net;SharedAccessKeyName=iothubowner;SharedAccessKey=xBmNYVmuqN9sVZYQprYKvpv/2kv9GX1CdiSb5W+5KBc="
        iothub_registry_manager = IoTHubRegistryManager(CONNECTION_STRING)
        auth_method = IoTHubRegistryManagerAuthMethod.SHARED_PRIVATE_KEY
        DEVICE_ID = str(DEVICE_ID)
        new_device = iothub_registry_manager.create_device(DEVICE_ID, primary_key, secondary_key, auth_method)
         
        device_info  = "HostName=ttpliot.azure-devices.net" + ";" + str(new_device.deviceId) +";" + str(primary_key)
        return device_info
    
    except IoTHubError as iothub_error:
        print ( "Unexpected error {0}".format(iothub_error) )
        return 
            #print("CreateDevice", new_device)

#get device_id from azure when device already register 
def get_device(device_id):
    try:
        print "hello"
        device_id = str(device_id)
        CONNECTION_STRING="HostName=ttpliot.azure-devices.net;SharedAccessKeyName=iothubowner;SharedAccessKey=xBmNYVmuqN9sVZYQprYKvpv/2kv9GX1CdiSb5W+5KBc="
        iothub_registry_manager = IoTHubRegistryManager(CONNECTION_STRING)
        iothub_device = iothub_registry_manager.get_device(device_id)
        print "iothub_device.deviceId",iothub_device.deviceId
        return iothub_device.deviceId
    
    except IoTHubError as iothub_error:
        print ( "Unexpected error {0}".format(iothub_error) )
        return None

def get_device_list(self):
        print ( "GetDeviceList" ) 
        iothub_registry_manager = IoTHubRegistryManager(CONNECTION_STRING)
        iothub_registry_statistics = iothub_registry_manager.get_statistics()
        number_of_devices = iothub_registry_statistics.totalDeviceCount
        dev_list = iothub_registry_manager.get_device_list(number_of_devices)
        print dev_list
        number_of_devices = len(dev_list)
        print ( "Number of devices                        : {0}".format(number_of_devices) )
        list1 = []
        for device in range(0, number_of_devices):
            list1.append(dev_list[device].deviceId)
        print list1
        
if __name__ == '__main__':
    print ( "\nPython %s" % sys.version )
    print ( "IoT Hub Client for Python" )
    PROTOCOL  = 'MQTT'
    print ( "Starting the IoT Hub Python sample..." )
    print ( "    Protocol %s" % PROTOCOL )
    print ( "    Connection string=%s" % CONNECTION_STRING )