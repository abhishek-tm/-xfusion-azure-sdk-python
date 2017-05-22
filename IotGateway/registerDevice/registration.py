#!/usr/bin/python
'''
Created on 06-Aug-2016

@author: TERAMATRIX/siddhika.nag

Script to register new device on IoTHub and store registerd device id in in-memory db
'''

from IotGateway.sdk.service.samples.azure_register import iothub_create_device,get_device 
from IotGateway.connection import redis_conn
from IotGateway.config import Config
from logger import log_function
import requests
import json
import os
# Python class to register device on xFusion Platform
class registration(object):
    
    def __init__(self):
	"""
	    From config file, get and initialization all variables.
	"""
        file_name = os.path.basename(__file__).split('.')[0]
        self.logger = log_function(file_name)
        self.redis_obj_register = redis_conn(db_name = 'REDIS_REGISTER')
        self.config_obj = Config()

    def device_registration_push(self,device = None):
        """
            If device id registered in gateway then get devices id from memcache 
            otherwise call device registration api .
            if device registration api response status '401' 
                then firstly  call user authentication api and authenticate users.
            and register the devices on gateway and return device id and device id
		 stored in  memcache
             
        Args:device
    
        return: None(if device registration fail that time return None)  
        """
        try:
            device_id = self.redis_obj_register.get(device)
            info  = self.redis_obj_register.get(str(device_id)+"azure_device_info")
            if device_id and info:
                return device_id
            else:
                gateway = self.config_obj.gateway()
                device_registration = self.config_obj.device_registration()
                user_authentication = self.config_obj.user_authentication()
                iot_hub = self.config_obj.iothub()
                data= {'device_id': device,
                       'gatewayid' : gateway['gateway_id'],
                       'protocol': iot_hub['protocol'],
                       'access_key' : user_authentication['access_key'],                       
                       }
                headers = {
                       'token': user_authentication['token'],
                       'user_id': user_authentication['user_id'],
                       'userkey': user_authentication['user_key']
                       }
                #print device_registration['device_registation_url'],data
                response = requests.post(device_registration['device_registation_url'],\
				data = data,verify=False)
                if response.status_code == 401:
                    authData = {'username':user_authentication['user_id'],
                                'password':user_authentication['password'],
                                'applicationid' : user_authentication['application_id']
                                }
                    authResponse = requests.post(user_authentication['Auth_URL'],data = authData, headers=headers, verify=False) 
                    authResponseData = json.loads(authResponse.content)
                    if authResponseData['valid']:
                        authResponseData = authResponseData['object']
                        token = authResponseData['access_token']
                        user_key = authResponseData['userKey']
                        access_key = authResponseData['access_key']
                        self.config_obj.write_user_authentication(token, user_key, access_key)
#                         data['token'] = authResponseData['access_token']
#                         data['userKey'] = authResponseData['userKey']
#                         data['access_key'] = authResponseData['access_key']
                        headers['userkey'] = authResponseData['userKey']
                        headers['token'] = authResponseData['access_token']
                        response = requests.post(device_registration['device_registation_url'],\
					data = data, headers=headers, verify=False)
                response_data = json.loads(response.content)
                self.logger.error("--- Registration response --- :{0}".format(str(response_data)))
                if response_data['valid'] and len(response_data['object']) > 0 :
                    device_id = response_data['object']
                    deviceId  = get_device(device_id)
                    if deviceId:
                        device_info  = "HostName=ttpliot.azure-devices.net" + ";" + str(deviceId) +";" + str(primary_key)
                        self.redis_obj_register.set(device, device_id[0]['id'])
                        self.redis_obj_register.set(str(device_id)+ "azure_device_info", device_info)
                    else:
                        device_info  =  iothub_create_device(device_id,primary_key,secondary_key)
                        self.redis_obj_register.set(device, device_id[0]['id'])
                        self.redis_obj_register.set(str(device_id)+"azure_device_info", device_info)
                else:
                    self.logger.error("Device Registration fail %s", response.text)
                return None
        except Exception as e:
            self.logger.exception('Exception in device_registration_push: %s', e)

        