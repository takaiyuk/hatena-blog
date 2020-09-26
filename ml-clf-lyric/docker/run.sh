#!/bin/bash
sudo docker run --rm -it -v ${PWD}:/workspace takaiyuk/lyric-classifiction run.py --headless --start $1 --end $2
