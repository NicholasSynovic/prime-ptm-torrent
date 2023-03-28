#!/bin/bash

mkdir ../../data/commits

fullPath=$1
author=${fullPath##*/}	# https://stackoverflow.com/a/1371283

ls $fullPath | parallel -j 10 -k --bar clime-git-commits-extract -d ${fullPath}/{} -o ../../data/commits/${author}_{}_commits_loc.json --log ../../data/commits/${author}_{}_log.log
