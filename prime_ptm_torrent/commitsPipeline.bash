#!/bin/bash

dataDir="~/data/commits"
fullPath=$1
author=${fullPath##*/}	# https://stackoverflow.com/a/1371283

mkdir -p $dataDir


ls $fullPath | sshpass parallel --sshdelay 0.1 -S node2 -S node5 -S node6 -S node7 -S node8 -S node9 -S node10 -S node11 -S node12 -S node14 -S node15 -S node16 -k --bar prime-commits-extract -d ${fullPath}/{} -l ${dataDir}/${author}_{}_log.log -o ${dataDir}/${author}_{}_commits_loc.json
