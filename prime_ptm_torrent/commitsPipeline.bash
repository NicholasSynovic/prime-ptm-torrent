#!/bin/bash

dataDir="/home/nsynovic/data/commits"
fullPath=$1
author=${fullPath##*/}	# https://stackoverflow.com/a/1371283

mkdir -p $dataDir


ls $fullPath | parallel -k --bar prime-commits-extract -d ${fullPath}/{} -l /home/nsynovic/data/commits/${author}_{}_log.log -o /home/nsynovic/data/commits/${author}_{}_commits_loc.json
