# restart nginx after certbot renewal
sudo systemctl daemon-reload
sudo systemctl restart nginx
sudo systemctl restart gunicorn