Important commands listed below:

find . -name "*.pyc" -exec rm -f {} \;
python3 manage.py collectstatic
python3 manage.py runserver
python3 manage.py makemigrations
python3 manage.py migrate