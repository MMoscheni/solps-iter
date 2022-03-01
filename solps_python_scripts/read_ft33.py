import numpy as np

def read_ft33(file = None):

    # nodes = read_ft33(file)
    #
    # Read fort.33-files (triangle nodes). Converts to SI units (m).
    #
    #

    # Author: Wouter Dekeyser
    # E-mail: wouter.dekeyser@kuleuven.be
    # November 2016
    #
    # Re-writte in python by: Matteo Moscheni
    # E-mail: matteo.moscheni@tokamakenergy.co.uk
    # February 2022

    fid = open(file, "r")

    print('read_ft33: assuming ntrfrm = 0.')
    ntrfrm = 0

    # Read coordinates

    # number of nodes
    nnodes = int(fid.readline().split()[0])
    nodes  = np.zeros((nnodes,2))

    if ntrfrm == 0:

        # CAUTION.
        #
        # Serial structure: 
        # - nnodes x coordinates
        # - nnodes y coordinates

        # x coordinate

        i = 0

        while i < nnodes:
            line = fid.readline().split()
            for j in range(len(line)):
                nodes[i + j,0] = float(line[j])
            i += len(line)

        # y coordinate

        i = 0

        while i < nnodes:
            line = fid.readline().split()
            for j in range(len(line)):
                nodes[i + j,1] = float(line[j])
            i += len(line)
        
    else:
        
        raise ValueError('read_ft33: wrong ntrfrm.')

    # Convert from cm to m
    nodes *= 1E-02

    # close file
    fid.close()

    return nodes

