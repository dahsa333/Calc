import numpy as np
import cv2


W_W = 1280
W_H = 720
pad = 0.05
SCALE = 0.4
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (255, 0, 0)
RED = (0, 0, 255)
CUSTOM1 = (255, 102, 103)
CUSTOM2 = (103, 102, 255)
LL = False
CURR_POS = [0, 0]
X_START = W_W * 0.05
Y_START = W_H // 2
D_SCALE = 0.02
PB = [0, 0]
PE = [0, 0]


def add_variables(f):
    for i in range(1, f.v["i_int"] + 1):
        f.add_variable("D_нз" + s(i), f.v["D_н" + s(i)], "")


def s(to_string):
    return str(to_string)


def mouse_event_callback(event, x, y, flags, param):
    global SCALE, LL, CURR_POS, X_START, Y_START, D_SCALE
    if event == cv2.EVENT_MOUSEWHEEL:
        if flags > 0:
            SCALE += D_SCALE
        else:
            SCALE -= D_SCALE
    elif event == cv2.EVENT_LBUTTONDOWN and LL is False:
        CURR_POS = [x, y]
        LL = True
    elif event == cv2.EVENT_LBUTTONUP and LL is True:
        LL = False
    elif event == cv2.EVENT_MOUSEMOVE:
        if LL is True:
            dx = CURR_POS[0] - x
            dy = CURR_POS[1] - y
            X_START -= dx
            Y_START -= dy
            CURR_POS = [x, y]


def show(img, f):
    cv2.namedWindow("win_calc")
    cv2.setMouseCallback("win_calc", mouse_event_callback)
    while True:
        cv2.imshow("win_calc", img)
        img = draw_func(f)
        if cv2.waitKey(1) & 0xFF == 27:
            break
    cv2.destroyAllWindows()


def w_to_r(x):
    global SCALE
    return x / SCALE


def r_to_w(x):
    global SCALE
    return SCALE * x


def set_start_scale(f):
    global SCALE, W_W
    la_len = f.v["az1ср" + s(1)] + f.v["bz1ср" + s(1)] + f.v["Sz1" + s(1)] * 1000.0
    for i in range(1, f.v["i_int"] + 1):
        la_len += f.v["az2ср" + s(i)] + f.v["bz2ср" + s(i)] + f.v["Sz2" + s(i)] * 1000.0
        la_len += f.v["az3ср" + s(i)] + f.v["bz3ср" + s(i)] + f.v["Sz3" + s(i)] * 1000.0
    if f.v["тип ступени"] != 3:
        la_len += f.v["az4ср" + s(1)] + f.v["bz4ср" + s(1)] + f.v["Sz4" + s(1)] * 1000.0
    SCALE = W_W * 1.0 / la_len


def draw_vna(img, p, f):
    global BLACK
    len = r_to_w(1000.0 * (f.v["D_н" + s(1)] - f.v["D_вт" + s(1)])) / 2.0
    avt = r_to_w(f.v["az1вт" + s(1)])
    bvt = r_to_w(f.v["bz1вт" + s(1)])
    an = r_to_w(f.v["az1н" + s(1)])
    bn = r_to_w(f.v["bz1н" + s(1)])
    aaver = r_to_w(f.v["az1ср" + s(1)])
    baver = r_to_w(f.v["bz1ср" + s(1)])
    p1 = (int(p[0] - avt), int(p[1] + len / 2.0))
    p2 = (int(p[0] - aaver), int(p[1]))
    p3 = (int(p[0] - an), int(p[1] - len / 2.0))
    p4 = (int(p[0] + bvt), int(p[1] + len / 2.0))
    p5 = (int(p[0] + baver), int(p[1]))
    p6 = (int(p[0] + bn), int(p[1] - len / 2.0))
    cv2.line(img, p1, p2, BLUE, 1)
    cv2.line(img, p2, p3, BLUE, 1)
    cv2.line(img, p4, p5, BLUE, 1)
    cv2.line(img, p5, p6, BLUE, 1)
    cv2.line(img, p3, p6, BLUE, 1)
    cv2.line(img, p1, p4, BLUE, 1)


def draw_rk(img, p, f, n_st):
    global BLACK
    len = r_to_w(1000.0 * (f.v["D_н" + s(n_st)] - f.v["D_вт" + s(n_st)])) / 2.0
    avt = r_to_w(f.v["az2вт" + s(n_st)])
    bvt = r_to_w(f.v["bz2вт" + s(n_st)])
    an = r_to_w(f.v["az2н" + s(n_st)])
    bn = r_to_w(f.v["bz2н" + s(n_st)])
    aaver = r_to_w(f.v["az2ср" + s(n_st)])
    baver = r_to_w(f.v["bz2ср" + s(n_st)])
    p1 = (int(p[0] - avt), int(p[1] + len / 2.0))
    p2 = (int(p[0] - aaver), int(p[1]))
    p3 = (int(p[0] - an), int(p[1] - len / 2.0))
    p4 = (int(p[0] + bvt), int(p[1] + len / 2.0))
    p5 = (int(p[0] + baver), int(p[1]))
    p6 = (int(p[0] + bn), int(p[1] - len / 2.0))
    cv2.line(img, p1, p2, BLACK, 1)
    cv2.line(img, p2, p3, BLACK, 1)
    cv2.line(img, p4, p5, BLACK, 1)
    cv2.line(img, p5, p6, BLACK, 1)
    cv2.line(img, p3, p6, BLACK, 1)
    cv2.line(img, p1, p4, BLACK, 1)


def draw_pna(img, p, f, n_st):
    global BLACK
    len = r_to_w(1000.0 * (f.v["D_н" + s(n_st)] - f.v["D_вт" + s(n_st)])) / 2.0
    avt = r_to_w(f.v["az3вт" + s(n_st)])
    bvt = r_to_w(f.v["bz3вт" + s(n_st)])
    an = r_to_w(f.v["az3н" + s(n_st)])
    bn = r_to_w(f.v["bz3н" + s(n_st)])
    aaver = r_to_w(f.v["az3ср" + s(n_st)])
    baver = r_to_w(f.v["bz3ср" + s(n_st)])
    p1 = (int(p[0] - avt), int(p[1] + len / 2.0))
    p2 = (int(p[0] - aaver), int(p[1]))
    p3 = (int(p[0] - an), int(p[1] - len / 2.0))
    p4 = (int(p[0] + bvt), int(p[1] + len / 2.0))
    p5 = (int(p[0] + baver), int(p[1]))
    p6 = (int(p[0] + bn), int(p[1] - len / 2.0))
    cv2.line(img, p1, p2, GREEN, 1)
    cv2.line(img, p2, p3, GREEN, 1)
    cv2.line(img, p4, p5, GREEN, 1)
    cv2.line(img, p5, p6, GREEN, 1)
    cv2.line(img, p3, p6, GREEN, 1)
    cv2.line(img, p1, p4, GREEN, 1)


def draw_sa(img, p, f):
    global BLACK
    len = r_to_w(1000.0 * (f.v["D_н" + s(f.v["i_int"])] - f.v["D_вт" + s(f.v["i_int"])])) / 2.0
    avt = r_to_w(f.v["az4вт" + s(1)])
    bvt = r_to_w(f.v["bz4вт" + s(1)])
    an = r_to_w(f.v["az4н" + s(1)])
    bn = r_to_w(f.v["bz4н" + s(1)])
    aaver = r_to_w(f.v["az4ср" + s(1)])
    baver = r_to_w(f.v["bz4ср" + s(1)])
    p1 = (int(p[0] - avt), int(p[1] + len / 2.0))
    p2 = (int(p[0] - aaver), int(p[1]))
    p3 = (int(p[0] - an), int(p[1] - len / 2.0))
    p4 = (int(p[0] + bvt), int(p[1] + len / 2.0))
    p5 = (int(p[0] + baver), int(p[1]))
    p6 = (int(p[0] + bn), int(p[1] - len / 2.0))
    cv2.line(img, p1, p2, RED, 1)
    cv2.line(img, p2, p3, RED, 1)
    cv2.line(img, p4, p5, RED, 1)
    cv2.line(img, p5, p6, RED, 1)
    cv2.line(img, p3, p6, RED, 1)
    cv2.line(img, p1, p4, RED, 1)


def get_center_point(f, n_st):
    global PB, PE, RED, X_START, Y_START
    pb = [X_START + r_to_w(f.v["Sz1" + s(1)] * 1000.0 + f.v["bz1ср" + s(1)] + f.v["az2ср" + s(1)]), Y_START]
    for i in range(1, n_st + 1):
        if i > 1:
            l_h = ((f.v["D_н" + s(i - 1)] - f.v["D_вт" + s(i - 1)]) - (f.v["D_н" + s(i)] - f.v["D_вт" + s(i)])) / 2.0
            delta_y = r_to_w(1000.0 * l_h / 2.0)
            pb[1] += delta_y
        if i == n_st:
            break
        pb[0] += r_to_w(f.v["Sz2" + s(i)] * 1000.0 + f.v["bz2ср" + s(i)] + f.v["az3ср" + s(i)])
        if i < f.v["i_int"]:
            if f.v["тип ступени"] == 3:
                pb[0] += r_to_w(f.v["Sz2" + s(i)] * 1000.0 + f.v["bz3ср" + s(i)] + f.v["az2ср" + s(i + 1)])
            else:
                pb[0] += r_to_w(f.v["Sz3" + s(i)] * 1000.0 + f.v["bz3ср" + s(i)] + f.v["az2ср" + s(i + 1)])
    return pb


def get_enter_blade_point(f, n_st):
    pe = get_center_point(f, n_st)
    len = r_to_w(1000.0 * (f.v["D_н" + s(n_st)] - f.v["D_вт" + s(n_st)])) / 2.0
    an = r_to_w(f.v["az2н" + s(n_st)])
    p = (pe[0] - an, pe[1] - len / 2.0)
    p_int = (int(p[0]), int(p[1]))
    return p


def get_back_rk(f, n_st):
    pc = get_center_point(f, n_st)
    bn = r_to_w(f.v["bz2н" + s(n_st)])
    bvt = r_to_w(f.v["bz2вт" + s(n_st)])
    len = r_to_w(1000.0 * (f.v["D_н" + s(n_st)] - f.v["D_вт" + s(n_st)])) / 2.0
    pb1 = (int(pc[0] + bvt), int(pc[1] + len / 2.0))
    pb2 = (int(pc[0] + bn), int(pc[1] - len / 2.0))
    return pb1, pb2


def get_front_rk(f, n_st):
    pc = get_center_point(f, n_st)
    an = r_to_w(f.v["az1н" + s(1)])
    avt = r_to_w(f.v["az1вт" + s(1)])
    len = r_to_w(1000.0 * (f.v["D_н" + s(n_st)] - f.v["D_вт" + s(n_st)])) / 2.0
    pb1 = (int(pc[0] - avt), int(pc[1] + len / 2.0))
    pb2 = (int(pc[0] - an), int(pc[1] - len / 2.0))
    return pb1, pb2


def get_part_list(n_st, n_parts):
    st_list = []
    delta_list = []
    h1 = n_st - n_parts - 1
    p1 = h1 // n_parts
    p2 = h1 % n_parts
    for i in range(n_parts):
        if p2 > 0:
            delta_list.append(p1 + 1)
            p2 -= 1
        else:
            delta_list.append(p1)
    for i in range(n_parts + 1):
        if i == 0:
            st_list.append(1)
        else:
            st_list.append(st_list[-1] + delta_list[i - 1] + 1)
    return st_list


def smoothing(img, f):
    global RED, BLUE, CUSTOM1, CUSTOM2, Y_START, P_1_Y
    n_parts = 3
    st_list = get_part_list(f.v["i_int"], n_parts)
    for i_n in range(1, n_parts + 1):
        n_curr = st_list[i_n - 1]
        p1 = get_enter_blade_point(f, n_curr)
        p1_int = (int(p1[0]), int(p1[1]))
        cv2.circle(img, p1_int, 5, BLUE, 2)
        p2 = get_enter_blade_point(f, st_list[i_n])
        p2_int = (int(p2[0]), int(p2[1]))
        cv2.circle(img, p2_int, 5, BLUE, 2)
        a1 = p1[1] - p2[1]
        b1 = p2[0] - p1[0]
        c1 = p1[0] * p2[1] - p2[0] * p1[1]
        for i in range(st_list[i_n - 1], st_list[i_n]):
            pb1, pb2 = get_back_rk(f, i)
            a2 = pb1[1] - pb2[1]
            b2 = pb2[0] - pb1[0]
            c2 = pb1[0] * pb2[1] - pb2[0] * pb1[1]
            y_find = (a2 * c1 - c2 * a1) / (a1 * b2 - a2 * b1)
            x_find = (-c1 - b1 * y_find) / a1
            p_new = (int(x_find), int(y_find))
            if p_new[1] > pb2[1]:
                len = r_to_w(1000.0 * (f.v["D_н" + s(i)] - f.v["D_вт" + s(i)])) / 2.0
                diff = get_enter_blade_point(f, i)[1] + len - y_find
                diff_r = w_to_r(diff) / 1000.0
                f.v["D_нз" + s(i)] = f.v["D_вт" + s(i)] + diff_r * 2.0
                cv2.circle(img, p_new, 5, CUSTOM1, 1)
        for i in range(st_list[i_n - 1], st_list[i_n]):
            pb1, pb2 = get_front_rk(f, i)
            a2 = pb1[1] - pb2[1]
            b2 = pb2[0] - pb1[0]
            c2 = pb1[0] * pb2[1] - pb2[0] * pb1[1]
            y_find = (a2 * c1 - c2 * a1) / (a1 * b2 - a2 * b1)
            x_find = (-c1 - b1 * y_find) / a1
            p_new = (int(x_find), int(y_find))
            if p_new[1] > pb2[1]:
                len = r_to_w(1000.0 * (f.v["D_н" + s(i)] - f.v["D_вт" + s(i)])) / 2.0
                diff = get_enter_blade_point(f, i)[1] + len - y_find
                diff_r = w_to_r(diff) / 1000.0
                f.v["D_н" + s(i)] = f.v["D_вт" + s(i)] + diff_r * 2.0
                cv2.circle(img, p_new, 5, CUSTOM1, 1)
                cv2.circle(img, p_new, 5, CUSTOM2, 1)
        cv2.line(img, p1_int, p2_int, RED, 1)


def draw_func(f):
    global X_START, Y_START
    global PB
    img = np.ones((W_H, W_W, 3), np.uint8) * 255
    x = X_START
    y = Y_START
    draw_vna(img, (x, y), f)
    x += r_to_w(f.v["Sz1" + s(1)] * 1000.0 + f.v["bz1ср" + s(1)] + f.v["az2ср" + s(1)])
    PB = [x, y]
    for i in range(1, f.v["i_int"] + 1):
        if i > 1:
            l_h = ((f.v["D_н" + s(i - 1)] - f.v["D_вт" + s(i - 1)]) - (f.v["D_н" + s(i)] - f.v["D_вт" + s(i)])) / 2.0
            delta_y = r_to_w(1000.0 * l_h / 2.0)
            y += delta_y
        draw_rk(img, (x, y), f, i)
        x += r_to_w(f.v["Sz2" + s(i)] * 1000.0 + f.v["bz2ср" + s(i)] + f.v["az3ср" + s(i)])
        draw_pna(img, (x, y), f, i)
        if i < f.v["i_int"]:
            if f.v["тип ступени"] == 3:
                x += r_to_w(f.v["Sz2" + s(i)] * 1000.0 + f.v["bz3ср" + s(i)] + f.v["az2ср" + s(i + 1)])
            else:
                x += r_to_w(f.v["Sz3" + s(i)] * 1000.0 + f.v["bz3ср" + s(i)] + f.v["az2ср" + s(i + 1)])
    if f.v["тип ступени"] != 3:
        x += r_to_w(f.v["Sz2" + s(1)] * 1000.0 + f.v["bz3ср" + s(f.v["i_int"])] + f.v["az4ср" + s(1)])
        draw_sa(img, (x, y), f)
    smoothing(img, f)
    return img


def create_img(f):
    global W_H, W_H
    img = draw_func(f)
    return img


def draw(f, is_show):
    add_variables(f)
    set_start_scale(f)
    img = create_img(f)
    if is_show is True:
        show(img, f)
