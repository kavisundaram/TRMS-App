from repositories.emp_repo import TRMSRepo


class TRMSService:

    def __init__(self, emp_repo: TRMSRepo):
        self.emp_repo = emp_repo

    def create_data(self, el):
        return self.emp_repo.create_data(el)

    def get_details(self, id):
        return self.emp_repo.get_details(id)

    def get_all(self):
        return self.emp_repo.get_all()


def _test():
    tr: TRMSRepo() = TRMSRepo()
    ts: TRMSService() = TRMSService(tr)
    print(ts.get_all())
    print(ts.get_details(1))


if __name__ == '__main__':
    _test()
