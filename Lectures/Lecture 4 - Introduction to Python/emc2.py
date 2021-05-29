C = 299792458


def main():
    m = float(input("Enter kilos of mass: "))
    e = m * C**2
    print("e + m * C**2")
    print("m = ", m, "kg")
    print("C =", C, "m/s")
    print(e, "joules of energy!")
    pass


if __name__ == "__main__":
    main()
