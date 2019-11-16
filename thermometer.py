class Thermometer():
    def __init__(self, temp, celsius, fahrenheit):
        self.temp = temp
        self.celsius = celsius
        self.fahrenheit = fahrenheit


    def get_temp(self, temp):
        self.inside = temp

    def set_temp(self, temp):
        self.temp = input("set_temp: > ")
        return temp

    def to_celsius(self, temp):
        if "C" in temp:
         self.temp = (temp * 9/5) + 32
        pass

    def to_fahrenheit(self):
        if "F" in temp:
            self.temp = (temp - 32)*5/9
        pass
