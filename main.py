import json


def json_indent(filepath):
    handler = read_a_file(filepath)
    filename = filename_only(filepath)
    path = path_only(filepath)
    file = open(path + filename + "_formatted.json", "w")
    file.write(json.dumps(json.load(handler), sort_keys=True, indent=4))
    file.close()


def read_a_file(filepath):
    content = open(filepath, "r")
    return content


def take_file_location_input():
    x = input("Provide file location:")
    return x


def filename_only(filepath):
    split_arr = filepath.split("/")
    count = len(split_arr)
    filename = split_arr[count-1].split(".")
    return filename[0]


def path_only(filepath):
    return '/'.join(filepath.split('/')[0:-1])+'/'


if __name__ == '__main__':
    filepath = take_file_location_input()
    json_indent(filepath)
