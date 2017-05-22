# xfusion-azure-sdk-python
SDK of platform for Python Developers is a set of libraries which allow you to work on xFusion Platform for device integration and data submission.

The SDK minimum system requirements includes:

- [x] Operating System – Ubuntu 14.04
- [x] CPU – 2 core
- [x] RAM – 4 GB 
- [x] Python v2.7
- [x] Internet connectivity is required for package installation and communication with Azure Protocol Hub.

##  Installation 
The required packages are installed by executing installUbuntuPackage.sh , build.sh and setup.sh script.

##  Configuration 
The authentication needs to be done in Azure SDK by updating following fields under [IOTHUB-Detail] section in config.ini file
**Usage:**
```python

* Connection string - primary key
Connection string  = <azure-iot-connecting-string>
```
	
## Features
The SDK includes following libraries:

### 1. Registration
This module is essential for device on-boarding. The device gets registered in the platform and Azure IotHUb sdk using a UNIQUE DEVICE IDENTIFIER and gets a mapped platform Device ID and device info.


**Usage:**
```python

* Import the library
from IotGateway.registerDevice import registration
from IotGateway.sdk.service.samples.azure_register import iothub_create_device

* Create a registration object
registrationObj=registration.registration()

* Using the registration object register the device with UNIQUE DEVICE IDENTIFIER
deviceID = registrationObj.device_registration_push(device = <UNIQUE DEVICE IDENTIFIER>)

* Using UNIQUE DEVICE IDENTIFIER device register on Azure IotHub 
device_info = iothub_create_device(<UNIQUE DEVICE IDENTIFIER>, <primary_key>, <sencondary_key>)

```

### 2. Data Formatter
This modules the data as it is required by xFusion Platform to understand.

**Usage:**
```python

* Import the library
from IotGateway.protocol.data_formatter import Formatter

* Create a formatter object
formatter_obj = Formatter()

* Using the formatter object format the data passing fetched deviceID
formatted_data =  formatter_obj.format_data(<formatted_data>, <deviceID>, <Service-Parameter> , <DataSource-Parameter>,  <Parameter-Value>,<Parameter value fetched time in UTC Epoch> , <Parameter value storage time in UTC Epoch> )

```

### 3. Publisher
This module publishes the formatted data to Azure IOt Hub in encrypted format.

**Usage:**
```python

* Import the library
from IotGateway.publishData.publisher import PublisherIOTHub
from IotGateway.sdk.device.sample.iothub_client_sample import iothub_client_init, iothub_client_sample_run

* Create a publisher object
pub_obj = PublisherIOTHub()

* Using the publisher object  publish the encrypted data to Azure iothub 
pub_obj.publish(<deviceID>, <encrypted data> )

```
