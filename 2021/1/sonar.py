"""
    Day 1 - Sonar

"""


def sonar(fpath):

    # Load input
    reading = load_input(fpath)

    # Algo
    status = []
    for ix, depth in enumerate(reading):
        if ix > 0:
            last_depth = reading[ix-1]
            if last_depth < depth:
                status.append("Increased")
            elif last_depth > depth:
                status.append("Decreased")
            else:
                status.append("Same")
        else:
            status.append("X")
        print("{} - {}".format(reading[ix], status[ix]))
    tot_inc = status.count("Increased")
    print("##########")
    print("Total Increased: {}".format(tot_inc))


def load_input(fpath):
    with open(fpath, "r") as f:
        reading = [int(x) for x in list(f.read().split("\n"))]

    return reading


if __name__ == "__main__":
    # Choose input
    input_file = r"input_test_2.txt"

    # Run
    sonar(input_file)