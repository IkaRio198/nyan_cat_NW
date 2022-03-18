from kandinsky import *

"""
Définitions des couleurs personnalisées. Récupérées grâce à https://imagecolorpicker.com/
0: grey, 1: blue, 2: red, 3: orange, 4: yellow, 5: green, 6: cyan, 7: purple, 8: pink, 9: magenta, 10: beige, 11: salmon
"""
colors = [(153, 153, 153), (0, 45, 110), (255, 16, 0), (255, 153, 0), (255, 242, 0), (16, 221, 0), (0, 140, 255),
          (105, 58, 255), (255, 169, 255), (254, 73, 152), (255, 203, 153), (255, 159, 156)]


def draw_star(x, y, variety):
    if variety == "small":
        x_diff_s = [0, 0, 5, -5]
        y_diff_s = [5, -5, 0, 0]
        for i in range(len(x_diff_s)):
            fill_rect(x + x_diff_s[i], y + y_diff_s[i], 5, 5, "white")
    elif variety == "medium":
        x_diff_m = [0, 0, -10, 10]
        y_diff_m = [10, -10, 0, 0]
        for i in range(len(x_diff_m)):
            fill_rect(x + x_diff_m[i], y + y_diff_m[i], 5, 5, "white")
    elif variety == "large":
        x_diff_l = [0, 0, 0, 0, 0, -10, -15, 10, 15]
        y_diff_l = [0, 10, 15, -10, -15, 0, 0, 0, 0]
        for i in range(len(x_diff_l)):
            fill_rect(x + x_diff_l[i], y + y_diff_l[i], 5, 5, "white")


def draw_rainbow(x, y):
    rainbow_colors = [colors[2], colors[3], colors[4], colors[5], colors[6], colors[7]]
    y_template = [0, 0, 0, 0, 5, 5, 5, 5, 5, 5, 5, 5, 0, 0, 0, 0, 0, 0, 0, 0, 5, 5, 5, 5]
    for i in range(len(rainbow_colors)):
        for j in range(3):
            for k in range(len(y_template)):
                fill_rect(x + k * 5, y + y_template[k] + j * 5 + i * 5 * 3, 5, 5, rainbow_colors[i])


def draw_cat_head(x, y):
    x_head_black = [10, 15, 60, 65, 5, 20, 55, 70, 5, 25, 50, 70, 5, 30, 35, 40, 45, 70, 5, 70, 0, 75, 0, 25, 60, 75, 0,
                    20, 25, 45, 55, 60, 75, 0, 75, 0, 25, 40, 55, 75, 5, 25, 30, 35, 40, 45, 50, 55, 70, 10, 65, 15, 20,
                    25, 30, 35, 40, 45, 50, 55, 60]
    x_head_white = [20, 55]
    x_head_salmon = [10, 15, 65, 70, 10, 15, 65, 70]
    x_head_grey = [10, 15, 60, 65, 10, 15, 20, 55, 60, 65, 10, 15, 20, 25, 50, 55, 60, 65, 10, 15, 20, 25, 30, 35, 40,
                   45, 50, 55, 60, 65, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 5, 10, 15, 30, 35, 40, 45,
                   50, 65, 70, 5, 10, 15, 30, 35, 40, 50, 65, 70, 5, 20, 25, 30, 35, 40, 45, 50, 55, 60, 5, 20, 30, 35,
                   45, 50, 60, 10, 15, 20, 60, 65, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]
    y_diff = [0, 6, 8, 1]
    head_x_colors = [x_head_black, x_head_white, x_head_salmon, x_head_grey]
    head_colors = ["black", "white", colors[11], colors[0]]
    for i in range(len(head_x_colors)):
        for j in range(len(head_x_colors[i])):
            fill_rect(x + head_x_colors[i][j], y + y_diff[i] * 5, 5, 5, head_colors[i])
            if j != len(head_x_colors[i]) - 1:
                if head_x_colors[i][j] > head_x_colors[i][j + 1]:
                    y_diff[i] += 1


def draw_cat_body(x, y):
    x_body_black = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 5, 95, 0, 100, 0, 100, 0, 100,
                    0, 100, 0, 100, 0, 100, 0, 100, 0, 100, 0, 100, 0, 100, 0, 100, 0, 100, 0, 100, 0, 100, 5, 95, 10,
                    15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90]
    y_constant = 0
    for i in range(len(x_body_black)):
        fill_rect(x + x_body_black[i], y + y_constant * 5, 5, 5, "black")
        if i != len(x_body_black) - 1:
            if x_body_black[i] > x_body_black[i + 1]:
                y_constant += 1
    fill_rect(x + 10, y + 10, 17 * 5, 14 * 5, colors[8])
    x_body_beige = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 5, 10, 15, 85, 90, 95, 5, 10,
                    90, 95, 5, 95, 5, 95, 5, 95, 5, 95, 5, 95, 5, 95, 5, 95, 5, 95, 5, 95, 5, 95, 5, 10, 90, 95, 5, 10,
                    15, 85, 90, 95, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90]
    y_constant = 1
    for i in range(len(x_body_beige)):
        fill_rect(x + x_body_beige[i], y + y_constant * 5, 5, 5, colors[10])
        if i != len(x_body_beige) - 1:
            if x_body_beige[i] > x_body_beige[i + 1]:
                y_constant += 1
    y_body_magenta = [55, 20, 70, 45, 30, 65, 50, 20, 60, 30, 70, 60, 35, 15, 50, 25, 65, 40, 20, 55, 30, 45, 65]
    x_constant = 3
    for i in range(len(y_body_magenta)):
        fill_rect(x + x_constant * 5, y + y_body_magenta[i], 5, 5, colors[9])
        if i != len(y_body_magenta) - 1:
            if y_body_magenta[i] > y_body_magenta[i + 1]:
                x_constant += 1


def draw_cat_leg(x, y, variety):
    if variety == "front":
        x_diff_f = [0, 15, 5, 10, 15]
        y_diff_f = [0, 0, 5, 5, 5]
        for i in range(len(x_diff_f)):
            fill_rect(x + x_diff_f[i], y + y_diff_f[i], 5, 5, "black")
        fill_rect(x + 5, y, 5, 5, colors[0])
        fill_rect(x + 10, y, 5, 5, colors[0])
    elif variety == "back":
        x_diff_b = [5, 10, 15, 5, 10]
        y_diff_b = [10, 10, 10, 15, 15]
        x_leg_black = [10, 5, 10, 15, 0, 20, 0, 15, 0, 5, 10]
        y_constant = 0
        for i in range(len(x_leg_black)):
            fill_rect(x + x_leg_black[i], y + y_constant * 5, 5, 5, "black")
            if i != len(x_leg_black) - 1:
                if x_leg_black[i] > x_leg_black[i + 1]:
                    y_constant += 1
        for i in range(len(x_diff_b)):
            fill_rect(x + x_diff_b[i], y + y_diff_b[i], 5, 5, colors[0])
    elif variety == "tail":
        x_diff_t = [5, 10, 15, 10, 15, 20, 25, 30]
        y_diff_t = [5, 5, 5, 10, 10, 10, 10, 15]
        x_leg_black = [5, 10, 15, 20, 0, 20, 25, 30, 0, 5, 30, 10, 15, 20, 25, 25, 30]
        y_constant = 0
        for i in range(len(x_leg_black)):
            fill_rect(x + x_leg_black[i], y + y_constant * 5, 5, 5, "black")
            if i != len(x_leg_black) - 1:
                if x_leg_black[i] >= x_leg_black[i + 1]:
                    y_constant += 1
        for i in range(len(x_diff_t)):
            fill_rect(x + x_diff_t[i], y + y_diff_t[i], 5, 5, colors[0])


def nyan_cat():
    fill_rect(0, 0, 320, 222, colors[1])
    draw_star(20, 30, "small")
    draw_star(140, 190, "medium")
    draw_star(250, 40, "large")
    draw_rainbow(0, 60)
    draw_cat_body(105, 65)
    draw_cat_head(155, 90)
    draw_cat_leg(190, 155, "front")
    draw_cat_leg(165, 155, "front")
    draw_cat_leg(115, 155, "front")
    draw_cat_leg(90, 140, "back")
    draw_cat_leg(70, 105, "tail")
    display()


nyan_cat()
