Django-Node-Chat
==================
An application for chatting on Django & Node.

## How to Work on this Project (on a mac)

### Setting up your system
```sh
https://github.com/pinetree408/django_node_chat.git

cd django_node_chat

//pip install virtualenv

virtualenv venv

. venv/bin/activate 

pip install -r requirements.txt

cd django_node_chat

python manage.py migrate

python manage.py createsuperuser

cd node

npm install

brew install redis

redis-server

```

### Running on local
```
python manage.py runserver

#another console
cd node

node chat.js

```
