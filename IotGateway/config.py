'''
Created on 24-Sep-2016

@author: TERAMATRIX/Rupam.kumari
'''

# start of config files for agent and input and output parser
from configobj import ConfigObj
import os
#from IotGateway.registerDevice import registration
class Config(object):

    def __init__(self,config_file=None):
        self.config_file = config_file if config_file else self.get_defaultfile()
        self.config = ConfigObj(self.config_file)
        #self.load_config(self.config_file)
        
    def get_defaultfile(self):
        path = os.path.dirname(os.path.abspath(__file__))
        CONF = os.path.join(path.split('IotGateway')[0],'config.ini')
        return CONF

    def gateway(self):
        gateway_conf= self.config.get('Gateway')
        return  gateway_conf
    
    def iothub(self):
        iothub_conf = self.config.get('IoTHub')
        return iothub_conf
    
    def device_registration(self):
        device_registation_conf = self.config.get('Device Registration')
        return device_registation_conf
    
    def user_authentication(self):
        user_authentication_conf = self.config.get('User Authentication')
        #print user_authentication_conf
        return user_authentication_conf
    
    def configuration(self):
        configuration_conf = self.config.get('Configuration')
        return configuration_conf

    def mongo(self):
        mongo_conf = self.config.get('MONGO')
        return mongo_conf
    
    def redis(self):
        redis_conf = self.config.get('REDIS')
        return redis_conf
    
    def acs(self):
        acs_conf = self.config.get('ACS')
        return acs_conf
    
    def set(self):
        set_conf = self.config.get('set')
        return set_conf
    
    def format_simple(self):
        format_simple_conf = self.config.get('format_simple')
        return format_simple_conf
    
    def email_config(self):
        email_config_conf = self.config.get('email_config') 
        return email_config_conf 
       
    def last_mail_time(self):
        last_mail_time_conf = self.config.get('last_mail_time')
        return last_mail_time_conf
    
    def kafka(self):
        kafka_conf = self.config.get('KAFKA')
        return kafka_conf
    
    def derived_KPI(self):
        derived_KPI_conf = self.config.get('DerivedKPI')
        return derived_KPI_conf
    
    def get_mqtt_config(self):
        mqtt_config = self.config.get('MQTT')
        return mqtt_config
  
    def write_user_authentication(self,token,user_key = None,access_key = None):
        user_authentication_conf = self.user_authentication()
        if user_key ==  None and access_key == None:
            user_authentication_conf.update({'token':token})
        else:
            user_authentication_conf.update({'token':token,
                                            'user_key':user_key,
                                            'access_key':access_key}
                                           )
        self.config.write()
        
    def write_last_mail_time(self,file_name,last_mail_time = None):
        last_mail_time_conf = self.last_mail_time()
        if last_mail_time == None:
            last_mail_time_conf.update({file_name:None})
        else:
            last_mail_time_conf.update({file_name:last_mail_time})    
        self.config.write()

    def wait_for_connection(self):
        connection_lost = self.config.get("waiting_for_connection")
        return connection_lost

    
if __name__== '__main__' :
    config = Config()
    gateway_conf = config.gateway()
    iothub_conf = config.iothub()
    deviceregistation = config.device_registration()
    user_authentication = config.user_authentication()
    configuration = config.configuration()
    memcache = config.memcache()
    mongo = config.mongo()
    acs = config.acs()
    set = config.set()
    format_simple = config.format_simple()
    email_config = config.email_config()
    last_mail_time = config.last_mail_time()
    kafka = config.kafka()
    write_user_authentication = config.write_user_authentication('token','user_key','access_key')
    #write_filename_for_last_mail_time = config.write_filename_for_last_mail_time('push')
    #config.write()
    #print iothub_conf
        
