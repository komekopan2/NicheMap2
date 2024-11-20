FROM postgres

COPY containers/postgres/docker-entrypoint-initdb.d/ /docker-entrypoint-initdb.d/
RUN apt update && apt install -y postgresql-16-postgis-3
