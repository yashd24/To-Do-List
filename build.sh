#!/usr/bin/env bash
# Exit on error
set -o errexit

# Install dependencies
pip install -r requirements.txt

# Convert static asset files
python manage.py collectstatic --noinput

# Apply database migrations
python manage.py migrate

# load the env variables
export $(cat .env | xargs)

# Create a superuser non interactively
python manage.py shell -c "
from App.models import CustomUser
import os

username = os.getenv('DJANGO_SUPERUSER_USERNAME')
email = os.getenv('DJANGO_SUPERUSER_EMAIL')
password = os.getenv('DJANGO_SUPERUSER_PASSWORD')

if not CustomUser.objects.filter(username=username).exists(): 
    CustomUser.objects.create_superuser(username=username, email=email, password=password);
    print(f'Superuser {username} created successfully.');
else:
    print(f'Superuser {username} already exists.');

"