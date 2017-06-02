# Script to stop configuration script
ps -ef | grep ./IotGateway/pushConfig/pushConfig.py | awk '{print $2}' |xargs kill -9
echo "Gateway Configuration Stopped"
