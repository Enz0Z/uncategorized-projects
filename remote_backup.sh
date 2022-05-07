#!/bin/sh

SERVER="IP"
USERNAME="USER"
PASSWORD="PASSWORD"
SOURCE="ROOT"

_DATE=`date '+%j_%Y-%m-%d'`
_HOSTNAME=`hostname`
_REMOTE="${_HOSTNAME}__${_DATE}.tar.gz"

tar -czf $_REMOTE $SOURCE

ftp -n -i $SERVER <<EOF
user $USERNAME $PASSWORD
mput $_REMOTE
quit
EOF

rm -rf $_REMOTE