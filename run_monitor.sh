#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

cd $DIR

(cd web ; node server.js ../data/ &)

python ./Monitor.py $DIR/data/live_output.json
