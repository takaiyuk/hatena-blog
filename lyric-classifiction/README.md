# Lyric Classification

## Setup & Run

### Crawler

```
$ ./docker/crawler/build.sh
$ ./docker/crawler/run.sh
```

local
```
$ ./shell/download_chromedriver.sh
$ python run.py crawler --headless
```

### Preprocess

```
$ ./docker/preprocess/build.sh
$ ./docker/preprocess/run.sh
$ ./docker/preprocess/exec.sh
root@xxx:/workspace# python run.py preprocess
```

### Train

```
$ ./docker/train/pull.sh
$ ./docker/train/run.sh
```
