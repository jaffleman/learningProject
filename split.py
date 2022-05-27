import re


def spliter(exp, m_split):
    operation_tab = re.findall('[-+*/]', exp)
    if len(operation_tab) == 0:
        m_split.append(int(exp))
    else:
        split_exp = exp.split(operation_tab[0], 1)
        m_split.append(int(split_exp[0]))
        m_split.append(operation_tab[0])
        spliter(split_exp[1], m_split)


def split_expression(express):
    master_split = []
    spliter(express, master_split)
    return master_split
