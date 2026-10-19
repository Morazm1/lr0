#!/bin/sh
echo "WHOAMI=$(whoami)"
echo "UID_GID=$(id -u):$(id -g)"
echo "HOSTNAME=$(hostname)"
while true; do sleep 3600; done
