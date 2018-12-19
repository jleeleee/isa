#!/usr/bin/env bash
apt-get update &&
apt-get install libmysqlclient-dev -y &&
pip3 install mysqlclient
