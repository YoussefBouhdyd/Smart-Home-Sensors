import random

class virtual_sensor:

    def __init__(self, start=None, variation=None, min=None, max=None):
        if start:
            self.value = start
        else:
            self.value = 0

        self.variation = variation
        self.min = min
        self.max = max

    def read_value(self):
        self.value += random.uniform(self.variation*-1, self.variation )

        if self.min and self.value < self.min: self.value = self.min
        if self.max and self.value > self.max: self.value = self.max
        
        return self.value