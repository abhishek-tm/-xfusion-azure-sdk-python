'''
Created on 20-Dec-2016

@author: TERAMATRIX/siddhika.nag

Script to format data as recognized by xFusion Platform and
store in in-memory DB for further computation
'''
from logger import log_function
from datetime import datetime
import os
from IotGateway.connection import redis_conn
from IotGateway.config import Config
file_name = (os.path.basename(__file__)).split('.')[0]
redis_obj_perf_data = redis_conn('REDIS_PERF_DATA')
logger = log_function(file_name)

#Python class to format data
class Formatter():
    
    def __init__(self):
        self.config_obj = Config()
        self.restrict_data = self.config_obj.gateway()['restrict_data']

    def format_data(self,formatted_data,device_id = None,service_name = None, data_source = None,\
                     current_value = None,check_timestamp= None,sys_timestamp = None,\
                     is_lat = False, is_long = False,is_host_state = False,\
                      on_state_value = None, off_state_value = None):
        
        """
        Format data in list of JSON format including keys for 
                            device_id,
                            service_name,
                            data_source,
                            current_value,
                            check_timestamp,
                            sys_timestamp,  
	    and all formatted data store in In-memory DB
        Args:    device_id - Registered device ID
                 service_name - Parameter service name
                 data_source - Parameter data source
                 current_value - Parameter current value
                 check_timestamp- Parameter value change time
                 sys_timestamp - Parameter value storage time

        return: Formatted JSON list
        """
        current_value = str(current_value)
        device_data_dic = {}
        global last_up_time
        if formatted_data == []:
            """
            Read last up time of device for which data was sent
            to pick the previous values for comparing
            """
            try:
                last_up_time = eval(redis_obj_perf_data.get(str('Device:'+device_id)))

            except Exception,error:
                pass

        state = None
        if device_id is not None and service_name is not None and data_source is not None :
            """
            Condition to add 'host_status' service/data-source if a particular service can be used to
            determine ON/OFF status of device
            """
            if is_host_state is not None and on_state_value is not None and off_state_value is not None :
                if current_value == on_state_value:
                    state = "ON"

                elif current_value == off_state_value:
                    state = "OFF"
                device_data_dic= {
                        "device_id": device_id,
                        "service_name": "host_status",
                        "data_source": "host_status",
                        "current_value": state,
                        "check_timestamp":  sys_timestamp ,
                        "sys_timestamp": sys_timestamp,
                          }
                if self.restrict_data == 'True':
                    try:
                        """
                        Read last value of parameter and compare with current value
                        If Value is not equal add status as "insert"
                        Else add status as "update"

                        In case the value is read first time add status as "insert"

                        After reading last value update the current value in in-memory DB
                        for reading value in next cycle
                        """
                        get_value = redis_obj_perf_data.get((str(device_id) + '_' + "host_status" + '_'
                                                              + "host_status" + '_' + str(last_up_time)))
                        if eval(get_value) == eval(state):
                            device_data_dic.update({"status":"update"})
                        else:
                            device_data_dic.update({"status":"insert"})
                        redis_obj_perf_data.set(str(device_id) + '_' + "host_status" + '_'
                                                 + "host_status" + '_' + str(sys_timestamp),state)
                    except Exception:
                        redis_obj_perf_data.set(str(device_id) + '_' + "host_status" + '_'
                                                + "host_status" + '_' + str(sys_timestamp),state)
                        device_data_dic.update({"status":"insert"})
                   
                formatted_data.append(device_data_dic)

                device_data_dic= {
                        "device_id": device_id,
                        "service_name": service_name,
                        "data_source": data_source,
                        "current_value": current_value,
                        "check_timestamp":  check_timestamp ,
                        "sys_timestamp": sys_timestamp,
                                   }
                if self.restrict_data == 'True':
                    try:
                        get_value = redis_obj_perf_data.get((str(device_id) + '_' + service_name + '_'
                        + data_source + '_' + str(last_up_time)))
                        if eval(get_value) == eval(device_data_dic["current_value"]):
                            device_data_dic.update({"status":"update"})
                        else:
                            device_data_dic.update({"status":"insert"})
                        redis_obj_perf_data.set(str(device_id) + '_' + service_name + '_'
                                                + data_source + '_' + str(sys_timestamp),device_data_dic[ "current_value"])
                    except Exception, error:
                        redis_obj_perf_data.set(str(device_id) + '_' + service_name + '_'
                                                + data_source + '_' + str(sys_timestamp),device_data_dic[ "current_value"])
                        device_data_dic.update({"status":"insert"})
                   
                formatted_data.append(device_data_dic)
            elif is_lat :
                """
                Condition to add 'xFusion_location'/'xFusion_latitude' service/data-source if a 
                particular service can be used to determine location of device
                """

                device_data_dic = {
                                   "device_id": device_id,
                                   "service_name": 'xFusion_location',
                                   "data_source": 'xFusion_latitude',
                                   "current_value": current_value,
                                   "check_timestamp":  check_timestamp ,
                                   "sys_timestamp": sys_timestamp, 
                                   }
                if self.restrict_data == 'True':
                    try:
                        get_value = eval(redis_obj_perf_data.get(str(device_id) + '_' + 'xFusion_location' + '_' 
                                        + 'xFusion_latitude' + '_' + str(last_up_time)))
                        if get_value == device_data_dic["current_value"]:
                            device_data_dic.update({"status":"update"})
                        else:
                            device_data_dic.update({"status":"insert"})
                            redis_obj_perf_data.set(str(device_id) + '_' + 'xFusion_location' + '_' 
                                        + 'xFusion_latitude' + '_' + str(sys_timestamp),device_data_dic[ "current_value"])
                    except Exception, error:
                        redis_obj_perf_data.set(str(device_id) + '_' + 'xFusion_location' + '_'
                                        + 'xFusion_latitude' + '_' + str(sys_timestamp),device_data_dic[ "current_value"])
                        device_data_dic.update({"status":"insert"})
                   
                formatted_data.append(device_data_dic)

                device_data_dic ={
                                  "device_id": device_id,
                                  "service_name": service_name,
                                  "data_source": data_source,
                                  "current_value": current_value,
                                  "check_timestamp":  check_timestamp ,
                                  "sys_timestamp": sys_timestamp,
                                  }
                if self.restrict_data == 'True':
                    try:
                        get_value = redis_obj_perf_data.get((str(device_id) + '_' + service_name + '_'
                                                + data_source + '_' + str(last_up_time)))
                        if get_value == device_data_dic["current_value"]:
                            device_data_dic.update({"status":"update"})
                        else:
                            device_data_dic.update({"status":"insert"})
                        redis_obj_perf_data.set(str(device_id) + '_' + service_name + '_'
                                                + data_source + '_' + str(sys_timestamp),device_data_dic[ "current_value"]) 
                    except Exception, error:
                        redis_obj_perf_data.set(str(device_id) + '_' + service_name + '_'
                        + data_source + '_' + str(sys_timestamp),device_data_dic[ "current_value"])
                        device_data_dic.update({"status":"insert"})
                formatted_data.append(device_data_dic)
            elif is_long :
                """
                Condition to add 'xFusion_location'/'xFusion_longitude' service/data-source if a 
                particular service can be used to determine location of device
                """
                device_data_dic= {
                            "device_id": device_id,
                            "service_name": 'xFusion_location',
                            "data_source": 'xFusion_longitude',
                            "current_value": current_value,
                            "check_timestamp":  check_timestamp ,
                            "sys_timestamp": sys_timestamp,
                                       }
                if self.restrict_data == 'True':
                    try:
                        get_value = redis_obj_perf_data.get((str(device_id) + '_' + 'xFusion_location' + '_' 
                                            + 'xFusion_longitude' + '_' + str(last_up_time)))
                        if get_value == device_data_dic["current_value"]:
                            device_data_dic.update({"status":"update"})
                        else:
                            device_data_dic.update({"status":"insert"})
                        redis_obj_perf_data.set(str(device_id) + '_' + 'xFusion_location' + '_'
                                            + 'xFusion_longitude' + '_' + str(sys_timestamp),device_data_dic["current_value"]) 
                    except Exception, error:
                        redis_obj_perf_data.set(str(device_id) + '_' + 'xFusion_location' + '_'
                                            + 'xFusion_longitude' + '_' + str(sys_timestamp),device_data_dic["current_value"]) 
                        device_data_dic.update({"status":"insert"})
                   
                formatted_data.append(device_data_dic)
                device_data_dic= {
                            "device_id": device_id,
                            "service_name": service_name,
                            "data_source": data_source,
                            "current_value": current_value,
                            "check_timestamp":  check_timestamp ,
                            "sys_timestamp": sys_timestamp,
                                       }
                if self.restrict_data == 'True':
                    try:
                        get_value = redis_obj_perf_data.get((str(device_id) + '_' + service_name + '_' 
                                                + data_source + '_' + str(last_up_time)))
                        if get_value == device_data_dic["current_value"]:
                            device_data_dic.update({"status":"update"})
                        else:
                            device_data_dic.update({"status":"insert"})
                        redis_obj_perf_data.set(str(device_id) + '_' + service_name + '_'
                                                + data_source + '_' + str(sys_timestamp),device_data_dic[ "current_value"])   
                    except Exception, error:
                        redis_obj_perf_data.set(str(device_id) + '_' + service_name + '_'
                                                + data_source + '_' + str(sys_timestamp),device_data_dic[ "current_value"])
                        device_data_dic.update({"status":"insert"})

                formatted_data.append(device_data_dic)

            else:
                device_data_dic = {
                            "device_id": device_id,
                            "service_name": service_name,
                            "data_source": data_source,
                            "current_value": current_value,
                            "check_timestamp":  check_timestamp ,
                            "sys_timestamp": sys_timestamp, 
                                       }
                if self.restrict_data == 'True':
                    try:
                        get_value = redis_obj_perf_data.get((str(device_id) + '_' + service_name + '_' 
                                        + data_source + '_' + str(last_up_time)))
                        #print get_value,device_data_dic["current_value"]
                        if get_value == device_data_dic["current_value"]:
                            device_data_dic.update({"status":"update"})
                        else:
                            device_data_dic.update({"status":"insert"})
                        redis_obj_perf_data.set((str(device_id) + '_' + service_name + '_'
                                        + data_source + '_' + str(sys_timestamp)),device_data_dic[ "current_value"] )
                    except Exception, error:
                        redis_obj_perf_data.set((str(device_id) + '_' + service_name + '_'
                                        + data_source + '_' + str(sys_timestamp)),device_data_dic[ "current_value"])
                        device_data_dic.update({"status":"insert"})

                formatted_data.append(device_data_dic)

            return formatted_data
