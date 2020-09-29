#!/bin/bash
sudo docker run -d --name lyric-classifiction-train -p 8888:8888 -v ${PWD}:/workspace takaiyuk/lyric-classifiction:train
