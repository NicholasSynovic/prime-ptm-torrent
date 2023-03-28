#!/bin/bash

mkdir ../../data/productivity

fullPath=$1
author=${fullPath##*/}  # https://stackoverflow.com/a/1371283

ls $fullPath | parallel -j 10 -k --bar clime-productivity-compute -i ../../data/commits/${author}_{}_commits_loc.json -o ../../data/productivity/${author}_{}_productivity.json
