import numpy as np

from solps_python_scripts.read_ft33 import read_ft33
from solps_python_scripts.read_ft34 import read_ft34
from solps_python_scripts.read_ft35 import read_ft35

def read_triangle_mesh(fort33 = None, fort34 = None, fort35 = None):

	# triangles = read_triangle_mesh(fort33,fort34,fort35)
	#
	# Wrapper routine to read all triangle data at once.
	#
	# Returns nodes, cells, nghbr, side and cont as fiels of triangles-struct.


	# Author: Wouter Dekeyser
	# E-mail: wouter.dekeyser@kuleuven.be
	# November 2016
	#
	# Re-writte in python by: Matteo Moscheni
	# E-mail: matteo.moscheni@tokamakenergy.co.uk
	# February 2022

	triangles = {}

	triangles['nodes'] = read_ft33(fort33)
	triangles['cells'] = read_ft34(fort34)
	links              = read_ft35(fort35)

	triangles['nghbr'] = links['nghbr']
	triangles['side']  = links['side']
	triangles['cont']  = links['cont']
	triangles['ixiy']  = links['ixiy']

	return triangles
