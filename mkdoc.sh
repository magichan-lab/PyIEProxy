#!/bin/sh

sphinx-apidoc -F -o doc simple
rm doc/make.bat
rm doc/Makefile
sed -i -e "s/^langulage = 'en'/language = 'ja'/" doc/conf.py
