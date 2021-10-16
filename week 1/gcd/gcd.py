a, b = 42, 30

def gcd(a, b):
    if not (a > 0 and b > 0):
        raise ArithmeticError("%s, %s: Must be positive int." % (a, b))
    while not a == b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a

def test_gcd():
    a, b = 42, 30
    v = gcd(a, b)
    assert(v == 6)

def test_gcd2():
    a, b = 6, 6
    v = gcd(a, b)
    assert(v == 6)

def test_gcd3():
    a, b = 42, -30
    try:
        v = gcd(a, b)
        assert(False)
    except ArithmeticError as e:
        assert("Must be positive int." in str(e))
    except:
        assert(False)
    finally:
        assert(True)