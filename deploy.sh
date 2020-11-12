#!/bin/bash
# This is a manual deployment script for ease of life. Would be much
# better if we have an auto deployment system like git hooks
# but I haven't been able to set it up yet

cd ~/website

# front end deployment
echo PULLING NEW FRONT END CODE...
cd front-end/
git checkout master
git pull
echo [OK]

echo BUILDING FRONT END CODE...
npm install
npm run build
echo [OK]

# back end deployment
echo PULLING NEW BACK END CODE...
cd ../back-end/
git checkout master
git pull
echo [OK]

echo UPDATING NGINX CONFIG...
cp ./tedxuwa_nginx.conf /etc/nginx/sites-available/default
sudo /etc/init.d/nginx restart 
echo [OK]

echo UPDATING CERTBOT HOOKS...
cp ./scripts/certbot_prerenew.sh /etc/letsencrypt/renewal-hooks/pre
cp ./scripts/certbot_postrenew.sh /etc/letsencrypt/renewal-hooks/post
chmod +x /etc/letsencrypt/renewal-hooks/pre/certbot_prerenew.sh
chmod +x /etc/letsencrypt/renewal-hooks/post/certbot_postrenew.sh
echo [OK]

echo UPDATING DEPLOYMENT SCRIPT...
cp deploy.sh ../
echo [OK]

echo INSTALLING REQUIREMENTS...
source env/bin/activate
pip install -r requirements.txt
echo [OK]

echo COLLECTING STATIC FILES...
python manage.py collectstatic --noinput --clear
echo [OK]

echo RUNNING MIGRATIONS...
python manage.py migrate  # migrate the database
echo [OK]

echo STARTING SERVER...
uwsgi --socket :8001 --module root.wsgi --home env -b 32768
