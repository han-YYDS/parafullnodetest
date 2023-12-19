#!/bin/bash

HDFS=/home/lixl/hadoop-3.3.4-src/hadoop-dist/target/hadoop-3.3.4

rm -rf $HDFS/logs
rm -rf $HDFS/dfs

for i in 1 2 3 4 5
do
    ssh agent$i "rm -rf $HDFS/dfs"
    ssh agent$i "rm -rf $HDFS/logs"
done
