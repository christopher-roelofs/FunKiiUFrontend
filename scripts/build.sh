#!/bin/bash
mkdir ../releases/$1
pyinstaller ../src/frontend.py
cp ../src/about.txt dist/frontend
cd dist/frontend/; zip ../../../releases/$1/frontend\ $1.zip *
cd ../../
rm -rf build & rm -r dist
