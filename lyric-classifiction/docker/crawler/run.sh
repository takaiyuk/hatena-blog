#!/bin/bash
sudo docker run --rm -it -v ${PWD}:/workspace takaiyuk/lyric-classifiction:crawler run.py crawler --headless
