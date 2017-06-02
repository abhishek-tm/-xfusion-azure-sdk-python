'''
Created on 25-Oct-2016
@author: TERAMATRIX/siddhika.nag
Script to calculate derived KPI according to formula provided
'''
from __future__ import division
import collections
import ast
import requests
import json
import os
from dateutil.parser import parse
from IotGateway.config import Config
from IotGateway.protocol.data_formatter import Formatter
from IotGateway.connection import redis_conn
from logger import log_function
formatter_obj = Formatter()
class derivedKPI(object):
    """ Class to implement derived KPIs calculation"""
    
    def __init__(self):
        """ Initialize  frequently used parameters"""
        file_name = os.path.basename(__file__).split('.')[0]
        self.logger = log_function(file_name)
        self.config_obj = Config()
        user_authentication = self.config_obj.user_authentication()
        gateway = self.config_obj.gateway()
        derived_KPI = self.config_obj.derived_KPI()
        self.auth_URL = user_authentication['Auth_URL']
        self.derivedKPI_url = derived_KPI['DerivedKPI_url']
        self.derivedKPI_fetch_interval = derived_KPI['DerivedKPI_fetch_interval']
        self.access_key = user_authentication['access_key']
        self.user_key = user_authentication['user_key']
        self.user_id = user_authentication['user_id']
        self.token = user_authentication['token']
        self.application_id = user_authentication['application_id']
        self.auth_password = user_authentication['password']
        self.gateway_id = gateway['gateway_id']
        self.redis_obj_perf_data = redis_conn(db_name = 'REDIS_PERF_DATA')
        redis_obj_derived_kpi_data = redis_conn(db_name ='REDIS_DERIVED_KPI')
        try :
            self.api_response = eval(redis_obj_derived_kpi_data.get("Derived_KPI"))
        except Exception,error :
            self.api_response = None
        self.redis_obj_derived_kpi_data = redis_conn(db_name ='REDIS_DERIVED_KPI')

    def fetch_derived_KPI(self):
        """
        fetch_derived_KPI(self)
            Function to fetch derived KPIs and formula to calculate 
            their value defined in platform
        Parameters : None
        Returns : derivedKPI dictionary
        """
        data = collections.OrderedDict()
        data['access_key'] =  self.access_key
        data['gateway_id'] = self.gateway_id
        headers = {
                   'token': self.token,
                   'user_id': self.user_id,
                   'userkey': self.user_key
                   }
        try :
            api_response = requests.post(self.derivedKPI_url, data=data, headers=headers, verify=False, timeout= 20)
            #print "Derived KPI API",self.derivedKPI_url,data, headers
            if api_response.status_code == 401:
                authData = {'username':self.user_id,
                            'password':self.auth_password,
                            'applicationid' : self.application_id
                            }
                authResponse = requests.post(self.auth_URL,data=authData, verify=False, timeout= 20)
                authResponseData = json.loads(authResponse.content)
                if authResponseData['valid']:
                    authResponseData= authResponseData['object']
                    token = authResponseData['access_token']
                    user_key = authResponseData['userKey']
                    access_key = authResponseData['access_key']
                    self.config_obj.write_user_authentication(token,user_key,access_key)
                    headers['token'] = authResponseData['access_token']

            api_response = requests.post(self.derivedKPI_url, data=data, headers=headers, verify=False, timeout= 20)

            self.logger.debug("json.loads(api_response) : %s",str(api_response))
            self.logger.debug("json.loads(api_url) : %s",str(self.derivedKPI_url))
            self.logger.debug("json.loads(api_data) : %s",str(data))

            if api_response.status_code == 200 :
                api_response_data = json.loads(api_response.content)
                derivedKPI = api_response_data["object"]
                self.logger.debug("derivedKPI %s",str(derivedKPI))
            else :
                derivedKPI = []
        except Exception,e :
            self.logger.error("Error in derivedKPI %s",str(e))
            derivedKPI = []
        if derivedKPI :
            self.redis_obj_derived_kpi_data.set("Derived_KPI",derivedKPI)
            self.redis_obj_derived_kpi_data.expire("Derived_KPI", self.derivedKPI_fetch_interval)
        return derivedKPI
    
    def calculate_derived_KPI(self,device_id,sys_time):
        """
        calculate_derived_KPI(self, device_id, sys_time)
            Function to calculate value of derived KPIs according to formula
        Paramaters : 
               device_id : Mapped device id
               sys_time : Current Epoch time
        Returns : derived data dictionary
        """
        formatted_data = []
        filtered_device_api_response = None
        if self.api_response is None :
            self.api_response = self.fetch_derived_KPI()
        #print "Derived KPI", self.api_response
        if self.api_response :
            # Filter Derived KPI defined for DeviceID
            filtered_device_api_response =  list(filter(lambda derive_data: int(derive_data['device_device_device_id']) == int(device_id) , self.api_response))
        #print "Filterd API response",filtered_device_api_response
        if filtered_device_api_response :
            for derived_KPI in filtered_device_api_response :
                service_name = derived_KPI['service_service_name']
                data_source = derived_KPI['service_servicedatasource_name']
                formula = derived_KPI['service_servicedatasource_formula']
                if formula is not None :
                    var_list = formula.split(" ")
                else :
                    continue
                for index,var in enumerate(var_list) :
                    try :
                        if isinstance(ast.literal_eval(var),basestring) :
                            var_formatted =  str(device_id) \
                                    + '_' \
                                    + var.replace("'", "") \
                                    + '_' + str(sys_time)
                            value_formatted = self.redis_obj_perf_data.get(var_formatted)
                            self.logger.error("Derived data_source %s: %s" % (str(var_formatted),str(value_formatted)))
                            if ':' in value_formatted :
                                try :
                                    value_formatted = parse(value_formatted).strftime("%s")
                                except :
                                    pass
                            self.logger.error("Derived data_source %s: %s" % (str(var_formatted),str(value_formatted))) 
                            var_list[index] = value_formatted
                    except Exception,error:
                        #print error,index,var
                        pass
                try :
                    #print var_list
                    val = "".join(var_list)
                    value =  eval(val)
                    if isinstance(value,float):
                        value = "%.6f" % value
                    if isinstance(value,int) or isinstance(value, unicode) or not isinstance(value, (str, unicode)):
                        device_data_dic = {
                            "device_id": device_id,
                            "service_name": str(service_name),
                            "data_source": str(data_source),
                            "current_value": str(value),
                            "check_timestamp": sys_time,
                            "sys_timestamp": sys_time}
                    
                        formatted_data = formatter_obj.format_data(formatted_data,device_data_dic["device_id"],device_data_dic["service_name"],\
                                                            device_data_dic["data_source"],device_data_dic["current_value"],\
                                                            device_data_dic["check_timestamp"],device_data_dic["sys_timestamp"])
                except Exception,error:
                    #print error,var_list
                    pass

            return formatted_data
