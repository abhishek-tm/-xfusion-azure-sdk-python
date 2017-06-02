# !/bin/bash

##########################################
# Gateway installation packet
##########################################

function install_basic
{
    sudo apt-get update
    sudo apt-get -y install python-pip
    sudo apt-get install wget
    sudo apt-get install tar
}

function install_gateway_packages
{
   sudo apt-get install redis-server
   sudo pip install pycrpto
   sudo pip install configobj
   sudo pip install paho-mqtt
   sudo pip install celery
   sudo pip install requests
   sudo pip install redis
   sudo pip install python-dateutil
   


}

if [ "$EUID" -ne 0 ]
        then echo "Installation must be done with root permission"
        exit
else
	read -p "Update Ubuntu? (y/n)" answer
	echo ""
	case $answer in 
		[Yy]*) install_basic ;;
	esac
	echo ""
fi
read -p "Install gateway packages? (y/n)" answer
echo ""
case $answer in
[Yy]*) install_gateway_packages ;;
esac
echo ""





