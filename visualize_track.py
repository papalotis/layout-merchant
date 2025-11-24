"""Visualization tool for Formula Student Driverless track layouts.

This module provides functionality to visualize track layouts stored as JSON files.
The tracks contain cone positions, colors, start positions, and timing line information.
"""

# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "matplotlib",
#     "numpy",
#     "typer",
# ]
# ///
import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import typer

INDEX_TO_COLOR = ["black", "gold", "blue", "orange", "red"]


def visualize_cones(path: Path):
    """Visualize cone positions and track features from a JSON layout file.

    This function reads a track layout JSON file and creates a matplotlib visualization
    showing cone positions (colored by type), the start position with orientation arrow,
    and the timing line.

    Args:
        path: Path to the JSON file containing the track layout data. The file must
            contain keys: 'x', 'y', 'color', 'start_position', 'start_orientation',
            'timing_line_position', 'timing_line_orientation', and 'timing_line_width'.

    Returns:
        None. Displays the plot using matplotlib.pyplot.show().

    Note:
        Cone colors are mapped as follows:
        0: unknown (black), 1: yellow (gold), 2: blue, 3: orange_small (orange),
        4: orange_big (red).
    """
    path = Path(path)
    if not path.exists():
        print(f"Path {path} does not exist.")
        return

    data = json.loads(path.read_text())

    _, ax = plt.subplots()

    if "start_orientation" in data:
        heading_rad = np.deg2rad(data["start_orientation"])

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
    heading_angle = np.deg2rad(data["timing_line_orientation"]) + np.pi / 2
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


def main(path: Path):
    """Visualize a track from the repository.

    Entry point for the command-line interface to visualize Formula Student
    Driverless track layouts.

    Args:
        path: Path to the JSON file containing the track layout to visualize.
    """
    visualize_cones(path)


if __name__ == "__main__":
    typer.run(main)
