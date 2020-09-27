#!/bin/bash
sudo docker build . -t takaiyuk/lyric-classifiction:preprocess -f ./docker/preprocess/Dockerfile
