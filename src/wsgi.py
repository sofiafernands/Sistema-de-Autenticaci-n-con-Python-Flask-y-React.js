# This file was created to run the application on heroku using gunicorn.
# Read more about it here: https://devcenter.heroku.com/articles/python-gunicorn
# Este archivo fue creado para ejecutar la aplicación en heroku usando gunicorn.
# Lea más sobre esto aquí: https://devcenter.heroku.com/articles/python-gunicorn

from app import app as application

if __name__ == "__main__":
    application.run()
