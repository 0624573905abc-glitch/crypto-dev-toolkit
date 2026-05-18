import time

class GameEngine:
    def __init__(self, fps=60):
        self.fps = fps
        self.delta_time = 0
        self.last_frame_time = time.time()

    def update(self):
        current_time = time.time()
        self.delta_time = current_time - self.last_frame_time
        self.last_frame_time = current_time
        self.logic()  # Call game logic

    def logic(self):
        # Optimized game logic processing
        speed = 5  # Game speed
        movement = speed * self.delta_time
        self.process_movement(movement)

    def process_movement(self, movement):
        # Efficiently handles movement calculations
        print(f'Moving character by {movement:.2f} units')

    def run(self):
        while True:
            self.update()
            time.sleep(1 / self.fps)

if __name__ == '__main__':
    game = GameEngine()
    game.run()