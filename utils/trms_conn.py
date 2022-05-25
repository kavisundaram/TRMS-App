import psycopg2
from psycopg2 import OperationalError


def create_connection():
    try:
        conec = psycopg2.connect(
            database="trms_db",
            user="postgres",
            password="eLsUvQPPo589VtizFudl",
            host="database-3.cix9g4y5vem2.us-east-2.rds.amazonaws.com",
            port="5432"
        )
        return conec
    except OperationalError as e:
        print(e)
        return None


trms_con = create_connection()


def _test():
    print(trms_con)


if __name__ == '__main__':
    _test()
