# making a py_game 
# game library for python 

# class creates objects 
# blob world
# import dependencies 

import random 
import pygame
from blob import Blob
import numpy as np

# number of blobs of each color 
STARTING_BLUE_BLOBS = 50
STARTING_RED_BLOBS = 50
STARTING_GREEN_BLOBS = 50

# defined veriables 
WIDTH = 800
HEIGHT = 600
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

game_display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Blob World by Erdem Balikci")
clock = pygame.time.Clock()


# child class or sub class to handle boundries, and colors
# main class for blob -- blue colors
class BlueBlob(Blob):
    
    def __init__(self, x_boundary, y_boundary):
        Blob.__init__(self, (0, 0, 255), x_boundary, y_boundary)

    def __add__(self, other_blob):
        if other_blob.color == (255, 0, 0):
            self.size -= other_blob.size
            other_blob.size -= self.size 
        elif other_blob.color == (0, 255, 0):
            self.size += other_blob.size
            other_blob.size = 0
        elif other_blob.color == (0 ,0 , 255):
            pass
        else:
            raise Exception('tried to combine one or multiple blobs of unsuported colors')

# each blob classes besides blue
class RedBlob(Blob):
    
    def __init__(self, x_boundary, y_boundary):
        Blob.__init__(self, (255, 0, 0), x_boundary, y_boundary)

class GreenBlob(Blob):
    
    def __init__(self, x_boundary, y_boundary):
        Blob.__init__(self, (0, 255, 0), x_boundary, y_boundary)

# if they are touching -- how to handle?
def is_touching(b1, b2):
    return np.linalg.norm(np.array([b1.x, b1.y]) - np.array([b2.x, b2.y])) < (b1.size + b2.size)

def handle_collision(blob_list):
    blues, reds, greens = blob_list
    
    for blue_id, blue_blob in blues.copy().items():
        for other_blobs in blues, reds, greens:
            for other_blob_id, other_blob in other_blobs.copy().items():
                if blue_blob == other_blob:
                    pass
                else:
                    if is_touching(blue_blob, other_blob):
                        blue_blob + other_blob
                        if other_blob.size <= 0:
                            del other_blobs[other_blob_id]
                        if blue_blob.size <= 0:
                            del blues[blue_id]

    return blues, reds, greens



    # def move_fast(self):
    #     self.x += random.randrange(-7,7)
    #     self.y += random.randrange(-7,7)

# take the class and imported into a program 
# take it put it somewhere
'''
# class Blob:
    
#     # first method 

#     def __init__(self, color):
#         self.x = random.randrange(0, WIDTH)
#         self.y = random.randrange(0, HEIGHT)
#         self.size = random.randrange(4, 8)
#         self.color = color

#     def move(self):
#         self.move_x = random.randrange(-1, 2)
#         self.move_y = random.randrange(-1, 2)

#         self.x += self.move_x
#         self.y += self.move_y

#         if self.x < 0: self.x = 0
#         elif self.x > WIDTH: self.x = WIDTH
        
#         if self.y < 0: self.y = 0
#         elif self.y > HEIGHT: self.y = HEIGHT
'''

# the environment -- white background 
def draw_environment(blob_list):
    
    blues, reds, greens = handle_collision(blob_list)
    game_display.fill(WHITE)
    

    for blob_dict in blob_list:
        for blob_id in blob_dict:
            blob = blob_dict[blob_id]
            pygame.draw.circle(game_display, blob.color, [blob.x, blob.y], blob.size)
            blob.move()
            blob.check_bounds()

            # if blob.x < 0: blob.x = 0
            # elif blob.x > blob.x_boundary: blob.x = blob.x_boundary
            
            # if blob.y < 0: blob.y = 0
            # elif blob.y > blob.y_boundary: blob.y = blob.y_boundary

    pygame.display.update()
    return blues, reds, greens
    
# the main function to handle the movements 
def main():
    
    blue_blobs = dict(enumerate([BlueBlob(WIDTH, HEIGHT) for i in range(STARTING_BLUE_BLOBS)]))
    red_blubs = dict(enumerate([RedBlob(WIDTH, HEIGHT) for i in range(STARTING_RED_BLOBS)]))
    green_blobs = dict(enumerate([GreenBlob(WIDTH, HEIGHT) for i in range(STARTING_GREEN_BLOBS)]))

    # print('Blue blob size: {} red size: {}'. format(blue_blobs[0].size + red_blubs[0].size))

    # blue_blobs[0] + red_blubs[0]

    # print('Blue blob size: {} red size: {}'. format(blue_blobs[0].size + red_blubs[0].size))


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        blue_blobs, red_blubs, green_blobs = draw_environment([blue_blobs, red_blubs, green_blobs])
        clock.tick(60)
        # print(red_blob.x, red_blob.y)

if __name__=='__main__':
    main()
