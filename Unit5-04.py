import ui
from numpy import random

my_number = []

def my_enter_number_button_touch_up_inside(sender):

    global my_number
    a = view['enter_number_textfield'].text
    view['enter_number_textview'].text = a
    view['enter_number_textfield'].text = ''
    
    print(a)
    my_number.append(str(a))
    
def my_number_touch_up_inside(sender):
	
    view['enter_number_textview'].text = ', '.join(my_number)

def sum_of_list(lista):

    global my_number
    sum_of_list = 0
    lista = my_number
    for index in range(len(lista)):
        sum_of_list += int(lista[index])
    return sum_of_list

def average_touch_up_inside(sender):
    global my_number
    global sum_of_list
    n = len(my_number)
    p = sum_of_list(my_number)
    total = p/n
    view['average_label'].text =str(total)


view = ui.load_view()
view.present('fullscreen')
