import traceback

from tool_lending_system.db import get_db


class Location:
    def __init__(self, id=None, name=None):
        if id is None:  # Id None, the rest depends os scenario
            self._id = id
            self._name = name

        else:  # Update all fields if the id is valid
            db = get_db()
            query = db.execute('SELECT * FROM location WHERE id = ?', (id, )).fetchone()

            self._id = id
            self._name = query['name']

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

    def create(self):
        db = get_db()
        error = None

        try:
            location = db.execute('SELECT id FROM location WHERE name = ?', (self._name, )).fetchone()
            if location:
                error = 'ERRO: Local já cadastrado no sistema!'
            else:
                db.execute('INSERT INTO location (name) VALUES (?)', (self._name, ))
                db.commit()

        except Exception as e:
            error = e.args[0]
            print("Erro ocorrido: ", e)
            print(e.args[0])
            traceback.print_exc()

        finally:
            return error

    def get_locations(self):
        db = get_db()

        if self._name == '':
            return db.execute('''SELECT id, name FROM location''').fetchall()
        else:
            return db.execute('''SELECT * FROM location WHERE name LIKE ('%' || ? || '%')''',
                              (self._name,)).fetchall()

    def get_location_by_id(self):
        db = get_db()
        location = db.execute("SELECT * FROM location WHERE id = ?", (self._id, )).fetchone()
        return location

    def update(self):
        db = get_db()
        error = None
        try:
            id = db.execute('SELECT id FROM location WHERE name = ?', (self._name, )).fetchone()
            if id and id['id'] != self._id:
                error = 'O nome já existe no sistema! Tente novamente com outro.'
            else:
                db.execute('UPDATE location SET name = ? WHERE id = ?',
                           (self._name, self._id))
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
