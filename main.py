# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import re
# calculator



def split_expression(express):
    master_split = []

    def splinter(exp):
        operation_tab = re.findall('[-,+,*,/]', exp)
        if len(operation_tab) == 0:
            master_split.append(int(exp))
        else:
            split_exp = exp.split(operation_tab[0], 1)
            master_split.append(int(split_exp[0]))
            master_split.append(operation_tab[0])
            splinter(split_exp[1])

    splinter(express)
    return master_split


def somme(n1, n2):
    return n1 + n2


def diff(n1, n2):
    return n1-n2


def mult(n1, n2):
    return n1*n2


def div(n1, n2):
    return n1/n2


def calc(n1, n2, op):
    if op == '+':
        return somme(n1, n2)
    elif op == '-':
        return diff(n1, n2)
    elif op == '*':
        return mult(n1, n2)
    else:
        return div(n1, n2)


def calculate(tab_data):
    sign_tab = [['/', '*'], ['+', '-']]
    for sign in sign_tab:
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
                calc_result = calc(nbr1, nbr2, operator)
                tab_data.insert(index - 1, calc_result)
                continuous = True
    return tab_data


while 1:
    expression = input('give an expression: \n')
    tab = split_expression(expression)
    result = calculate(tab)[0]
    print(result)
