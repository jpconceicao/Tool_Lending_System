# import db from db file

class User:
    def __int__(self, id=None, name=None, email=None, password=None, status=None):
        self._id = id
        self._name = name
        self._email = email
        self._password = password
        self._status = status

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

    def create(self):
        pass

    def get_user(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass

