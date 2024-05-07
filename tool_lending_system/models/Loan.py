import traceback

from tool_lending_system.db import get_db


class Loan:
    def __init__(self, id=None, tool_id=None, user_id=None, loan_date=None, devolution_date=None,
                 user_id_checked_out=None, returned=None, requester_name=None, requester_area=None, obs=None,
                 description=None):
        if id is None:
            self._id = id
            self._tool_id = tool_id
            self._user_id = user_id
            self._loan_date = loan_date
            self._devolution_date = devolution_date
            self._user_id_checked_out = user_id_checked_out
            self._returned = returned
            self._requester_name = requester_name
            self._requester_area = requester_area
            self._obs = obs

        else:
            db = get_db()
            query = db.execute('SELECT * FROM loan WHERE id = ?', (id,)).fetchone()

            self._id = id
            self._tool_id = query['tool_id']
            self._user_id = query['user_id']
            self._loan_date = query['loan_date']
            self._devolution_date = query['devolution_date']
            self._user_id_checked_out = query['user_id_checked_out']
            self._returned = query['returned']
            self._requester_name = query['requester_name']
            self._requester_area = query['requester_area']
            self._obs = query['obs']

        # Atributos auxiliares
        self._description = description

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
    def user_id_checked_out(self):
        return self._user_id_checked_out

    @user_id_checked_out.setter
    def user_id_checked_out(self, user_id_checked_out):
        self._user_id_checked_out = user_id_checked_out

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

    @property
    def obs(self):
        return self._obs

    @obs.setter
    def obs(self, obs):
        self._obs = obs

    def create(self):
        db = get_db()
        error = None
        try:
            db.execute('''INSERT INTO loan (tool_id, user_id, requester_name, requester_area, obs, returned, loan_date) 
            VALUES (?, ?, ?, ?, ?, ?, ?)''', (self._tool_id, self._user_id, self._requester_name,
                                           self._requester_area, self._obs, self._returned, self._loan_date))
            db.commit()

            db.execute('UPDATE tool SET available = 0 WHERE id = ?', (self._tool_id,))
            db.commit()

        except Exception as e:
            error = e.args[0]
            print("Erro ocorrido: ", e)
            print(e.args[0])
            traceback.print_exc()

        finally:
            return error

    def get_loan_by_id(self):
        db = get_db()
        return db.execute('SELECT * FROM loan WHERE id = ?', (self._id, )).fetchone()

    def get_loans(self):
        db = get_db()

        if self._description == "":
            loans = db.execute('''SELECT id,
                                (SELECT description FROM tool WHERE id = loan.tool_id)as description,
                                (SELECT email FROM user WHERE id = loan.user_id) as email,
                                (SELECT code FROM tool WHERE id = loan.tool_id) as code,
                                loan_date, requester_name, requester_area, obs, returned, devolution_date, 
                                (SELECT email FROM user WHERE id = loan.user_id_checked_out) as email_checked_out
                                FROM loan WHERE returned = ? order by id desc''',
                               (self._returned, )).fetchall()
            return loans

        else:
            if ' ' in self._description:
                # Aplica a busca concatenada
                parts = self._description.split(" ")  # Separa as strings
                conditions = [f"description LIKE '%{part}%'" for part in parts]  # Cria lista das buscas p/ o SQL
                conc_conditions = " AND ".join(conditions)
                loans = db.execute(f'''SELECT id,
                                    (SELECT description FROM tool WHERE id = loan.tool_id)as description,
                                    (SELECT email FROM user WHERE id = loan.user_id) as email,
                                    (SELECT code FROM tool WHERE id = loan.tool_id) as code,
                                    loan_date, requester_name, requester_area, obs, returned,  devolution_date, 
                                    (SELECT email FROM user WHERE id = loan.user_id_checked_out) as email_checked_out
                                    FROM loan WHERE returned = ? AND {conc_conditions} order by id desc''',
                                   (self._returned, )).fetchall()

            else:
                print("executou")  # DEBUG
                loans = db.execute('''SELECT id,
                                (SELECT description FROM tool WHERE id = loan.tool_id)as description,
                                (SELECT email FROM user WHERE id = loan.user_id) as email,
                                (SELECT code FROM tool WHERE id = loan.tool_id) as code,
                                loan_date, requester_name, requester_area, obs, returned, devolution_date, 
                                (SELECT email FROM user WHERE id = loan.user_id_checked_out) as email_checked_out
                                FROM loan WHERE returned = ? AND description LIKE ('%' || ? || '%') order by id desc''',
                                   (self._returned, self._description)).fetchall()
            return loans

    def update(self):
        db = get_db()
        error = None
        try:
            db.execute('UPDATE loan SET requester_name = ?, requester_area = ?, obs = ? WHERE id = ?',
                       (self._requester_name, self._requester_area, self._obs, self._id))
            db.commit()

        except Exception as e:
            error = e.args[0]
            print("Erro ocorrido: ", e)
            print(e.args[0])
            traceback.print_exc()

        finally:
            return error

    def close_loan(self):
        db = get_db()

        db.execute('''UPDATE loan SET returned = ?, user_id_checked_out = ?, devolution_date = ? 
                WHERE id = ?''',
               (self._returned, self._user_id_checked_out, self._devolution_date, self._id))
        db.commit()

        db.execute('UPDATE tool SET available = 1 WHERE id = ?', (self._tool_id, ))
        db.commit()

    def delete(self):
        pass

    def print_obj(self):
        print("Printando objeto: ")
        print(self._id)
        print(self._tool_id)
        print(self._user_id)
        print(self._loan_date)
        print(self._devolution_date)
        print(self._user_id_checked_out)
        print(self._returned)
        print(self._requester_name)
        print(self._requester_area)
        print(self._obs)
