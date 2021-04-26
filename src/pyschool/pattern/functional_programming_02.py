"""This module is a laboratory application of the principles taught in the preceding
module.
>>> import functional_programming_02 as fp2
"""
from abc import ABC, abstractmethod
from typing import Generator, Iterator, NamedTuple, Tuple, Type, Union

import pytest

"""
Given:
A group of people `p` who all received a degree in year `degree` (int).
All people have degrees.
Some people (retirees) have retired and thus have retirement year `retirement` (int).
Some people (workers) have not yet retired, thus have no retirement year `retirement`.
All people are either retirees or workers.
The current year is `year_now` (int).
If someone is retired, they did so in either the current year, or a previous year, thus
retirement <= year_now.
The number of years of experience a retired person has is (retirement - degree) >= 0.
The number of years of experience a non-retired person has is (year_now - degree) >= 0.

Find:
The total number of years of experience for any group of people `p`.

Solution via OOP:
"""


class Person_OOP(ABC):
    def __init__(self, *, name: str, degree: int):
        self.name = name
        self.degree = degree

    @abstractmethod
    def experience(self, *, current_year: int):
        pass


class Retiree_OOP(Person_OOP):
    def __init__(self, *, name: str, degree: int, retirement: int):
        super().__init__(name=name, degree=degree)
        self.retirement = retirement
        if self.retirement < self.degree:
            raise ValueError("Error: retirement cannot be less than degree.")

    def experience(self):
        return self.retirement - self.degree


class Worker_OOP(Person_OOP):
    def __init__(self, *, name: str, degree: int):
        super().__init__(name=name, degree=degree)

    def experience(self, *, current_year: int):
        if current_year < self.degree:
            raise ValueError("Error: current year cannot be less than degree.")
        return current_year - self.degree


"""
Use pytest to demonstrate and confirm behavior.
> pytest functional_programming_02.py -v
"""


def test_disallow_ABC_creation():
    with pytest.raises(TypeError):
        # retain for test, even though linter will highlight the error
        _ = Person_OOP(name="Anna", degree=1970)


def test_retiree_bad_value():
    with pytest.raises(ValueError):
        _ = Retiree_OOP(name="Anna", degree=1970, retirement=1960)


def test_worker_bad_value():
    w = Worker_OOP(name="Charles", degree=1990)
    with pytest.raises(ValueError):
        w.experience(current_year=1970)


def test_retiree():
    r = Retiree_OOP(name="Anna", degree=1970, retirement=2000)
    assert r.experience() == 30


def test_worker():
    w = Worker_OOP(name="Charles", degree=1990)
    c = 2000  # current year
    assert w.experience(current_year=c) == 10


# g is the group of people
def test_OOP():
    # Now make a group of people, some retired, some non-retired.
    a = Retiree_OOP(name="Anna", degree=1970, retirement=1980)  # 10 years experience
    b = Retiree_OOP(name="Bob", degree=1970, retirement=1990)  # 20 years experience
    now = 2000  # assume as the current year
    c = Worker_OOP(name="Charles", degree=1981)  # 19 years experience
    d = Worker_OOP(name="Donna", degree=1991)  # 9 years experience

    group = [a, b, c, d]

    total_experience = 0
    for g in group:
        if isinstance(g, Retiree_OOP):
            total_experience += g.experience()
        else:  # then g is necessarily a worker
            total_experience += g.experience(current_year=now)

    assert total_experience == 58


"""
Solution via FP:
"""


def test_FP():
    # class Person(NamedTuple):
    #     degree: int
    #     retirement: Union[int, None]

    class Person(NamedTuple):
        name: str
        degree: int
        retirement: int

    class Retiree(NamedTuple):
        name: str
        degree: int
        retirement: int

    class Worker(NamedTuple):
        name: str
        degree: int

    a = Person(name="Anna", degree=1970, retirement=1980)  # 10 years experience
    b = Person(name="Bob", degree=1970, retirement=1990)  # 20 years experience

    now = 2000  # assume as the current year

    c = Person(name="Charles", degree=1981, retirement=0)  # 19 years experience
    d = Person(name="Donna", degree=1991, retirement=0)  # 9 years experience

    def retiree(x: Person) -> Retiree:
        return Retiree(name=x.name, degree=x.degree, retirement=x.retirement)

    def worker(x: Person) -> Worker:
        return Worker(name=x.name, degree=x.degree)

    group = (
        a,
        b,
        c,
        d,
    )

    def retired(x: Person) -> bool:
        return x.retirement != 0

    def retirees(x: Tuple[Person, ...]) -> Iterator:
        # def retirees(x: Tuple[Person, ...]) -> Tuple[Retiree, ...]:
        # def retirees(x: Tuple[Person, ...]):
        # aa = tuple(filter(lambda i: i.retirement != 0, x))
        aa = tuple(filter(retired, x))
        # bb = (
        #     Retiree(name=a.name, degree=a.degree, retirement=a.retirement) for a in aa
        # )
        bb = map(retiree, aa)
        return bb

    r = retirees(group)
    known_retirees_names = ["Anna", "Bob"]
    calc_retirees_names = [x.name for x in r]
    assert known_retirees_names == calc_retirees_names

    def experience(x: Retiree) -> int:
        return x.retirement - x.degree

    assert experience(retiree(a)) == 10
    assert experience(retiree(b)) == 20

    def experience_sum(x: Tuple[Retiree, ...]) -> int:
        experiences = tuple(map(experience, x))
        return sum(experiences)

    assert experience_sum((retiree(a), retiree(b))) == 30

    def current_experience(x: Worker, current_year: int) -> int:
        return current_year - x.degree

    assert current_experience(worker(c), now) == 19
    assert current_experience(worker(d), now) == 9

    # def retirees_experience(x: Tuple[Retiree, ...]) -> int:
    #     aa = sum(map(retiree_experience, x))
    #     return aa

    def working(p: Person) -> bool:
        return p.retirement == 0

    def workers(x: Tuple[Person, ...]) -> tuple:
        # aa = tuple(filter(lambda i: i.retirement == 0, x))
        aa = tuple(filter(working, x))
        return aa

    w = workers(group)
    known_workers = ["Charles", "Donna"]
    calc_workers = [x.name for x in w]
    assert known_workers == calc_workers

    # def retiree(p: Person) -> Retiree:
    #     if retired(p):
    #         return Retiree(name=p.name, degree=p.degree, retirement=p.retirement)

    # def worker(p: Person) -> Worker:
    #     return Worker(name=p.name, degree=p.degree)

    # a = tuple(map(retired, group))
    # b = tuple(filter(retired, group))
    # c = tuple(filter(working, group))

    # def retirees(g: Tuple[Person, ...]) -> tuple:
    #     return tuple(filter(retired, g))
    # def retirees(ps: Tuple[Person]) -> Generator:
    #     qq = (retiree(p) for p in ps)
    #     return qq

    # def workers(g: Tuple[Person, ...]) -> tuple:
    #     return tuple(filter(working, g))

    # w = workers(group)
    # known_workers = ["Charles", "Donna"]
    # calc_workers = [x.name for x in w]
    # assert known_workers == calc_workers

    # def experience(r: Retiree) -> int:
    #     return r.retirement - r.degree

    a = 4

    # def worker(p: Person_FP) -> Worker:
    #     return Worker(degree=p.degree)

    # def experience(r: Retiree) -> int:
    #     return r.retirement - r.degree

    # def experience(w: Worker, current_year: int) -> int:
    #     return current_year - w.degree

    # def retired_person(person: Person_FP) -> bool:
    #     return person.retirement is not None

    # known_retired_states = (True, True, False, False)
    # # the traditional approach
    # for g, s in zip(group, known_retired_states):
    #     assert retired_person(g) == s

    # # the more functional approach
    # calculated_retirement_states = tuple(map(retired_person, group))
    # assert known_retired_states == calculated_retirement_states

    # def working_person(person: Person_FP) -> bool:
    #     return not retired_person(person=person)

    # known_working_states = (False, False, True, True)
    # calculated_working_states = tuple(map(working_person, group))

    # assert known_working_states == calculated_working_states

    # def retiree_experience(p: Person_FP) -> int:
    #     return p.retirement - p.degree

    # def worker_experience(p: Person_FP, current_year: int) -> int:
    #     return current_year - p.degree

    # def retirees_experience(retirees: tuple) -> Tuple[int]:
    #     a = tuple(map(retiree_experience, retirees))
    #     return a

    # def workers_experience(workers: tuple, current_year: int) -> Tuple[int]:
    #     b = tuple(map(worker_experience(workers, current_year), workers))
    #     return b

    r = retirees(group)
    w = workers(group)

    # def experience(person: Person_FP, current_year: int) -> int:
    #     retirees = map(retiree, group)

    #     retirees_experience = sum(filter(retired_person, group))
    #     assert retirees_experience == 30

    #     workers_experience = sum(filter(working_person, group))
    #     assert workers_experience == 28

    #     return sum(filter(retired_person, group)) + sum(filter(working_person, group))

    # assert experience == 42

    a = 4

    # def experience(person: Person_FP) -> int:


def main():
    test_OOP()
    test_FP()


if __name__ == "__main__":
    main()
