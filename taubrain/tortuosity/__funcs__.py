import numpy as np


def euclidian_distance_two_points(point_a, point_b) -> float:
    distance = np.linalg.norm(point_a - point_b)
    return distance


def distance_points_array(points) -> float:
    distance = 0
    for position_point in range(len(points) - 1):
        distance += euclidian_distance_two_points(
            points[position_point], points[position_point + 1]
        )
    return distance


def tortuosity_geometric_streamline(streamline_points) -> float:
    distance_across = euclidian_distance_two_points(
        streamline_points[0], streamline_points[-1]
    )
    return distance_points_array(streamline_points) / distance_across


def tortuosity_geometric(streamlines) -> float:
    if len(streamlines) > 1:
        length_streamlines = len(streamlines)
        tau_geometric = 0
        for streamline in streamlines:
            if streamline.shape[0] > 1:
                tau_geometric += tortuosity_geometric_streamline(streamline)
        return tau_geometric / length_streamlines
    return 0.0
