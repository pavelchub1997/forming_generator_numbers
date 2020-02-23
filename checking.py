import random, math, determining_the_sum_point

def check_NOD(par_a, field):

    if par_a == 1: return 1
    if par_a<field: par_a, field = field, par_a
    if par_a%field == 1: return 1
    elif par_a%field == 0: return 0
    else: return check_NOD(par_a%field, par_a)

def test_Ferma(n):

    while True:
        a = random.randint(2, n - 2)
        if math.gcd(a, n) != 1: print('Числа не взаимно простые!!!')
        else:
            r = pow(a, (n-1))%n
            if r == 1: return True
            else: return False

def check_elleptic(par_a, par_b, field):

    D = int(4*pow(par_a, 3)+27*pow(par_b,2))%field
    if D == 0: return False
    else: return True

def check_point(coord_x, coord_y, list_all_coord_x, list_all_coord_y):

    if coord_x in list_all_coord_x:
        index = list_all_coord_x.index(coord_x, 0, len(list_all_coord_x))
        if coord_y in list_all_coord_y[index]: return True
        else: return False
    else: return False

def point_order(curve_order, coord_x, coord_y, par_a, field):

    bord_0, bord_1 = curve_order + 1 - 2*math.sqrt(curve_order), curve_order + 1 + 2*math.sqrt(curve_order)
    for point_order in range(int(bord_0), int(bord_1)+1):
        coord_x, coord_y = determining_the_sum_point.coeff_split(coord_x, coord_y, par_a, point_order, field)
        if coord_y == 0 or coord_x == 0: return point_order

def check_elem(lst, val_0):

    for elem in lst:
        if elem == val_0: return False
    return True