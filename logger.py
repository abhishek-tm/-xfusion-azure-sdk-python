'''
Created on 27-May-2016
@author: TERAMATRIX/Rupam.Kumari

Script to handle logging and send mail in case of exception
'''

#!/usr/bin/python
import os
import smtplib
import string
import logging.handlers
from datetime import datetime, timedelta
from IotGateway.config import Config
from string import upper
config_obj = Config()
format_simple = config_obj.format_simple()
email_config = config_obj.email_config()
last_mail_time_config = config_obj.last_mail_time()
logger_set = config_obj.set()
#print last_mail_time
user_authentication = config_obj.user_authentication()
#last_mail_time_conf=config_obj.last_mail_time_conf
#print last_mail_time_conf,"last_mail_time_conf"
#log_config_file = os.path.dirname(os.path.abspath(__file__))
loggers = {}

class TlsSMTPHandler(logging.handlers.SMTPHandler):

    def __init__(self, mailhost, fromaddr, toaddrs, subject,
                 last_check, credentials=None, file_name=None, mailing_interval=60):
        """
        Initialize the handler.

        Initialize the instance with the from and to addresses and subject
        line of the email. To specify a non-standard SMTP port, use the
        (host, port) tuple format for the mailhost argument. To specify
        authentication credentials, supply a (username, password) tuple
        for the credentials argument. To specify the use of a secure
        protocol (TLS), pass in a tuple for the secure argument. This will
        only be used when authentication credentials are supplied. The
        tuple
        will be either an empty tuple, or a single-value tuple with the
        name
        of a keyfile, or a 2-value tuple with the names of the keyfile and
        certificate file. (This tuple is passed to the `starttls` method).
        """
        logging.Handler.__init__(self)
        if isinstance(mailhost, tuple):
            self.mailhost, self.mailport = mailhost
        else:
            self.mailhost, self.mailport = mailhost, None
        if isinstance(credentials, tuple):
            self.username, self.password = credentials
        else:
            self.username = None
        self.fromaddr = fromaddr
        if isinstance(toaddrs, basestring):
            toaddrs = [toaddrs]
        self.toaddrs = toaddrs
        self.subject = subject
        self.secure = ()
        self._timeout = 5.0
        self.file_name = file_name
        self.mailing_interval = mailing_interval
        self.last_check = last_check

    def emit(self, record):
        """
        Emit a record.
        Format the record and send it to the specified addressees.
        """
        current_time = datetime.now().strftime("%Y%m%d%H%M")
        check_time = datetime.now() - \
            timedelta(minutes=int(self.mailing_interval))
        check_time = check_time.strftime("%Y%m%d%H%M")
        #print "Current Time : Last Check Time", check_time, self.last_check
        if self.last_check is None or (
                int(check_time) >= int(self.last_check)):
            try:
                try:
                    from email.utils import formatdate
                except ImportError:
                    formatdate = self.date_time
                port = self.mailport
                if not port:
                    port = smtplib.SMTP_PORT
                smtp = smtplib.SMTP(self.mailhost, port)
                msg = self.format(record)
                msg = "From: %s\r\nTo: %s\r\nSubject: %s\r\nDate: %s\r\n\r\n%s" % (
                    self.fromaddr,
                    string.join(self.toaddrs, ","),
                    self.getSubject(record),
                    formatdate(), msg)
                if self.username:
                    smtp.ehlo()  # for tls add this line
                    smtp.starttls()  # for tls add this line
                    smtp.ehlo()  # for tls add this line
                    #print self.username, self.password
                    smtp.login(self.username, self.password)
                # print msg
                smtp.sendmail(self.fromaddr, self.toaddrs, msg)
                smtp.quit()
            except (KeyboardInterrupt, SystemExit):
                raise
            except:
                self.handleError(record)

            try:
                last_mail_time_config[self.file_name] =  str(current_time)
                last_mail_time = last_mail_time_config[self.file_name]
                
                config_obj.write_last_mail_time(self.file_name,last_mail_time)
            except Exception as e:
                print "Exception !!", e
        else:
            print "Message already sent"


def log_function(file_name):
    '''
        create a 'log_config.ini' file, this file set debug and error value 'True' or 'False'
        call 'set_log_info' and 'set_log_error' function
        and return log_info and log_error
    '''
    # path to generate log files
    #print "In Log Function"
    # log_path="/home/logs"
    #print "file_name",file_name
    #config = ConfigObj(CONF)
    user_id =user_authentication['user_id']
    log_path = logger_set['log_path']
    # get 'set = debug' from  log_config.ini file
    log_debug = logger_set['debug']
    # get 'set = error' from  log_config.ini file
    log_error = logger_set['error']
    log_file_name = logger_set['log_file_name']

    if log_debug == 'True' and log_error == 'False':
        # call setup_custom_logger_info function  and return logger_info
        log_info = set_log_info(log_path,log_file_name, file_name, user_id)
        return log_info
    elif log_error == 'True' and log_debug == 'False':
        # call setup_custom_logger_error function and return logger_error
        log_error = set_log_error(log_path,log_file_name, file_name, user_id)
        return log_error
    elif log_debug == 'True' and log_error == 'True':
        # call setup_custom_logger_info function and return logger_info
        log_info = set_log_error(log_path,log_file_name, file_name, user_id, log_level=logging.DEBUG)
        return log_info
    else:
        # if debug and error value 'False' then call this function
        return disable_log()


def set_log_info(log_path,log_file_name, file_name, user_id, log_level=logging.DEBUG):
    '''
        In 'set_log_info' function pass two parameter 'log_path','file_name'
        logsfiles created path 'log_path' and file_name which current filename(eg :- rrd_migration)
        this function, use 'getLogger' function which Return a logger with the specified 'log_path'
            and use 'logging.FileHandler' function which function create a logfile
            'logging.Formatter'function ,logs create specific format
            and set level 'DEBUG'
    '''
    global loggers
    #print "loggers",loggers
    if loggers.has_key(file_name):
        return loggers[file_name]
    else : 
        #print "Here"
        #config = ConfigObj(CONF)
        # get log format from  log_config.ini file
        log_format = format_simple['format']
        # replace '#' to '%' in logging_set_to_format
        log_format = log_format.replace('^', '%')
        logger = logging.getLogger(log_path)
        file_handler = logging.FileHandler(
            os.path.join(
                log_path,
                log_file_name +
                datetime.now().strftime("_%Y%m%d.log")))  # log files create location
        format_handler = logging.Formatter(log_format)
        #print "format",format
        file_handler.setFormatter(format_handler)
        logger.setLevel(log_level)  # set level type 'DEBUG'
        logger.addHandler(file_handler)
        #print "File handler",dir(logger.handlers[0])
        loggers[file_name] = logger
        return logger


def set_log_error(log_path,log_file_name, file_name, user_id, log_level=logging.ERROR):
    '''
        In 'set_log_error' function pass two parameter 'log_path','file_name
        logsfiles created path 'log_path' and file_name which current filename(eg :- rrd_migration)
        this function, use 'getLogger' function which Return a logger with the specified 'log_path'
        and use 'logging.FileHandler' function which function create a logfile
       'logging.Formatter'function ,logs create specific format
        and set level 'ERROR'
    '''
    #print "In set_log_error"
    global loggers
    #print "loggers",loggers
    if loggers.has_key('file_name'):
        return loggers['file_name']
    else :
        #print "Here"
        #config = ConfigObj(CONF)
        # get log format from  log_config.ini file
        log_format = format_simple['format']
        # replace '#' to '%' in logging_set_to_format
        log_format = log_format.replace('^', '%')
        logger = logging.getLogger(log_path)
    
        # error_mail_handler.setLevel(logging.ERROR)
        # error_mail_handler.setFormatter(log_format)
        file_handler = logging.FileHandler(
            os.path.join(
                log_path,
                log_file_name +
                datetime.now().strftime("_error_%Y%m%d.log")))  # log files create location
        format_handler = logging.Formatter(log_format)
        #print "format",log_format
        file_handler.setFormatter(format_handler)
        logger.setLevel(log_level)  # set level type 'ERROR'
        logger.addHandler(file_handler)
        #print "File handler",logger.handlers[0].get_name.__get__
        send_mail = email_config['send_mail']
    
        if upper(send_mail) == 'TRUE':
    
            mailhost = email_config['mailhost']
            mailhost_port = email_config['mailhost_port']
            from_address = email_config['from_address']
            to_address = email_config['to_address']
            mail_username = email_config['mail_username']
            mail_password = email_config['mail_password']
            mailing_interval = email_config['mailing_interval']
            try:
                last_mail_time = int(last_mail_time_config.get(file_name))
            except Exception:
                config_obj.write_last_mail_time(file_name)
                last_mail_time = None
            #last_mail_time = None if config.get('last_mail_time').get(file_name) == '' else int(config.get('last_mail_time').get(file_name))
            error_mail_handler = TlsSMTPHandler((mailhost, mailhost_port),
                                                from_address,
                                                to_address.split(','),
                                                "Gateway Exception For [%s]" % (
                                                    user_id),
                                                last_mail_time, (mail_username,
                                                                 mail_password),
                                                file_name, mailing_interval)
    
            error_mail_handler.setLevel(logging.ERROR)
            logger.addHandler(error_mail_handler)
        else:
            print "Mail Handler Disabled"
    
        # send_mail(file_name)
        loggers['file_name']=logger
        return logger


def disable_log():
    """
    In 'disable_log' function call,when log_config.ini file set debug and error value 'False'

    """
    logger = logging.getLogger()  # create logger object
    logger.disabled = True  # set logger is disable
    return logger
