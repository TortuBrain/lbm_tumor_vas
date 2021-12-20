from scipy.spatial import distance
from nibabel.streamlines.array_sequence import ArraySequence
from scipy.spatial import distance
from math import sqrt
from numba.core.decorators import njit
from numba import jit
import numpy as np

def euclidian_distance_two_points(point_a, point_b):
    return distance.euclidean(point_a, point_b)

def euclidian_distance_array_points(points):
    d = np.diff(points, axis=0)
    return np.sum(np.sqrt((d ** 2).sum(axis=1)))

def tortuosity_section(streamline,section_index ):
    return euclidian_distance_array_points(streamline[0:section_index+2])/euclidian_distance_two_points(streamline[0], streamline[section_index + 1])

def tortuosity_streamline(streamline):
    tortuosity_for_each_section = []
    for i in range(len(streamline) - 1):
            tortuosity_for_each_section.append(tortuosity_section(streamline, i))
    return tortuosity_for_each_section



def tortuosity(streamlines):
    tortuosity_streamlines= ArraySequence()
    for streamline in streamlines:
        tortuosity_streamlines.append(tortuosity_streamline(streamline))
    return tortuosity_streamlines
#            __
#           / _)
#    .-^^^-/ /
# __/       /
# <__.|_|-|_| -> octajos
