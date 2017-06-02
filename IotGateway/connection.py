'''
Created on 06-Aug-2016

@author: TERAMATRIX\rupam.kumari
'''
import os
import pymongo
from redis import StrictRedis
from pymongo import MongoClient
from logger import log_function
from IotGateway.config import Config
file_name = os.path.basename(__file__)
file_name = file_name.split('.')[0]
config_obj = Config()
mongo_conf = config_obj.mongo()
redis_conf = config_obj.redis()
def mongo_conn() :
    """
    
        Function_name : mongo_conn (function for making 
        mongo db connection) 
        return: db
        Exception:
               PyMongoError
    
    """
    #config = ConfigObj(CONF)
    host=mongo_conf['host']
    port=mongo_conf['port']
    database=mongo_conf['database']
    try:
        client = MongoClient(host, int(port))
        db = client.genieacs
    except pymongo.errors.PyMongoError, e:
        raise pymongo.errors.PyMongoError, e
        #logger.exception('Exception pymongo errors %s'% (e) )
    return db

def redis_conn(db_name=None):
    """
        Function_name : redis_conn 
        Function to create redis connection
        return: redis connetion object
        Exception:
               redis Connection Exception
    
    """
    redis_config = redis_conf[db_name]
    # TODO: Use sentinel to make connection to master
    try:
        redis_db = StrictRedis(**redis_config) 
    except Exception as exc:
        redis_db = None
        print 'Error redis conn: {0}'.format(exc)
    return redis_db

