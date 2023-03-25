def remove_empty_tuples(tuple_list):
    """remove tuplas vazias"""
    for i in tuple_list:
        if(i == ()):
            tuple_list.remove(())
    return tuple_list

def average_tuple(tuple_tuple):
    """retorna tupla das médias"""
    t_return = ()
    for t in tuple_tuple:
        t_return += (sum(t)/len(t),)
    return t_return

def contains_alnum(string_list):
    """retorna sublista somente com strings que contêm pelo menos um caracter do alfabeto e um numérico"""
    l = []
    for s in string_list:
        a = False
        b = False
        for c in s:
            if c.isalpha() == True:
                a = True
            if c.isdigit() == True:
                b = True

        if a and b:
            l.append(s)
    return l

def contains_chr_from_string(s1, s2):
    """ s1: string a partir do qual os caracteres são escolhidos
    s2: string em que os caracteres serão procurados"""

    for c1 in s1:
        if s2.find(c1) == -1:
            return False
    return True

def mat_mult(m1, m2):
    """multiplica duas matrizes"""
    li = len(m1)
    lj = len(m2[0])

    m_ret = []

    for i in range(li):
        m_ret.append([])
        for j in range(lj):
            m_ret[i].append(0)
            for n in range(len(m2)):
                m_ret[i][j] += m1[i][n]*m2[n][j]
    
    return m_ret

def reverse_list(l):
    """retorna lista inversa"""
    value = 1
    while value <= len(l):
        yield l[-value]
        value += 1

def primes():
    """lista infinita de primos"""
    value = 2
    while True:
        is_prime = True
        for i in range(2, value):
            if(value % i == 0):
                is_prime = False
        if is_prime:
            yield value
        value += 1
    
        
def filter_pair(l):
    """retorna uma sublista só com os elementos pares"""
    return list(filter(lambda x: (x%2 == 0), l))


def sum_lines(m):
    """retorna uma lista no qual cada elemento é a soma dos números de uma linha"""
    return(list(map(sum, m)))
