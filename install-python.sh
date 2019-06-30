#!/bin/bash

echo "install dependences"
yum -y groupinstall "Development tools"
yum -y install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel libffi-devel

echo "download and compile python"
# wget https://www.python.org/ftp/python/3.7.3/Python-3.7.3.tar.xz
wget https://npm.taobao.org/mirrors/python/3.7.3/Python-3.7.3.tar.xz
tar -xvJf  Python-3.7.3.tar.xz
cd Python-3.7.3
./configure --prefix=/usr/local/bin/python3.7
make
make install

echo "link python bin to app path"
ln -s /usr/local/bin/python3.7/bin/python3.7 /usr/bin/python3.7
ln -s /usr/local/bin/python3.7/bin/pip3.7 /usr/bin/pip3.7