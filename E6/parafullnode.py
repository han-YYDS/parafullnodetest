# usage:
#   python fn_hdfs.py
#       1. cluster [office|aliyunhdd|csencs1]
#       2. CODE [RSPIPE|Clay]
#       3. ECN [4|14]
#       4. ECK [2|10]
#       5. ECW [1|1]
#       6. method [conv|dist]
#       7. blkmib [1|64|256]
#       8. pktkib [64]
#       9. num_stripes [20] (default: the number of agent nodes)
#       10. batchsize [29] (default: the number of agent nodes -1)
#       11. gen_files [true|false]
#       12. gen_blocks [true|false]
#       13. gen_meta [true|false]

# This script runs the full node recovery of a specific code

import os
import sys
import subprocess
import time

CLUSTER=sys.argv[1]
CODE=sys.argv[2]
ECN=int(sys.argv[3])
ECK=int(sys.argv[4])
ECW=int(sys.argv[5])
METHOD=sys.argv[6]
BLKMB=int(sys.argv[7])
PKTKB=int(sys.argv[8])
NUM_STRIPES=int(sys.argv[9])
BATCHSIZE=int(sys.argv[10])
GEN_FILES=sys.argv[11]
GEN_BLOCKS=sys.argv[12]
GEN_META=sys.argv[13]

# home dir
cmd = r'echo ~'
home_dir_str, stderr = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE).communicate()
home_dir = home_dir_str.decode().strip()

# test dir
test_dir="{}/parafullnodetest".format(home_dir)
data_dir=test_dir+"/data"
cluster_dir="{}/cluster/{}".format(test_dir, CLUSTER)

# proj dir
proj_dir="{}/parafullnode".format(home_dir)
script_dir = "{}/script".format(proj_dir)
stripeStore_dir = "{}/stripeStore".format(proj_dir)

# 1. stop previous run
cmd="cd {}; python stop.py".format(script_dir)
os.system(cmd)

# 2. gendata
cmd="cd "+data_dir+"; python gendata_from_oec_fullnode.py "+CLUSTER+" "+str(NUM_STRIPES-1)+" "+CODE+" "+str(ECN)+" "+str(ECK)+" "+str(ECW)+" "+str(BLKMB)+" "+str(PKTKB)+" "+ GEN_FILES + " " + GEN_BLOCKS + " " + GEN_META + " " + str(BATCHSIZE)
print(cmd)
os.system(cmd)
sys.exit()

# 3. conf
cmd="cd {}/conf; python3 createconf.py {} hdfs {} {} {} {} {} {} {}".format(script_dir, CLUSTER, BLKMB, PKTKB, CODE, ECN, ECK, ECW, BATCHSIZE)
print(cmd)
os.system(cmd)

# 3. start
cmd="cd {}/pretest; python bw.py {} {} {} {} {} parallel scatter {} {} {} {} false 1000".format(script_dir, CLUSTER, CODE, ECN, ECK, ECW, BLKMB, PKTKB, BATCHSIZE, NUM_STRIPES)
print(cmd)
os.system(cmd)
