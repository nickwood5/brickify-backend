
#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt
python -m pipenv install

python manage.py migrate