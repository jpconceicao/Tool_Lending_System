

class Tool:
    def __int__(self, id=None, description=None, location=None, available=None, image_path=None, serial_number=None,
                pat_number=None):
        self._id = id
        self._description = description
        self._location = location
        self._available = available
        self._image_path = image_path
        self._serial_number = serial_number
        self._pat_number = pat_number

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

    @property
    def image_path(self):
        return self._image_path

    @image_path.setter
    def image_path(self, image_path):
        self._image_path = image_path

    @property
    def serial_number(self):
        return self._serial_number

    @serial_number.setter
    def serial_number(self, serial_number):
        self._serial_number = serial_number

    @property
    def pat_number(self):
        return self._pat_number

    @pat_number.setter
    def pat_number(self, pat_number):
        self._pat_number = pat_number

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
