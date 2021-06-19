from enum import Enum


class _PersonTypeEnum(Enum):
    e_type = 'E'
    m_type = 'M'
    gm_type = 'GM'


class Name():
    def __init__(self, first_name: str, second_name: str, last_name: str):
        self._first_name = first_name
        self._second_name = second_name
        self._last_name = last_name


class _Person:
    def __init__(self, name: Name,
                 salary: float,
                 account: int):
        self._name = name
        self._salary = salary
        self._account = account

    @property
    def name(self) -> str:
        raise NotImplementedError


class Employee(_Person):
    _type = _PersonTypeEnum.e_type


    @property
    def name(self) -> str:
        return f'{self._name} E'


class Manager(_Person):
    _type = _PersonTypeEnum.m_type

    @property
    def name(self) -> str:
        return f'{self._name} M'

class GeneralManager(_Person):
    _type = _PersonTypeEnum.gm_type

    @property
    def name(self) -> str:
        return f'{self._name} GM'


if __name__ == '__main__':
    print('start')
    e = [
        Employee(name=f'Артём{i} Михайлович Тугарёв', salary=15000. + i, account=1234 + i)
        for i in range(1000)
    ]
    e.append(Manager(name='Миша Михайлович Ф.', salary=30000, account=9876))
    e.append(GeneralManager(name='Jason Михайлович', salary=1030000, account=98764))
    e.append(GeneralManager(name='Jason Михайлович', salary=1130000, account=98766))

    salary = sum(_e._salary for _e in e)

    for _e in e:
        print(f'Привет, {_e.name}. Вот твоя зарплата {_e._salary}')
