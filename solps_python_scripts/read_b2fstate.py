
import numpy as np
from solps_python_scripts.read_rfield import read_rfield
from solps_python_scripts.read_ifield import read_ifield

def read_b2fstate(file = None, save = None):

    # state = read_b2fstate(file)
    #
    # Read b2fstati/b2fstate file created by B2.5.
    #
    # Output is a struct "state" with all the data fields in the b2fstate/i
    # file (except for the dimensions nx,ny,ns, which are implicit in the array
    # sizes).
    #

    # Author: Wouter Dekeyser
    # E-mail: wouter.dekeyser@kuleuven.be
    # November 2016
    #
    # Re-writte in python by: Matteo Moscheni
    # E-mail: matteo.moscheni@tokamakenergy.co.uk
    # February 2022 


    # Open file
    fid = open(file, "r")


    ## Get version of the b2fstate file

    line    = fid.readline()
    version = line[7:17]

    state = {}

    print('read_b2fstate -- file version ' + version)
    state['version'] = version


    ## Read dimensions nx, ny, ns

    dim = read_ifield(fid,'nx,ny,ns',3)
    nx  = int(dim[0])
    ny  = int(dim[1])
    ns  = int(dim[2])
    
    state['ns'] = ns

    fluxdim  = [nx+2,ny+2,2]
    fluxdimp = [nx+2,ny+2]
    fluxdims = [nx+2,ny+2,2,ns]
    if version >= '03.001.000':
        fluxdim  = [nx+2,ny+2,2,2]
        fluxdimp = fluxdim
        fluxdims = [nx+2,ny+2,2,2,ns]

    ## Read charges etc.

    state['zamin'] = read_rfield(fid,'zamin',ns)
    state['zamax'] = read_rfield(fid,'zamax',ns)
    state['zn']    = read_rfield(fid,'zn   ',ns)
    state['am']    = read_rfield(fid,'am   ',ns)


    ## Read state variables

    state['na']     = read_rfield(fid,'na'    ,[nx+2,ny+2,ns])
    state['ne']     = read_rfield(fid,'ne'    ,[nx+2,ny+2])
    state['ua']     = read_rfield(fid,'ua'    ,[nx+2,ny+2,ns])
    state['uadia']  = read_rfield(fid,'uadia' ,[nx+2,ny+2,2,ns])
    state['te']     = read_rfield(fid,'te'    ,[nx+2,ny+2])
    state['ti']     = read_rfield(fid,'ti'    ,[nx+2,ny+2])
    state['po']     = read_rfield(fid,'po'    ,[nx+2,ny+2])


    ## Read fluxes

    state['fna']    = read_rfield(fid,'fna'   ,fluxdims)
    state['fhe']    = read_rfield(fid,'fhe'   ,fluxdim)
    state['fhi']    = read_rfield(fid,'fhi'   ,fluxdim)
    state['fch']    = read_rfield(fid,'fch'   ,fluxdim)
    state['fch_32'] = read_rfield(fid,'fch_32',fluxdim)
    state['fch_52'] = read_rfield(fid,'fch_52',fluxdim)
    state['kinrgy'] = read_rfield(fid,'kinrgy',[nx+2,ny+2,ns])
    state['time']   = read_rfield(fid,'time'  ,1)
    state['fch_p']  = read_rfield(fid,'fch_p' ,fluxdimp)

    if int(version.split(".")[2]) >= int("03.000.005".split(".")[2]):
        # Starting at version 03.000.005, a large number of additional fields
        # was added to remove restart effect for 5.2 model equations (BCs)
        state['fna_mdf']     = read_rfield(fid,'fna_mdf'    ,fluxdims)
        state['fhe_mdf']     = read_rfield(fid,'fhe_mdf'    ,fluxdim)
        state['fhi_mdf']     = read_rfield(fid,'fhi_mdf'    ,fluxdim)
        state['fna_fcor']    = read_rfield(fid,'fna_fcor'   ,fluxdims)
        state['fna_nodrift'] = read_rfield(fid,'fna_nodrift',fluxdims)
        state['fna_he']      = read_rfield(fid,'fna_he'     ,fluxdims)
        state['fnaPSch']     = read_rfield(fid,'fnaPSch'    ,fluxdims)
        state['fhePSch']     = read_rfield(fid,'fhePSch'    ,fluxdim)
        state['fhiPSch']     = read_rfield(fid,'fhiPSch'    ,fluxdim)
        state['fna_eir']     = read_rfield(fid,'fna_eir'    ,fluxdims)
        state['fne_eir']     = read_rfield(fid,'fne_eir'    ,fluxdim)
        state['fhe_eir']     = read_rfield(fid,'fhe_eir'    ,fluxdim)
        state['fhi_eir']     = read_rfield(fid,'fhi_eir'    ,fluxdim)
        state['fna_32']      = read_rfield(fid,'fna_32'     ,fluxdims)
        state['fna_52']      = read_rfield(fid,'fna_52'     ,fluxdims)
        state['fni_32']      = read_rfield(fid,'fni_32'     ,fluxdim)
        state['fni_52']      = read_rfield(fid,'fni_52'     ,fluxdim)
        state['fne_32']      = read_rfield(fid,'fne_32'     ,fluxdim)
        state['fne_52']      = read_rfield(fid,'fne_52'     ,fluxdim)
        state['fchdia']      = read_rfield(fid,'fchdia'     ,fluxdim)
        state['fchin']       = read_rfield(fid,'fchin'      ,fluxdim)
        state['fchvispar']   = read_rfield(fid,'fchvispar'  ,fluxdim)
        state['fchvisper']   = read_rfield(fid,'fchvisper'  ,fluxdim)
        state['fchvisq']     = read_rfield(fid,'fchvisq'    ,fluxdim)
        state['fchinert']    = read_rfield(fid,'fchinert'   ,fluxdim)
        
        state['vaecrb'] = read_rfield(fid,'vaecrb' ,[nx+2,ny+2,2,ns])
        state['vadia']  = read_rfield(fid,'vadia'  ,[nx+2,ny+2,2,ns])
        state['wadia']  = read_rfield(fid,'wadia'  ,[nx+2,ny+2,2,ns])
        state['veecrb'] = read_rfield(fid,'veecrb' ,[nx+2,ny+2,2])
        state['vedia']  = read_rfield(fid,'vedia'  ,[nx+2,ny+2,2])
        
        state['floe_noc']  = read_rfield(fid,'floe_noc' ,fluxdim)
        state['floi_noc']  = read_rfield(fid,'floi_noc' ,fluxdim)

    ## Close file

    fid.close()

    return state
