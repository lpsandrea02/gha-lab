from hi.hello import hello

def test_hello():
    if hello() != 1:
        raise ValueError
