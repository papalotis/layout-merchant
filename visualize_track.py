import json
from pathlib import Path

try:
    import matplotlib.pyplot as plt
except ImportError:
    print("Matplotlib not found. Please install it to visualize the track.")
    raise SystemExit(1)

import numpy as np  # matplotlib depends on numpy so if we have matplotlib we have numpy

INDEX_TO_COLOR = ["black", "gold", "blue", "orange", "red"]


def visualize_cones(path: Path):
    path = Path(path)
    if not path.exists():
        print(f"Path {path} does not exist.")
        return

    data = json.loads(path.read_text())

    _, ax = plt.subplots()

    if "start_orientation" in data:

        heading_rad = np.deg2rad(data["start_oritenation"])

        n = 3

        ax.arrow(
            data["start_position"][0],
            data["start_position"][1],
            np.cos(heading_rad) * n,
            np.sin(heading_rad) * n,
            head_width=1.5,
            head_length=1,
            fc="k",
            ec="k",
        )

    # visualize the timing line
    heading_angle = np.deg2rad(data["timing_line_oritenation"]) + np.pi / 2
    heading = np.array([np.cos(heading_angle), np.sin(heading_angle)])

    width = data["timing_line_width"]
    point_1_timing_line = np.array(data["timing_line_position"]) + heading * width / 2
    point_2_timing_line = np.array(data["timing_line_position"]) - heading * width / 2

    ax.plot(
        [point_1_timing_line[0], point_2_timing_line[0]],
        [point_1_timing_line[1], point_2_timing_line[1]],
        "k",
    )

    cones = np.column_stack((data["x"], data["y"]))

    ax.scatter(cones[:, 0], cones[:, 1], c=[INDEX_TO_COLOR[x] for x in data["color"]])

    ax.set_title(f"{path.stem}: {len(cones)} cones")

    plt.axis("equal")
    plt.show()


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("path", type=Path, help="Path to the json file.")
    args = parser.parse_args()

    visualize_cones(args.path)
