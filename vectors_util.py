import math
import random

def calculate_position(current_position, current_speed, time_elapsed):
    return current_position + current_speed * time_elapsed


def update_speed(current_speed, acceleration, time_elapsed):
    return current_speed + time_elapsed * acceleration


def update_velocity(current_velocity, acceleration, time_elapsed):
    current_velocity.x = update_speed(current_velocity.x, acceleration.x, time_elapsed)
    current_velocity.y = update_speed(current_velocity.y, acceleration.y, time_elapsed)


def update_position(current_position, current_velocity, time_elapsed):
    current_position.x = calculate_position(current_position.x, current_velocity.x, time_elapsed)
    current_position.y = calculate_position(current_position.y, current_velocity.y, time_elapsed)


def get_random_direction_vector():
    return Vector((random.random() - 0.5) * 2, (random.random() - 0.5) * 2)


class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def calculate_distance(self, target):
        return math.sqrt(math.pow(self.x - target.x, 2) + math.pow(self.y - target.y, 2))