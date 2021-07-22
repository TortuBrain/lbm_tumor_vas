# IMPORTS PACKAGES
import numpy as np


def euclidian_distance_two_points(point_a, point_b) -> float:
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
    distance = np.linalg.norm(point_a - point_b)
    return distance


def distance_points_array(points) -> float:
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


def tortuosity_geometric_streamline(streamline_points) -> float:
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
    return distance_points_array(streamline_points) / distance_across


def tortuosity_geometric(streamlines) -> float:
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
    if len(streamlines) > 1:
        length_streamlines = len(streamlines)
        tau_geometric = 0
        for streamline in streamlines:
            if streamline.shape[0] > 1:
                tau_geometric += tortuosity_geometric_streamline(streamline)
        return tau_geometric / length_streamlines
    return 0.0
