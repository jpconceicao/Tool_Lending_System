from tool_lending_system.db import get_db


class Loan:
    def __init__(self, id=None, tool_id=None, user_id=None, loan_date=None, devolution_date=None, returned=None,
                requester_name=None, requester_area=None):
        if id is None:
            self._id = id
            self._tool_id = tool_id
            self._user_id = user_id
            self._loan_date = loan_date
            self._devolution_date = devolution_date
            self._returned = returned
            self._requester_name = requester_name
            self._requester_area = requester_area

        else:
            db = get_db()
            query = db.execute('SELECT * FROM loan WHERE id = ?', (id, )).fetchone()

            self._id = id
            self._tool_id = query['tool_id']
            self._user_id = query['user_id']
            self._loan_date = query['loan_date']
            self._devolution_date = query['devolution_date']
            self._returned = query['returned']
            self._requester_name = query['requester_name']
            self._requester_area = query['requester_area']

    # Getters e setters
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def tool_id(self):
        return self._tool_id

    @tool_id.setter
    def tool_id(self, tool_id):
        self._tool_id = tool_id

    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        self._user_id = user_id

    @property
    def loan_date(self):
        return self._loan_date

    @loan_date.setter
    def loan_date(self, loan_date):
        self._loan_date = loan_date

    @property
    def devolution_date(self):
        return self._devolution_date

    @devolution_date.setter
    def devolution_date(self, devolution_date):
        self._devolution_date = devolution_date

    @property
    def returned(self):
        return self._returned

    @returned.setter
    def returned(self, returned):
        self._returned = returned

    @property
    def requester_name(self):
        return self._requester_name

    @requester_name.setter
    def requester_name(self, requester_name):
        self._requester_name = requester_name

    @property
    def requester_area(self):
        return self._requester_area

    @requester_area.setter
    def requester_area(self, requester_area):
        self._requester_area = requester_area

    def create(self):
        pass

    def get_loan(self):
        pass

    def get_loans(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass
