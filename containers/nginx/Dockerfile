FROM nginx:1.21-alpine

RUN apk add --no-cache certbot certbot-nginx

# ローカルのdefault.confをコンテナにコピー
COPY containers/nginx/conf.d/default.conf /etc/nginx/conf.d/default.conf
COPY fullchain.pem /etc/letsencrypt/live/niche-map.shimizu-v.net/fullchain.pem
COPY privkey.pem /etc/letsencrypt/live/niche-map.shimizu-v.net/privkey.pem
COPY polls/static/admin /static/admin
COPY polls/static/polls /static/polls

# タイムゾーン設定に必要なパッケージをインストール
RUN apk add --no-cache tzdata

# タイムゾーンをTokyoに設定
ENV TZ=Asia/Tokyo
