import numpy as np

def read_ft44_rfield(fid = None, ver = None, fieldname = None, dims = None):

    # field = read_ft44_rfield(fid,ver,fieldname,dims)
    #
    # Auxiliary routine to read real fields from fort.44 file
    # 

    # Author: Wouter Dekeyser
    # E-mail: wouter.dekeyser@kuleuven.be
    # November 2016
    #
    # Re-writte in python by: Matteo Moscheni
    # E-mail: matteo.moscheni@tokamakenergy.co.uk
    # February 2022

    # Version 20160829: field label and size are specified in fort.44
    # Do consistency check on the data

    if ver >= 20160829:
        # Search the file until identifier 'fieldname' is found
        line = fid.readline()
        print(fieldname)
        while line.find(fieldname) == -1:
            line = fid.readline()
            if line == "":
                raise ValueError("EOF reached without finding" + fieldname + ".")

        line = line.split()
        
        # Consistency check: number of elements specified in the file should equal
        # prod(dims)
        
        numin = int(line[6])
        if numin != np.array(dims).prod():
            raise ValueError('read_ft44_rfield: inconsistent number of input elements.')

        # Read the data
        iin = 0
        field = np.zeros((numin))
        while iin < numin and line != "":
            line = fid.readline().split()
            iil = 0
            while iil < len(line):
                field[iin + iil] = line[iil]
                iil += 1
            iin += len(line)

        if len(dims) > 1:
            field = np.reshape(field, tuple(dims), order = "F")

    else:
        raise ValueError("fort.44 version NOT regonised!")
    
    return field