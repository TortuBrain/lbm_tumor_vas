import numpy as np
from scipy.spatial import distance
from tabulate import tabulate
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

    if streamline_points.shape[0] == 1:
        return 1.00
    distance_across = euclidian_distance_two_points(
        streamline_points[0], streamline_points[-1]
    )
    line = distance_points_array(streamline_points)

    tau = line * (1 / distance_across)

    if tau <= 1.0:
        tau = 1.0
    return tau


def _print_result_tau(tau_final, tau_final_backward, tau_final_onward) -> None:
    """
    Print the result of the geometric tortuosity
    """

    table = [
        ["Tortuosity Mean", tau_final],
        ["Tortuosity Backward", tau_final_backward],
        ["Tortuosity Onward", tau_final_onward],
    ]
    print(tabulate(table, headers=["\033[1mProperties", "\033[1mResult\033[0m"]))


def distance_points_backward_and_onward(points):
    points_reverse = points[::-1]
    number_section = math.floor(points.shape[0] * 0.25)
    tau_onward = []
    tau_backward = []
    if number_section >= 1:
        onward = [
            points[i : i + number_section]
            for i in range(0, len(points), number_section)
        ]
        backward = [
            points_reverse[i : i + number_section]
            for i in range(0, len(points_reverse), number_section)
        ]
        for stream in onward:
            tau_onward.append(tortuosity_geometric_streamline(stream))
        for stream in backward:
            tau_backward.append(tortuosity_geometric_streamline(stream))
        final = np.array(tau_onward) + np.array(tau_backward)
        return final / 2, np.array(tau_onward), np.array(tau_backward)
    return np.array([1.00])


def tortuosity_geometric_track(streamlines) -> float:
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
    tau_geometric_mean = 0
    tau_geometric_backward = 0
    tau_geometric_onward = 0
    length_streamlines = len(streamlines)
    if length_streamlines > 1:
        tau_geometric = 0
        for stream in streamlines:
            if stream.shape[0] >= 2:
                tau = distance_points_backward_and_onward(stream)
                if len(tau) == 3:
                    tau_geometric_mean += tau[0].mean()
                    tau_geometric_backward += tau[1].mean()
                    tau_geometric_onward += tau[2].mean()
                else:
                    length_streamlines -= 1
            else:
                length_streamlines -= 1
        tau_final_mean = tau_geometric_mean / length_streamlines
        tau_final_backward = tau_geometric_backward / length_streamlines
        tau_final_onward = tau_geometric_backward / length_streamlines
        _print_result_tau(tau_final_mean, tau_final_backward, tau_final_onward)
        return tau_final_mean, tau_final_backward, tau_final_onward
    return 0.0
