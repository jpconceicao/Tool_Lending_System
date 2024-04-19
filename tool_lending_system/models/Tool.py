from tool_lending_system.db import get_db


class Tool:
    def __init__(self, id=None, description=None, location=None, available=None, image_path=None, serial_number=None,
                pat_number=None):
        if id is None:
            self._id = id
            self._description = description
            self._location = location
            self._available = available
            self._location = location

        else:
            db = get_db()
            query = db.execute('SELECT * FROM tool id = ?', (id, )).fetchone()

            self._id = id
            self._description = query['description']
            self._location = query['location']
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
        pass

    def get_tool(self):
        pass

    def get_tools(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass
