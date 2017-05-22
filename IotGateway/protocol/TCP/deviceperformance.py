'''
Created on 31-jan-2017
@author: $iddhik@.nag
'''
from __builtin__ import float


'''
Script to read data from tcp server
and publish format data on platform  
'''

import SocketServer
import socket, sys
import threading
import time
import os
from datetime import datetime, timedelta
import thread
from dateutil.parser import parse
file_name = os.path.basename(__file__).split('.')[0]
from logger import log_function
logger = log_function(file_name)
#haversine used for calculate distance between two lat_lng
from haversine import haversine

# SDK Imports
from IotGateway.publishData.publisher import PublisherIOTHub
from IotGateway.registerDevice import registration
from IotGateway.protocol.data_formatter import Formatter
from IotGateway.connection import redis_conn
redis_obj_perf_data_register  = redis_conn(db_name = 'REDIS_REGISTER')
redis_obj_perf_data = redis_conn('REDIS_PERF_DATA')
registrationObj=registration.registration()
formatter_obj = Formatter()
pub_obj = PublisherIOTHub()
host = '192.168.1.38'
port = 9000


threadcounter=0
count = 0

class service(SocketServer.BaseRequestHandler):
    def __init__(self, request, client_address, server):
        SocketServer.BaseRequestHandler.__init__(self, request, client_address, server)
        return

    '''
    def handle(self): method receive data from 9000 port
    and register devices and publish formated data
    on IOT_HUB
    override the server socket class handle method 
    '''
        
    def handle(self):
        
        try:
        #while data_string:    
            while True: 
                data_string = ''
                Lat  = ''
                Lng = ''
                
                #request to recv data 
                data_string = self.request.recv(1024)
            
                #when data_string is not null
                if len(data_string)>5:
                    data_string  =  data_string + 'distance'+ ":" + '0.0' 
                    data_string = data_string +";" +'time_travelled' + ":" + '0'
                    data_string1  = data_string.split(';')
                    tacker_time = ''
                    tracker_time = data_string1[40].strip("Tracker_time:")
                    time1 = (parse(tracker_time) + timedelta(hours = 5,minutes= 30)).strftime('%s')   
                    
                    #find unqiue_id 
                    device_name = str(data_string1[1].split(':')[1]) + str(data_string1[6].split(':')[1])
                    #device register and get device id 
                    device_id = registrationObj.device_registration_push(device = device_name)
                     
                    #Formatted data list to publish
                    formatted_data = []
                            
                    if device_id and len(data_string1) <= 55 :
                        
                        current_lat_lng = []
                        current_lat_lng.append(data_string1[8:10])
                        current_lat_lng1 = current_lat_lng.pop(0)
                        c_lat,c_lng = float(str(current_lat_lng1[0]).split(':')[1]),float(str(current_lat_lng1[1]).split(':')[1])
                        
                        '''
                        set lat_lng first time when redis have no 
                        keys [str(device_id) + "_Latitude_Longitude]
                        '''

                        if not redis_obj_perf_data.keys(str(device_id) + "_previous_Latitude_Longitude"):
                            redis_obj_perf_data.set( str(device_id) + "_previous_Latitude_Longitude" , str(c_lat)+ ':' + str(c_lng))
                        
                        if redis_obj_perf_data.keys(str(device_id) + "check_timestamp"):
                                check_timestamp = redis_obj_perf_data.get( str(device_id) + "check_timestamp")
                            
                        #set check_timestamap on redis. when device state change
                        else:
                            check_timestamp = redis_obj_perf_data.set( str(device_id) +"check_timestamp" , str(int(time.time())))
                            
                        if redis_obj_perf_data.keys(str(device_id) + "previous_time"):
                            time_travelled = redis_obj_perf_data.get( str(device_id) + "previous_time")
                            redis_obj_perf_data.set( str(device_id) + "previous_time",str(int(time1)))
                        else:
                            redis_obj_perf_data.set( str(device_id) + "previous_time",str(int(time1)))
                        
                        distance = ''
                        #p_lat_lng is previous lat_lng
                        p_lat_lng = (redis_obj_perf_data.get(str(device_id) + "_previous_Latitude_Longitude")).split(':')
                        
                        #separate previous lat_lng and current_lat_lng 
                        p_lat,p_lng = float(p_lat_lng[0]),float(p_lat_lng[1])
                        
                        if (c_lat) == 0 and (c_lng) == 0:
                            redis_obj_perf_data.set( str(device_id) +"sys_timestamp" , str(int(time.time())))
                           
                        else:
                            redis_obj_perf_data.set( str(device_id) +"sys_timestamp" , str(int(time1)))
                                
                        #Data process when lat_lng > 0 
                        latitude = (p_lat,p_lng)
                        longtitude = (c_lat,c_lng)
                        
                        #calculate distance between previous lat_lng and current lat_lng in meter  
                        distance = haversine(latitude,longtitude)*1000
                        
                        #sys_timestamp = int(time.time())
                        sys_timestamp = int(redis_obj_perf_data.get( str(device_id) +"sys_timestamp"))
                        
                        #when calculated distance less than and equal 50 meter than send previous lat_lng with gmr services 
                        if distance <= 50 or distance > 1000000:
                            data_string1[8]  = str(Lat) + ':' +str(p_lat_lng[0])
                            data_string1[9] = str(Lng) + ':' +str(p_lat_lng[1])
                            #data_string1[-1] =  "distance" + ':' + str(round(distance, 2)) 
                        else:
                            time_travelled = int(sys_timestamp) - int(time_travelled)
                            data_string1[-1] = "time_travelled" + ':' + str(time_travelled)
                            data_string1[-2] =  "distance" + ':' + str(round(distance, 2))
                            redis_obj_perf_data.set(str(device_id) + "_previous_Latitude_Longitude" , str(c_lat)+ ':' + str(c_lng))
                   
                        #services for gmr_tracker  
                        for index in range(len(data_string1)):
                            
                            gmr_sensor_parameters = data_string1[index].split(':')

                            if index == 2:
                                formatted_data = formatter_obj.format_data(formatted_data, device_id, 'gmr_Sensor_Temperature' ,'gmr_Sensor_Temperature',\
                                                                           gmr_sensor_parameters[1], check_timestamp, sys_timestamp)
                                
                            elif index == 3:    
                                formatted_data = formatter_obj.format_data(formatted_data, device_id, 'gmr_Sensor_Humidity' ,'gmr_Sensor_Humidity',\
                                                                           gmr_sensor_parameters[1],check_timestamp, sys_timestamp)
                            
                            elif index == 4:
                                formatted_data = formatter_obj.format_data(formatted_data, device_id, 'gmr_Sensor_IsLowVoltage' ,'gmr_Sensor_IsLowVoltage',\
                                                                            gmr_sensor_parameters[1],check_timestamp, sys_timestamp)
            
                            elif index == 5:
                                formatted_data = formatter_obj.format_data(formatted_data, device_id, 'gmr_Sensor_IsVBV' ,'gmr_Sensor_IsVBV', \
                                                                            gmr_sensor_parameters[1],check_timestamp, sys_timestamp)
            
                            elif index == 6:
                                formatted_data = formatter_obj.format_data(formatted_data, device_id, 'gmr_Sensor_Connected_IMEI' ,'gmr_Sensor_Connected_IMEI',\
                                                                           gmr_sensor_parameters[1],check_timestamp, sys_timestamp)
                                
                            elif index == 8:
                                latitude_location = gmr_sensor_parameters[1]
                                formatted_data = formatter_obj.format_data(formatted_data, device_id, 'gmr_Sensor_Latitude' ,'gmr_Sensor_Latitude',\
                                                                            gmr_sensor_parameters[1],check_timestamp, sys_timestamp,is_lat = True)
                                
                            elif index == 9:
                                longitude_location = gmr_sensor_parameters[1]
                                formatted_data = formatter_obj.format_data(formatted_data, device_id, 'gmr_Sensor_Longitude' ,'gmr_Sensor_Longitude', \
                                                                            gmr_sensor_parameters[1],check_timestamp, sys_timestamp,is_long = True)
                        
                            elif index == 16:
                                formatted_data = formatter_obj.format_data(formatted_data, device_id, 'gmr_gpsTracker_FirmwareVersion' ,'gmr_gpsTracker_FirmwareVersion',\
                                                                           gmr_sensor_parameters[1],check_timestamp, sys_timestamp)
                    
                            elif index == 27:
                                formatted_data = formatter_obj.format_data(formatted_data, device_id, 'gmr_gpsTracker_Mileage' ,'gmr_gpsTracker_Mileage', \
                                                                            gmr_sensor_parameters[1],check_timestamp, sys_timestamp)
                                
                            elif index == 31:
                                formatted_data = formatter_obj.format_data(formatted_data, device_id, 'gmr_SatelliteCount' ,'gmr_SatelliteCount', \
                                                                           gmr_sensor_parameters[1],check_timestamp, sys_timestamp)    
                            
                            elif index == 34:
                                formatted_data = formatter_obj.format_data(formatted_data, device_id, 'gmr_gpsTracker_Speed' ,'gmr_gpsTracker_Speed',\
                                                                            gmr_sensor_parameters[1],check_timestamp, sys_timestamp)    
                            
                            elif index == 35:
                                gmr_sensor_parameters = gmr_sensor_parameters[1]
                                
                                if int(gmr_sensor_parameters[-5]) == 1:
                                    gmr_sensor_parameters1 = "ON"
                                    formatted_data = formatter_obj.format_data(formatted_data, device_id, 'gmr_IgnitionStatus' ,'gmr_IgnitionStatus',\
                                                                                gmr_sensor_parameters1,check_timestamp, sys_timestamp)    
                                    
                                else:
                                    gmr_sensor_parameters1 = "OFF"
                                    formatted_data = formatter_obj.format_data(formatted_data, device_id, 'gmr_IgnitionStatus' ,'gmr_IgnitionStatus',\
                                                                                gmr_sensor_parameters1, check_timestamp, sys_timestamp)
                            elif index == 47:
                                distance1 = gmr_sensor_parameters[1]
                                formatted_data = formatter_obj.format_data(formatted_data, device_id, 'gmr_distance_travelled' ,'gmr_distance_travelled',\
                                                                                gmr_sensor_parameters[1],check_timestamp, sys_timestamp)
                            elif index == 48:
                                    formatted_data = formatter_obj.format_data(formatted_data, device_id, 'gmr_time_travelled' ,'gmr_time_travelled',\
                                                                                gmr_sensor_parameters[1],check_timestamp, sys_timestamp)
                        
                        #print "formatted_data", formatted_data
                        # Publish formatted data on platform using SDK  
                        pub_obj.publish(str(device_id), formatted_data, sys_timestamp)
                            
                time.sleep(.01)

        except Exception as e:
            print "ERROR: Unable to allocate connection" + str(e),
            
            
            logger.error('Error in client connection: %s' %(e))
                
            
#To build asynchronous handlers, use the ThreadingMixIn classes
class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    pass


if __name__ == '__main__':
    
    try:
        SocketServer.TCPServer.allow_reuse_address = True
        t = ThreadedTCPServer((host,port), service)
        t.serve_forever()
    
    except Exception,e:
        #logger.error('Error in client connection: %s' %(e))
        print "Error",str(e)

