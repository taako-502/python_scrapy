# python_scrapy

## 参考文献
https://qiita.com/Chanmoro/items/f4df85eb73b18d902739

## 使ったコマンド
プロジェクトの作成
```
scrapy startproject <プロジェクト名>
```

Spiderを追加
```
scrapy genspider <スパイダー名> <クロール対象ドメイン名>
```

実行するとき
```
scrapy crawl <スパイダー名>
```

例）
```
scrapy crawl quotes
scrapy crawl scrapy_blog_spider
```
