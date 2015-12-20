#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
SOURCE=$DIR/data/live_output.json
DATE=$(date +"%Y_%m_%d_%H_%M")
DEST_NAME="output_$DATE.json"
DEST=/media/temperature_data/$DEST_NAME

cp $SOURCE $DIR/data/$DEST_NAME
cp $SOURCE $DEST 
if [ -f $dest ];
then
    rm $SOURCE
fi
