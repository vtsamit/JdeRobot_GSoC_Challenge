import numpy as np

class BrownianMotion:
    def __init__(self, robot_radius=15, robot_color = (255, 0, 0), windowsize=[700,700], linear_speed=5, rotational_speed=3):
        
        self.robot_radius = robot_radius
        self.robot_color = robot_color
        self.windowsize = windowsize
        self.linear_speed = linear_speed
        self.rotational_speed = rotational_speed

        self.position = np.array([windowsize[0] / 2, windowsize[1] / 2])
        self.direction = np.array([1, 0])
        

    def start_robot(self):

        # simulate linear motion
        self.position +=  self.linear_speed * self.direction

        hit = False
        # Collision Conditions
        if self.position[0] <= self.robot_radius or self.position[0] >= self.windowsize[0] - self.robot_radius or self.position[1] <= self.robot_radius or self.position[1] >= self.windowsize[1] - self.robot_radius:
            
            # change direction on collision
            self.direction[0] = -self.direction[0]
            self.direction[1] = -self.direction[1]
            hit = True
           

        if hit:
            random_time = np.random.randint(1, 10)
   
            #rotation for a random duration using rotation matrix
            for i in range(random_time):
                self.direction = np.dot(self.direction, np.array([[np.cos(self.rotational_speed), -np.sin(self.rotational_speed)], [np.sin(self.rotational_speed), np.cos(self.rotational_speed)]]))

        return hit