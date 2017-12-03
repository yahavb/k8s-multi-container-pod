#!/bin/bash

dpa_url="localhost:11021/ports/$pod_name/$container"
trap "{`curl -X DELETE $dpa_url`}" SIGINT SIGTERM

container_file="$shared_folder/$container.container"

echo `date` "-" $0 "- going to call DPA for random socket port"
port=`curl -s $dpa_url | awk -F PortNumber '{print $2}'| awk -F\, '{print $1}'| awk -F\: '{print $NF}'`
echo `date` "-" $0 "- DPA allocated number:" $port

echo $port > $container_file
echo $port > "$shared_folder/$port.kubeproxy"

/usr/bin/kubectl proxy --port=$port
