import numpy as np
from scipy.spatial import distance
import math


def euclidian_distance_two_points(point_a, point_b):
    """
    Find the Euclidean distance between two points
    d(x,y)lim_r->2(∑|x_k-y_k|^r)^(1/r)
    Parameters
    ----------
    point_a : int
        Starting point
    point_b : int
        End point
    Returns
    -------
    float
        The distance between two points
    """
    return distance.euclidean(point_a, point_b)


def distance_points_array(points):
    """
    Euclidean distance between a list of points
    Parameters
    ----------
    points : array
        A list of points in 3D
    Returns
    -------
    float
        The distance between all points in the array
    """
    distance = 0
    for position_point in range(len(points) - 1):
        distance += euclidian_distance_two_points(
            points[position_point], points[position_point + 1]
        )

    return distance


def tortuosity_geometric_streamline(streamline_points):
    """
    Geometric tortuosity of a streamline
        π=distance_points_array/distance_across
    Parameters
    ----------
    streamline_points : array
        A array of points belonging to a streamline
    Returns
    -------
    float
        Geometric tortuosity of a streamline
    """
    distance_across = euclidian_distance_two_points(
        streamline_points[0], streamline_points[-1]
    )
    tau = distance_points_array(streamline_points) * (1 / distance_across)
    if tau <= 1.0:
        tau = 1.0
    return tau


def _print_result_tau(value_tau) -> None:
    """
    Print the result of the geometric tortuosity
    """
    print(f'Results\n{"="*10}\ntortuosity:{value_tau}')


def tortuosity_geometric(streamlines, output="steam_tg.csv") -> float:
    """
    Geometric tortuosity a list of streamlines.
    It is the average of the geometric tortuosity for each streamline
        π=∑tortuosity_geometric_streamline_i/lenght(streamlines)

    Parameters
    ----------
    streamlines : array
        A list of streamlines
    Returns
    -------
    float
        Average geometric tortuosity of all streamlines
    """
    file = open("steam_tg.csv", "w")
    file.write("stream_length,tau \n")
    length_streamlines = len(streamlines)
    if length_streamlines > 1:
        tau_geometric = 0
        number = 0
        for streamline in streamlines:
            if streamline.shape[0] > 1:
                tau = tortuosity_geometric_streamline(streamline)
                tau_geometric += tau
                file.write(f"{streamline.size/3},{tau} \n")
                number += 1
        tau_final = tau_geometric / length_streamlines
        _print_result_tau(tau_final)
        return tau_final
    return 0.0


def distance_points_backward_and_onward(points):
    points_reverse = points[::-1]
    number_section = math.floor(line1.shape[0] * 0.25)
    onward = [
        points[i : i + number_section] for i in range(0, len(points), number_section)
    ]
    backward = [
        points_reverse[i : i + number_section]
        for i in range(0, len(points_reverse), number_section)
    ]
    tau_onward = []
    tau_backward = []

    for stream in onward:
        tau_onward.append(tortuosity_geometric_streamline(stream))
    for stream in backward:
        tau_backward.append(tortuosity_geometric_streamline(stream))
    return tau_onward, tau_backward
