"""
    Day 25 - Sea Cucumbers

"""


def sea_cucumbers(fpath, max_steps=5):

    # Load input
    in_map = load_input(fpath)
    x_lim = len(in_map[0])
    y_lim = len(in_map)
    print("########## Input map:")
    for row in in_map:
        print("".join(row))

    # Algo
    step_count = 0
    next_step_possible = True
    cur_map = in_map.copy()
    while next_step_possible:
        step_count += 1
        next_step_possible, cur_map = run_step(cur_map, x_lim, y_lim)
        print("########## Step {}: ".format(step_count))
        # Print map
        for row in cur_map:
            print("".join(row))
        if step_count > max_steps:
            break

    # Output steps
    print("########## Done")
    print("Number of steps: {}".format(step_count))
    return step_count


def load_input(fpath):
    with open(fpath, "r") as f:
        in_map = [list(row) for row in f.read().split("\n")]
    return in_map


def run_step(cur_map, x_lim, y_lim):
    # Copy current map
    next_map = deepcopy(cur_map)
    east_move_counter = 0
    south_move_counter = 0
    # Move east herd
    for y_ix in range(y_lim):
        for x_ix in range(x_lim):
            # Check if east cucumber
            if cur_map[y_ix][x_ix] == ">":
                # Get next east position
                next_x = x_ix + 1
                if next_x == x_lim:
                    next_x = 0
                # Move cucumber is next position is empty
                if cur_map[y_ix][next_x] == ".":
                    next_map[y_ix][x_ix] = "."
                    next_map[y_ix][next_x] = ">"
                    east_move_counter += 1
    # Update map
    cur_map = deepcopy(next_map)
    # Move south herd
    for y_ix in range(y_lim):
        for x_ix in range(x_lim):
            # Check if south cucumber
            if cur_map[y_ix][x_ix] == "v":
                # Get next south position
                next_y = y_ix + 1
                if next_y == y_lim:
                    next_y = 0
                # Move cucumber is next position is empty
                if cur_map[next_y][x_ix] == ".":
                    next_map[y_ix][x_ix] = "."
                    next_map[next_y][x_ix] = "v"
                    south_move_counter += 1
    # Check moves
    if east_move_counter + south_move_counter == 0:
        return False, next_map
    else:
        return True, next_map


if __name__ == "__main__":
    
    # Choose input
    input_file = r"input_test_4.txt"

    # Run
    sea_cucumbers(input_file, max_steps=100000)
