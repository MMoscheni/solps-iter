
import numpy as np
from read_ft44_rfield import read_ft44_rfield 

def read_ft46(file = None, save = None):

    # tdata = read_ft46(file)
    #
    # Read fort.46 file. Convert to SI units.
    #
    # For now, only fort.46 version 20160513 recognized 
    #

    # Author: Wouter Dekeyser
    # E-mail: wouter.dekeyser@kuleuven.be
    # November 2016
    #
    # Re-writte in python by: Matteo Moscheni
    # E-mail: matteo.moscheni@tokamakenergy.co.uk
    # February 2022
    
    fid = open(file, "r")

    ## Read dimensions

    # ntri, version
    line = fid.readline().split()
    ntri = int(line[0])
    ver  = int(line[1])

    if ver != 20160513 and ver != 20160829 and ver != 20170930:
        raise ValueError('read_ft46: unknown format of fort.46 file')

    # natm, nmol, nion
    line = fid.readline().split()
    natm = int(line[0])
    nmol = int(line[1])
    nion = int(line[2])

    # for now, ignore reading species labels
    for i in range(natm):
        line = fid.readline()
    for i in range(nmol):
        line = fid.readline()
    for i in range(nion):
        line = fid.readline()

    eV   = 1.6022e-19

    ## Read data

    tdata = {}

    tdata['pdena']  = read_ft44_rfield(fid,ver,'pdena',[ntri,natm])*1e6 # m^{-3}
    tdata['pdenm']  = read_ft44_rfield(fid,ver,'pdenm',[ntri,nmol])*1e6
    tdata['pdeni']  = read_ft44_rfield(fid,ver,'pdeni',[ntri,nion])*1e6

    tdata['edena']  = read_ft44_rfield(fid,ver,'edena',[ntri,natm])*1e6*eV # J m^{-3}
    tdata['edenm']  = read_ft44_rfield(fid,ver,'edenm',[ntri,nmol])*1e6*eV
    tdata['edeni']  = read_ft44_rfield(fid,ver,'edeni',[ntri,nion])*1e6*eV

    tdata['vxdena'] = read_ft44_rfield(fid,ver,'vxdena',[ntri,natm])*1e1 # kg s^{-1} m^{-2}
    tdata['vxdenm'] = read_ft44_rfield(fid,ver,'vxdenm',[ntri,nmol])*1e1
    tdata['vxdeni'] = read_ft44_rfield(fid,ver,'vxdeni',[ntri,nion])*1e1

    tdata['vydena'] = read_ft44_rfield(fid,ver,'vydena',[ntri,natm])*1e1 # kg s^{-1} m^{-2}
    tdata['vydenm'] = read_ft44_rfield(fid,ver,'vydenm',[ntri,nmol])*1e1
    tdata['vydeni'] = read_ft44_rfield(fid,ver,'vydeni',[ntri,nion])*1e1

    tdata['vzdena'] = read_ft44_rfield(fid,ver,'vzdena',[ntri,natm])*1e1 # kg s^{-1} m^{-2}
    tdata['vzdenm'] = read_ft44_rfield(fid,ver,'vzdenm',[ntri,nmol])*1e1
    tdata['vzdeni'] = read_ft44_rfield(fid,ver,'vzdeni',[ntri,nion])*1e1


    ## Close file

    fid.close()

    if save is True:
        location = file.split("fort.46")[0]
        pickle.dump(tdata, open(location + "ft46_tdata.pkl", "wb"))

    return tdata