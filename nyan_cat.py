from kandinsky import *

# Définition des couleurs
grey = color(153, 153, 153)
blue = color(0, 45, 110)
red = color(255, 16, 0)
orange = color(255, 153, 0)
yellow = color(255, 242, 0)
green = color(16, 221, 0)
cyan = color(0, 140, 255)
purple = color(105, 58, 255)
pink = color(255, 169, 255)
magenta = color(254, 73, 152)
beige = color(255, 203, 153)
salmon = color(255, 159, 156)

def drawStar(x, y, type):
    if type == "small":
        x_diff_S = [0, 0, 5, -5]
        y_diff_S = [5, -5, 0, 0]
        for i in range(len(x_diff_S)):
            fill_rect(x + x_diff_S[i], y + y_diff_S[i], 5, 5, "white")
    elif type == "medium":
        x_diff_M = [0, 0, -10, 10]
        y_diff_M = [10, -10, 0, 0]
        for i in range(len(x_diff_M)):
            fill_rect(x + x_diff_M[i], y + y_diff_M[i], 5, 5, "white")
    elif type == "large":
        x_diff_L = [0, 0, 0, 0, 0, -10, -15, 10, 15]
        y_diff_L = [0, 10, 15, -10, -15, 0, 0, 0, 0]
        for i in range(len(x_diff_L)):
            fill_rect(x + x_diff_L[i], y + y_diff_L[i], 5, 5, "white")

def drawRainbow(x, y):
    rainbow_colors = [red, orange, yellow, green, cyan, purple]
    y_Template = [0, 0, 0, 0, 5, 5, 5, 5, 5, 5, 5, 5, 0, 0, 0, 0, 0, 0, 0, 0, 5, 5, 5, 5]
    for i in range(len(rainbow_colors)):
        for j in range(3):
            for k in range(len(y_Template)):
                fill_rect(x + k*5, y + y_Template[k] + j*5 + i*5*3, 5, 5, rainbow_colors[i])

def drawCatHead(x, y):
    x_head_Black = [10, 15, 60, 65, 5, 20, 55, 70, 5, 25, 50, 70, 5, 30, 35, 40, 45, 70, 5, 70, 0, 75, 0, 25, 60, 75, 0, 20, 25, 45, 55, 60, 75, 0, 75, 0, 25, 40, 55, 75, 5, 25, 30, 35, 40, 45, 50, 55, 70, 10, 65, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]
    y_constant = 0
    for i in range(len(x_head_Black)):
        fill_rect(x + x_head_Black[i], y + y_constant*5, 5, 5, "black")
        if i != len(x_head_Black) - 1:
            if x_head_Black[i] > x_head_Black[i+1]:
                y_constant += 1
    x_head_White = [20, 55]
    y_constant = 6
    for i in range(len(x_head_White)):
        fill_rect(x + x_head_White[i], y + y_constant*5, 5, 5, "white")
    x_head_S = [10, 15, 65, 70, 10, 15, 65, 70]
    y_constant = 8
    for i in range(len(x_head_S)):
        fill_rect(x + x_head_S[i], y + y_constant*5, 5, 5, salmon)
        if i != len(x_head_S) - 1:
            if x_head_S[i] > x_head_S[i+1]:
                y_constant += 1
    x_head_Grey = [10, 15, 60, 65, 10, 15, 20, 55, 60, 65, 10, 15, 20, 25, 50, 55, 60, 65, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 5, 10, 15, 30, 35, 40, 45, 50, 65, 70, 5, 10, 15, 30, 35, 40, 50, 65, 70, 5, 20, 25, 30, 35, 40, 45, 50, 55, 60, 5, 20, 30, 35, 45, 50, 60, 10, 15, 20, 60, 65, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]
    y_constant = 1
    for i in range(len(x_head_Grey)):
        fill_rect(x + x_head_Grey[i], y + y_constant*5, 5, 5, grey)
        if i != len(x_head_Grey) - 1:
            if x_head_Grey[i] > x_head_Grey[i+1]:
                y_constant += 1

def drawCatBody(x, y):
    x_body_Black = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 5, 95, 0, 100, 0, 100, 0, 100, 0, 100, 0, 100, 0, 100, 0, 100, 0, 100, 0, 100, 0, 100, 0, 100, 0, 100, 0, 100, 0, 100, 5, 95, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90]
    y_constant = 0
    for i in range(len(x_body_Black)):
        fill_rect(x + x_body_Black[i], y + y_constant * 5, 5, 5, "black")
        if i != len(x_body_Black) - 1:
            if x_body_Black[i] > x_body_Black[i + 1]:
                y_constant += 1
    fill_rect(x+10, y+10, 17*5, 14*5, pink)
    x_body_Beige = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 5, 10, 15, 85, 90, 95, 5, 10, 90, 95, 5, 95, 5, 95, 5, 95, 5, 95, 5, 95, 5, 95, 5, 95, 5, 95, 5, 95, 5, 95, 5, 10, 90, 95, 5, 10, 15, 85, 90, 95, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90]
    y_constant = 1
    for i in range(len(x_body_Beige)):
        fill_rect(x + x_body_Beige[i], y + y_constant * 5, 5, 5, beige)
        if i != len(x_body_Beige) - 1:
            if x_body_Beige[i] > x_body_Beige[i + 1]:
                y_constant += 1
    y_body_Magenta = [55, 20, 70, 45, 30, 65, 50, 20, 60, 30, 70, 60, 35, 15, 50, 25, 65, 40, 20, 55, 30, 45, 65]
    x_constant = 3
    for i in range(len(y_body_Magenta)):
        fill_rect(x + x_constant * 5, y + y_body_Magenta[i], 5, 5, magenta)
        if i != len(y_body_Magenta) - 1:
            if y_body_Magenta[i] > y_body_Magenta[i + 1]:
                x_constant += 1

def drawCatLeg(x, y, type):
    if type == "front": # Il y a 3 petites pattes
        x_diff_F = [0, 15, 5, 10, 15]
        y_diff_F = [0, 0, 5, 5, 5]
        for i in range(len(x_diff_F)):
            fill_rect(x + x_diff_F[i], y + y_diff_F[i], 5, 5, "black")
        fill_rect(x + 5, y, 5, 5, grey)
        fill_rect(x + 10, y, 5, 5, grey)
    elif type == "back": # Il y a une grande patte arrière
        x_diff_B = [5, 10, 15, 5, 10]
        y_diff_B = [10, 10, 10, 15, 15]
        x_leg_Black = [10, 5, 10, 15, 0, 20, 0, 15, 0, 5, 10]
        y_constant = 0
        for i in range(len(x_leg_Black)):
            fill_rect(x + x_leg_Black[i], y + y_constant * 5, 5, 5, "black")
            if i != len(x_leg_Black) - 1:
                if x_leg_Black[i] > x_leg_Black[i + 1]:
                    y_constant += 1
        for i in range(len(x_diff_B)):
            fill_rect(x + x_diff_B[i], y + y_diff_B[i], 5, 5, grey)
    elif type == "tail": # La queue est une 5ème patte ;)
        x_diff_T = [5, 10, 15, 10, 15, 20, 25, 30]
        y_diff_T = [5, 5, 5, 10, 10, 10, 10, 15]
        x_leg_Black = [5, 10, 15, 20, 0, 20, 25, 30, 0, 5, 30, 10, 15, 20, 25, 25, 30]
        y_constant = 0
        for i in range(len(x_leg_Black)):
            fill_rect(x + x_leg_Black[i], y + y_constant * 5, 5, 5, "black")
            if i != len(x_leg_Black) - 1:
                if x_leg_Black[i] >= x_leg_Black[i + 1]:
                    y_constant += 1
        for i in range(len(x_diff_T)):
            fill_rect(x + x_diff_T[i], y + y_diff_T[i], 5, 5, grey)



def nyan_cat():
    fill_rect(0, 0, 320, 222, blue)
    drawStar(20, 30, "small")
    drawStar(140, 190, "medium")
    drawStar(250, 40, "large")
    drawRainbow(0, 60)
    drawCatBody(105, 65)
    drawCatHead(155, 90)
    drawCatLeg(190, 155, "front")
    drawCatLeg(165, 155, "front")
    drawCatLeg(115, 155, "front")
    drawCatLeg(90, 140, "back")
    drawCatLeg(70, 105, "tail")

nyan_cat()
