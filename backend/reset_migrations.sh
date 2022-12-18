rm db.sqlite3
mv user/migrations/0002_create_superuser.py .
rm **/migrations/0*
python manage.py makemigrations
mv 0002_create_superuser.py user/migrations/0002_create_superuser.py
python manage.py migrate
python manage.py loaddata cars.json
