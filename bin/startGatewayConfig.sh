script_dir=$(dirname "$(readlink -f "$0")")
script_dir="$(dirname "$script_dir")"
#echo ${script_dir}


cd ${script_dir}
export PYTHONPATH=.
echo ${script_dir}

nohup /usr/local/bin/python './IotGateway/pushConfig/pushConfig.py' &

