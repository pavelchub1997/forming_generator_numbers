def symbol_Legandra(value, field):

    result = pow(value, int((field-1)/2), field)
    if result == 1: return 1
    elif result == field-1: return -1
    elif result == 0: return 0

def find_nonchedule(list_point_elliptic_curve, field):

    for elem in list_point_elliptic_curve:
        if symbol_Legandra(elem, field) == -1: return elem

def droblenie_field(field):
    k, s = field - 1, 0
    while True:
        if k % 2 == 0:
            s += 1
            Q, k = int((field - 1) / int(pow(2, s))), k/2
            continue
        else: break
    return s, Q

def forming_list(list_point_elliptic_curve, par_a, par_b, field):
    list_coord_y, list_coord_x, count_point_elliptic_curve = [], [], 0
    s, Q = droblenie_field(field)
    val_non_deduction = find_nonchedule(list_point_elliptic_curve, field)
    for elem in list_point_elliptic_curve:
        val = int(elem**3 + elem*par_a + par_b)
        if symbol_Legandra(val, field) == -1: continue
        else:
            if symbol_Legandra(val, field) == 1: count_point_elliptic_curve += 2
            elif symbol_Legandra(val, field) == 0: count_point_elliptic_curve += 1
            list_coord_y.append(value_coord_point(val, val_non_deduction, s, Q, field))
            list_coord_x.append(elem)
    return list_coord_x, list_coord_y, count_point_elliptic_curve

def forming_point(par_a, par_b, field):

    buff_list = [i for i in range(field)]
    list_all_coord_x, list_all_coord_y, count_point_elliptic_curve = forming_list(buff_list, par_a, par_b, field)
    # print(list_x, list_y)
    return list_all_coord_x, list_all_coord_y, count_point_elliptic_curve

def find_value_i(M, t, field):

    for i in range(1, M):
        if (t**(2**i)) % field == 1: return i

def finding_coord_point(y_2, val_non_deduction, Q, s, field):

    c, R, t, M = (val_non_deduction ** Q) % field, (y_2 ** ((Q + 1) // 2)) % field, (y_2 ** Q) % field, s
    while True:
        if t % field == 1: return [R, (field - R) % field]
        else:
            if M < 3: i = 1
            else: i = find_value_i(M, t, field)
            b = (c ** int(2 ** ((M - i - 1) % field))) % field
            R, t, c, M = (R * b) % field, (t * (b ** 2)) % field, (b ** 2) % field, i

def value_coord_point(y_2, val_non_deduction, s, Q, field):

    if y_2 % field == 0: return [y_2%field]
    else:
        if s == 1:
            R = (y_2 ** ((field+1)//4)) % field
            return [R, (field-R)%field]
        else: finding_coord_point(y_2, val_non_deduction, Q, s, field)

def output_point(list_x, list_y):
    str_1, x = '', 0
    for i in range(len(list_x)):
        if list_y[i].count(x) == 1: str_1 += 'P(' + str(list_x[i]) + ',' + str(list_y[i][0]) + ')' + '\n'
        else:
            for j in range(len(list_y[i])): str_1 += 'P(' + str(list_x[i]) + ',' + str(list_y[i][j]) + ')' + '\n'
    return str_1

def output_lst(buff_lst):
    str_1 = ''
    for i in range(len(buff_lst)): str_1 += 'Элемент № ' + str(i+1) + ': ' + str(buff_lst[i]) + '\n'
    return str_1