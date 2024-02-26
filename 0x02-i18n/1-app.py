#!/usr/bin/env python3
"""
A basic Flask application with internationalization support.
"""

from flask import Flask, request, render_template
from flask_babel import Babel


class Config(object):
    """
    Application configuration class.
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'

# Instantiate the Flask application object


app = Flask(__name__)


app.config.from_object(Config)

# Wrap the application with Babel for internationalization
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """
    Gets the locale from the request object.
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def index() -> str:
    """
    Renders a basic HTML template.
    """
    return render_template('2-index.html')


if __name__ == '__main__':
    # Run the application
    app.run()
