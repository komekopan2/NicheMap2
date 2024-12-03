FROM postgres:17.1

COPY containers/postgres/docker-entrypoint-initdb.d/ /docker-entrypoint-initdb.d/
RUN apt update && apt install -y postgresql-17-postgis-3
