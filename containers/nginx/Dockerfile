FROM nginx:1.21-alpine

RUN apk add --no-cache certbot certbot-nginx

# ローカルのdefault.confをコンテナにコピー
COPY containers/nginx/conf.d/default.conf /etc/nginx/conf.d/default.conf
