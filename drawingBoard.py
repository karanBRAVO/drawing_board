# import statement
import pygame

# initializing pygame
pygame.init()

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
aqua = (0, 255, 255)
purple = (255, 0, 255)
grey = (128, 128, 128)
pink = (255, 174, 199)
orange = (255, 127, 39)
brown = (185, 122, 87)

# setting font
font = pygame.font.SysFont("Helvetica", 18, True, False)

# window and terminal settings
windowWidth = 700
windowHeight = 600
window = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption("Drawing Board")
print("*** Drawing Board ***")
print("""   <--- mouse --->
+ => increase pixels
- => decrease pixels
e => erase pixel
r => remove all pixels
g => show or remove grid
s => save the drawing
    <--- keys --->
f => remove grid
t => show grid
r => remove all pixels
s => save drawing
e => select eraser
w => unselect eraser
ESC => exit
""")

# gap b/w two lines of grid
gap = 5  # do not change it
# color size
color_option_dimension = 15  # do not change it
# Available Colors
available_colors = [black, brown, red, orange, yellow, green, pink, blue, purple, aqua, white]  # can add more colors

# dictionary of color Rect
pos_color_option = {}
for i in range(1, 12, 1):
    pos_color_option[f"color_{i}"] = pygame.Rect(i * 20, windowHeight - (gap * 4), color_option_dimension, color_option_dimension)

# initial mouse position
mouse_x = -1
mouse_y = -1

# takes corrected mouse position
pos = None
# empty list for storing positions
black_pos = []
brown_pos = []
red_pos = []
orange_pos = []
yellow_pos = []
green_pos = []
pink_pos = []
blue_pos = []
purple_pos = []
aqua_pos = []
white_pos = []

# variables for which color is selected
selected_black = True
selected_brown = False
selected_red = False
selected_orange = False
selected_yellow = False
selected_green = False
selected_pink = False
selected_blue = False
selected_purple = False
selected_aqua = False
selected_white = False

# show grid initially
show_grid = True
# eraser is initially off
can_erase = False

# button dimensions
button_width = 35
button_height = 25

# buttons
increase_pixels_buttons = pygame.Rect(250, windowHeight - (gap * 5), button_width, button_height)
decrease_pixels_buttons = pygame.Rect(250 + button_height * 2, windowHeight - (gap * 5), button_width, button_height)
remove_button = pygame.Rect(250 + button_height * 4, windowHeight - (gap * 5), button_width, button_height)
erase_button = pygame.Rect(250 + button_height * 6, windowHeight - (gap * 5), button_width, button_height)
grid_button = pygame.Rect(250 + button_height * 8, windowHeight - (gap * 5), button_width, button_height)
save_button = pygame.Rect(250 + button_height * 10, windowHeight - (gap * 5), button_width, button_height)


# contains color to be drawn
class Color:
    def __init__(self, color=None):
        self.color = color
        self.pixelFactor = 1
        self.rect_dimension = gap * self.pixelFactor

    def inc_pixels(self):
        self.pixelFactor += 1

    def dec_pixels(self):
        self.pixelFactor -= 1

    def make_pen_brown(self):
        self.color = brown

    def make_pen_black(self):
        self.color = black

    def make_pen_red(self):
        self.color = red

    def make_pen_green(self):
        self.color = green

    def make_pen_blue(self):
        self.color = blue

    def make_pen_yellow(self):
        self.color = yellow

    def make_pen_purple(self):
        self.color = purple

    def make_pen_aqua(self):
        self.color = aqua

    def make_pen_white(self):
        self.color = white

    def make_pen_pink(self):
        self.color = pink

    def make_pen_orange(self):
        self.color = orange

    def drawRect(self, x, y):
        pygame.draw.rect(window, self.color, (x, y, self.rect_dimension, self.rect_dimension))


draw = Color(None)


# remove all the drawing
def Reset():
    global selected_black, selected_brown, selected_red, selected_orange, selected_yellow, selected_green, selected_pink, selected_blue, selected_purple, selected_aqua, selected_white, pos, \
        mouse_y, mouse_x

    selected_black = True
    selected_brown = False
    selected_red = False
    selected_orange = False
    selected_yellow = False
    selected_green = False
    selected_pink = False
    selected_blue = False
    selected_purple = False
    selected_aqua = False
    selected_white = False
    pos = None
    mouse_x = -1
    mouse_y = -1
    black_pos.clear()
    brown_pos.clear()
    red_pos.clear()
    orange_pos.clear()
    yellow_pos.clear()
    green_pos.clear()
    pink_pos.clear()
    blue_pos.clear()
    purple_pos.clear()
    aqua_pos.clear()
    white_pos.clear()


# TODO: ERASER -> erase if pixel factor is not 1
def drawPixels():
    global mouse_x, mouse_y, pos, can_erase

    keys = pygame.key.get_pressed()

    # assigning mouse position to mouse_x and mouse_y
    if pygame.mouse.get_pressed(3)[0]:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        # append to pos if clicked on white board
        if mouse_y < windowHeight - (gap * 6):
            # making corrections
            if mouse_x / gap >= int(mouse_x / gap):
                mouse_x = int(mouse_x / gap) * gap
            if mouse_y / gap >= int(mouse_y / gap):
                mouse_y = int(mouse_y / gap) * gap
            pos = [mouse_x, mouse_y]
        # do not append to pos if clicked outside white board
        if mouse_y > windowHeight - (gap * 6):
            pos = None

    # remove all drawing
    if pygame.mouse.get_pressed(3)[1] or remove_button.collidepoint(mouse_x, mouse_y) or keys[pygame.K_r]:
        Reset()

    # select eraser
    if keys[pygame.K_e]:
        draw.pixelFactor = 1
        draw.rect_dimension = gap * draw.pixelFactor
        pos = None
        can_erase = True
    # unselect eraser
    elif keys[pygame.K_w]:
        pos = None
        can_erase = False

    # what to erase
    if can_erase:
        if black_pos.count(pos) != 0:
            black_pos.pop(black_pos.index(pos))
        if brown_pos.count(pos) != 0:
            brown_pos.pop(brown_pos.index(pos))
        if red_pos.count(pos) != 0:
            red_pos.pop(red_pos.index(pos))
        if orange_pos.count(pos) != 0:
            orange_pos.pop(orange_pos.index(pos))
        if yellow_pos.count(pos) != 0:
            yellow_pos.pop(yellow_pos.index(pos))
        if green_pos.count(pos) != 0:
            green_pos.pop(green_pos.index(pos))
        if blue_pos.count(pos) != 0:
            blue_pos.pop(blue_pos.index(pos))
        if pink_pos.count(pos) != 0:
            pink_pos.pop(pink_pos.index(pos))
        if purple_pos.count(pos) != 0:
            purple_pos.pop(purple_pos.index(pos))
        if aqua_pos.count(pos) != 0:
            aqua_pos.pop(aqua_pos.index(pos))
        if white_pos.count(pos) != 0:
            white_pos.pop(white_pos.index(pos))

    # append clicked position to lists
    if pos is not None and not can_erase:
        if selected_black:
            if black_pos.count(pos) == 0:
                black_pos.append(pos)
        elif selected_brown:
            if brown_pos.count(pos) == 0:
                brown_pos.append(pos)
        elif selected_red:
            if red_pos.count(pos) == 0:
                red_pos.append(pos)
        elif selected_orange:
            if orange_pos.count(pos) == 0:
                orange_pos.append(pos)
        elif selected_yellow:
            if yellow_pos.count(pos) == 0:
                yellow_pos.append(pos)
        elif selected_green:
            if green_pos.count(pos) == 0:
                green_pos.append(pos)
        elif selected_pink:
            if pink_pos.count(pos) == 0:
                pink_pos.append(pos)
        elif selected_blue:
            if blue_pos.count(pos) == 0:
                blue_pos.append(pos)
        elif selected_purple:
            if purple_pos.count(pos) == 0:
                purple_pos.append(pos)
        elif selected_aqua:
            if aqua_pos.count(pos) == 0:
                aqua_pos.append(pos)
        elif selected_white:
            if white_pos.count(pos) == 0:
                white_pos.append(pos)

    # draw till not erased
    for mouse_pos in black_pos:
        draw.make_pen_black()
        draw.drawRect(mouse_pos[0], mouse_pos[1])
    for mouse_pos in brown_pos:
        draw.make_pen_brown()
        draw.drawRect(mouse_pos[0], mouse_pos[1])
    for mouse_pos in red_pos:
        draw.make_pen_red()
        draw.drawRect(mouse_pos[0], mouse_pos[1])
    for mouse_pos in orange_pos:
        draw.make_pen_orange()
        draw.drawRect(mouse_pos[0], mouse_pos[1])
    for mouse_pos in yellow_pos:
        draw.make_pen_yellow()
        draw.drawRect(mouse_pos[0], mouse_pos[1])
    for mouse_pos in green_pos:
        draw.make_pen_green()
        draw.drawRect(mouse_pos[0], mouse_pos[1])
    for mouse_pos in pink_pos:
        draw.make_pen_pink()
        draw.drawRect(mouse_pos[0], mouse_pos[1])
    for mouse_pos in blue_pos:
        draw.make_pen_blue()
        draw.drawRect(mouse_pos[0], mouse_pos[1])
    for mouse_pos in purple_pos:
        draw.make_pen_purple()
        draw.drawRect(mouse_pos[0], mouse_pos[1])
    for mouse_pos in aqua_pos:
        draw.make_pen_aqua()
        draw.drawRect(mouse_pos[0], mouse_pos[1])
    for mouse_pos in white_pos:
        draw.make_pen_white()
        draw.drawRect(mouse_pos[0], mouse_pos[1])


# checks which color is selected
def get_selected_color():
    global selected_black, selected_red, selected_brown, selected_green, selected_white, selected_purple, selected_pink, selected_orange, selected_yellow, selected_blue, selected_aqua

    if pos_color_option[f"color_{1}"].collidepoint(mouse_x, mouse_y):  # black
        selected_black = True
        selected_brown = False
        selected_red = False
        selected_orange = False
        selected_yellow = False
        selected_green = False
        selected_pink = False
        selected_blue = False
        selected_purple = False
        selected_aqua = False
        selected_white = False
    if pos_color_option[f"color_{2}"].collidepoint(mouse_x, mouse_y):  # brown
        selected_black = False
        selected_brown = True
        selected_red = False
        selected_orange = False
        selected_yellow = False
        selected_green = False
        selected_pink = False
        selected_blue = False
        selected_purple = False
        selected_aqua = False
        selected_white = False
    if pos_color_option[f"color_{3}"].collidepoint(mouse_x, mouse_y):  # red
        selected_black = False
        selected_brown = False
        selected_red = True
        selected_orange = False
        selected_yellow = False
        selected_green = False
        selected_pink = False
        selected_blue = False
        selected_purple = False
        selected_aqua = False
        selected_white = False
    if pos_color_option[f"color_{4}"].collidepoint(mouse_x, mouse_y):  # orange
        selected_black = False
        selected_brown = False
        selected_red = False
        selected_orange = True
        selected_yellow = False
        selected_green = False
        selected_pink = False
        selected_blue = False
        selected_purple = False
        selected_aqua = False
        selected_white = False
    if pos_color_option[f"color_{5}"].collidepoint(mouse_x, mouse_y):  # yellow
        selected_black = False
        selected_brown = False
        selected_red = False
        selected_orange = False
        selected_yellow = True
        selected_green = False
        selected_pink = False
        selected_blue = False
        selected_purple = False
        selected_aqua = False
        selected_white = False
    if pos_color_option[f"color_{6}"].collidepoint(mouse_x, mouse_y):  # green
        selected_black = False
        selected_brown = False
        selected_red = False
        selected_orange = False
        selected_yellow = False
        selected_green = True
        selected_pink = False
        selected_blue = False
        selected_purple = False
        selected_aqua = False
        selected_white = False
    if pos_color_option[f"color_{7}"].collidepoint(mouse_x, mouse_y):  # pink
        selected_black = False
        selected_brown = False
        selected_red = False
        selected_orange = False
        selected_yellow = False
        selected_green = False
        selected_pink = True
        selected_blue = False
        selected_purple = False
        selected_aqua = False
        selected_white = False
    if pos_color_option[f"color_{8}"].collidepoint(mouse_x, mouse_y):  # blue
        selected_black = False
        selected_brown = False
        selected_red = False
        selected_orange = False
        selected_yellow = False
        selected_green = False
        selected_pink = False
        selected_blue = True
        selected_purple = False
        selected_aqua = False
        selected_white = False
    if pos_color_option[f"color_{9}"].collidepoint(mouse_x, mouse_y):  # purple
        selected_black = False
        selected_brown = False
        selected_red = False
        selected_orange = False
        selected_yellow = False
        selected_green = False
        selected_pink = False
        selected_blue = False
        selected_purple = True
        selected_aqua = False
        selected_white = False
    if pos_color_option[f"color_{10}"].collidepoint(mouse_x, mouse_y):  # aqua
        selected_black = False
        selected_brown = False
        selected_red = False
        selected_orange = False
        selected_yellow = False
        selected_green = False
        selected_pink = False
        selected_blue = False
        selected_purple = False
        selected_aqua = True
        selected_white = False
    if pos_color_option[f"color_{11}"].collidepoint(mouse_x, mouse_y):  # white
        selected_black = False
        selected_brown = False
        selected_red = False
        selected_orange = False
        selected_yellow = False
        selected_green = False
        selected_pink = False
        selected_blue = False
        selected_purple = False
        selected_aqua = False
        selected_white = True


# increases or decreases pixel size
def Inc_Dec_pixels():
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            x1, y1 = pygame.mouse.get_pos()
            if increase_pixels_buttons.collidepoint(x1, y1) and draw.pixelFactor <= 10:
                draw.inc_pixels()
                draw.rect_dimension = gap * draw.pixelFactor
            elif decrease_pixels_buttons.collidepoint(x1, y1) and draw.pixelFactor > 1:
                draw.dec_pixels()
                draw.rect_dimension = gap * draw.pixelFactor


# saving the image
def save_image():
    global show_grid, pos
    keys = pygame.key.get_pressed()

    if keys[pygame.K_s] or save_button.collidepoint(mouse_x, mouse_y):
        pos = None
        show_grid = False
        pygame.image.save(window, "untitled.png")


# showing available colors on window
def showColor_options():
    for num in range(1, 12):
        pygame.draw.rect(window, available_colors[num - 1], pos_color_option[f"color_{num}"])


# draws the grid on window
def drawGrid():
    global show_grid

    keys = pygame.key.get_pressed()

    if show_grid:
        if keys[pygame.K_f]:
            show_grid = False
        for row in range(0, windowHeight - (gap * 5), gap):
            pygame.draw.line(window, grey, start_pos=(0, row), end_pos=(windowWidth, row), width=1)
        for col in range(0, windowWidth, gap):
            pygame.draw.line(window, grey, start_pos=(col, 0), end_pos=(col, windowHeight - (gap * 5) - gap), width=1)
    elif not show_grid:
        if keys[pygame.K_t]:
            show_grid = True


# makes a button
def button(text, button_x, button_y, button_type):
    icon = font.render(f"{text}", True, black, None)
    pygame.draw.rect(window, black, button_type, border_radius=2, width=2)
    window.blit(icon, [button_x, button_y])


# draw button on window
def draw_buttons():
    button("+", increase_pixels_buttons.x + 12, increase_pixels_buttons.y + 2, increase_pixels_buttons)
    button("-", decrease_pixels_buttons.x + 14, decrease_pixels_buttons.y + 1, decrease_pixels_buttons)
    button("r", remove_button.x + 13, remove_button.y - 2, remove_button)
    button("e", erase_button.x + 12, erase_button.y - 2, erase_button)
    button("g", grid_button.x + 12, grid_button.y - 3, grid_button)
    button("s", save_button.x + 13, save_button.y - 2, save_button)


# background of tools
def tool_board():
    pygame.draw.rect(window, grey, (0, windowHeight - (gap * 6), windowWidth, 30))


# takes the functions to be ran continuously
def redrawWindow():
    # fill the whole window with white color
    window.fill(white)
    drawPixels()
    drawGrid()
    Inc_Dec_pixels()
    save_image()
    get_selected_color()
    tool_board()
    showColor_options()
    draw_buttons()


# main function which will be called
def mainloop():
    global show_grid, can_erase

    run = True
    while run:
        # handling events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                run = False
            # taking mouse position on clicking
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                # when to show grid
                if show_grid:
                    if grid_button.collidepoint(x, y):
                        show_grid = False
                elif not show_grid:
                    if grid_button.collidepoint(x, y):
                        show_grid = True
                # when to erase
                if can_erase:
                    if erase_button.collidepoint(x, y):
                        can_erase = False
                elif not can_erase:
                    if erase_button.collidepoint(x, y):
                        draw.pixelFactor = 1
                        draw.rect_dimension = gap * draw.pixelFactor
                        can_erase = True

        redrawWindow()
        # updates window everytime
        pygame.display.update()
    # quit
    pygame.quit()


if __name__ == "__main__":
    mainloop()
