#!/bin/bash
sudo docker run --rm -it -v ${PWD}:/workspace takaiyuk/lyric-classifiction:train run.py train
