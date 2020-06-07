# Name

## Portfolio
Djangoで作成したポートフォリオ
[https://maro-portfolio.herokuapp.com/](https://maro-portfolio.herokuapp.com/)

# Features

## ブログ風のポートフォリオ

### 記事投稿
Django管理ページから記事投稿

### 目次自動作成
記事投稿時、見出しをh2タグで囲む目次を自動で作成

#### 目次の機能
* 本文中の各見出しへのリンク
* リンクを押すとスムーズにスクロール

### コメント投稿
各記事にコメント投稿可能
投稿したコメントは即時に本文下に反映

### スクロールボタン
ページトップヘスクロールするボタン

#### スクロールボタンの機能
* ページを下にスクロールすると表示
* スムーズにページトップヘスクロール

# Requirement

* python          3.7.7
* dj-database-url 0.5.0
* Django          2.0.2
* django-heroku   0.3.1
* gunicorn        19.9.0
* psycopg2        2.8.5
* pytz            2020.1
* whitenoise      5.1.0

# Author

* 作成者    maro
* Twitter   [@maroblog28](https://twitter.com/maroblog28)
