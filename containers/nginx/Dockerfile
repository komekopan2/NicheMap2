FROM nginx:1.21-alpine

RUN apk add --no-cache certbot certbot-nginx

# ローカルのdefault.confをコンテナにコピー
COPY containers/nginx/conf.d/default.conf /etc/nginx/conf.d/default.conf
COPY fullchain.pem /etc/letsencrypt/live/niche-map.shimizu-v.net/fullchain.pem
COPY privkey.pem /etc/letsencrypt/live/niche-map.shimizu-v.net/privkey.pem
COPY polls/static/admin /static/admin
COPY polls/static/polls /static/polls

# タイムゾーン設定に必要なパッケージをインストール、タイムゾーンを設定
RUN apk add --no-cache tzdata
ENV TZ=Asia/Tokyo

# alpのインストール
RUN curl -LO https://github.com/tkuchiki/alp/releases/latest/download/alp_linux_amd64.zip
RUN unzip alp_linux_amd64.zip
RUN mv alp /usr/local/bin/alp
RUN chmod +x /usr/local/bin/alp
