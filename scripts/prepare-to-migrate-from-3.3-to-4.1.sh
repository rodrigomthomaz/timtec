#!/bin/bash

export current_branch=$(git branch | sed -n -e 's/^\* \(.*\)/\1/p')

git checkout tags/v3.3
python manage.py migrate core 0018 --fake
python manage.py migrate core 0017
python manage.py migrate core 0016 --fake
python manage.py migrate core 0015
git checkout $current_branch
