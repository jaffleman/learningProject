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
