import csv
import pandas as pd
from data_create import name_data, surname_data, phone_data, addres_data


def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    addres = addres_data()
    var = int(input(f"В каком формате записать данные\n\n"
    f"1 вариант: \n"
    f"{name}\n{surname}\n{phone}\n{addres}\n\n"
    f"2 вариант: \n"
    f"{name};{surname};{phone};{addres}\n"
    f"Выберите вариант: "))

    while var != 1 and var != 2:
        print("Неправильный ввод")
        var = int(input('Введите число: '))

    if var == 1:
        with open('data_first_variant.csv', 'a', encoding = 'utf - 8') as f:
            f.write(f"{name}\n{surname}\n{phone}\n{addres}\n\n")
    elif var == 2:
        with open('data_second_vasiant.csv', 'a', encoding = 'utf - 8') as f:
            f.write(f"{name};{surname};{phone};{addres}\n\n")

def print_data():
    print('Вывожу данные из 1 файла: \n')
    with open('data_first_variant.csv', 'r', encoding = 'utf - 8') as f:
        data_first = f.readlines()
        data_first_list = []
        j = 0
        for i in range(len(data_first)):
            if data_first[i] == '\n' or i == len(data_first) - 1:
                data_first_list.append(''.join(data_first[j:i+1]))
                j = i
        print(''.join(data_first_list))

        print('Вывожу данные из 2 файла: \n')
    with open('data_second_vasiant.csv', 'r', encoding = 'utf - 8') as f:
        data_second = f.readlines()
        print(*data_second)

def delite_data(file, column_name, *args):
    row_to_remove = []
    for row_name in args:
        row_to_remove.append(row_name)
    try:
        df = pd.read_csv(file)
        for row in row_to_remove:
            df = df[eval("df.{}".format(column_name)) != row]
        df.to_csv(file, index = false)
    except Exception as e:
        raise Exception("Error message....")

delite_data('data_second_vasiant.csv', "Y")