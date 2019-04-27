import math


def get_burette_capacity_as_list(filename):
    with open(filename) as f:
        content = f.readlines()
    # you may also want to remove whitespace characters like `\n` at the end of each line
    return [x.strip() for x in content]


def sample_standard_deviation(number_list):
    data_length = len(number_list)
    data_mean = calculate_mean(number_list)
    normalized_list = [(item - data_mean) for item in number_list]
    squared_deviation = [(item * item) for item in normalized_list]
    variance = sum(squared_deviation) / (data_length - 1)
    return math.sqrt(variance)


def calculate_mean(number_list):
    data_length = len(number_list)
    return sum(number_list) / data_length


def correcting_recording_bug(number_list):
    # For every 10th volume data, the data point is 10 times larger than it should be
    return [(number_list[i] / 10) if (i + 1) % 10 == 0 else number_list[i] for i in range(len(number_list))]


if __name__ == "__main__":

    # Get Data
    filename = "burette.txt"
    burettes = get_burette_capacity_as_list(filename)

    # Data Transform
    burettes_float = [float(item) for item in burettes]

    # a
    q1 = sample_standard_deviation(burettes_float)
    print("a. Without correcting the recording bug, the standard deviation of the data is ")
    print(q1)

    # b
    corrected_burettes_float = correcting_recording_bug(burettes_float)
    q2 = sample_standard_deviation(corrected_burettes_float)
    print("b. After correcting the recording bug, the standard deviation of the data is ")
    print(q2)
