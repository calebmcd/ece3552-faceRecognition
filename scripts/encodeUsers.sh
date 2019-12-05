#!/bin/bash

cd ~/finalProject

python3 encode_faces.py --dataset dataset --encodings encodings.pickle \
	--detection-method hog
