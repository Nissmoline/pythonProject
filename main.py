import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np
from figures import *
from buttons import *
from render_text import *
from render_figure import *

# Глобальные переменные для углов поворота и положения мыши
rotation_x = 0
rotation_y = 0
rotation_angle_tetrahedron = 0
rotation_angle_hexahedron = 0
rotation_angle_octahedron = 0
mouse_last_pos = None

def init_pygame():
    pygame.init()
    display = (1000, 1000)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -15)
    glEnable(GL_DEPTH_TEST)
    return display

# Функция для двухточечной перспективной проекции
def create_two_point_perspective_matrix():
    p = 0  # Смещение точки схода по оси X
    q = 0  # Смещение точки схода по оси Y
    near = 0.9
    far = 100.0

    # Определяем матрицу 4x4
    matrix = np.array([
        [1, 0, 0, p],
        [0, 1, 0, q],
        [0, 0, -(far + near) / (far - near), -(1 * far * near) / (far - near)],
        [0, 0, -1, 0]
    ], dtype=np.float32)

    return matrix


# Функция для двухточечной перспективной проекции
def set_two_point_perspective():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    # Получаем матрицу двухточечной перспективы
    matrix = create_two_point_perspective_matrix()

    # Загружаем матрицу в OpenGL
    glLoadMatrixf(matrix)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glTranslatef(0.0, 0.0, -5)

def main_menu(display):
    global rotation_angle_tetrahedron, rotation_angle_hexahedron, rotation_angle_octahedron
    pygame.font.init()
    selected_figure = None

    # Позиции кнопок (x, y, ширина, высота)
    button_y = 750  # Позиция кнопок по оси Y
    button_tetra = pygame.Rect(70, button_y, 200, 50)
    button_hexa = pygame.Rect(420, button_y, 200, 50)
    button_octa = pygame.Rect(730, button_y, 200, 50)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if button_tetra.collidepoint(mouse_pos):
                    selected_figure = 'Tetrahedron'
                elif button_hexa.collidepoint(mouse_pos):
                    selected_figure = 'Hexahedron'
                elif button_octa.collidepoint(mouse_pos):
                    selected_figure = 'Octahedron'

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # Устанавливаем перспективу для 3D
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(70, (display[0] / display[1]), 0.1, 50.0)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glTranslatef(0.0, 0.0, -8)  #Отделение камеры от обьект

        # Устанавливаем режим каркасной отрисовки для всех фигур
        glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)

        # Вращаем тетраэдр
        glPushMatrix()
        glTranslatef(-3.5, 0, 0)
        glRotatef(rotation_angle_tetrahedron, 1, 1, 1)  # Вращаем вокруг трёх осей
        draw_tetrahedron()
        glPopMatrix()

        # Вращаем гексаэдр
        glPushMatrix()
        glTranslatef(0, 0, 0)
        glRotatef(rotation_angle_hexahedron, 1, 1, 1)
        draw_hexahedron()
        glPopMatrix()

        # Вращаем октаэдр
        glPushMatrix()
        glTranslatef(3.5, 0, 0)
        glRotatef(rotation_angle_octahedron, 1, 1, 1)
        draw_octahedron()
        glPopMatrix()

        # Восстанавливаем полигональный режим после отрисовки фигур
        glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)

        render_text("Выберите фигуру:", 400, 900, 48)

        render_button(button_tetra.x, button_tetra.y, button_tetra.width, button_tetra.height, display[0], display[1])
        render_button(button_hexa.x, button_hexa.y, button_hexa.width, button_hexa.height, display[0], display[1])
        render_button(button_octa.x, button_octa.y, button_octa.width, button_octa.height, display[0], display[1])

        render_text("Тетраэдр", button_tetra.x + 35, button_tetra.y - 545, 36)
        render_text("Гексаэдр", button_hexa.x + 35, button_hexa.y - 545, 36)
        render_text("Октаэдр", button_octa.x + 35, button_octa.y - 545, 36)

        # Углы вращения для анимации
        rotation_angle_tetrahedron += 1
        rotation_angle_hexahedron += 1
        rotation_angle_octahedron += 1

        pygame.display.flip()
        pygame.time.wait(10)

        if selected_figure:
            view_figure(selected_figure)
            selected_figure = None

def main():
    display = init_pygame()
    main_menu(display)

if __name__ == "__main__":
    main()