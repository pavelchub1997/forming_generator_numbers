import checking, random

def split_symbol(val, symb):
    str_1 = ''
    for elem in val:
        if elem != symb:
            str_1+=elem
    return str_1

def get_length_reg(val):

    for ind, elem in enumerate(val):
        if elem == '+' or ind == len(val)-1:
            return ind

def in_list_str_to_int(lst):
    for i in range(len(lst)):
        lst[i] = int(lst[i])
    return lst

def shift_reg(buff, length_reg):

    Reg = [0 for i in range(length_reg)]
    for elem in buff:
        Reg[elem] = 1
    Reg.reverse()
    return Reg

def conv_str_2(reg):

    str_1 = '['
    for i in range(len(reg)):
        if i == len(reg)-1:
            str_1 += str(reg[i])
        else:
            str_1+=str(reg[i])+','
    str_1+=']'
    return str_1

def int_to_bit(val):

    str_1 = bin(val)
    str_1 = str_1[2:]
    lst = in_list_str_to_int(list(str_1))
    return lst

def izm_list_C(list_C, val):

    list_C.insert(0, val)
    del list_C[len(list_C)-1]
    return list_C

def forming_buff_lst(reg, length):

    buff_lst = []
    val_1 = random.randint(0, len(reg)-1)
    buff_lst.append(val_1)
    while length != 0:
        val_1 = random.randint(0, len(reg)-1)
        if checking.check_elem(buff_lst, val_1) == False:
            continue
        else:
            buff_lst.append(val_1)
            length-=1
    buff_lst.sort()
    print(buff_lst)
    return buff_lst

def forming_reg(buff_lst, reg):

    val = reg[buff_lst[0]]
    for i in range(1, len(buff_lst)):
        val ^= reg[buff_lst[i]]
    return val

def form_reg(val_1):
    reg = split_symbol(val_1, '[')
    reg = split_symbol(reg, ']')
    reg = split_symbol(reg, ',')
    return in_list_str_to_int(list(reg))

def work_reg(val, reg):

    lst = int_to_bit(val)
    length = random.randint(2, len(reg) - 1)
    print(length)
    res_lst = []
    buff_lst = forming_buff_lst(reg, length)
    for i in range(len(lst)):
        value = forming_reg(buff_lst, reg)
        res_lst.append(value^lst[i])
        reg = izm_list_C(reg, value)
    return res_lst

def bin_to_int(val, val_1):

    str_1, lst = '', work_reg(val, val_1)
    for elem in lst:
        str_1+=str(elem)
    return int(str_1, 2)

def poly(val):
    buff = []
    while len(val) != 0:
        ind = get_length_reg(val)
        if ind == len(val)-1:
            if val != '1': buff.append(int(val[1:]))
            else: buff.append(0)
            break
        else:
            buff.append(int(val[1:ind]))
            val = val[(ind+1):]
    length_reg = buff[0]
    buff.remove(buff[0])
    reg = shift_reg(buff, length_reg)
    return conv_str_2(reg)
