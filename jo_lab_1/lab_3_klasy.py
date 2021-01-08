class Car:

    def __init__(self, car_type, brand, model, engine):
        self.car_type = car_type
        self.brand = brand
        self.model = model
        self.engine = engine
        self.doors = None
        self.airbag = None
        self.navigation = None
        self.backup_camera = None
        self.bluetooth = None
        self.sport_driver = None

    def set_doors(self, doors):
        self.doors = doors

    def set_airbag(self, airbag):
        self.airbag = airbag

    def set_navigation(self, navigation):
        self.navigation = navigation


class SportCar(Car):
    def __init__(self):
        super(Car, self).__init__()


SportCar.set_airbag(3)
