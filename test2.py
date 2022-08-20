import pygame
import pygame._sdl2


class Game_Window:
    def __init__(self) -> None:
        self.window = pygame._sdl2.Window()
        self.renderer = pygame._sdl2.Renderer(self.window)


    def render(self):
        self.renderer.clear()


    def handle_event(self, event:pygame.event.Event):
        if event.type == pygame.WINDOWCLOSE:
            self.close()

    
    def close(self):
        self.window.destroy()



game_windows = [
    Game_Window(),
    Game_Window(),
    Game_Window()]
running = True
clock = pygame.time.Clock()



while running:
    clock.tick(60)

    # render
    for window in game_windows: window.render()

    # event handle
    for event in pygame.event.get():
        event_window = getattr(event, "window", None)
        for game_window in game_windows:
            if event.type == pygame.QUIT:
                running = False

                
            if game_window.window != event_window: continue

            game_window.handle_event(event)
            break


pygame.quit()