#!/bin/bash

function check_return_code {
    return_code=$?;
    if [[ $return_code != 0 ]]; then
        exit $return_code;
    fi
}

# Check if database is ready
echo "Checking Database"
while ! python manage.py showmigrations 2> /dev/null; do
  echo "Database isn’t ready yet"
  sleep 1
done

# Check API is ready
echo "Checking API"
while ! curl --insecure --silent --connect-timeout 1 $API_URL/health/ping; do
  echo "API isn’t ready yet"
  sleep 1
done

# Run migrations
echo "Runing migrations"
python manage.py migrate
check_return_code

# Migrate legacy users
echo "Migrating legacy users"
python manage.py migrate_legacy_users
check_return_code

# Process statics
echo "Process statics"
python manage.py collectstatic --noinput
check_return_code

# Launch serve app
echo "Starting Django"
gunicorn -b :8000 app.wsgi
