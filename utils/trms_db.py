from models.trms_classes import Employees, ReimburseStatus


class TRMSdb():
    emp = {
        1: Employees(emp_id=8, name='Fahim Jordan', supervisor_id=16, sup_name='Claire Shelby', dept_id=111,
                     designation='Software Developer', email='shelby_01claire@outlook.com')
    }

    reim = {
        1: ReimburseStatus(eid=8, e_name="Fahim Jordan", s_name='Claire Shelby', dept=111,
                           course='Seminars', price=350, grade=78.2, amt=700, email_add='shelby01_claire@outlook.com')
    }