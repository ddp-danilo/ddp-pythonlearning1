def maximo3(a, b, c):
    """Recebe três números e retorna o maior"""
    if a >= b and a >= c:
        return a 
    if b >= a and b >= c:
        return b
    if c >= b and c >= a:
        return c

  #  Testes
"""
def test_1(): 
    assert maximo3(4, 6, 8) == 8
def test_4():
    assert maximo3(4, 8, 6) == 8
def test_2():
    assert maximo3(8, 4, 6) == 8
def test_3():
    assert maximo3(0, 0, 0) == 0
"""