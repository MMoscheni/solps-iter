
import numpy as np
from read_ft44_rfield import read_ft44_rfield 

def read_ft44(file = None, save = None):

    # [neut,wld] = read_ft44(file)
    #
    # Read fort.44 file
    #
    # For now
    # - only fort.44 version 20081111 recognized
    # - assuming nfla = 1 until a better fix 
    # - assuming nlwrmsh = 1 until a better fix
    #
    # 
    #

    # Author: Wouter Dekeyser
    # E-mail: wouter.dekeyser@kuleuven.be
    # November 2016
    #
    # Re-writte in python by: Matteo Moscheni
    # E-mail: matteo.moscheni@tokamakenergy.co.uk
    # February 2022

    print('read_ft44: assuming nlwrmsh = 1, nfla = 1.')
    nlwrmsh = 1
    nfla = 1

    fid = open(file, "r")

    neut = {}
    wld  = {}


    ## Read dimensions

    # nx, ny, version
    line = fid.readline().split()
    nx   = int(line[0])
    ny   = int(line[1])
    ver  = int(line[2])

    if ver != 20081111 and ver != 20160829 and ver != 20170328 and ver != 20201006:
        raise ValueError('read_ft44: unknown format of fort.44 file')

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

    ## Read basic data

    neut['dab2']     = read_ft44_rfield(fid,ver,'dab2',[nx,ny,natm])
    neut['tab2']     = read_ft44_rfield(fid,ver,'tab2',[nx,ny,natm])
    neut['dmb2']     = read_ft44_rfield(fid,ver,'dmb2',[nx,ny,nmol])
    neut['tmb2']     = read_ft44_rfield(fid,ver,'tmb2',[nx,ny,nmol])
    neut['dib2']     = read_ft44_rfield(fid,ver,'dib2',[nx,ny,nion])
    neut['tib2']     = read_ft44_rfield(fid,ver,'tib2',[nx,ny,nion])
    neut['rfluxa']   = read_ft44_rfield(fid,ver,'rfluxa',[nx,ny,natm])
    neut['rfluxm']   = read_ft44_rfield(fid,ver,'rfluxm',[nx,ny,nmol])
    neut['pfluxa']   = read_ft44_rfield(fid,ver,'pfluxa',[nx,ny,natm])
    neut['pfluxm']   = read_ft44_rfield(fid,ver,'pfluxm',[nx,ny,nmol])
    neut['refluxa']  = read_ft44_rfield(fid,ver,'refluxa',[nx,ny,natm])
    neut['refluxm']  = read_ft44_rfield(fid,ver,'refluxm',[nx,ny,nmol])
    neut['pefluxa']  = read_ft44_rfield(fid,ver,'pefluxa',[nx,ny,natm])
    neut['pefluxm']  = read_ft44_rfield(fid,ver,'pefluxm',[nx,ny,nmol])
    neut['emiss']    = read_ft44_rfield(fid,ver,'emiss',[nx,ny,1])
    neut['emissmol'] = read_ft44_rfield(fid,ver,'emissmol',[nx,ny,1])
    neut['srcml']    = read_ft44_rfield(fid,ver,'srcml',[nx,ny,nmol])
    neut['edissml']  = read_ft44_rfield(fid,ver,'edissml',[nx,ny,nmol])

    # ## Data on wall loading
    # 
    # # nlim, nsts, nstra
    # dims  = fscanf(fid,'#d',3)
    # nlim  = dims(1)
    # nsts  = dims(2)
    # nstra = dims(3)
    # 
    # wld['wldnek = zeros(nlim+nsts,nstra+1)
    # wld['wldnep = zeros(nlim+nsts,nstra+1)
    # wld['wldna  = zeros(nlim+nsts,natm,nstra+1)
    # wld['ewlda  = zeros(nlim+nsts,natm,nstra+1)
    # wld['wldnm  = zeros(nlim+nsts,nmol,nstra+1)
    # wld['ewldm  = zeros(nlim+nsts,nmol,nstra+1)
    # 
    # wld['wldnek(:,1)  = read_ft44_rfield(fid,nlim+nsts)
    # wld['wldnep(:,1)  = read_ft44_rfield(fid,nlim+nsts)
    # wld['wldna(:,:,1) = read_ft44_rfield(fid,[nlim+nsts,natm])
    # wld['ewlda(:,:,1) = read_ft44_rfield(fid,[nlim+nsts,natm])
    # wld['wldnm(:,:,1) = read_ft44_rfield(fid,[nlim+nsts,nmol])
    # wld['ewldm(:,:,1) = read_ft44_rfield(fid,[nlim+nsts,nmol])
    # 
    # wld['poly = read_ft44_rfield(fid,[4,nlim])
    # 
    # wld['wldra  = read_ft44_rfield(fid,[nlim+nsts,natm])
    # wld['wldrm  = read_ft44_rfield(fid,[nlim+nsts,nmol])
    # 
    # if (nstra > 1)
    #     for i = 2:nstra+1
    #         wld['wldnek(:,i)  = read_ft44_rfield(fid,nlim+nsts)
    #         wld['wldnep(:,i)  = read_ft44_rfield(fid,nlim+nsts)
    #         wld['wldna(:,:,i) = read_ft44_rfield(fid,[nlim+nsts,natm])
    #         wld['ewlda(:,:,i) = read_ft44_rfield(fid,[nlim+nsts,natm])
    #         wld['wldnm(:,:,i) = read_ft44_rfield(fid,[nlim+nsts,nmol])
    #         wld['ewldm(:,:,i) = read_ft44_rfield(fid,[nlim+nsts,nmol])
    #     end
    # end
    # 
    # 
    # wld['wldpp   = zeros(nlim+nsts,nfla,nstra+1)
    # wld['wldpa   = zeros(nlim+nsts,natm,nstra+1)
    # wld['wldpm   = zeros(nlim+nsts,nmol,nstra+1)
    # wld['wldpeb  = zeros(nlim+nsts,nstra+1)
    # wld['wldspt  = zeros(nlim+nsts,nstra+1)
    # 
    # wld['wldpp(:,:,1) = read_ft44_rfield(fid,[nlim+nsts,nfla])
    # wld['wldpa(:,:,1) = read_ft44_rfield(fid,[nlim+nsts,natm])
    # wld['wldpm(:,:,1) = read_ft44_rfield(fid,[nlim+nsts,nmol])
    # wld['wldpeb(:,1)  = read_ft44_rfield(fid,nlim+nsts)
    # wld['wldspt(:,1)  = read_ft44_rfield(fid,nlim+nsts)
    # 
    # if (nstra > 1)
    #     for i = 2:nstra+1
    #         wld['wldpp(:,:,i) = read_ft44_rfield(fid,[nlim+nsts,nfla])
    #         wld['wldpa(:,:,i) = read_ft44_rfield(fid,[nlim+nsts,natm])
    #         wld['wldpm(:,:,i) = read_ft44_rfield(fid,[nlim+nsts,nmol])
    #         wld['wldpeb(:,i)  = read_ft44_rfield(fid,nlim+nsts)
    #         wld['wldspt(:,i)  = read_ft44_rfield(fid,nlim+nsts)
    #     end
    # end
    # 
    # wld['isrftype = read_ft44_ifield(fid,nlim+nsts)

    # MMM decommented from here down to penultimate line
    if nlwrmsh == 0:

        raise ValueError("Not translated yet!")
        
        # wld['wlarea']  = read_ft44_rfield(fid,nlim+nsts)
        
        # wld['wlabsrp'] = zeros(natm+nmol+nion+nfla,nlim+nsts)
        # line = fgetl(fid)
        # wld['wlabsrp'](1:natm,:) = read_ft44_rfield(fid,[natm,nlim+nsts])
        # line = fgetl(fid)
        # ns = natm
        # wld['wlabsrp'](ns+1:ns+nmol,:) = read_ft44_rfield(fid,[nmol,nlim+nsts])
        # line = fgetl(fid)
        # ns = natm+nmol
        # wld['wlabsrp'](ns+1:ns+nion,:) = read_ft44_rfield(fid,[nion,nlim+nsts])
        # line = fgetl(fid)
        # ns = natm+nmol+nion
        # wld['wlabsrp'](ns+1:ns+nfla,:) = read_ft44_rfield(fid,[nfla,nlim+nsts])
        
        # neut['eneutrad'] = read_ft44_rfield(fid,[nx,ny,natm])
        
        # wld['eirdiag_nds_ind']   = read_ft44_ifield(fid,nsts+1)
        # wld['eirdiag_nds_typ']   = read_ft44_ifield(fid,nsts)
        # wld['eirdiag_nds_srf']   = read_ft44_ifield(fid,nsts)
        # wld['eirdiag_nds_start'] = read_ft44_ifield(fid,nsts)
        # wld['eirdiag_nds_end']   = read_ft44_ifield(fid,nsts)
        
        # ncl = wld['eirdiag_nds_ind'](nsts+1)
        
        # wld['sarea_res']  = read_ft44_rfield(fid,ncl)
        # wld['wldna_res']  = read_ft44_rfield(fid,[natm,ncl])
        # wld['wldnm_res']  = read_ft44_rfield(fid,[nmol,ncl])
        # wld['ewldna_res'] = read_ft44_rfield(fid,[natm,ncl])
        # wld['ewldnm_res'] = read_ft44_rfield(fid,[nmol,ncl])
        # wld['ewldea_res'] = read_ft44_rfield(fid,[natm,ncl])
        # wld['ewldem_res'] = read_ft44_rfield(fid,[nmol,ncl])
        # wld['ewldrp_res'] = read_ft44_rfield(fid,ncl)
        # wld['ewldmr_res'] = read_ft44_rfield(fid,[nmol,ncl])
        
        # neut['PDENA_INT']    = read_ft44_rfield(fid,[natm,nstrata])
        # neut['PDENM_INT']    = read_ft44_rfield(fid,[nmol,nstrata])
        # neut['PDENI_INT']    = read_ft44_rfield(fid,[nion,nstrata])
        # neut['PDENA_INT_B2'] = read_ft44_rfield(fid,[natm,nstrata])
        # neut['PDENM_INT_B2'] = read_ft44_rfield(fid,[nmol,nstrata])
        # neut['PDENI_INT_B2'] = read_ft44_rfield(fid,[nion,nstrata])
        # neut['EDENA_INT']    = read_ft44_rfield(fid,[natm,nstrata])
        # neut['EDENM_INT']    = read_ft44_rfield(fid,[nmol,nstrata])
        # neut['EDENI_INT']    = read_ft44_rfield(fid,[nion,nstrata])
        # neut['EDENA_INT_B2'] = read_ft44_rfield(fid,[natm,nstrata])
        # neut['EDENM_INT_B2'] = read_ft44_rfield(fid,[nmol,nstrata])
        # neut['EDENI_INT_B2'] = read_ft44_rfield(fid,[nion,nstrata])
    else:
        # MMM
        # neut['eneutrad = read_ft44_rfield(fid,[nx,ny,natm])
        # neut['eneutrad'] = read_ft44_rfield(fid,ver,'eneutrad',[nx,ny,natm])
        pass

    fid.close()

    if save is True:
        location = file.split("fort.44")[0]
        pickle.dump(neut, open(location + "ft44_neut.pkl", "wb"))
        pickle.dump(wdl, open(location + "ft44_wld.pkl", "wb"))

    return (neut, wld)