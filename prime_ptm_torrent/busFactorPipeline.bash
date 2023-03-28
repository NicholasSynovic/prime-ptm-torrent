#!/bin/bash

mkdir ../../data/busFactor

fullPath=$1
author=${fullPath##*/}  # https://stackoverflow.com/a/1371283

ls $fullPath | parallel -j 10 -k --bar clime-git-bus-factor-compute -i ../../data/commits/${author}_{}_commits_loc.json -o ../../data/busFactor/${author}_{}_bus_factor.json
