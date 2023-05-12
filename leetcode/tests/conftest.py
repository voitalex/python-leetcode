
def pytest_configure(config):

    for index in range(1, 1500):
        config.addinivalue_line('markers', f'T{index:04}')
