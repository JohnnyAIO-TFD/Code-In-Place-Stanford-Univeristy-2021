def main():
    fanh = float(input('Enter Temperature in Fahrenheit : '))
    celsius = (fanh-32)*5/9
    print('Temperature:', str(fanh)+'F =', str(celsius)+'C')
    pass


if __name__ == "__main__":
    main()
