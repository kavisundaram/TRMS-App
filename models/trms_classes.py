class Employees:

    def __init__(self, emp_id, name, supervisor_id, sup_name, dept_id, designation, email):
        self.emp_id = emp_id
        self.name = name
        self.supervisor_id = supervisor_id
        self.sup_name = sup_name
        self.dept_id = dept_id
        self.designation = designation
        self.email = email

    def __repr__(self):
        return str(
            {
                "Employee_ID": self.emp_id,
                "Employee_Name": self.name,
                "Supervisor-ID": self.supervisor_id,
                "Supervisor_Name" : self.sup_name,
                "Department": self.dept_id,
                "Designation": self.designation,
                "Email": self.email
            }
        )

    def json(self):
        return {
                "Employee_ID": self.emp_id,
                "Employee_Name": self.name,
                "Supervisor_ID": self.supervisor_id,
                "Supervisor_Name": self.sup_name,
                "Department": self.dept_id,
                "Designation": self.designation,
                "Email": self.email
            }


class ReimburseStatus:

    def __init__(self, eid, e_name, s_name, dept, course, price, grade, amt, email_add):
        self.eid = eid
        self.e_name = e_name
        self.s_name = s_name
        self.dept = dept
        self.course = course
        self.price = price
        self.grade = grade
        self.amt = amt
        self.email_add = email_add

    def __repr__(self):
        return str(
            {
                "Employee_ID": self.eid,
                "Employee_Name": self.e_name,
                "Supervisor_Name" : self.s_name,
                "Department": self.dept,
                "Course_Type": self.course,
                "Price": self.price,
                "Grade_Received": self.grade,
                "Amount left for Reimb": self.amt,
                "Email": self.email_add
            }
        )

    def json(self):
        return {
                "Employee_ID": self.eid,
                "Employee_Name": self.e_name,
                "Supervisor_Name" : self.s_name,
                "Department": self.dept,
                "Course_Type": self.course,
                "Price": self.price,
                "Grade_Received": self.grade,
                "Amount left for Reimb": self.amt,
                "Email": self.email_add
            }
