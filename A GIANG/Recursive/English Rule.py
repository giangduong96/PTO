
""" Recursive  Ruler """
def draw_line(tick_length, tick_lable =""):
    "draw one line with given tick length(followed by optional lable"
    line = '-' * tick_length
    if tick_lable:
        line += " " +tick_lable
    print(line)

def draw_interval(center_length):
    "draw tick interval based upin a central tick length"
    if center_length > 0:
        draw_interval(center_length -1)
        draw_line(center_length)
        draw_interval(center_length -1)

def draw_ruler(num_inches, major_length):
    draw_line(major_length, '0')
    for j in range (1, 1 + num_inches):
        draw_interval(major_length-1)
        draw_line(major_length, str(j))


if __name__ == '__main__':
    draw_ruler(12,3)