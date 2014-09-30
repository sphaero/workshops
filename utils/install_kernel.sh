#!/bin/bash
set -e

if [ -z $1 ]; then
    echo "please provide a deb kernel package as a first argument"
    exit 1
fi

rm -rf debian-binary data.* control.* usr/ lib/ boot/ || true
#wget http://security.debian.org/debian-security/pool/updates/main/l/linux/linux-image-3.2.0-4-486_3.2.57-3+deb7u1_i386.deb

ar -x $1
unxz data.tar.xz
tar -xf data.tar
cp -r lib jessie/
rm -rf data.tar control.tar.gz lib/ usr/ debian-binary
