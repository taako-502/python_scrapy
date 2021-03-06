# python_scrapy

## 参考文献
[10分で理解する Scrapy](https://qiita.com/Chanmoro/items/f4df85eb73b18d902739)

## 使ったコマンド
### プロジェクトの作成
```
scrapy startproject <プロジェクト名>
```

### Spiderを追加
```
scrapy genspider <スパイダー名> <クロール対象ドメイン名>
```

### 実行するとき
```
scrapy crawl <スパイダー名>
```

例）
```
scrapy crawl quotes
scrapy crawl scrapy_blog_spider
```

### ファイルに出力するとき
下記はCSVファイルに出力するコマンドです。
```
scrapy crawl {スパイダー名} -o data.csv
```
例）
```
scrapy crawl scrapy_blog_spider -o data.csv
```
csv の他にもデフォルトで json, json lines, xml に対応しています。

## sqlite3
作成したデータベースの中身の内容の確認方法。<br>
参考文献：[sqlite のコマンド集](https://qiita.com/rhinonolike/items/d7641e84af2c048ccb32)
```
sqlite3 <データベース名>
select * from post
.quit
```
