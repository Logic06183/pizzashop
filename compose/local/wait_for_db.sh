#!/bin/sh

set -e

host="$DB_HOST"
user="$POSTGRES_USER"
shift

until pg_isready -h "$host" -U "$user"; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 5
done

>&2 echo "Postgres is up - executing command"
exec "$@"
