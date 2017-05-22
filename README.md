# GMR Gateway

# 1. Introduction

GMR Data Processing Gateway is integrated with xfusion-python-sdk. This gateway allows GMR Device to connect using TCP Listner for getting the data. This raw data is parsed and the string is set into the required format to publish on xFusion Platform.

The minimum system requirements for Gateway includes:

	Operating System – Ubuntu 14.04
	CPU – 2 core
	RAM – 4 GB
	python v2.7
	Internet connectivity is required for communication with GMR Devices and xFusion Protocol Hub.

# 2. Installation

The required packages are installed by executing installUbuntuPackage.sh script.

# 3. Configuration

The authentication needs to be done for GMR Data Processing Gateway using Python SDK by updating following fields under User Authentication section in config.ini file

``` python
	user_id = <xFusion Platform Login ID>

	password = <xFusion Platform Login Password>

	application_id = <xFusion Platform Application ID>
```

# 4. Features

The SDK includes following libraries: 

## 4.1 Get GMR Data

This process is essential for getting data of GMR device. The TCP Listner is configured on defined ip and port, then TCP Listner keep awake continuosly. The GMR Device, placed into vehicle connects to TCP Listner and send hexadecimal data string. Here the Gateway differentiate hex data for required parameter.

> Example -

Data received from GMR Deives :- 545A006E242401110115000008616930333774901101140A1C1D0016000000000000000000000000000000000000000000000004007B26AF000CAA4000001F37017400000000000000000000001A03100062160162087A2D0062160163086630006216016108843000000000000000D362C50D0A 

## 4.2 Device Registration

This module is essential for device on-boarding. The device gets registered in the platform using a UNIQUE DEVICE IDENTIFIER and gets a mapped platform Device ID

Usage:

* Import the library
from IotGateway.registerDevice import registration
	
* Create a registration object
registrationObj=registration.registration()

* Using the registration object register the device with UNIQUE DEVICE IDENTIFIER
deviceID = registrationObj.device_registration_push(device = <UNIQUE DEVICE IDENTIFIER>)

## 4.3 Processiong on GMR Data

This modules the data from raw string to required data in proper units and format.

The processing on Data includes following steps:

* On the basis of currnet and previous lat-lng we calculate travelled distance. If travelled distance > 50 metter than send current lat-lng on IoTHub else send privous lat-lng for Removing zig-zag problem.

* On the basis of IgnitionStatus we calculate **Total Trip Time** and **Total travelled Distance** covered is calculated. The data is stored into the InRam Database when the trip is in progress. When trips ends the data is retrieved from InRam Database and Total Trip Time and Total travelled Distance Covered is calculated.

* On the basis of last data occurrence time manage device state ON/OFF. 

## 4.4 Data Formatter

This modules the data as it is required by xFusion Platform to understand.

Usage:

* Import the library
from IotGateway.protocol.data_formatter import Formatter

* Create a formatter object
formatter_obj = Formatter()

* Using the formatter object format the data passing fetched deviceID
formatted_data =  formatter_obj.format_data(<formatted_data>, <deviceID>, <Service-Parameter>, <DataSource-Parameter>,  <Parameter-Value>, <Parameter value fetched time in UTC Epoch>, <Parameter value storage time in UTC Epoch>)

## 4.5 Publisher

This module publishes the formatted data to Protocol Hub in encrypted format.

Usage:

* Import the library
from IotGateway.publishData.publisher import PublisherIOTHub

* Create a publisher object
pub_obj = PublisherIOTHub()

* Using the publisher object  publish the formatted data
pub_obj.publish(<deviceID>, <encryptedcontent>, <IoTHub_IP>, <IoTHub_Port>)

# Reference:-

https://docs.python.org/2/library/socketserver.html

