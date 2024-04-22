import traceback

from tool_lending_system.db import get_db


class Tool:
    def __init__(self, id=None, description=None, code=None, available=None, location=None):
        if id is None:
            self._id = id
            self._description = description
            self._code = code
            self._available = available
            self._location = location

        else:
            db = get_db()
            query = db.execute('SELECT * FROM tool WHERE id = ?', (id, )).fetchone()

            self._id = id
            self._description = query['description']
            self._code = query['code']
            self._available = query['available']
            self._location = query['location']

    # Getters e setters
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        self._description = description

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, code):
        self._code = code

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, location):
        self._location = location

    @property
    def available(self):
        return self._available

    @available.setter
    def available(self, available):
        self._available = available

    def create(self):
        db = get_db()
        error = None
        try:
            code = db.execute('SELECT code FROM tool WHERE code = ?', (self._code, )).fetchone()
            if code:
                error = 'Código já existe no sistema! Tente outro.'
            else:
                db.execute('INSERT INTO tool (description, code, available, location) VALUES (?, ?, ?, ?)',
                           (self._description, self._code, self._available, self._location))
                db.commit()

        except Exception as e:
            error = e.args[0]
            print("Erro ocorrido: ", e)
            print(e.args[0])
            traceback.print_exc()

        finally:
            return error

    def get_tool_by_id(self):
        db = get_db()
        return db.execute('SELECT * FROM tool WHERE id = ?', (self._id, )).fetchone()

    def get_tools(self):
        db = get_db()
        if self._description == '' and self._location == 'todos':
            tools = db.execute('SELECT * FROM tool WHERE available = ? order by id', (self._available, )).fetchall()
            return tools

        elif self._description != '' and self._location == 'todos':
            if ' ' in self._description:
                # Aplica a busca concatenada
                parts = self._description.split(" ")  # Separa as strings
                conditions = [f"description LIKE '%{part}%'" for part in parts]  # Cria lista das buscas p/ o SQL
                conc_conditions = " AND ".join(conditions)
                tools = db.execute(f'''SELECT * FROM tool WHERE available = ? AND {conc_conditions} 
                                                    order by id desc;''',
                                   (self._available, )).fetchall()

            else:
                tools = db.execute('''SELECT * FROM tool WHERE available = ? AND description LIKE ('%' || ? || '%') 
                                    order by id desc;''',
                                   (self._available, self._description)).fetchall()
            return tools

        elif self._description == '' and self._location != 'todos':
            tools = db.execute('''SELECT * FROM tool WHERE available = ? AND location = ? 
                                                order by id desc;''',
                               (self._available, self._location)).fetchall()
            return tools

        elif self._description != '' and self._location != 'todos':
            if ' ' in self._description:
                # Aplica a busca concatenada
                parts = self._description.split(" ")  # Separa as strings
                conditions = [f"description LIKE '%{part}%'" for part in parts]  # Cria lista das buscas p/ o SQL
                conc_conditions = " AND ".join(conditions)
                tools = db.execute(f'''SELECT * FROM tool WHERE available = ? AND {conc_conditions} AND location = ?  
                                                    order by id desc;''',
                                   (self._available, self._location)).fetchall()

            else:
                tools = db.execute('''SELECT * FROM tool WHERE available = ? AND description LIKE ('%' || ? || '%') 
                                    AND location = ? order by id desc;''',
                                   (self._available, self._description, self._location)).fetchall()
            return tools

    def update(self):
        db = get_db()
        error = None
        try:
            id = db.execute('SELECT id FROM tool WHERE code = ?', (self._code,)).fetchone()
            if id and id['id'] != self._id:
                error = 'Código já existe no sistema! Tente outro.'
            else:
                db.execute('UPDATE tool SET description = ?, code = ?, location = ? WHERE id = ?',
                           (self._description, self._code, self._location, self._id))
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
