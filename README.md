# Nuxt/Flask JWT

JWT authentication boilerplate with nuxt.js static site, flask, and mongodb

## Installation (macOS)

1. Install mongodb
2. Install python3
3. Install nodejs
4. Clone repo `git clone git@github.com:robyedlin/nuxt-flask-jwt.git`
5. Run `cd nuxt-flask-jwt`
2. Run `python3 -m venv .venv`

## Development

1. Start mongodb

### Flask

Start in project root

1. Run `cd flask`
2. Run `pip install -r requirements.txt`
3. Run `FLASK_ENV=development FLASK_APP=main.py flask run`

### Nuxt

Start in project root

1. Run `cd nuxt`
2. Run `npm install`
3. Run `npm run dev`