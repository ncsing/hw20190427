import math


def get_burette_capacity_as_list(filename):
    with open(filename) as f:
        content = f.readlines()
    # you may also want to remove whitespace characters like `\n` at the end of each line
    return [x.strip() for x in content]


if __name__ == "__main__":

    # Get Data
    filename = "burette.txt"
    burettes = get_burette_capacity_as_list(filename)

    # Data Transform
    burettes_float = [float(item) for item in burettes]
