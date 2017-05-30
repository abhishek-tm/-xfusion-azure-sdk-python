'''
Created on 02-Dec-2016

@author: TERAMATRIX/siddhika.nag

Script to manage device state
'''

from logger import log_function
from datetime import datetime, timedelta
import os
from IotGateway.connection import redis_conn
from IotGateway.config import Config
from IotGateway.publishData.publisher import PublisherIOTHub

file_name = (os.path.basename(__file__)).split('.')[0]
redis_obj_perf_data = redis_conn('REDIS_PERF_DATA')
logger = log_function(file_name)
pub_obj = PublisherIOTHub()
config_obj = Config()
gateway_conf = config_obj.gateway()
#from start.entry import app

#@app.task(name='set_state_to_off', ignore_result=True)
def set_state_to_off():  
    """
    set_state_to_off(self)
        Function to set device state to if no packet received in device down threshold time defined in config.ini
        Parameters : None
        Returns : None
    """     
    try :
        device_list = redis_obj_perf_data.keys('Device:*')
        print device_list
        logger.debug("Device in redis %s"%str(device_list))
        if device_list :
            for device in device_list:
                #fetched_last_uptime = redis_obj_perf_data.get(str(device))
                device_id = device.split(":")[1]
                fetched_last_uptime1 = redis_obj_perf_data.get(str(device_id)+"_Device_last_up_time")
                if fetched_last_uptime1 < (datetime.now() -
                                timedelta(minutes = int(gateway_conf['device_down_threshold']) + 1)).strftime("%s"):
                    sys_timestamp = redis_obj_perf_data.get( str(device_id) +"sys_timestamp")
                    sys_timestamp = str(int(sys_timestamp) + 600)
                    formatted_data = [{ "device_id":device_id,
                                       "service_name": "host_status",
                                       "data_source": "host_status",
                                       "current_value": "OFF",
                                       "check_timestamp":  sys_timestamp ,
                                       "sys_timestamp": sys_timestamp,
                                    }]
                    logger.info("Formatted data : %s",str(formatted_data))
                    pub_obj.publish(str(device_id),formatted_data,sys_timestamp)
                    redis_obj_perf_data.delete( str(device_id) + "check_timestamp")
                    redis_obj_perf_data.delete(device)
                    
    except Exception,exp:
        logger.exception("Exception in set_state_to_off : %s", str(exp))
