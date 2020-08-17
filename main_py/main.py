
def test_vector():
    from main_py import vector
    # import vector
    vector.test()


def test_electrostatics():
    from main_py import electrostatics
    electrostatics.test()


def main():
    test_vector()
    test_electrostatics()

if __name__ == '__main__':
    main()
