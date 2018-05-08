# tedxuwa-server-backend [![CircleCI](https://circleci.com/gh/TEDxUWA/tedxuwa-server-backend.svg?style=svg)](https://circleci.com/gh/TEDxUWA/tedxuwa-server-backend)  [![codecov](https://codecov.io/gh/TEDxUWA/tedxuwa-server-backend/branch/master/graph/badge.svg)](https://codecov.io/gh/TEDxUWA/tedxuwa-server-backend)

This repo contains code for the database and server of the TEDxUWA website

## Getting started
The instructions below will help you set up a development environment

### Python prerequisite
Download and install [python 3](https://www.python.org/downloads/)

### Virtual environment
`cd` into the project folder
```bash
$ cd tedxuwa-server-backend
```
Download virtualenv
```bash
$ pip install virtualenv
```
If you have multiple versions of python installed, please run `pip3` instead

A virtual environment ensure everyone working on this project will have the same dependencies
installed and avoid the "it worked on my machine" bug. Create a new virtualenv with
```bash
$ virtualenv env
```
If you have multiple versions of python installed, run:
```bash
$ virtualenv -p python3 env
```
To activate the virtual environment, run
```bash
$ source env/bin/activate
```
You will need to run this command every time you want to continue working on this repo

### Requirements
Installing requirements
```bash
$ pip install -r requirements.txt
```

### Database setup
Run migrations
```bash
$ python manage.py migrate
```
Load dummy data


### Starting the server
To start up the server, run
```bash
$ python manage.py runserver
```
The server will now be avalaible at [localhost:8000](http://localhost:8000/).
For more server starting options, visit the [django docs](https://docs.djangoproject.com/en/2.0/ref/django-admin/#runserver) for the runserver command

## Deployment

### Using deployment script
On the digital ocean instance there is a folder called `website` on the root directory. Inside this folder there are 2 more folders: `front-end` and `back-end` each having the code from the repo. To use the auto deployment script, cd from the root into the back-end
```shell
$ cd website/back-end/
```
Then run the deployment script with 
```shell
$ ./deploy.sh
```
If for some reason it tells you the file doesn't have execute permission, run the following command then try again
```shell
$ chmod +x deploy.sh
```

### Manual deployment
If the deployment script no longer work, these are the steps to fully deploy both backend and front end

#### Front end deployment
```shell
$ cd website/front-end/  # go to the front end folder
$ git checkout master  # change branch to the master branch
$ git pull  # pull new code if any
$ npm build  # this bundles the files
```

#### Back end deployment
```shell
$ cd website/back-end/  # go to the back end folder
$ git checkout master  # change branch to the master branch
$ git pull  # pull new code if any
$ source env/bin/activate  # activate the virtual environment
$ pip install -r requirements.txt  # install new requirements if any
$ python manage.py collectstatic --noinput  # collect static files (images, html, css, etc...)
$ python manage.py migrate  # run new migration files if any
$ python manage.py runserver 0.0.0.0:8000  # runserver on port 8000
```
## Built with
- Django: [a server framework for python](https://www.djangoproject.com/)
- Sqlite: [small imbeded database](https://www.sqlite.org/index.html)
- Circleci: [continuous intergration service](https://circleci.com/gh/TEDxUWA/tedxuwa-server-backend)
- Codecov: [code coverage service](https://codecov.io/gh/TEDxUWA/tedxuwa-server-backend)
- Sentry: [automated error log capture](https://sentry.io/tedxuwa/tedxuwa/)

## Notes
- The `db.sqlite3` IS the database. Backup regularly and don't delete it on production
- The front end template dir is set to `static/build/` with entry point of `react_base.html`

## Things to remember
- [ ] set `DEPLOYMENT` environment variable in production
- [ ] regenerate django secret key
- [ ] protect master branch
- [ ] run `collectstatic`
