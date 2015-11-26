#!/bin/bash
# coding=utf-8
echo "run the auto_vote"

base_dir=~/autovote

git fetch
git pull

if [ ! -f $base_dir/env/bin/activate ]
then
	# cd $project_env
	virtualenv $base_dir/env
	sudo $base_dir/env/bin/pip install -r $base_dir/requirements.txt
	
fi


source  $base_dir/env/bin/activate

python $base_dir/run.py