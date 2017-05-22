# Script to start TTPL Gateway
# Usage :
#	cd TTPLGateway
#	sh bin/startGateway.sh
script_dir=$(dirname "$(readlink -f "$0")")
script_dir="$(dirname "$script_dir")"

cd ${script_dir}
export PYTHONPATH=.

python './IotGateway/protocol/TR069/devicePerformance.py'
