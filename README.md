Our goal for today is to build a realtime chatroom using Django, Redis, and Socket.IO.
While we'll be building a chatroom the concepts can be applied to almost any web app. 

Setup

1. Django 1.10
2. nodeJs
3. redis-server

Redis Installation

### [Redis Server](http://redis.io/download)

sudo apt-get install redis-server

### [Redis-py](https://github.com/andymccurdy/redis-py)

sudo pip install redis    

### [NodeJs Installation](https://github.com/joyent/node/wiki/Installing-Node.js-via-package-manager)

sudo apt-get install python-software-properties
sudo add-apt-repository ppa:chris-lea/node.js
sudo apt-get update
sudo apt-get install nodejs

Ones this is done then go to node directory 

npm install

Django Installation

Ones virtual environment activate 

pip install Django==1.10

After then go to project directory 

python manage.py makemigration

python manage.py migrate

python manage.py createsuperuser

python manage.py runserver
