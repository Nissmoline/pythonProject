import pygame
from pygame.locals import *
from OpenGL.GL import *
from main import *

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

        # Применяем вращение сначала
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
