def main():
    suma = 0
    i = 1
    while i <= 3:
        x = float(input('What is the length of side'+str(i)+'? '))
        suma = suma+x
        i += 1
    print('The perimeter of the triangle is', suma)
    pass


if __name__ == "__main__":
    main()
