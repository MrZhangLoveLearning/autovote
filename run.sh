#!/bin/bash
echo "run the auto_vote"

base_dir=~/autovote

git fetch
git pull

if [ ! -f $base_dir/env/bin/activate ]
then
	# cd $project_env
	virtualenv $base_dir/env
	
fi


source  $base_dir/env/bin/activate
sudo $base_dir/env/bin/pip install -r $base_dir/requirements.txt
python $base_dir/run.py