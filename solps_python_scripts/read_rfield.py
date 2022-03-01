
import numpy as np

def read_rfield(fid = None, fieldname = None, dims = None):

    # field = read_ifield(fid,fieldname,dims)
    #
    # Auxiliary routine to read integer fields from B2.5 b2f* files
    # 

    # Author: Wouter Dekeyser
    # E-mail: wouter.dekeyser@kuleuven.be
    # November 2016
    #
    # Re-written in python by: Matteo Moscheni
    # E-mail: matteo.moscheni@tokamakenergy.co.uk
    # February 2022

    # Search the file until identifier 'fieldname' is found
    line = fid.readline()
    while line.find(fieldname) == -1:
        line = fid.readline()
        if line == "":
            raise ValueError("EOF reached without finding " + fieldname + ".")

    # Consistency check: number of elements specified in the file should equal
    # prod(dims)
    numin = int((line.split())[2])
    if numin != np.array(dims).prod():
        raise ValueError("read_ifield: inconsistent number of input elements.")

    # Read the data
    iin = 0
    field = np.zeros((numin))
    while iin < numin and line != "":
        line = fid.readline().split()
        iil = 0
        while iil < len(line):
            field[iin + iil] = float(line[iil])
            iil += 1
        iin += len(line)

    if isinstance(dims, list) and len(dims) > 1:
        field = np.reshape(field, tuple(dims), order = "F")

    return field