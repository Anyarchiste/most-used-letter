"""Asks for the input file path and outputs a string only with letters in lowercase and punctuation"""


# Asks the user to give the file path
# C:\Users\prive\Documents\Bk-Up\GitHub\most-used-letter-french\test.txt
def get_file_path():
    return input("Provide the full path to a .txt file: ")


# Reads the file and outputs it as a list
def read_file(path_def):
    with open(path_def, "r") as f:
        raw_data = f.readlines()
        return raw_data


# Takes a list and turns it in one string without "\n" or " "
def get_string(f):
    string = ""
    for x in range(len(f)):
        t = f[x].replace("\n", "")
        r = t.replace(" ", "")
        string = string + r
    return string


def parse_file(raw_data):
    data = get_string(raw_data)
    return data


def main():
    path = get_file_path()
    file = read_file(path)
    data = parse_file(file)
    return data
