import tkinter as tk

class RobotGame(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Robot Game")
        self.geometry("400x400")

        self.grid_size = 5
        self.grid = [[' ' for _ in range(self.grid_size)] for _ in range(self.grid_size)]

        self.robot_x = 0
        self.robot_y = 0
        self.direction = 'up'  # The robot starts facing upwards

        #self.create_widgets()
        self.draw_grid()

    # ... (Same as before) ...

    def move_forward(self):
        # Implement logic to move the robot forward

        # Update the robot's position based on its current direction
        if self.direction == 'up' and self.robot_y > 0:  # Move up
            self.robot_y -= 1
        elif self.direction == 'down' and self.robot_y < self.grid_size - 1:  # Move down
            self.robot_y += 1
        elif self.direction == 'left' and self.robot_x > 0:  # Move left
            self.robot_x -= 1
        elif self.direction == 'right' and self.robot_x < self.grid_size - 1:  # Move right
            self.robot_x += 1

        self.update_robot_position()
        print(f"Robot moved forward. Current position: ({self.robot_x}, {self.robot_y})")
        self.update()  # Update the GUI to show the new position

    def turn_left(self):
        # Implement logic to turn the robot left

        if self.direction == 'up':
            self.direction = 'left'
        elif self.direction == 'left':
            self.direction = 'down'
        elif self.direction == 'down':
            self.direction = 'right'
        else:  # right
            self.direction = 'up'

        print(f"Robot turned left. Current direction: {self.direction}")

    def turn_right(self):
        # Implement logic to turn the robot right

        if self.direction == 'up':
            self.direction = 'right'
        elif self.direction == 'right':
            self.direction = 'down'
        elif self.direction == 'down':
            self.direction = 'left'
        else:  # left
            self.direction = 'up'

        print(f"Robot turned right. Current direction: {self.direction}")

    # ... (Same as before) ...

if __name__ == "__main__":
    app = RobotGame()
    app.mainloop()
