Django-Node-Chat
==================
An application for chatting on Django & Node.
Python version : 2.7.10 

## How to Work on this Project (on a mac)

### Setting up your system
```sh
git clone https://github.com/pinetree408/django_node_chat.git

cd django_node_chat

//pip install virtualenv

virtualenv venv

. venv/bin/activate 

cd django

pip install -r requirements.txt

cd app

python manage.py migrate

python manage.py createsuperuser

cd ../../node

npm install

```

### Running on local
```
cd django

python manage.py runserver

#another console
cd node

node server.js

```

## Code covention
depends on pep8

#License
all directories and their contents are Copyright Lee Sang-Yoon.

You may not reuse anything therein without my permission.
