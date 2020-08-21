import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import itertools

size = 50
alpha = .75

fig = plt.figure()

ax = Axes3D(fig)
    

def cubic(n, *args):
    for basis, i, j, k in itertools.product(args, range(n), range(n), range(n)):
        ax.scatter(basis[0]+k,
                   basis[1]+j,
                   basis[2]+i,
                   c=basis[3], alpha=alpha, s=size)


def fcc(n, *args):
    for basis, i, j, k in itertools.product(args, range(n), range(n), range(n)):
        ax.scatter([basis[0]+k, basis[0]+.5+k, basis[0]+k, basis[0]+.5+k],
                   [basis[1]+j, basis[1]+.5+j, basis[1]+.5+j, basis[1]+j],
                   [basis[2]+i, basis[2]+i, basis[2]+.5+i, basis[2]+.5+i],
                   c=basis[3], alpha=alpha, s=size)


def bcc(n, *args):
    for basis, i, j, k in itertools.product(args, range(n), range(n), range(n)):
        ax.scatter([basis[0]+k, basis[0]+.5+k],
                   [basis[1]+j, basis[1]+.5+j],
                   [basis[2]+i, basis[2]+.5+i],
                   c=basis[3], alpha=alpha, s=size)


def tetragonal(n, height_ratio, *args):
    for basis, i, j, k in itertools.product(args, range(n), range(n), range(n)):
        ax.scatter(basis[0]+k,
                   basis[1]+j,
                   basis[2]+i*height_ratio,
                   c=basis[3], alpha=alpha, s=size)

def tetragonal_bc(n, height_ratio, *args):
    for basis, i, j, k in itertools.product(args, range(n), range(n), range(n)):
        ax.scatter([basis[0]+k, basis[0]+.5+k],
                   [basis[1]+j, basis[1]+.5+j],
                   [basis[2]+i*height_ratio, basis[2]+.5*height_ratio+i*height_ratio],
                   c=basis[3], alpha=alpha, s=size)


def hexagonal(n, height_ratio, *args):
    for basis, i, j, k in itertools.product(args, range(n), range(n), range(n)):
        ax.scatter(basis[0]+k+j*np.cos(2*np.pi/3)+np.cos(2*np.pi/3)*basis[1],
                   basis[1]*np.sin(2*np.pi/3)+j*np.sin(2*np.pi/3),
                   basis[2]+i*height_ratio,
                   c=basis[3], alpha=alpha, s=size)


# Thank you stack exchange for this solution
# https://stackoverflow.com/questions/13685386/matplotlib-equal-unit-length-with-equal-aspect-ratio-z-axis-is-not-equal-to
# User: karlo
def set_axes_equal(ax):
    '''Make axes of 3D plot have equal scale so that spheres appear as spheres,
    cubes as cubes, etc..  This is one possible solution to Matplotlib's
    ax.set_aspect('equal') and ax.axis('equal') not working for 3D.

    Input
      ax: a matplotlib axis, e.g., as output from plt.gca().
    '''

    x_limits = ax.get_xlim3d()
    y_limits = ax.get_ylim3d()
    z_limits = ax.get_zlim3d()

    x_range = abs(x_limits[1] - x_limits[0])
    x_middle = np.mean(x_limits)
    y_range = abs(y_limits[1] - y_limits[0])
    y_middle = np.mean(y_limits)
    z_range = abs(z_limits[1] - z_limits[0])
    z_middle = np.mean(z_limits)

    # The plot bounding box is a sphere in the sense of the infinity
    # norm, hence I call half the max range the plot radius.
    plot_radius = 0.5*max([x_range, y_range, z_range])

    ax.set_xlim3d([x_middle - plot_radius, x_middle + plot_radius])
    ax.set_ylim3d([y_middle - plot_radius, y_middle + plot_radius])
    ax.set_zlim3d([z_middle - plot_radius, z_middle + plot_radius])


def show():
    set_axes_equal(ax)
    plt.show()

