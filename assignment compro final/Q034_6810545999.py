# Name: Inthat # Student ID: 68010545999

from math import pi
from pathlib import Path


def file_exists(filename):
    file_path = Path(filename)
    if not file_path.exists():
        print(f"Error: {filename} not found.\n")
        return False
    return True


def print_summary(circle_count, rectangle_count, square_count, total_shapes, total_area, filename=""):
    if filename != "":
        title = f"Report for {filename}"
    else:
        title = "Grand Total"

    if filename == "":
        shapes_label = "Total shapes:"
    else:
        shapes_label = "Shapes:"

    if filename == "":
        overall_prefix = "overall "
    else:
        overall_prefix = ""

    print(f"--- {title} ---")
    print(f"{shapes_label}")
    print(f"  circle: {circle_count}")
    print(f"  rectangle: {rectangle_count}")
    print(f"  square: {square_count}")
    print(f"Total {overall_prefix}shapes: {total_shapes}")
    print(f"Total {overall_prefix}area: {total_area:.2f}")
    print("-------------------")


def valid_format(data_list):
    if not data_list:
        return False

    s = data_list[0]
    if s not in ["circle", "rectangle", "square"]:
        return False

    try:
        if s == "circle" and len(data_list) == 2:
            float(data_list[1])
            return True
        elif s == "rectangle" and len(data_list) == 3:
            float(data_list[1])
            float(data_list[2])
            return True
        elif s == "square" and len(data_list) == 2:
            float(data_list[1])
            return True
    except (ValueError, IndexError):
        return False

    return False


def get_shape_parameters(data_list):
    try:
        shape = data_list[0]
        num_1 = float(data_list[1])
        if len(data_list) > 2:
            num_2 = float(data_list[2])
        else:
            num_2 = None
    except (ValueError, IndexError):
        return None, None, None
    return shape, num_1, num_2


def update_data(shape, area):
    if shape == "circle":
        local_data["circle_count"] += 1
        grand_data["circle_count"] += 1
    elif shape == "rectangle":
        local_data["rectangle_count"] += 1
        grand_data["rectangle_count"] += 1
    elif shape == "square":
        local_data["square_count"] += 1
        grand_data["square_count"] += 1

    local_data["total_shapes"] += 1
    local_data["total_area"] += area
    grand_data["total_shapes"] += 1
    grand_data["total_area"] += area


grand_data = {
    "circle_count": 0,
    "rectangle_count": 0,
    "square_count": 0,
    "total_shapes": 0,
    "total_area": 0
}

if file_exists("index.txt"):
    with open("index.txt", "r", encoding="utf-8") as file:
        file_lines = file.readlines()

    for filename_line in file_lines:
        filename = filename_line.strip()

        if not filename:
            continue

        if not file_exists(filename):
            continue

        print(f"Processing file: {filename}")

        with open(Path(filename), "r", encoding="utf-8") as shape_file:
            shape_lines = shape_file.readlines()

        local_data = {
            "circle_count": 0,
            "rectangle_count": 0,
            "square_count": 0,
            "total_shapes": 0,
            "total_area": 0
        }

        for line in shape_lines:
            data = line.split()
            if not data:
                continue

            if valid_format(data):
                shape, num_1, num_2 = get_shape_parameters(data)

                if shape is None:
                    print(f"Error on line: {line}", end="")
                    continue

                if shape == "circle":
                    area = pi * (num_1 ** 2)  # type: ignore
                elif shape == "rectangle":
                    area = num_1 * num_2  # type: ignore
                elif shape == "square":
                    area = num_1 ** 2  # type: ignore

                update_data(shape, area)
            else:
                print(f"Error on line: {line}", end="")

        print_summary(
            local_data["circle_count"],
            local_data["rectangle_count"],
            local_data["square_count"],
            local_data["total_shapes"],
            local_data["total_area"],
            filename
        )
        print()

    print_summary(
        grand_data["circle_count"],
        grand_data["rectangle_count"],
        grand_data["square_count"],
        grand_data["total_shapes"],
        grand_data["total_area"]
    )