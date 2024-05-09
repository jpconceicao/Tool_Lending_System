import os
import sqlite3

from flask import Flask


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    db_path = os.path.join(app.instance_path, 'Tool_Lending_System.sqlite')

    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=db_path,
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('../config.py', silent=True)

    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    if not os.path.exists(db_path):
        create_db(db_path, app)
        print('Banco de dados inicializado')  # DEBUG

    from . import auth
    app.register_blueprint(auth.bp)

    from . import lending_system
    app.register_blueprint(lending_system.bp)

    from . import admin
    app.register_blueprint(admin.bp)

    app.add_url_rule('/', endpoint='lending_system.index')

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    return app


def create_db(db_path, app):
    db = sqlite3.connect(db_path, detect_types=sqlite3.PARSE_DECLTYPES)
    with app.open_resource('schema.sql') as file:
        db.executescript(file.read().decode('utf8'))


my_app = create_app()
