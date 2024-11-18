### 注意
- 以下のコマンドは、docker-compose.yml が存在するディレクトリで実行してください。
- windows_mainブランチで作業してください。

### ローカル環境起動
```
docker compose -f docker-compose.prod.yml up --build -d --remove-orphans
```
- -f オプションをつけると指定したファイルを使ってコンテナを起動します。
- --build オプションをつけるとイメージを再ビルドします。
- -d オプションをつけるとバックグラウンドで起動します。

### イメージ作成
```
docker compose -f docker-compose.prod.yml build --no-cache
```
- --no-cache オプションをつけるとキャッシュを使わずにイメージを作成します。

### ローカル環境削除
```
docker compose -f docker-compose.prod.yml down
```

### webコンテナに入ってログを出力
```
docker exec -it web /bin/sh

tail -f /var/log/nginx/default_access.log
tail -f /var/log/nginx/json_access.log
```
