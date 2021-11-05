from pico2d import *

open_canvas(2561,217)

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
             running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
             running = False
Map=load_image('map.png')
running=True
while running:
    handle_events()
    clear_canvas()
    Map.draw(2561,217)
    update_canvas()

close_canvas()

