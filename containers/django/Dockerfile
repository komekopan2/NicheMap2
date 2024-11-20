# syntax=docker/dockerfile:1
# Pythonのイメージを指定
FROM python:3.9
# PYTHONDONTWRITEBYTECODEとPYTHONUNBUFFEREDはオプション
# pycファイル(および__pycache__)の生成を行わないようにする
ENV PYTHONDONTWRITEBYTECODE=1
# 標準出力・標準エラーのストリームのバッファリングを行わない
ENV PYTHONUNBUFFERED=1

# 必要なパッケージをインストール
RUN apt-get update && apt-get install -y \
    binutils \
    libproj-dev \
    gdal-bin \
    libgeos-dev \
    libgdal-dev

# コンテナのワークディレクトリを/codeに指定
WORKDIR /code
# ローカルのrequirements.txtをコンテナの/codeフォルダ直下に置く
COPY ../../requirements.txt /code/
# コンテナ内でpipをアップグレード
RUN pip install --upgrade pip
# pip install -r requirements.txtを実行
RUN pip install -r requirements.txt
# ソースコードをコンテナにコピー
COPY ../.. /code/
# ヒストリを保存するディレクトリを作成
RUN mkdir /root/myhistory
# ヒストリファイルを作成
RUN touch /root/myhistory/.history
# ヒストリファイルのパーミッションを変更
RUN chmod 600 /root/myhistory/.history