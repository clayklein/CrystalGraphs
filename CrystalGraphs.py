import matplotlib.pyplot as plt
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import itertools
# use all_basis instead of args in the islice part of the function

size = 50
marker = 'o'

plt.rcParams['grid.color'] = '#252525'

fig = plt.figure()

ax = Axes3D(fig)

ax.set_facecolor('black')
ax.w_xaxis.set_pane_color((0.0, 0.0, 0.0, 0.0))
ax.w_yaxis.set_pane_color((0.0, 0.0, 0.0, 0.0))
ax.w_zaxis.set_pane_color((0.0, 0.0, 0.0, 0.0))

x=[]
y=[]
z=[]

def cubic(n, *args, draw_path=False):
    all_basis = args
    
    # Lattice vectors
    ax.plot([0,1],[0,0],[0,0], c='red', label='$\\vec{a}$')
    ax.plot([0,0],[0,1],[0,0], c='blue', label='$\\vec{b}$')
    ax.plot([0,0],[0,0],[0,1], c='green', label='$\\vec{c}$')

    # Cube corners
    for i, j, k in itertools.product(range(n+1), range(n+1), range(n+1)):
        x.append(all_basis[0][0]+k)
        y.append(all_basis[0][1]+j)
        z.append(all_basis[0][2]+i)
    ax.scatter(x, y, z, c=all_basis[0][3], s=size)
    x.clear()
    y.clear()
    z.clear()

    # Additional basis points
    for index in range(1, len(all_basis)):
        for i, j, k in itertools.product(range(n), range(n), range(n)):
            x.append(all_basis[index][0]+k)
            y.append(all_basis[index][1]+j)
            z.append(all_basis[index][2]+i)     
        ax.scatter(x, y, z, c=all_basis[index][3], s=size)
        x.clear()
        y.clear()
        z.clear()

    # Show path along lattice vectors for basis points
    if draw_path == True:
        for i in range(len(all_basis)):
            ax.plot([0,all_basis[i][0]], [0,0], [0,0], c='grey', linestyle=':')
            ax.plot([all_basis[i][0],all_basis[i][0]], [0,all_basis[i][1]], [0,0], c='grey', linestyle=':')
            ax.plot([all_basis[i][0],all_basis[i][0]], [all_basis[i][1],all_basis[i][1]], [0,all_basis[i][2]], c='grey', linestyle=':')


def fcc(n, *args, draw_path=False):
    all_basis = args
    
    # Lattice vectors
    ax.plot([0,1],[0,0],[0,0], c='red', label='$\\vec{a}$')
    ax.plot([0,0],[0,1],[0,0], c='blue', label='$\\vec{b}$')
    ax.plot([0,0],[0,0],[0,1], c='green', label='$\\vec{c}$')
    
    # Cube corners
    for i, j, k in itertools.product(range(n+1), range(n+1), range(n+1)):
        x.append(all_basis[0][0]+k)
        y.append(all_basis[0][1]+j)
        z.append(all_basis[0][2]+i)
    ax.scatter(x, y, z, c=all_basis[0][3], s=size)
    x.clear()
    y.clear()
    z.clear()

    # Face points
    for i, j, k in itertools.product(range(n+1), range(n), range(n)):
        x.extend([all_basis[0][0]+.5+k, all_basis[0][0]+.5+k, all_basis[0][0]+i])
        y.extend([all_basis[0][1]+.5+j, all_basis[0][1]+i, all_basis[0][1]+.5+k])
        z.extend([all_basis[0][2]+i, all_basis[0][2]+.5+j, all_basis[0][2]+.5+j])
    ax.scatter(x, y, z, c=all_basis[0][3], s=size)
    x.clear()
    y.clear()
    z.clear()
    
    # Additional basis points
    for index in range(1, len(all_basis)):
        for i, j, k in itertools.product(range(n), range(n), range(n)):
            x.extend([all_basis[index][0]+k, all_basis[index][0]+.5+k, all_basis[index][0]+k, all_basis[index][0]+.5+k])
            y.extend([all_basis[index][1]+j, all_basis[index][1]+.5+j, all_basis[index][1]+.5+j, all_basis[index][1]+j])
            z.extend([all_basis[index][2]+i, all_basis[index][2]+i, all_basis[index][2]+.5+i, all_basis[index][2]+.5+i])
        ax.scatter(x, y, z, c=all_basis[index][3], s=size)
        x.clear()
        y.clear()
        z.clear()

    # Show path along lattice vectors for basis points
    if draw_path == True:
        for i in range(len(all_basis)):
            ax.plot([0,all_basis[i][0]], [0,0], [0,0], c='grey', linestyle=':')
            ax.plot([all_basis[i][0],all_basis[i][0]], [0,all_basis[i][1]], [0,0], c='grey', linestyle=':')
            ax.plot([all_basis[i][0],all_basis[i][0]], [all_basis[i][1],all_basis[i][1]], [0,all_basis[i][2]], c='grey', linestyle=':')


def bcc(n, *args, draw_path=False):
    all_basis = args
    
    # Lattice vectors
    ax.plot([0,1],[0,0],[0,0], c='red', label='$\\vec{a}$')
    ax.plot([0,0],[0,1],[0,0], c='blue', label='$\\vec{b}$')
    ax.plot([0,0],[0,0],[0,1], c='green', label='$\\vec{c}$')
    
    # Cube corners
    for i, j, k in itertools.product(range(n+1), range(n+1), range(n+1)):
        x.append(all_basis[0][0]+k)
        y.append(all_basis[0][1]+j)
        z.append(all_basis[0][2]+i)
    ax.scatter(x, y, z, c=all_basis[0][3], s=size)
    x.clear()
    y.clear()
    z.clear()

    # Center points
    for i, j, k in itertools.product(range(n), range(n), range(n)):
        x.extend([all_basis[0][0]+.5+k])
        y.extend([all_basis[0][1]+.5+j])
        z.extend([all_basis[0][2]+.5+i])
    ax.scatter(x, y, z, c=all_basis[0][3], s=size)
    x.clear()
    y.clear()
    z.clear()

    # Additional basis points
    for index in range(1, len(all_basis)):
        for i, j, k in itertools.product(range(n), range(n), range(n)):
            x.extend([all_basis[index][0]+k, all_basis[index][0]+.5+k])
            y.extend([all_basis[index][1]+j, all_basis[index][1]+.5+j])
            z.extend([all_basis[index][2]+i, all_basis[index][2]+.5+i])
        ax.scatter(x, y, z, c=all_basis[index][3], s=size)
        x.clear()
        y.clear()
        z.clear()

    # Show path along lattice vectors for basis points
    if draw_path == True:
        for i in range(len(all_basis)):
            ax.plot([0,all_basis[i][0]], [0,0], [0,0], c='grey', linestyle=':')
            ax.plot([all_basis[i][0],all_basis[i][0]], [0,all_basis[i][1]], [0,0], c='grey', linestyle=':')
            ax.plot([all_basis[i][0],all_basis[i][0]], [all_basis[i][1],all_basis[i][1]], [0,all_basis[i][2]], c='grey', linestyle=':')


def tetragonal(n, height_ratio, *args, draw_path=False):
    all_basis = args
    
    # Lattice vectors
    ax.plot([0,1],[0,0],[0,0], c='red', label='$\\vec{a}$')
    ax.plot([0,0],[0,1],[0,0], c='blue', label='$\\vec{b}$')
    ax.plot([0,0],[0,0],[0,height_ratio], c='green', label='$\\vec{c}$')
    
    # Cell corners
    for i, j, k in itertools.product(range(n+1), range(n+1), range(n+1)):
        x.append(all_basis[0][0]+k)
        y.append(all_basis[0][1]+j)
        z.append(all_basis[0][2]+i*height_ratio)
    ax.scatter(x, y, z, c=all_basis[0][3], s=size)
    x.clear()
    y.clear()
    z.clear()

    # Additional basis points
    for index in range(1, len(all_basis)):
        for i, j, k in itertools.product(range(n), range(n), range(n)):
            x.append(all_basis[index][0]+k)
            y.append(all_basis[index][1]+j)
            z.append(all_basis[index][2]+i*height_ratio)     
        ax.scatter(x, y, z, c=all_basis[index][3], s=size)
        x.clear()
        y.clear()
        z.clear()

    # Show path along lattice vectors for basis points
    if draw_path == True:
        for i in range(len(all_basis)):
            ax.plot([0,all_basis[i][0]], [0,0], [0,0], c='grey', linestyle=':')
            ax.plot([all_basis[i][0],all_basis[i][0]], [0,all_basis[i][1]], [0,0], c='grey', linestyle=':')
            ax.plot([all_basis[i][0],all_basis[i][0]], [all_basis[i][1],all_basis[i][1]], [0,all_basis[i][2]], c='grey', linestyle=':')


def tetragonal_bc(n, height_ratio, *args, draw_path=False):
    all_basis = args
    
    # Lattice vectors
    ax.plot([0,1],[0,0],[0,0], c='red', label='$\\vec{a}$')
    ax.plot([0,0],[0,1],[0,0], c='blue', label='$\\vec{b}$')
    ax.plot([0,0],[0,0],[0,2], c='green', label='$\\vec{c}$')
    
    # Cube corners
    for i, j, k in itertools.product(range(n+1), range(n+1), range(n+1)):
        x.append(all_basis[0][0]+k)
        y.append(all_basis[0][1]+j)
        z.append(all_basis[0][2]+i*height_ratio)
    ax.scatter(x, y, z, c=all_basis[0][3], s=size)
    x.clear()
    y.clear()
    z.clear()

    # Center points
    for i, j, k in itertools.product(range(n), range(n), range(n)):
        x.extend([all_basis[0][0]+.5+k])
        y.extend([all_basis[0][1]+.5+j])
        z.extend([all_basis[0][2]+.5*height_ratio+i*height_ratio])
    ax.scatter(x, y, z, c=all_basis[0][3], s=size)
    x.clear()
    y.clear()
    z.clear()

    # Additional basis points
    for index in range(1, len(all_basis)):
        for i, j, k in itertools.product(range(n), range(n), range(n)):
            x.extend([all_basis[index][0]+k, all_basis[index][0]+.5+k])
            y.extend([all_basis[index][1]+j, all_basis[index][1]+.5+j])
            z.extend([all_basis[index][2]+i*height_ratio, all_basis[index][2]+.5*height_ratio+i*height_ratio])
        ax.scatter(x, y, z, c=all_basis[index][3], s=size)
        x.clear()
        y.clear()
        z.clear()

    # Show path along lattice vectors for basis points
    if draw_path == True:
        for i in range(len(all_basis)):
            ax.plot([0,all_basis[i][0]], [0,0], [0,0], c='grey', linestyle=':')
            ax.plot([all_basis[i][0],all_basis[i][0]], [0,all_basis[i][1]], [0,0], c='grey', linestyle=':')
            ax.plot([all_basis[i][0],all_basis[i][0]], [all_basis[i][1],all_basis[i][1]], [0,all_basis[i][2]], c='grey', linestyle=':')


def hexagonal(n, height_ratio, *args, draw_path=False):
    all_basis = args # chjange to all_basis or vice versa
    
    # Lattice vectors
    ax.plot([0,1],[0,0],[0,0], c='red', label='$\\vec{a}$')
    ax.plot([0,-np.cos(np.pi/3)],[0,np.sin(np.pi/3)],[0,0], c='blue', label='$\\vec{b}$')
    ax.plot([0,0],[0,0],[0,height_ratio], c='green', label='$\\vec{c}$')
    
    # Corner points
    for i, j, k in itertools.product(range(n+1), range(n+1), range(n+1)):
        x.extend([all_basis[0][0]+k+j*np.cos(2*np.pi/3)+np.cos(2*np.pi/3)*all_basis[0][1]])
        y.extend([all_basis[0][1]*np.sin(2*np.pi/3)+j*np.sin(2*np.pi/3)])
        z.extend([all_basis[0][2]+i*height_ratio])
    ax.scatter(x, y, z, c=all_basis[0][3], s=size)
    x.clear()
    y.clear()
    z.clear()
    
    # Addition basis points
    for index in range(1, len(all_basis)):
        for i, j, k in itertools.product(range(n), range(n), range(n)):
            x.extend([all_basis[index][0]+k+j*np.cos(2*np.pi/3)+np.cos(2*np.pi/3)*all_basis[index][1]])
            y.extend([all_basis[index][1]*np.sin(2*np.pi/3)+j*np.sin(2*np.pi/3)])
            z.extend([all_basis[index][2]+i*height_ratio])
        ax.scatter(x, y, z, c=all_basis[index][3], s=size)
        x.clear()
        y.clear()
        z.clear()

    # Show path along lattice vectors for basis points
    if draw_path == True:
        for i in range(len(all_basis)):
            ax.plot([0,all_basis[i][0]], [0,0], [0,0], c='grey', linestyle=':')
            ax.plot([all_basis[i][0],all_basis[i][0]+all_basis[i][1]*np.cos(2*np.pi/3)], [0,all_basis[i][1]*np.sin(2*np.pi/3)], [0,0], c='grey', linestyle=':')
            ax.plot([all_basis[i][0]+all_basis[i][1]*np.cos(2*np.pi/3),all_basis[i][0]+all_basis[i][1]*np.cos(2*np.pi/3)], [all_basis[i][1]*np.sin(2*np.pi/3),all_basis[i][1]*np.sin(2*np.pi/3)], [0,all_basis[i][2]], c='grey', linestyle=':')

    


# Thank you stack exchange for this solution
# matplotlib's ax.set_aspect('equal') does not currently work for 3D plots
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
    ax.legend()
    plt.show()

