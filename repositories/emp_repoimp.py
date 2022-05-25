from utils.trms_conn import trms_con
from exceptions.resource_notfound import ResourceNotFound
from models.trms_classes import Employees
from repositories.emp_repo import TRMSRepo


def _build_movie(record):
    if record:
        return Employees(emp_id=record[0], name=record[1], supervisor_id=record[2],
                         sup_name=record[3], dept_id=record[4], designation=record[5],
                         email=record[6])
    else:
        return None


class ReimburseImp(TRMSRepo):

    def create_data(self, empl):
        sql = 'insert into employees values (%s, %s, %s, %s, %s, %s, %s) returning *'
        cursor = trms_con.cursor()
        cursor.execute(sql, [empl.emp_id, empl.name, empl.supervisor_id, empl.sup_name, empl.dept_id, empl.designation,
                             empl.email])
        trms_con.commit()
        data_e = cursor.fetchone()
        return _build_movie(data_e)

    def get_details(self, id):
        sql = 'select * from employees where emp_id = %s'
        cursor = trms_con.cursor()
        cursor.execute(sql, [id])
        data_g = cursor.fetchone()

        if data_g:
            return Employees(emp_id=str(data_g[0]), name=data_g[1], supervisor_id=data_g[2],
                             sup_name=data_g[3], dept_id=str(data_g[4]), designation=data_g[5],
                             email=data_g[6])
        else:
            raise ResourceNotFound(f"This employee id {id} is not available")

    def get_all(self):
        sql = "Select * from employees"
        cursor = trms_con.cursor()
        cursor.execute(sql)

        records = cursor.fetchall()
        emp_list = [_build_movie(record) for record in records]
        return emp_list


def _test():
    e = ReimburseImp()
    eg = e.get_details(11)
    print(eg)
    print(e.get_all())


if __name__ == '__main__':
    _test()
