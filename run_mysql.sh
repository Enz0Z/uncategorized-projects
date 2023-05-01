#!/bin/bash

wget https://cdn.mysql.com/archives/mysql-8.0/mysql-8.0.32-linux-glibc2.12-x86_64.tar.xz
tar xf mysql-8.0.32-linux-glibc2.12-x86_64.tar.xz
chown -R 700 mysql-8.0.32-linux-glibc2.12-x86_64
cd mysql-8.0.32-linux-glibc2.12-x86_64/bin
apt-get install libnuma-dev libaio1 -y
./mysqld --initialize
# ./mysqld --console --user=root <-- NOT RECOMMENDED
