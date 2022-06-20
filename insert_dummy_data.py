import json
import pymongo


def read_userdata():
    with open("testdata/userdata.json") as f:
        data = json.loads(f.read())
    return data


def main():
    mongo_client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = mongo_client["foobar"]
    userdata_col = db["userdata"]

    data = read_userdata()

    res = userdata_col.insert_many(data)
    print(res.inserted_ids)


if __name__ == "__main__":
    main()
