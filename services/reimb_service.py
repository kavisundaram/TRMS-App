from repositories.reimb_repo import TRMSReimbRepo


class TRMSReimbService:

    def __init__(self, reimb_repo: TRMSReimbRepo):
        self.reimb_repo = reimb_repo

    def sub_data(self, ri):
        return self.reimb_repo.sub_data(ri)

    def get_reim(self, id):
        return self.reimb_repo.get_reim(id)


def _test():
    trim: TRMSReimbRepo() = TRMSReimbRepo()
    trims: TRMSReimbService() = TRMSReimbService(trim)
    print(trims.get_reim(1))


if __name__ == '__main__':
    _test()
