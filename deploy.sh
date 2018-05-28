#!/bin/sh
# This is a manual deployment script for ease of life. Would be much
# better if we have an auto deployment system like git hooks
# but I haven't been able to set it up yet

# THIS ASSUME YOU'RE IN /website

# front end deployment
echo -n PULLING NEW FRONT END CODE...\ 
cd front-end/
git checkout master
git pull
echo [OK]

echo -n BUILDING FRON END CODE...\ 
npm run build
echo [OK]

# back end deployment
echo -n PULLING NEW BACK END CODE...\ 
cd ../back-end/
git checkout master
git pull
echo [OK]

echo -n INSTALLING REQUIREMENTS...\ 
source env/bin/activate
pip install -r requirements.txt
echo [OK]

echo -n COLLECTING STATIC FILES...\ 
python manage.py collectstatic --noinput --clear
echo [OK]

echo -n RUNNING MIGRATIONS...\ 
python manage.py migrate  # migrate the database
echo [OK]

echo -n STARTING SERVER...\ 
python manage.py runserver 0.0.0.0:80  # start the server on port 8000
