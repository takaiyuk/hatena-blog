#!/bin/bash
sudo docker run -d --name lyric-classifiction-preprocess -p 8888:8888 -v ${PWD}:/workspace takaiyuk/lyric-classifiction:preprocess
