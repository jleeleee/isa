#/bin/bash

bash /tmp/data/dependencies.sh

bin/spark-class org.apache.spark.deploy.master.Master -h spark-master
