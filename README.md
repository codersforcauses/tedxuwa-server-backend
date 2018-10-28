# tedxuwa-server-backend [![CircleCI](https://circleci.com/gh/TEDxUWA/tedxuwa-server-backend.svg?style=svg)](https://circleci.com/gh/TEDxUWA/tedxuwa-server-backend)  [![codecov](https://codecov.io/gh/TEDxUWA/tedxuwa-server-backend/branch/master/graph/badge.svg)](https://codecov.io/gh/TEDxUWA/tedxuwa-server-backend)

This repo contains code for the database and server of the TEDxUWA website

## Table of Contents
  * [Getting started](#getting-started)
    + [Python prerequisite](#python-prerequisite)
    + [Virtual environment](#virtual-environment)
    + [Requirements](#requirements)
    + [Database setup](#database-setup)
    + [Starting the server](#starting-the-server)
  * [Deployment](#deployment)
    + [Folder structure](#folder-structure)
    + [Using deployment script](#using-deployment-script)
    + [Setting up a new server](#setting-up-a-new-server)
      - [1. Installing system dependencies](#1-installing-system-dependencies)
      - [2. Create folder structure](#2-create-folder-structure)
      - [3. Run deployment script](#3-run-deployment-script)
      - [4. Setup https](#4-setup-https)
      - [5. Load data from existing database?](#5-load-data-from-existing-database-)
  * [Built with](#built-with)
  * [Notes](#notes)
  * [Things to remember](#things-to-remember)



## Getting started

The instructions below will help you set up a development environment

### Python prerequisite

Download and install [python 3.6](https://www.python.org/downloads/)

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
$ virtualenv -p python3.6 env
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

### Folder structure

The folder structure is as follows:
```
root (~/)
└── website
    ├── back-end
    ├── deploy.sh
    └── front-end
```

Where `back-end` is this repo and `front-end` is our [front end repo](https://github.com/TEDxUWA/tedxuwa-react). This structure is embedded in most of
the code (nginx config, deployment script, etc...) so it's a little hard to change.

`deploy.sh` is a copy of the `deploy.sh` file in this repo. It's copied out to the 
website folder so that we don't have to add execute permission to it everytime backend updates.
This is the script to be run when you want to deploy either front end or back end code.

### Using deployment script

To run the deployment script, run
```bash
$ cd ~/website
$ ./deploy.sh
```
If deploy.sh doesn't have the permission to run, do `chmod +x deploy.sh` first then try again. If that still
doesn't work, open up the file and copy paste the commands inside

**NOTE:** If you made a change to the deployment script, running `./deploy.sh` once will update the deployment script file on the server and running it a second time will make the changes take effect

### Setting up a new server

If you are setting up a brand new server, access the server's console and follow these steps:
**NOTE:** before you setup a new server, make sure you have a backup of the `db.sqlite3` file from
the server available. This **IS** the database including all the data so copy it out before you delete the old server

#### 1. Installing system dependencies
```bash
$ sudo apt-get update
# python and pip
$ sudo apt-get install python3.6-dev
$ sudo apt-get install -y python3-pip
# c compiler for uWSGI
$ sudo apt-get install build-essential
# nginx
$ sudo apt-get install nginx
```

#### 2. Create folder structure
```bash
$ cd ~/
$ mkdir website
$ cd website
$ git clone https://github.com/TEDxUWA/tedxuwa-server-backend.git ./back-end
$ git clone https://github.com/TEDxUWA/tedxuwa-react.git ./front-end
```

#### 3. Run deployment script
```bash
# copy it out to ~/website
$ cp back-end/deploy.sh ./
# add execute permission
$ sudo chmod +x deploy.sh
# run it
$ ./deploy.sh
```
The server should now be setup and running!

#### 4. Setup https
Certbot can be used to setup https. Head to [https://certbot.eff.org/](https://certbot.eff.org/) 
and select NGINX and the appropriate OS that the new server is running on and follow the instructions.

#### 5. Load data from existing database?
If you're migrating the server and closing down the old one, you have 2 options to migrate the data over
1. Copying `db.sqlite3`
If the new server will still be using sqlite as the database, you can simply copy the `db.sqlite3` file from the old server over the the new one and all should be working
2. Using Django's [dumpdata](https://docs.djangoproject.com/en/2.1/ref/django-admin/#dumpdata) and [loaddata](https://docs.djangoproject.com/en/2.1/ref/django-admin/#loaddata)
You can use `dumpdata` to dump everything in the database into a json file then use `loaddata` on the new server to populate them all again. Using this you can switch from using sqlite to using another database by [changing the database driver](https://docs.djangoproject.com/en/2.0/ref/settings/#databases) and load the data into the new database

## Built with
- Django: [a server framework for python](https://www.djangoproject.com/)
- Nginx: [webserver](https://www.nginx.com/)
- uWSGI: [application server container](https://uwsgi-docs.readthedocs.io/en/latest/)
- Sqlite: [small imbeded database](https://www.sqlite.org/index.html)
- Circleci: [continuous intergration service](https://circleci.com/gh/TEDxUWA/tedxuwa-server-backend)
- Codecov: [code coverage service](https://codecov.io/gh/TEDxUWA/tedxuwa-server-backend)
- Sentry: [automated error log capture](https://sentry.io/tedxuwa/tedxuwa/)

## Notes
- The `db.sqlite3` **IS** the database. Backup regularly and don't delete it on production
- The front end template dir is set to `static/build/` with entry point of `react_base.html`

## Things to remember
- [x] set `DEPLOYMENT` environment variable in production
- [x] regenerate django secret key
- [ ] protect master branch
- [x] run `collectstatic`
