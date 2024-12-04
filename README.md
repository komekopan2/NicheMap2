# docker composeコマンド

### ローカル環境起動
- Dockerfileと関連するファイルに変更があった場合は、イメージ作成のコマンドを叩いてから起動する。
```
docker compose -f docker-compose.prod.yml up -d --remove-orphans
```
- -f オプションをつけると指定したファイルを使ってコンテナを起動します。
- -d オプションをつけるとバックグラウンドで起動します。
- --remove-orphans オプションをつけると未使用のコンテナを削除します。
- （--build オプションをつけるとイメージを再ビルドします。）

### イメージ作成
```
docker compose -f docker-compose.prod.yml build --no-cache
```
- --no-cache オプションをつけるとキャッシュを使わずにイメージを作成します。

### ローカル環境削除
```
docker compose -f docker-compose.prod.yml down
```
# docker execコマンド

### webコンテナに入ってログを出力
- コンテナに入る
```
docker exec -it web /bin/sh
```

- デフォルトのアクセスログをリアルタイムで見る
```
tail -f /var/log/nginx/default_access.log
```

- JSON形式のアクセスログをリアルタイムで見る
```
tail -f /var/log/nginx/json_access.log
```

### dbコンテナに入る
```
docker exec -it nichemap2-db-1 /bin/bash
```

### appコンテナに入る
```
docker exec -it nichemap2-app-1 /bin/bash
```
# ストレージが足りない場合の対処法

### システムのディスク容量を確認
```
df -h
```

### 全ての停止中コンテナ、未使用イメージ、ネットワーク、ボリュームを一括削除
```
docker system prune -a
```

### Dockerのキャッシュディレクトリをクリア
```
docker builder prune
```
