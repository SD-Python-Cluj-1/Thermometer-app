class Thermometer():
    def __init__(self, inside, temp, celsius, fahrenheit):
        self.temp = temp
        self.celsius = celsius
        self.fahrenheit = fahrenheit
        self.inside = set.temp

    def get_temp(self, temp):
        self.inside = temp

    def set_temp(self, temp):
        self.temp = input("set_temp: > ")
        return temp

    def to_celsius(self, temp):
        if "C" in temp:
        self.temp = (temp * 9/5) + 32
        pass

    def to_fahrenheit(self, temp):
        if "F" in temp:
            self.temp = (temp - 32)*5/9
        pass
