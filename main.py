import json


def json_indent(file_path):
    handler = read_a_file(file_path)
    filename = filename_only(file_path)
    path = path_only(file_path)
    file = open(path + filename + "_formatted.json", "w")
    file.write(json.dumps(json.load(handler), sort_keys=True, indent=4))
    file.close()


def read_a_file(file_path):
    content = open(file_path, "r")
    return content


def take_file_location_input():
    x = input("Provide file location:")
    return x


def filename_only(file_path):
    split_arr = file_path.split("/")
    count = len(split_arr)
    filename = split_arr[count-1].split(".")
    return filename[0]


def path_only(file_path):
    return '/'.join(file_path.split('/')[0:-1])+'/'


if __name__ == '__main__':
    filepath = take_file_location_input()
    json_indent(filepath)
