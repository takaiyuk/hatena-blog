### 利用例

#### デフォルトは下書き投稿
```
cp config.yml.example config.yml  # 項目を適宜書き換える
python main.py
```

#### 下書き投稿ではなく即投稿でよければ
```
python main.py --production
```

### config.yml 書き換え例
```
QIITA_USER: takaiyuk
OUTPUT_DIR: articles
HATENA_USER: takaishikawa42
HATENA_BLOG: takaishikawa42.hatenablog.com
HATENA_APIKEY: xxxxxxxx
```
