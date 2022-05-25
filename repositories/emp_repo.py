from abc import ABC
from models.trms_classes import Employees

from utils.trms_db import TRMSdb as td


class TRMSRepo(ABC):

    def create_data(self, empl):
        td.emp[empl.emp_id] = empl

    def get_details(self, id):
        return td.emp[id]

    def get_all(self):
        return td.emp


def _test():
    tr = TRMSRepo()
    tr.create_data(Employees(emp_id=9, name='Tony Brown', supervisor_id=19, sup_name='Neil Burrell', dept_id=112,
                             designation='Cloud Security Specialist', email='brown44.tony@gmail.com'))
    print(td.emp)
    ga = TRMSRepo()
    print(ga.get_details(9))
    print(ga.get_all())


if __name__ == '__main__':
    _test()
