
def test_vector():
    from main_py import vector
    # import vector
    vector.test()


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


def main():
    test_vector()
    test_electrostatics()
    test_utils()

if __name__ == '__main__':
    main()
