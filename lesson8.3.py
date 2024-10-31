class Car():
    def __int__(self, model, __vin):
        self.model = model
        self.__vin = __vin

    def __is_valid_vin(vin_number):
        if isinstance(vin_number, int):
            return True

        raise IncorrectCarNumbers('Некорректный тип данных для номеров')

    def __is_valid_numbers(numbers):
        if isinstance(numbers, str) and len(numbers)==6:
            return True
        else:
            raise  IncorrectCarNumbers('Неверная длина номера')


try:
    first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{first.model} успешно создан')

try:
    second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{second.model} успешно создан')

try:
    third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{third.model} успешно создан')

