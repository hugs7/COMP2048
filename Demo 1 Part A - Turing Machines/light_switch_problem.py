"""
Light switch problem
Hugo Burton
Numberphile video
02/03/2023
"""

class Lights:
    def __init__(self, num_lights, multiple):
        self.num_lights = num_lights
        self.multiple = multiple
        self.lights = [0 for _ in range(self.num_lights)]

    def get_light(self, light):
        return self.lights[light]

    def light_on(self, light):
        self.lights[light] = 1

    def light_off(self, light):
        self.lights[light] = 0

    def toggle_light(self, light):
        self.lights[light] = 1 - self.lights[light]

    def __str__(self):
        str_return = ""
        for row in range(self.multiple):
            for col in range(self.num_lights // self.multiple):
                str_return += str(self.lights[row * self.multiple + col]) + " "
            str_return += "\n"

        return str_return

lights = Lights(100, 10)

print(lights)

for i in range(0, 100):
    print("Person:", i + 1)
    for l in range(i, 100, i + 1):
        # print(l)
        lights.toggle_light(l)

    print(lights)