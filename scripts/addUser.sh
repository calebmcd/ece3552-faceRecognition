#!/bin/bash

cd ~/finalProject

echo Name of User:
read userName

python3 build_face_dataset.py --cascade haarcascade_frontalface_default.xml \
	--output dataset/$userName
