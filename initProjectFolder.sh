#!/bin/bash

#run in local project root2e

#create local config folder with environment details
mkdir config
cd config
touch environment.sh
echo "#!/bin/bash
USERNAME='juhapekm'
PROJECT_FOLDER='tisu_sandbox' 
HOST='users.cs.helsinki.fi'" > environment.sh
cd ..

#create local folder app for application files
mkdir app
cd app
touch hello.py
echo '#!/usr/bin/env python
print("hello!")' > hello.py
cd ..

#use server environment detail from file
source config/environment.sh

#connect to server
#create project root to server
#server must have htdocs folder at user root
ssh $USERNAME@$HOST "
cd htdocs
touch favicon.ico
mkdir $PROJECT_FOLDER
cd $PROJECT_FOLDER
touch .htaccess
echo 'RewriteEngine On
RewriteCond %{REQUEST_FILENAME} !-f
RewriteRule ^ index.php [QSA,L]' > .htaccess
exit"

#secure file transfer created folders 
#from local to server (recursively)
scp -r app config $USERNAME@$HOST:htdocs/$PROJECT_FOLDER

#set up access rights
ssh $USERNAME@$HOST "
chmod -R a+rX htdocs
exit"

echo "PROJECT SET UP DONE!"