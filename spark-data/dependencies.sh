#!/usr/bin/env bash
apt-get update &&
apt-get install python3-dev default-libmysqlclient-dev -y &&
apt-get install python3-pip -y &&
pip3 install mysqlclient &&
apt-get install python3-mysqldb
