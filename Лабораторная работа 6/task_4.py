import json

INPUT_FILE = "input.csv"
# TODO реализовать конвертер из csv в json


def csv_to_list_dict(file) -> list[dict]:
    with open(file) as f:
        list_ = []
        header = f.readline()[:-1].split(",")
        for n in f:
            info = n[:-1].split(',')
            dict_result = dict(zip(header, info))
            list_.append(dict_result)

    return list_


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
