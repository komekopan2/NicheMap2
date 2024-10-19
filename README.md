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

### ローカル環境削除
```
docker compose -f docker-compose.prod.yml down
```
