
from OpenGL.GL import *

# Функция для отрисовки кнопок
def render_button(x, y, width, height, display_width, display_height):
    glDisable(GL_DEPTH_TEST)
    glMatrixMode(GL_PROJECTION)
    glPushMatrix()
    glLoadIdentity()
    glOrtho(0, display_width, display_height, 0, -1, 1)  # Ортографическая проекция
    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()
    glLoadIdentity()

    glColor3f(1, 0, 0)

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

# Функция для отрисовки кнопок назад
def render_back_button(x, y, width, height, display_width, display_height):

    glDisable(GL_DEPTH_TEST)
    glDisable(GL_TEXTURE_2D)
    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)

    glMatrixMode(GL_PROJECTION)
    glPushMatrix()
    glLoadIdentity()
    glOrtho(0, display_width, display_height, 0, -1, 1)

    # Переходим на модельно-видовую матрицу
    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()
    glLoadIdentity()

    glColor3f(1.0, 0.0, 0.0)

    glBegin(GL_QUADS)
    glVertex2f(x, y)
    glVertex2f(x + width, y)
    glVertex2f(x + width, y + height)
    glVertex2f(x, y + height)
    glEnd()

    # Восстанавливаем прежние настройки
    glPopMatrix()
    glMatrixMode(GL_PROJECTION)
    glPopMatrix()

    glEnable(GL_DEPTH_TEST)
    glEnable(GL_TEXTURE_2D)