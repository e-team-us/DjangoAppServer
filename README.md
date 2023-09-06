# 児童出欠管理アプリ「おるん」

## システム概要
幼稚園や保育園での、児童の出欠管理を行うためのアプリケーションです。
保育士は、児童一覧から保護者によって登録された児童の出欠情報を確認することができます。
保育士は児童の出欠登録を確認し、欠席の場合には確認ボタンを押すことで保護者に確認された旨が送信されます。

## 必要環境
- Python
- Django
- Node.js
- Vue.js
- Vuetify


## アプリのディレクトリ構成
```
mySite
│  db.sqlite3
│  manage.py
│
├─myapp
│  │  admin.py
│  │  apps.py
│  │  initChildren.py
│  │  initSetData.py
│  │  models.py
│  │  setDummyData.py
│  │  tests.py
│  │  urls.py
│  │  views.py
│  │  __init__.py
│  │
│  ├─migrations
│     └─ __init__.py
│
└─mySite
    │  asgi.py
    │  settings.py
    │  urls.py
    │  wsgi.py
    └─ __init__.py
```

### 起動方法→下を参照
1. mySite/に入る。
2. ``` python manage.py migrate ```を実行し、データベースを作成する。
3. ``` python3 manage.py runserver ```を実行してDjango側でAPサーバーを立ち上げる。

4. vuetify-project/に入り、``` npm run dev ```を実行してVue.js側でWebサーバーを立ち上げる。

5. ``` npm run dev ```により立ち上がったサーバーにアクセスすると、アプリの画面が開かれる。


## アプリの使い方
#### 保護者
1. ログイン画面で保護者のタブを選択し、児童IDを入力して "ログイン" ボタンを押す。
2. メイン画面で "出欠登録" ボタンを押す。
3. "出席" か "欠席" を選択して "送信" ボタンを押す。欠席の場合は、欠席理由を入力する。
4. 保育士が確認し次第、メイン画面に確認した旨が表示される。

#### 保育士
1. ログイン画面で保育士のタブを選択し、保育士IDを入力して "ログイン" ボタンを押す。
2. 児童一覧表を見て、児童の出欠状況を確認する。
3. 表の欠席の欄にある児童をタップする。
4. 欠席理由を確認し、"確認" ボタンをタップする。 



<!--
### 環境構築、アプリ立ち上げの手順
0. corsheadersをインストール, '''conda install -c conda-forge django-cors-headers'''
1. mySite/に入る。
2. ``` python manage.py migrate ```を実行し、データベースを作成する。
3. ``` python manage.py runserver ```を実行してDjango側でAPサーバーを立ち上げる。

3. '''npm create vuetify''' をしてファイルを作る。'''npm install axios''' '''npm install vue-router'''

3. vuetify-projectの中身を入れ替える

4. vuetify-project/に入り、``` npm run dev ```を実行してVue.js側でWebサーバーを立ち上げる。

5. ``` npm run dev ```により立ち上がったサーバーにアクセスすると、アプリの画面が開かれる。


6. 再起動時は'''python manage.py runserver''' '''npm run dev'''をそれぞれ別のターミナルでやることで再起動

7. バックエンドの方は起動字に表示されるアドレスに"/admin"をつけることで管理画面に行ける。ターミナルでアカウントを作ることで（djangoのチュートリアル参照）管理画面に行ける。

### バックエンドのtips:
- [django document](https://docs.djangoproject.com/ja/4.2/)
- [Djanoの render, redirect](https://kuma-server.com/django-render-redirect-httpresponse/)

#### Python HTTPserver
- [Python http通信のサンプル](https://itsakura.com/python-http)
- [python3 -m http.serverをCORSにする【Access-Control-Allow-Origin】](https://qiita.com/relu/items/3461753e3886072349c7)
- [python3にてJSONを受け取ってJSONを返す簡単なサーバを立てる](https://qiita.com/komorin0521/items/dfc02444a60180688e43
)
- [Django REST FrameworkなしでJSONを送受信するapiを作る](https://qiita.com/t-iguchi/items/ac9638dbdbe509515148)
- [apiのテストにつけるツール。リクエストをフロントエンドなしに送るツール](https://chrome.google.com/webstore/detail/talend-api-tester-free-ed/aejoelaoggembcahagimdiliamlcdmfm?hl=ja)

### フロントエンドのTips:
- [vuetifyの公式ベージ コンポーネントの情報ここにある](https://vuetifyjs.com/en/components/buttons/)
- [getを送ると天気を返してくれる場所、テスト用](https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current_weather=true)

### ReadmeのTips:
- [素敵なREADMEの書き方](https://qiita.com/koeri3/items/f85a617dcb6efebb2cab)
- [↑の記事内で紹介されている素敵なREADMEがまとまったgithub](https://github.com/matiassingers/awesome-readme)
-->
