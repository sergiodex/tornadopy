# Prerequisites

To start developing in the "tornadopy" project, you must install the following tools.

## Tornadopy python 2.7

`pip install tornado`

## Tornadopy python 3.7

`sudo apt-get install -y python3-tornado`

## PostgreSQL

`apt install postgresql postgresql-contrib`

## Visual Code Debugging

* install extension python.
* next: Start Debugin.
* next: Select File main.py.

# Getting Started

Prepare the environment and run the app with the steps detailed below.

## Create virtual env
`python3 -m venv /path/to/new/virtual/environment`

## Activate virtual env
`source  /path/to/new/virtual/environment/bin/activate`

## Install requeriments
`pip install -r tornado/requirements.txt`

## Import DB

Check the `db.ini` file.

* Create a database (`db.ini = database`)
* Create an user (`db.ini = user`)
* Assign password to created user (`db.ini = password`)

You can visit this link to execute the steps described above (https://medium.com/coding-blocks/creating-user-database-and-adding-access-on-postgresql-8bfcd2f4a91e)

* Import db.sql (pinned in the slack group ) using this command line:
    `psql -U tornadopy -h localhost tornadopydb < db.sql`

## Run the server console
`python3 main.py`

`options:`

    --port 8080
