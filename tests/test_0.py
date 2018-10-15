# dummy test, used to ensure pytest as well as travis integration works fine!

def foo():
    return 'Hello from Python!'

def test_foo():
    assert foo() == 'Hello from Python!'
