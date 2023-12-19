#!/bin/bash

HADOOP_SRC=/home/lixl/hadoop-3.3.4-src
HADOOP_CONF=$HADOOP_SRC/hadoop-dist/target/hadoop-3.3.4/etc/hadoop

for i in 1 2 3 4 5
do
    rsync -avzr $HADOOP_SRC/hadoop-dist agent$i:$HADOOP_SRC
    rsync -avzr $HADOOP_SRC/oeclib agent$i:$HADOOP_SRC
done
