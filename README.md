# Build & Deploy a Python Web App To Schedule Tweets.
I'm using Flask, Heroku, the Twitter API & Google Sheets API for this. The app can be hosted for free.

You can use this repo as a starting point. Watch how I build and deploy this app step by step here: 

[![Alt text](https://img.youtube.com/vi/yCYPzoG25ak/hqdefault.jpg)](https://www.youtube.com/watch?v=yCYPzoG25ak)

## Flask Quickstart:
### Create virtual env
```console
python3 -m venv venv
Activate (on Mac):
. venv/bin/activate
```

```console
pip install Flask
export FLASK_APP=app/main.py
flask run
```

## Heroku start
```console
heroku login -i
heroku create your_app_name
```

add config vars:
```console
heroku config:set CONSUMER_KEY=xxx
heroku config:set CONSUMER_SECRET=xxx
heroku config:set ACCESS_TOKEN=xxx
heroku config:set ACCESS_SECRET=xxx
heroku config:set INTERVAL=1200
heroku config:set DEBUG=0
```

Scale worker:
```console
heroku ps:scale worker=1
```

Test locally:
```console
heroku local
```

Push to Heroku:
```console
git init
heroku git:remote -a your_app_name
git add .
git commit -m "initial commit"
git push heroku master
```

and later your secret.json:
```console
git checkout -b secret-branch
  --> remove secret.json from *.gitignore* on new branch
git add .
git commit -m "add credentials"
git push heroku secret-branch:master
```