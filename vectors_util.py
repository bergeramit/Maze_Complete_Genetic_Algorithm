import math

def calculate_position(current_position, current_speed, acceleration, time_elapsed):
    return current_position + current_speed * time_elapsed + 0.5 * math.pow(time_elapsed, 2) * acceleration

def update_speed(current_speed, acceleration, time_elapsed):
    return current_speed + time_elapsed * acceleration

def update_velocity(current_velocity, acceleration, time_elapsed):
    current_velocity.x = update_speed(current_velocity.x, acceleration.x, time_elapsed)
    current_velocity.y = update_speed(current_velocity.y, acceleration.y, time_elapsed)

def update_position(current_position, current_velocity, acceleration, time_elapsed):
    current_position.x = calculate_position(current_position.x, current_velocity.x, acceleration.x, time_elapsed)
    current_position.y = calculate_position(current_position.y, current_velocity.y, acceleration.y, time_elapsed)

class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
