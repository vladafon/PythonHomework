import pygame
import pygame as pg
import numpy as np
import math
import numba

res = W, H = 800, 500
max_iter = 30

texture = pg.image.load('texture.jpg')
texture_size = min(texture.get_size()) - 1
texture_array = pg.surfarray.array3d(texture)

offset_shift = 2
zoom_shift = 2.2 / H * 0.01


class Fractal:
    def __init__(self, app):
        self.app = app
        self.screen_array = np.full((W, H, 3), [0, 0, 0], dtype=np.uint8)
        self.x = np.linspace(0, W, num=W, dtype=np.float32)
        self.y = np.linspace(0, H, num=H, dtype=np.float32)

    @staticmethod
    @numba.njit(fastmath=True)
    def render(screen_array,offset,zoom):
        for x in range(W):
            for y in range(H):
                c = (x - offset[0]) * zoom + 1j * (y - offset[1]) * zoom
                z = 0
                num_iter = 0

                for i in range(max_iter):
                    z = z ** 2 + c
                    if z.real ** 2 + z.imag ** 2 > 4:
                        break

                    num_iter += 1

                col = int(texture_size * num_iter / max_iter)
                screen_array[x, y] = texture_array[col,col]
        return  screen_array

    # def render(self):
    #
    #     # x = (self.x - offset[0]) * zoom
    #     # y = (self.y - offset[1]) * zoom
    #     #
    #     # c = x + 1j * y[:,None]
    #     #
    #     # num_iter = np.full(c.shape,max_iter)
    #     # z = np.empty(c.shape, np.complex64)
    #     # for i in range(max_iter):
    #     #     mask = (num_iter == max_iter)
    #     #     z[mask] = z[mask] ** 2 + c[mask]
    #     #     num_iter[mask & (z.real ** 2 + z.imag ** 2 > 4.0)] = i + 1
    #     #
    #     # col = (num_iter.T * texture_size / max_iter).astype(np.uint8)
    #     # self.screen_array = texture_array[col,col]
    #
    #     #
    #     for x in range(W):
    #         for y in range(H):
    #             c = (x - offset[0]) * zoom + 1j * (y - offset[1]) * zoom
    #             z = 0
    #             num_iter = 0
    #
    #             for i in range(max_iter):
    #                 z = z ** 2 + c
    #                 if z.real ** 2 + z.imag ** 2 > 4:
    #                     break
    #
    #                 num_iter += 1
    #
    #             col = int(texture_size * num_iter / max_iter)
    #             self.screen_array[x, y] = texture_array[col,col]

    def update(self,offset,zoom):
        #self.render()


        self.screen_array = self.render(self.screen_array,offset,zoom)

    def draw(self):
        pg.surfarray.blit_array(self.app.screen, self.screen_array)

    def run(self,offset,zoom):
        self.update(offset,zoom)
        self.draw()


class App:
    def __init__(self):
        self.screen = pg.display.set_mode(res, pg.SCALED)
        self.clock = pg.time.Clock()
        self.fractal = Fractal(self)
        self.right_pressed = False
        self.left_pressed = False
        self.up_pressed = False
        self.down_pressed = False

        self.offset = np.array([1.3 * W, H]) // 2
        self.zoom = 2.2 / H

    def run(self):
        while True:
            self.screen.fill('Black')
            self.fractal.run(self.offset,self.zoom)
            pg.display.flip()

            # event loop
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    exit()
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_d:
                        self.right_pressed = True
                    if event.key == pg.K_a:
                        self.left_pressed = True
                    if event.key == pg.K_w:
                        self.up_pressed = True
                    if event.key == pg.K_s:
                        self.down_pressed = True

                    if event.key == pg.K_r:
                        self.offset = np.array([1.3 * W, H]) // 2
                        self.zoom = 2.2 / H
                if event.type == pg.KEYUP:
                    if event.key == pg.K_d:
                        self.right_pressed = False
                    if event.key == pg.K_a:
                        self.left_pressed = False
                    if event.key == pg.K_w:
                        self.up_pressed = False
                    if event.key == pg.K_s:
                        self.down_pressed = False
                if event.type == pg.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()

                    if event.button == 4:
                        print('zoom in')
                        self.offset = [self.offset[0]*1.0, self.offset[1]*1.0]
                        self.zoom -= zoom_shift
                    elif event.button == 5:
                        print('zoom out')
                        self.offset = [self.offset[0]*1.0, self.offset[1]*1.0]
                        self.zoom += zoom_shift




            #print(self.offset)
            if (self.right_pressed):
                self.offset[0] -= offset_shift/(self.zoom/(2.2 / H))
            if (self.left_pressed):
                self.offset[0] += offset_shift/(self.zoom/(2.2 / H))
            if (self.up_pressed):
                self.offset[1] += offset_shift/(self.zoom/(2.2 / H))
            if (self.down_pressed):
                self.offset[1] -= offset_shift/(self.zoom/(2.2 / H))



            self.clock.tick()
            pg.display.set_caption(f'FPS: {self.clock.get_fps()}')


if __name__ == '__main__':
    app = App()
    app.run()