from scipy.spatial import distance
from nibabel.streamlines.array_sequence import ArraySequence
from scipy.spatial import distance
from math import sqrt
from numba.core.decorators import njit
import taubrain as tb
from numba import jit
import numpy as np

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


@jit(nopython=True)
def find(x, y, p):
	mind = 0
	for i in range(len(p)):
		a = p[i][0]
		b = p[i][1]
		mind += sqrt((x - a) * (x - a) +
					(y - b) * (y - b))			
	return mind

@jit(nopython=True)
def euclidian_distance_array_points(p):
	x = 0
	y = 0
	
	for i in range(len(p)):
		x += p[i][0]
		y += p[i][1]
	x = x // len(p)
	y = y // len(p)
	mind = find(x, y, p)

	return mind

def tortuosity_array_points(points):
    array_euclian_distance = []
    for i in range(len(points)-1):
        distance_euclidian_L = euclidian_distance_two_points(points[0], points[i+1])
        tortuosity_in_point=euclidian_distance_array_points(points[0:i+1])/distance_euclidian_L
        if (tortuosity_in_point > 0):
            array_euclian_distance.append(tortuosity_in_point)
        else:
         array_euclian_distance.append(1.0000000)
        
    return np.array(array_euclian_distance)
        


def stream_tortuosity(streamlines):

    """
    Calculate the tortuosity of a streamline
    Parameters
    ----------
    streamline : list
        The streamline
    Returns
    -------
    array
        The tortuosity of the streamline
    """
    tortuosity_streamline= ArraySequence()
    for streamline in streamlines:
        tortuosity_streamline.append(tortuosity_array_points((streamline)))
    return tortuosity_streamline
#            __
#           / _)
#    .-^^^-/ /
# __/       /
# <__.|_|-|_| -> octajos
