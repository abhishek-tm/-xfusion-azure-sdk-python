'''
Created on 24-May-2016
@author: TERAMATRIX/siddhika.nag

Script to initialize publisher object and call encrypData & publish_to_IoTHub  modules  
'''

from IotGateway.publishData.encryptData import encryptData
from IotGateway.publishData.pushData import connect_to_IoTHub , publish_to_IoTHub
from IotGateway.derivedKPI.calculate_derivedKPI import derivedKPI
from IotGateway.protocol.data_formatter import Formatter
from IotGateway.sdk.device.sample.iothub_client_sample import iothub_client_init, iothub_client_sample_run
from IotGateway.connection import redis_conn
from IotGateway.config import Config
from logger import log_function
import os
import time
# Class to define publisher 
class PublisherIOTHub(object) :
    
    def __init__(self):
        file_name = os.path.basename(__file__).split('.')[0]
        self.logger = log_function(file_name)
        self.config_obj = Config()
        iothub = self.config_obj.iothub()
        self.IoTHub_IP = iothub['IP']
        self.IoTHub_port = iothub['Port']
        self.publisher = False 
        self.publisher = connect_to_IoTHub(self.IoTHub_IP,self.IoTHub_port)
        self.derivedKPI_obj = derivedKPI()
        self.redis_obj_perf_data = redis_conn('REDIS_PERF_DATA')
        connection_lost   = self.config_obj.wait_for_connection()
        self.DataSource = connection_lost['data_source']
        self.ServiceName = connection_lost['service_name']

    """
    publish(self,deviceId,content)
	Function to call encryptData() and publishredis_conn_to_IoTHub() if 
	  publisher object exists and publisher object doesn't exists
       then data send on redis-dbs
	Parameters : DeviceID and Performance Data
        Returns : Encrypted data
    """
    def publish(self, deviceId, content, sys_timestamp):
        formatter_obj = Formatter()
        check_timestamp = self.redis_obj_perf_data.get( str(deviceId) + "_check_timestamp")
        update_content = []
        for dict_data in content :
            if 'host_status' in dict_data['service_name']:
                add_host_status = False
                break
            else :
                add_host_status = True
        if add_host_status:
            formatted_data = []
            formatted_data = formatter_obj.format_data(formatted_data=formatted_data,device_id=deviceId,service_name='host_status',\
                                                            data_source = 'host_status',current_value = "ON",\
                                                            check_timestamp=check_timestamp,sys_timestamp=sys_timestamp)
#
                
            self.redis_obj_perf_data.set("%s_check_timestamp" % str(deviceId),sys_timestamp)            
            content.extend(formatted_data)

        derived_data = self.derivedKPI_obj.calculate_derived_KPI(deviceId,sys_timestamp)
        
        if derived_data :
            content.extend(derived_data)
        

        """ 
        when publisher object doesn't exists we store content list on redis.
        and store only those records on redis which is different to previous records
        and data publish on IOT Hub when publisher object exists..
        
        """
        if iothub_client_init():
            encryptedcontent = encryptData(self.IoTHub_IP, self.IoTHub_port, deviceId, str(update_content))
            #print encryptedcontent
            iothub_client_sample_run(deviceId, encryptedcontent)
            self.logger.debug('Published to IOTHub !!!!: %s' %(deviceId ))
            

        self.redis_obj_perf_data.set("Device:%s"%str(deviceId), sys_timestamp)
        self.redis_obj_perf_data.set(str(deviceId)+"_Device_last_up_time",int(time.time())) 
