#!/bin/bash

wget https://cdn.mysql.com//Downloads/MySQL-8.0/mysql-8.0.31-linux-glibc2.12-x86_64.tar.xz
tar xf mysql-8.0.31-linux-glibc2.12-x86_64.tar.xz
chown -R 700 mysql-8.0.31-linux-glibc2.12-x86_64
cd mysql-8.0.31-linux-glibc2.12-x86_64/bin
apt-get install libnuma-dev -y
./mysqld --initialize
# ./mysqld --console --user=root <-- NOT RECOMMENDED