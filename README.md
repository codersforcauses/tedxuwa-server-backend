# txuwa-server-backend

This repo contains code for the database and server of the TEDxUWA website

## Getting started
The instructions below will help you set up a development environment

### Prerequisite
1. Download and install [python 3](https://www.python.org/downloads/)

### Installing
1. `cd` into the project folder. For example:
```bash
$ cd somepathname/txuwa-server-backend
```
2. Download virtualenv
```bash
$ pip install virtualenv
```
If you have multiple versions of python installed, please run `pip3` instead

3. Create a virtualenv

A virtual environment ensure everyone working on this project will have the same dependencies
installed and avoid the "it worked on my machine" bug
```bash
$ virtualenv env
```
If you have multiple versions of python installed, run:
```bash
$ virtualenv -p python3 env
```
4. Activating the virtual environment

To activate the virtual environment, run
```bash
$ source env/bin/activate
```
You will need to run this command every time you want to continue working on this repo

5. Installing requirements
```bash
$ pip install -r requirements.txt
```

6. Run migrations
```bash
$ python manage.py migrate
```
7. Point to settings file
Run `vim env/bin/activate`
right below the
```
_OLD_VIRTUAL_PATH="$PATH"
PATH="$VIRTUAL_ENV/bin:$PATH"
export PATH
```
put in
```
export DJANGO_SETTINGS_MODULE="root.settings"
```
reactivate the virtualenv
```bash
$ source env/bin/activate
```

7. Load dummy data


### Starting the server
To start up the server, run
```bash
$ python manage.py runserver
```
The server will now be avalaible at [localhost:8000](http://localhost:8000/).
For more server starting options, visit the [django docs](https://docs.djangoproject.com/en/2.0/ref/django-admin/#runserver) for the runserver command

## Deployment
TO BE WRITTEN
Digital Ocean and Github hook??

## Built with
- Django (a server framework for python)
- Sqlite (small imbeded database)

## Notes
- The `db.sqlite3` IS the database. Backup regularly and don't delete it on production

## Things to remember
- [ ] set `DEPLOYMENT` environment variable in production
- [ ] protect master branch