# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import calcul_function as func
import split as s
# calculator


def calculate(tab_data):
    for sign in [['/', '*'], ['+', '-']]:
        continuous = True
        while continuous:
            index = -1
            if sign[0] in tab_data:
                div_index = tab_data.index(sign[0])
            else:
                div_index = -1
            if sign[1] in tab_data:
                mult_index = tab_data.index(sign[1])
            else:
                mult_index = -1
            if div_index == -1 and mult_index == -1:
                continuous = False
            else:
                if div_index > -1 and mult_index > -1:
                    if div_index < mult_index:
                        index = div_index
                    else:
                        index = mult_index
                elif div_index > -1 or mult_index > -1:
                    if div_index > -1:
                        index = div_index
                    else:
                        index = mult_index
                nbr2 = tab_data.pop(index + 1)
                operator = tab_data.pop(index)
                nbr1 = tab_data.pop(index - 1)
                calc_result = func.calc(nbr1, nbr2, operator)
                tab_data.insert(index - 1, calc_result)
                reduce = "= "
                for elem in tab_data:
                    reduce += str(elem)
                print(reduce)
                continuous = True


while 1:
    try:
        expression = input('give an expression: \n')
        tab = s.split_expression(expression)
        calculate(tab)
    except ValueError:
        print('Check out your expression, an error has been detected')
