from enum import Enum



class Person:
    def __init__(self, name: str, salary: float, account: int, type_: PersonTypeEnum):
        self._name = name
        self._salary = salary
        self._account = account
        self._type = type_

class _PersonTypeEnum(Enum):
    e_type = 'E'
    m_type = 'M'
    gm_type = "GM"

class Employee (_Person):
    _type = _PersonTypeEnum.e_type





if __name__ == '__main__':
    print ('start')
    e = [
        Person(name='Артём{i}', salary = 15000. + i, account = 1234 + i, type_ = PersonTypeEnum.e_type)
        for i in range (1000)
    ]
    m = Person(name = 'Misha', salary = 30000, account = 9876, type_ = m_type)
    j = Person(name='Jason', salary=1000000, account=98764, type_= gm_type)
