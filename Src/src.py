import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *


# Глобальные переменные для углов поворота и положения мыши как называются команды для ctrl z  (отмена последнего действия)\
rotation_x = 0
rotation_y = 0
mouse_last_pos = None

# Глобальные переменные для углов вращения каждой фигуры в главном меню
rotation_angle_tetrahedron = 0
rotation_angle_hexahedron = 0
rotation_angle_octahedron = 0

def init_pygame():
    pygame.init()
    display = (1000, 1000)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -15)
    glEnable(GL_DEPTH_TEST)
    return display

# Функция для отрисовки текста
def render_text(text, x, y, font_size=36, color=(255, 255, 255)):
    font = pygame.font.SysFont('Arial', font_size)
    text_surface = font.render(text, True, color)
    text_data = pygame.image.tostring(text_surface, "RGBA", True)
    width, height = text_surface.get_size()

    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    glDisable(GL_DEPTH_TEST)

    glMatrixMode(GL_PROJECTION)
    glPushMatrix()
    glLoadIdentity()
    glOrtho(0, 1000, 0, 1000, -1, 1)
    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()
    glLoadIdentity()

    glEnable(GL_TEXTURE_2D)
    texture_id = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texture_id)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, width, height, 0, GL_RGBA, GL_UNSIGNED_BYTE, text_data)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)

    glColor3f(1, 1, 1)
    glBegin(GL_QUADS)
    glTexCoord2f(0, 0); glVertex2f(x, y)
    glTexCoord2f(1, 0); glVertex2f(x + width, y)
    glTexCoord2f(1, 1); glVertex2f(x + width, y + height)
    glTexCoord2f(0, 1); glVertex2f(x, y + height)
    glEnd()

    glDeleteTextures([texture_id])
    glDisable(GL_TEXTURE_2D)
    glMatrixMode(GL_PROJECTION)
    glPopMatrix()
    glMatrixMode(GL_MODELVIEW)
    glPopMatrix()

    glEnable(GL_DEPTH_TEST)
    glDisable(GL_BLEND)

# Функция для отрисовки кнопок
def render_button(x, y, width, height, display_width, display_height):
    glDisable(GL_DEPTH_TEST)  # Отключаем глубинное тестирование для отрисовки кнопок
    glMatrixMode(GL_PROJECTION)
    glPushMatrix()
    glLoadIdentity()
    glOrtho(0, display_width, display_height, 0, -1, 1)  # Ортографическая проекция
    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()
    glLoadIdentity()

    glColor3f(1, 0, 0)  # Красный цвет для кнопки

    glBegin(GL_QUADS)
    glVertex2f(x, y)
    glVertex2f(x + width, y)
    glVertex2f(x + width, y + height)
    glVertex2f(x, y + height)
    glEnd()

    glPopMatrix()  # Возвращаемся к старой матрице
    glMatrixMode(GL_PROJECTION)
    glPopMatrix()
    glEnable(GL_DEPTH_TEST)  # Включаем обратно глубинное тестирование после отрисовки кнопок

# Функция для отрисовки кнопки "Назад"
def render_back_button(x, y, width, height, display_width, display_height):
    glDisable(GL_DEPTH_TEST)
    glDisable(GL_TEXTURE_2D)

    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)  # Включаем заливку полигона

    glMatrixMode(GL_PROJECTION)
    glPushMatrix()
    glLoadIdentity()
    glOrtho(0, display_width, display_height, 0, -1, 1)

    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()
    glLoadIdentity()

    glColor3f(1.0, 0.0, 0.0)  # Красный цвет

    glBegin(GL_QUADS)
    glVertex2f(x, y)
    glVertex2f(x + width, y)
    glVertex2f(x + width, y + height)
    glVertex2f(x, y + height)
    glEnd()

    glPopMatrix()
    glMatrixMode(GL_PROJECTION)
    glPopMatrix()

    glEnable(GL_DEPTH_TEST)
    glEnable(GL_TEXTURE_2D)

# Функция для двухточечной перспективной проекции
def set_two_point_perspective():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    # Определение параметров для glFrustum вместо  gluPerspective
    # Это создаст эффект двухточечной перспективы
    glFrustum(-1.0, 1.0, -1.0, 1.0, 2.0, 50.0)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    # Позиция камеры отдалена по оси Z и добавлены повороты для эффекта двухточечной перспективы
    glTranslatef(0.0, 0.0, -10)

    # Повороты для имитации двух точек схода
    glRotatef(30, 1, 0, 0)  # X
    glRotatef(45, 0, 1, 0)  # Y


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

# Функция просмотра фигуры
def view_figure(selected_figure):
    global rotation_x, rotation_y, mouse_last_pos

    back_button_rect = pygame.Rect(850, 50, 100, 50)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if back_button_rect.collidepoint(mouse_pos):
                    return
                mouse_last_pos = pygame.mouse.get_pos()
            elif event.type == pygame.MOUSEMOTION:
                if pygame.mouse.get_pressed()[0]:
                    mouse_pos = pygame.mouse.get_pos()
                    if mouse_last_pos:
                        dx = mouse_pos[0] - mouse_last_pos[0]
                        dy = mouse_pos[1] - mouse_last_pos[1]
                        rotation_x += dy * 0.3
                        rotation_y += dx * 0.3
                    mouse_last_pos = mouse_pos

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        set_two_point_perspective()

        glPushMatrix()
        glRotatef(rotation_x, 1, 0, 0)
        glRotatef(rotation_y, 0, 1, 0)

        glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)

        if selected_figure == 'Tetrahedron':
            draw_tetrahedron()
        elif selected_figure == 'Hexahedron':
            draw_hexahedron()
        elif selected_figure == 'Octahedron':
            draw_octahedron()

        glPopMatrix()

        glMatrixMode(GL_PROJECTION)
        glPushMatrix()
        glLoadIdentity()
        glOrtho(0, 1000, 1000, 0, -1, 1)
        glMatrixMode(GL_MODELVIEW)
        glPushMatrix()
        glLoadIdentity()

        render_back_button(back_button_rect.x, back_button_rect.y, back_button_rect.width, back_button_rect.height, 1000, 1000)
        render_text("Назад", back_button_rect.x + 5, back_button_rect.y + 855, 36)

        glPopMatrix()
        glMatrixMode(GL_PROJECTION)
        glPopMatrix()

        pygame.display.flip()
        pygame.time.wait(10)

# Главное меню с вращением фигур
def main_menu(display):
    global rotation_angle_tetrahedron, rotation_angle_hexahedron, rotation_angle_octahedron
    pygame.font.init()
    selected_figure = None

    button_y = 750
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

        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(70, (display[0] / display[1]), 0.1, 50.0)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glTranslatef(0.0, 0.0, -8)

        glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)

        glPushMatrix()
        glTranslatef(-3.5, 0, 0)
        glRotatef(rotation_angle_tetrahedron, 1, 1, 1)
        draw_tetrahedron()
        glPopMatrix()

        glPushMatrix()
        glTranslatef(0, 0, 0)
        glRotatef(rotation_angle_hexahedron, 1, 1, 1)
        draw_hexahedron()
        glPopMatrix()

        glPushMatrix()
        glTranslatef(3.5, 0, 0)
        glRotatef(rotation_angle_octahedron, 1, 1, 1)
        draw_octahedron()
        glPopMatrix()
        set_two_point_perspective()
        glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)

        render_text("Выберите фигуру:", 400, 900, 48)

        render_button(button_tetra.x, button_tetra.y, button_tetra.width, button_tetra.height, display[0], display[1])
        render_button(button_hexa.x, button_hexa.y, button_hexa.width, button_hexa.height, display[0], display[1])
        render_button(button_octa.x, button_octa.y, button_octa.width, button_octa.height, display[0], display[1])

        render_text("Тетраэдр", button_tetra.x + 35, button_tetra.y - 545, 36)
        render_text("Гексаэдр", button_hexa.x + 35, button_hexa.y - 545, 36)
        render_text("Октаэдр", button_octa.x + 35, button_octa.y - 545, 36)

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
