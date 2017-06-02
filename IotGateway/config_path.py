'''
Created on 27-May-2016

Script to read config.ini path
'''
import os

path = os.path.dirname(os.path.abspath(__file__))
CONF = os.path.join(path.split('IotGateway')[0],'config.ini')
