from pygame import draw

from circleshape import CircleShape
from constants import LINE_WIDTH


class asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen, colour, pos, radius):
        draw.circle(screen, colour, pos, radius, LINE_WIDTH)

    def update(self, dt):

