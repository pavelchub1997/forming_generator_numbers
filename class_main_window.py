from Check import *
from PyQt5 import QtWidgets
import main_window, checking, Error_1, Error_2, point_definition, work_with_poly, sys

class Main_Window(QtWidgets.QMainWindow, main_window.Ui_Form):

    def __init__(self):
        super().__init__()
        self.generator_numbers = []
        self.count = 1
        self.setupUi(self)
        self.pushButton.clicked.connect(self.psh_Btn)
        self.pushButton_2.clicked.connect(self.psh_Btn_1)
        self.pushButton_3.clicked.connect(self.psh_Btn_2)
        self.pushButton_4.clicked.connect(self.psh_Btn_3)
        self.pushButton_5.clicked.connect(self.psh_Btn_4)

    def value(self):
        val_field, val_param_a, val_param_b = int(self.lineEdit.text()), int(self.lineEdit_2.text()), int(self.lineEdit_3.text())
        self.lineEdit.setText(str(val_field))
        self.lineEdit_2.setText(str(val_param_a))
        self.lineEdit_3.setText(str(val_param_b))
        return val_field, val_param_a, val_param_b

    def input_value(self):
        val_x, val_y = int(self.lineEdit_6.text()), int(self.lineEdit_5.text())
        self.lineEdit_6.setText(str(val_x))
        self.lineEdit_5.setText(str(val_y))
        return val_x, val_y

    def check_Error(self):
        self.window = Error_1.Error_1_Output()
        self.window.show()
        self.close()

    def check_Error_2(self):
        self.window = Error_2.Error_2_Output()
        self.window.show()

    def result(self, a, b, field):

        bool_shit = checking.check_elleptic(a, b, field)
        if bool_shit == False:
            self.check_Error()
        else:
            list_x, list_y, count = point_definition.forming_point(a, b, field)
            str_1 = point_definition.output_point(list_x, list_y)
            print(str_1)
            self.textBrowser_7.setText(str_1)

    def result_1(self, val, buff_lst):
        val_1 = self.lineEdit_8.text()
        reg = work_with_poly.form_reg(val_1)
        self.lineEdit_9.setText(str(self.return_val(buff_lst, work_with_poly.bin_to_int(val, reg), reg)))

    def return_val(self, generator_numbers, val, shift_register):

        while 1:
            if checking.check_elem(generator_numbers, val) == False:
                if self.count == len(generator_numbers):
                    self.window = Check_1(generator_numbers)
                    self.window.show()
                    self.close()
                    break
                else:
                    val = work_with_poly.bin_to_int(generator_numbers[0], shift_register)
                    print('Value parameter is count for number not input in list: ', self.count)
                    self.count += 1
            else:
                generator_numbers.append(val)
                self.count = 1
                print('Count value in list: ', len(generator_numbers), '\nValue parameter is count: ', self.count)
                return val

    def psh_Btn(self):
        field, par_a, par_b = self.value()
        bool = checking.test_Ferma(field)
        if bool == False: self.check_Error()
        else:
            if par_a < 0: par_a+=field
            if par_a == 0: self.result(par_a, par_b, field)
            else:
                if checking.check_NOD(par_a, field) != 1: self.check_Error()
                else: self.result(par_a, par_b, field)

    def psh_Btn_1(self):
        field, par_a, par_b = self.value()
        val_coord_x, val_coord_y = self.input_value()
        list_all_coord_x, list_all_coord_y, count = point_definition.forming_point(par_a, par_b, field)
        bool = checking.check_point(val_coord_x, val_coord_y, list_all_coord_x, list_all_coord_y)
        if bool == False:
            self.check_Error_2()
        else:
            val = checking.point_order(count, val_coord_x, val_coord_y, par_a, field)
            self.generator_numbers.append(val)
            self.lineEdit_4.setText(str(val))

    def psh_Btn_2(self):
        val = self.lineEdit_7.text()
        self.lineEdit_8.setText(work_with_poly.poly(val))

    def psh_Btn_3(self):
        val = int(self.lineEdit_4.text())
        print(self.generator_numbers)
        self.result_1(val, self.generator_numbers)

    def psh_Btn_4(self):
        sys.exit()