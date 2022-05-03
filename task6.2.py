class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def material_calculate(self, weight=24.4, thickness=5):
        asphalt_mass = (self._length * self._width * weight * thickness)/1000
        print(f'Масса асфальтобетона: {asphalt_mass} тонн')

a = Road(500, 27.5)
a.material_calculate()

