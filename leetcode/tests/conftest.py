
def pytest_configure(config):

    for index in range(1, 2000):
        config.addinivalue_line('markers', f'T{index:04}')
