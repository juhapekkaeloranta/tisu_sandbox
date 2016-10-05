#!/bin/bash

#Get path of this file
#(should be project root)
CURRENTDIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )

source $CURRENTDIR/config/environment.sh

echo "Moving files to server: $HOST"

# Move files to server with rsync (only changes)
# -z for compressing during transfer
# -r for recursive copy
# -v for verbosity (info during transfer)
rsync -z -r -v $CURRENTDIR/config $CURRENTDIR/app $USERNAME@$HOST:htdocs/$PROJECT_FOLDER

echo "Sync done!"