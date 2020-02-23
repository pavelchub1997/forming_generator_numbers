import math

def count(top, lower, field):

    top %= field
    lower %= field

    while top % lower != 0: top += field
    return top//lower

def sum_point_P(val_coord_x_first_point, val_coord_x_second_point, val_coord_y_first_point, val_coord_y_second_point, field):

    if val_coord_x_first_point == val_coord_x_second_point: return 0, 0

    val_drob = count(val_coord_y_second_point - val_coord_y_first_point, val_coord_x_second_point-val_coord_x_first_point, field)

    val_coord_x_third_point = (pow(val_drob, 2) - (val_coord_x_first_point + val_coord_x_second_point)) % field
    val_coord_y_third_point = ((-1)*val_coord_y_first_point + ((val_drob)*(val_coord_x_first_point - val_coord_x_third_point))) % field

    return val_coord_x_third_point, val_coord_y_third_point

def sum_point_2P(val_coord_x_first_point, val_coord_y_first_point, par_a, field):

    if val_coord_y_first_point == 0: return 0, 0
    val_drob = count((3 * pow(val_coord_x_first_point, 2) + par_a), (2 * val_coord_y_first_point), field)

    val_coord_x_third_point = (pow(val_drob, 2) - 2 * val_coord_x_first_point) % field
    val_coord_y_third_point = ((-1) * val_coord_y_first_point + ((val_drob) * (val_coord_x_first_point - val_coord_x_third_point))) % field

    return val_coord_x_third_point, val_coord_y_third_point

def calc_sum(buff_list, field):

    val_coord_x_third_point, val_coord_y_third_point = buff_list[0][0], buff_list[0][1]
    for i in range(1, len(buff_list)): val_coord_x_third_point, val_coord_y_third_point = sum_point_P(val_coord_x_third_point, buff_list[i][0], val_coord_y_third_point, buff_list[i][1], field)
    return val_coord_x_third_point, val_coord_y_third_point

def coeff_split(val_coord_x, val_coord_y, par_a, coeff, field):

    buff_list = []
    val_coord_x_third_point, val_coord_y_third_point = val_coord_x, val_coord_y
    while coeff != 0:
        if coeff // 2 == 0:
            val_coord_x_third_point, val_coord_y_third_point = calc_sum(buff_list, field)
            if val_coord_y_third_point == 0: return val_coord_x_third_point, val_coord_y_third_point
            while coeff != 0:
                x_1, y_1 = sum_point_P(val_coord_x, val_coord_x_third_point, val_coord_y, val_coord_y_third_point, field)
                val_coord_x_third_point, val_coord_y_third_point, coeff = x_1, y_1, coeff-1
        else:
            degree = int(math.log2(coeff))
            coeff -= pow(2, degree)
            while degree != 0:
                x_2, y_2 = sum_point_2P(val_coord_x_third_point, val_coord_y_third_point, par_a, field)
                val_coord_x_third_point, val_coord_y_third_point = x_2, y_2
                if val_coord_y_third_point == 0: return val_coord_x_third_point, val_coord_y_third_point
                degree -= 1
            buff_list.append([val_coord_x_third_point, val_coord_y_third_point])
            if coeff == 0: val_coord_x_third_point, val_coord_y_third_point = calc_sum(buff_list, field)
            else: val_coord_x_third_point, val_coord_y_third_point = val_coord_x, val_coord_y
    return val_coord_x_third_point, val_coord_y_third_point
