#!/bin/bash
# Apply database migrations
python manage.py migrate

# Start the application
exec "$@"