
import os
import numpy as np
import matplotlib.pyplot as plt
# import matplotlib.tri as tri

# from matplotlib.patches import Polygon
# from matplotlib.collections import PatchCollection

from solps_python_scripts.read_ft46 import read_ft46
from solps_python_scripts.read_triangle_mesh import read_triangle_mesh

def plot_b2(directory = None, key = None):
	return

def plot_eirene(directory = None, key = None):

	triangles = read_triangle_mesh(fort33 = os.path.join(directory, "fort.33"),
								   fort34 = os.path.join(directory, "fort.34"),
								   fort35 = os.path.join(directory, "fort.35"))

	fort46 = read_ft46(file = os.path.join(directory, "fort.46"), save = False)

	cells = triangles['cells']
	nodes = triangles['nodes']

	#values = np.log10(fort46[key] + fort46[key].min() * 1E-01)
	values = np.log10(fort46[key])
	values = values[:,0]

	# triang = Triangulation(nodes[:,0], nodes[:,1], cells)

	# patches = []

	# for cell in cells:

	# 	polygon = [nodes[int(cell[0]),:],
	# 			   nodes[int(cell[1]),:],
	# 			   nodes[int(cell[2]),:]]

	# 	patches.append(Polygon(xy = polygon, closed = True, linewidth = 0, fill = None))

	fig, ax = plt.subplots()
	tpc = ax.tripcolor(nodes[:,0], nodes[:,1], cells, values, shading = 'flat', cmap = 'turbo')
	# p = PatchCollection(patches)
	# p.set_array(values)
	# ax.add_collection(p)
	fig.colorbar(tpc)
	ax.set_aspect('equal')
	plt.show()

	return


