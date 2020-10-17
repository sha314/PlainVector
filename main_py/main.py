
def test_vector():
    from main_py import vector
    # import vector
    # vector.test()
    vector.test_rotate2D()
    pass


def test_electrostatics():
    from main_py import electrostatics
    electrostatics.test()


def test_utils():
    print("test_utils")
    from main_py import utils
    print(utils.sign())
    print(utils.sign())
    print(utils.sign())
    print(utils.sign())


def test_linear_algebra():
    from main_py import linear_algebra
    linear_algebra.test()


def main():
    test_vector()
    # test_electrostatics()
    # test_utils()
    # test_linear_algebra()


if __name__ == '__main__':
    main()
