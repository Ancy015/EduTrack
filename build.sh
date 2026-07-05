#!/usr/bin/env bash
set -o errexit
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic --noinput
echo "from django.contrib.auth.models import User; User.objects.filter(username='admin').exists() or User.objects.create_superuser('admin', 'admin@edutrack.com', 'Ancy@2026')" | python manage.py shell
