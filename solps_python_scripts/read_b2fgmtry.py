
import numpy as np
from solps_python_scripts.read_ifield import read_ifield
from solps_python_scripts.read_rfield import read_rfield

def read_b2fgmtry(file = None, save = None):

    # gmtry = read_b2fgmtry(file)
    #
    # Read b2fgmtry file created by B2.5.
    #
    #

    # Author: Wouter Dekeyser
    # E-mail: wouter.dekeyser@kuleuven.be
    # November 2016
    #
    # Re-written in python by: Matteo Moscheni
    # E-mail: matteo.moscheni@tokamakenergy.co.uk
    # February 2022

    fid = open(file, "r")

    ## Get version of the b2fstate file

    line    = fid.readline()
    version = line[7:17]

    print("read_b2fgmtry -- file version " + version)


    ## Read dimensions nx, ny, and symmetry

    dim = read_ifield(fid,'nx,ny',[2])
    nx  = int(dim[0])
    ny  = int(dim[1])

    # Expected array sizes, gmtry
    qcdim = [nx+2, ny+2]
    if version >= '03.001.000':
        qcdim = [nx+2, ny+2, 2]

    gmtry = {}

    ## Read symmetry information

    gmtry['isymm'] = read_ifield(fid,'isymm',1)


    ## Read gmtry variables

    gmtry['crx']  = read_rfield(fid,'crx' ,[nx+2,ny+2,4])
    gmtry['cry']  = read_rfield(fid,'cry' ,[nx+2,ny+2,4])
    gmtry['fpsi'] = read_rfield(fid,'fpsi',[nx+2,ny+2,4])
    gmtry['ffbz'] = read_rfield(fid,'ffbz',[nx+2,ny+2,4])
    gmtry['bb']   = read_rfield(fid,'bb'  ,[nx+2,ny+2,4])
    gmtry['vol']  = read_rfield(fid,'vol' ,[nx+2,ny+2])
    gmtry['hx']   = read_rfield(fid,'hx'  ,[nx+2,ny+2])
    gmtry['hy']   = read_rfield(fid,'hy'  ,[nx+2,ny+2])
    gmtry['qz']   = read_rfield(fid,'qz'  ,[nx+2,ny+2,2])
    gmtry['qc']   = read_rfield(fid,'qc'  ,qcdim)
    gmtry['gs']   = read_rfield(fid,'gs'  ,[nx+2,ny+2,3])


    ## Some other geometrical parameters

    gmtry['nlreg'] = read_ifield(fid,'nlreg',1)
    gmtry['nlxlo'] = read_ifield(fid,'nlxlo',gmtry['nlreg'])
    gmtry['nlxhi'] = read_ifield(fid,'nlxhi',gmtry['nlreg'])
    gmtry['nlylo'] = read_ifield(fid,'nlylo',gmtry['nlreg'])
    gmtry['nlyhi'] = read_ifield(fid,'nlyhi',gmtry['nlreg'])
    gmtry['nlloc'] = read_ifield(fid,'nlloc',gmtry['nlreg'])

    gmtry['nncut']     = read_ifield(fid,'nncut'    ,1)
    gmtry['leftcut']   = read_ifield(fid,'leftcut'  ,gmtry['nncut'])
    gmtry['rightcut']  = read_ifield(fid,'rightcut' ,gmtry['nncut'])
    gmtry['topcut']    = read_ifield(fid,'topcut'   ,gmtry['nncut'])
    gmtry['bottomcut'] = read_ifield(fid,'bottomcut',gmtry['nncut'])

    gmtry['leftix']    = read_ifield(fid,'leftix'   ,[nx+2,ny+2])
    gmtry['rightix']   = read_ifield(fid,'rightix'  ,[nx+2,ny+2])
    gmtry['topix']     = read_ifield(fid,'topix'    ,[nx+2,ny+2])
    gmtry['bottomix']  = read_ifield(fid,'bottomix' ,[nx+2,ny+2])
    gmtry['leftiy']    = read_ifield(fid,'leftiy'   ,[nx+2,ny+2])
    gmtry['rightiy']   = read_ifield(fid,'rightiy'  ,[nx+2,ny+2])
    gmtry['topiy']     = read_ifield(fid,'topiy'    ,[nx+2,ny+2])
    gmtry['bottomiy']  = read_ifield(fid,'bottomiy' ,[nx+2,ny+2])

    gmtry['region']      = read_ifield(fid,'region'     ,[nx+2,ny+2,3])
    gmtry['nnreg']       = read_ifield(fid,'nnreg'      ,3)
    gmtry['resignore']   = read_ifield(fid,'resignore'  ,[nx+2,ny+2,2])
    gmtry['periodic_bc'] = read_ifield(fid,'periodic_bc',1)

    gmtry['pbs']  = read_rfield(fid,'pbs' ,[nx+2,ny+2,2])

    gmtry['parg'] = read_rfield(fid,'parg',100)

    ## Close file

    fid.close()

    if save is True:
        location = file.split("b2fgmtry")[0]
        pickle.dump(gmtry, open(location + "gmtry.pkl", "wb"))

    return gmtry
