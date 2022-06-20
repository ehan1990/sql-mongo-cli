import readline
import shlex
from pymongo import MongoClient
from smc.libs.constants import *


class Command:

    CMD_MAP = None
    db = None

    @classmethod
    def init(cls):
        cls.CMD_MAP = {
            SHOW_DBS: cls.show_dbs,
            SHOW_COLS: cls.show_cols,
            USE_DB: cls.use_dbs,
            SELECT: cls.select,
            DELETE: cls.delete
        }
        cls.db = None

    @classmethod
    def parse(cls, cmd, args, mongo_client):
        if cmd == "exit":
            return (None, 0)
        else:
            q = f'{cmd} {" ".join(args)}'
            cls.parse_cmd(q, mongo_client)
            return (q, None)

    @classmethod
    def parse_cmd(cls, q, mongo_client):
        for cmd, f in cls.CMD_MAP.items():
            if q == cmd:
                f(q, mongo_client)
            elif q.split()[0] == cmd:
                f(q, mongo_client)

    @classmethod
    def show_dbs(cls, q, mongo_client):
        cursor = mongo_client.list_databases()
        for db in cursor:
            print(db)

    @classmethod
    def show_cols(cls, q, mongo_client):
        db = mongo_client[cls.db]
        collection = db.list_collection_names()
        for collect in collection:
            print(collect)

    @classmethod
    def use_dbs(cls, q, mongo_client):
        cls.db = q.split()[1]
        print(f"using db {cls.db}")

    @classmethod
    def select(cls, q, mongo_client):
        col_name = q.split()[-1]
        db = mongo_client[cls.db]
        col = db[col_name]
        for item in col.find():
            print(item)

    @classmethod
    def delete(cls, q, mongo_client):
        # delete from table where key=foo
        col_name = q.split()[2]
        cond = q.split()[-1]
        key = cond.split("=")[0]
        val = cond.split("=")[-1]
        q = {key: val}

        db = mongo_client[cls.db]
        col = db[col_name]
        col.delete_one(q)
        print(f"deleted {q}")


def main():
    mongo_client = MongoClient('localhost', 27017)
    Command.init()
    print('Enter a command to do something, e.g. `create name price`.')
    print('To get help, enter `help`.')

    while True:
        cmd, *args = shlex.split(input('> '))
        q, exit = Command.parse(cmd, args, mongo_client)

        if exit is None:
            continue
        if exit == 0:
            break


if __name__ == "__main__":
    main()


