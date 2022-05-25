from utils.trms_conn import trms_con
from exceptions.resource_notfound import ResourceNotFound
from models.trms_classes import ReimburseStatus
from repositories.reimb_repo import TRMSReimbRepo


def _build_reimb(record):
    if record:
        return ReimburseStatus(eid=record[0], e_name=record[1], s_name=record[2],
                               dept=record[3], course=record[4], price=float(record[5]),
                               grade=float(record[6]), amt=float(record[7]), email_add=record[8])
    else:
        return None


class ReimbImp(TRMSReimbRepo):

    def sub_data(self, reimb):
        sql = 'insert into reimburse values (%s, %s, %s, %s, %s, %s, %s, %s, %s) returning *'
        cursor = trms_con.cursor()
        cursor.execute(sql, [reimb.eid, reimb.e_name, reimb.s_name, reimb.dept, reimb.course,
                             reimb.price, reimb.grade, reimb.amt, reimb.email_add])
        trms_con.commit()
        data_e = cursor.fetchone()
        return _build_reimb(data_e)

    def get_reim(self, id):
        sql = 'select * from reimburse where eid = %s'
        cursor = trms_con.cursor()
        cursor.execute(sql, [id])
        data_g = cursor.fetchone()

        if data_g:
            return ReimburseStatus(eid=str(data_g[0]), e_name=data_g[1], s_name=data_g[2],
                                   dept=data_g[3], course=str(data_g[4]), price=data_g[5],
                                   grade=data_g[6], amt=data_g[7], email_add=data_g[8])
        else:
            raise ResourceNotFound(f"This employee id {id} is not available")


def _test():
    tri = TRMSReimbRepo()
    print(tri.get_reim(1))
    # e1 = Employees(emp_id=10, name='Blake Reynolds', supervisor_id=20, sup_name='George Willis', dept_id=114, designation='HR Assistant', email= 'blake1985@gmail.com')
    # e.create_data(e1)
    # eg = e.get_details(11)
    # print(eg)
    # print(e.get_all())


if __name__ == '__main__':
    _test()
