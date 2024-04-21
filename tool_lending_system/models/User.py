import traceback

from tool_lending_system.db import get_db
from werkzeug.security import check_password_hash, generate_password_hash


class User:
    def __init__(self, id=None, name=None, email=None, password=None, status=None, level=None):
        if id is None:  # Id None, the rest depends os scenario
            self._id = id
            self._name = name
            self._email = email
            self._password = password
            self._status = status
            self._level = level

        else:  # Update all fields if the id is valid
            db = get_db()
            query = db.execute('SELECT * FROM user WHERE id = ?', (id, )).fetchone()

            self._id = id
            self._name = query['name']
            self._email = query['email']
            self._password = query['password']
            self._status = query['status']
            self._level = query['level']

    # Getters e setters
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = password

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        self._status = status

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, level):
        self._level = level

    def create(self):
        pass

    def get_user_by_id(self):
        db = get_db()
        return db.execute('SELECT * FROM user WHERE id = ?', (self._id, )).fetchone()

    def update(self):
        pass

    def update_without_password(self):
        db = get_db()
        error = None
        try:
            db.execute('UPDATE user SET name = ?, email = ? WHERE id = ?',
                       (self._name, self._email, self._id))
            db.commit()

        except Exception as e:
            error = e.args[0]
            print("Erro ocorrido: ", e)
            print(e.args[0])
            traceback.print_exc()

        finally:
            return error

    def update_with_password(self):
        db = get_db()
        error = None
        try:
            db.execute('UPDATE user SET name = ?, email = ?, password = ? WHERE id = ?',
                       (self._name, self._email, generate_password_hash(self._password), self._id))
            db.commit()

        except Exception as e:
            error = e.args[0]
            print("Erro ocorrido: ", e)
            print(e.args[0])
            traceback.print_exc()

        finally:
            return error

    def delete(self):
        pass

    def auth(self):
        db = get_db()
        error_dict = {'error': None, 'user': None}

        query = db.execute('SELECT * FROM user WHERE email = ?', (self._email, )).fetchone()
        if query is None:
            error_dict['error'] = 'Email incorreto!'
        elif not check_password_hash(query['password'], self._password):
            error_dict['error'] = 'Senha incorreta!'

        if error_dict['error'] is None:
            if query['status'] == 'active':
                error_dict['user'] = query
            else:
                error_dict['error'] = 'Usuário inativo no sistema! Solicite ativação ao administrador.'

        return error_dict

