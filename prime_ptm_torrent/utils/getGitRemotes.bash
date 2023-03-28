#!/bin/bash

for repo in $(ls $1)
do
	git -C $repo remote get-url --all origin >> ghRepos.txt
done
