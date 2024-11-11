
from OpenGL.GL import *

# Создание фигур
def draw_tetrahedron():
    vertices = [
        (1, 1, 1),
        (-1, -1, 1),
        (-1, 1, -1),
        (1, -1, -1)
    ]
    edges = [
        (0, 1), (1, 2), (2, 0),
        (0, 3), (1, 3), (2, 3)
    ]

    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

def draw_hexahedron():
    vertices = [
        (1, -1, -1),
        (1, 1, -1),
        (-1, 1, -1),
        (-1, -1, -1),
        (1, -1, 1),
        (1, 1, 1),
        (-1, -1, 1),
        (-1, 1, 1)
    ]
    edges = [
        (0, 1), (0, 3), (0, 4), (2, 1),
        (2, 3), (2, 7), (6, 3), (6, 4),
        (6, 7), (5, 1), (5, 4), (5, 7)
    ]

    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

def draw_octahedron():
    vertices = [
        (1, 0, 0),
        (-1, 0, 0),
        (0, 1, 0),
        (0, -1, 0),
        (0, 0, 1),
        (0, 0, -1)
    ]
    edges = [
        (0, 2), (2, 1), (1, 3), (3, 0),
        (0, 4), (1, 4), (2, 4), (3, 4),
        (0, 5), (1, 5), (2, 5), (3, 5)
    ]

    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()