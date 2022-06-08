#1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки
# формата «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod.
# Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число». Второй,
# с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

#############################################################################################################

class Date:
    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @classmethod
    def extraction(cls, day_month_year):
        my_date = day_month_year.split("-")
        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod
    def validity(day, month, year):
        if year >= 0:
            if 1 <= day <= 31:
                if 1 <= month <= 12:
                    print('all right!')
                else:
                    print("wrong month value, repeat enter")
            else:
                print('wrong day value, repeat enter')
        else:
            print('wrong year value, repeat enter')
        return f'enter date: {day:02}-{month:02}-{year}'


a = Date("")
print(Date.extraction("12-05-2022"))
print(a.extraction("11-02-2022"))
print(a.validity(12, 8, 2013))
print(Date.validity(12, 15, 2016))