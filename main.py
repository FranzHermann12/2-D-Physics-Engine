
import pygame
import random

from physics.vector import Vector2
from physics.body import Body
from physics.rectangle import RectangleBody
from physics.world import World


pygame.init()

WIDTH = 900
HEIGHT = 650
FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PyPhysics2D - Physics Sandbox")

clock = pygame.time.Clock()
font = pygame.font.SysFont("consolas", 18)

world = World(
    gravity=Vector2(0, 900),
    restitution=0.75,
    friction=0.3,
    width=WIDTH,
    height=HEIGHT
)

BACKGROUND = (18, 18, 24)
BLUE = (70, 150, 255)
WHITE = (240, 240, 240)
GRAY = (100, 100, 110)
GREEN = (80, 200, 130)


def create_world():
    world.bodies.clear()

    # Static platforms
    floor = RectangleBody(
        Vector2(WIDTH / 2, HEIGHT - 20),
        WIDTH,
        40,
        is_static=True
    )

    platform = RectangleBody(
        Vector2(450, 440),
        250,
        25,
        is_static=True
    )

    platform_two = RectangleBody(
        Vector2(200, 300),
        180,
        25,
        is_static=True
    )

    world.add_body(floor)
    world.add_body(platform)
    world.add_body(platform_two)

    # Dynamic balls
    for _ in range(8):
        radius = random.randint(12, 25)

        ball = Body(
            position=Vector2(
                random.randint(80, WIDTH - 80),
                random.randint(50, 180)
            ),
            mass=1,
            radius=radius,
            velocity=Vector2(
                random.randint(-100, 100),
                random.randint(-50, 50)
            )
        )

        world.add_body(ball)


def draw_world():
    screen.fill(BACKGROUND)

    for body in world.bodies:
        if isinstance(body, RectangleBody):
            left, top, right, bottom = body.get_bounds()

            pygame.draw.rect(
                screen,
                GREEN if body.is_static else GRAY,
                pygame.Rect(left, top, right - left, bottom - top)
            )
        else:
            pygame.draw.circle(
                screen,
                BLUE,
                (int(body.position.x), int(body.position.y)),
                int(body.radius)
            )

    instructions = [
        "PyPhysics2D Physics Sandbox",
        "SPACE: Pause / Resume",
        "R: Reset simulation",
        "ESC: Quit"
    ]

    for index, line in enumerate(instructions):
        text = font.render(line, True, WHITE)
        screen.blit(text, (15, 15 + index * 23))

    fps_text = font.render(
        f"FPS: {int(clock.get_fps())}",
        True,
        WHITE
    )
    screen.blit(fps_text, (WIDTH - 110, 15))

    pygame.display.flip()


create_world()

running = True
paused = False

while running:
    delta_time = min(clock.tick(FPS) / 1000, 0.033)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

            elif event.key == pygame.K_SPACE:
                paused = not paused

            elif event.key == pygame.K_r:
                create_world()

    if not paused:
        world.step(delta_time)

    draw_world()

pygame.quit()
