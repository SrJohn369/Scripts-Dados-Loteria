from funcitions import *


def main():
    dataFrame = criar_dataFrame("./xlsx/+Milionária.xlsx", 10)
    adicionar_dados(dataFrame, 'milionaria')


if __name__ == "__main__":
    main()