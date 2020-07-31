import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for k, v in kwargs.items():
            for i in range(v):
                self.contents.append(k)

    def draw(self, number):
        cont = self.contents
        draw = []
        if number >= len(cont):
            number = len(cont)
        for i in range(number):
            index = random.randint(0, len(cont)-1)
            draw.append(cont.pop(index))
        return draw

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    success_count = 0
    for i in range(num_experiments):
        is_success = True
        hat_copy = copy.deepcopy(hat)
        drawn_balls = hat_copy.draw(num_balls_drawn)
        for color, number in expected_balls.items():
            if drawn_balls.count(color) < number:
                is_success = False
        if is_success:
            success_count += 1
    return success_count/num_experiments