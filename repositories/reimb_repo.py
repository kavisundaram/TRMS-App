from abc import ABC
from models.trms_classes import ReimburseStatus

from utils.trms_db import TRMSdb as td


class TRMSReimbRepo(ABC):

    def sub_data(self, reimb):
        td.reim[reimb.eid] = reimb

    def get_reim(self, id):
        return td.reim[id]


def _test():
    trr = TRMSReimbRepo()
    trr.sub_data(ReimburseStatus(eid=9, e_name='Tony Brown', s_name='Neil Burrell', dept=112,
                                 course='Technical Training', price=500, grade=75.00, amt=300,
                                 email_add='brown44.tony@gmail.com'))
    print(td.reim)
    ga = TRMSReimbRepo()
    print(ga.get_reim(9))
    # print(ga.get_all())


if __name__ == '__main__':
    _test()
