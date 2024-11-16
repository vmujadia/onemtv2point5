#!/bin/bash

virtualenv -p python3.8 venv
source venv/bin/activate

pip3 install --upgrade pip==24.0.0

git clone https://github.com/pytorch/fairseq
cd fairseq
git checkout v0.12.2
pip install --editable ./

cd ..
pip3 install -r requirements.txt


mkdir models
python3 downloadmodels.py
