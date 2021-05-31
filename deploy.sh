pip install -U pip
pip install -r requirements.txt
coverage run --source='.'./ manage.py test .
echo 'Deploy DONE'
