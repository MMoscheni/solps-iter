*-----------------------------------------------------------------------
*.specification

      subroutine shtci_kin(te, ti, shtci0, strength, shtci,
     .                     ncall, diagno, ib, iy)
      use b2mod_types
      use b2mod_constants
      use b2mod_indirect
      use b2mod_geo
      use b2mod_b2cmpa
      implicit none
*   ..input arguments (unchanged on exit)
      real (kind=R8) :: te, ti, shtci0, strength
      integer :: ncall, diagno, ib, iy
*   ..output argument (unspecified on entry)
      real (kind=R8) :: shtci
*
*-----------------------------------------------------------------------
*.documentation
*
*  1. purpose
*
*     This subroutine calculates the ION sheath INTERNAL energy
*     transmission cofficient according to:
*     
*     [P.C. Stangeby, 2000. url: https://books.google.co.uk/books?id=qOliQgAACAAJ.]
*     [D.F. Brunner, "Development of probes for assessment of ion heat transport
*      and heat heat flux in the boundary of the Alcator C-Mod tokamak", PhD Thesis, 2013]
*     [D. Tskhakaya, 2017, Plasma Phys. Control. Fusion, vol. 59, pp. 114001]
*
*     Input parameters:
*     - te: electron temperature
*     - ti: ion temperature
*     - shtci0 = enipar('W'/'E',1) [= 1.5 if SOLPS-ITER default value]:
*       minimum shtci allowed (preventing shtci = 0 - CHECK independence!)
*     - strength = enipar('W'/'E',2):
*	tuneable parameter to avoid abrupt changes in BC (eventually 1.0 required)
*
*     Output parameters:
*     shtci - sheath heat transmission coefficient for ions
*             (scalar, but now cell-specific <=> space-varying)  
*
*     ***************************************************************************************
*                                       *** THEORY ***
*     
*     Kinetic results > ION TOTAL energy [Stangeby][Brunner]:
*       shtci_kin_tot = 5/2 * ti/te
*
*     "Classical" fluid approach with v = cs @sheath [Tskhakaya]:
*       shtci_fld_tot = shtci_fld_int + mi*cs^2/ti/2, 
*
*     => shtci_kin_tot = shtci_fld_tot
*     => shtci = shtci_fld_int = shtci_kin_tot - mi*cs^2/ti/2 = 0.5 * (5 * ti/te - te/ti - 1)   
*
*     IMPORTANT:
*
*     To avoid "un-reasonably small" values:
*       shtci = max(shtci, shtci0 > 0)
*     but one should verify that the result does NOT depend on shtci0 (if small enough)
*
*     However:
*     if (ti/te > (1.0+sqrt(21.00))/10 ~ 0.56) then shtci > 0.0
*     => given that usually ti/te >~ 1 => shtci > shtci0 ~ 0 => usually OK
*
*     ***************************************************************************************
*
*  2. Criticalities to be addressed:
*
*     - appropriateness of shtci_kin_tot = shtci_fld_tot (kin vs. fld)
*     - validity of shtci_kin_tot in presence of impurities
*     - currently sound speed implicitly evaluated according to:
*       cs = sqrt((te + ti) / mi)
*       therefore assuming:
*           - pure hydrogenic plasma (no impurities)
*           - adiabatic coefficient GAMMAI = 1 
*     - raise warning if is.gt.2 (impurities are present)
*     - Internal parameters: variable instead of 1.5 as reference
*     - ???
*
*  3. contacts
*
*     M. Moscheni: Matteo.Moscheni@tokamakenergy.co.uk
*     F. Subba <3: fabio.subba@polito.it
*
*-----------------------------------------------------------------------
*.declarations
*   ..procedures
	  intrinsic max
      external subini, subend, bcint, xertst
*
*-----------------------------------------------------------------------
*.computations
*
* ..preliminaries
*   ..subprogram start-up calls
      call subini ('shtci_kin')
*   ..test input parameters
      call xertst (0.le.te, 'faulty argument te')
      call xertst (0.le.ti, 'faulty argument ti')
*
*   ..inform user (only once)
      if (ncall.eq.0 .and. iy.eq.1) then
        write (*,*) '    MMM: shtci_kin.F activated'
        write (*,*) '         - hp: hydrogenic plasma'
        write (*,*) '         - hp: GAMMAI = 1'
      endif
*
*   ..WARNING
      if (strength.eq.0.0_R8) then
        write (*,*) '    MMM: shtci_kin.F with strength = 0.0 !'
        write (*,*) '         enipar(,2) needed...'
      endif
*
*     reminder: b2stbc_phys.F enforces boundary conditions cell-by-cell
*
      shtci = 0.5 * (5 * ti/te - te/ti - 1)
      shtci = 1.5 * (1.0 + strength * (shtci - 1.5))
      shtci = max(shtci, shtci0)
*
*     informing user if shtci < shtci0
*
      if (shtci.lt.shtci0) then
        write (*,*) '  MMM: shtci < shtci0 detected in shtci_kin.F'
      endif
*
      if (diagno.ge.2) then
        if (iy.eq.1) then
          write (*,*) '  MMM: shtci_kin.F > diagnosis...'
        endif
        write(*,*) '  ib, iy, ti/te, shtci: ', ib, iy, ti/te, shtci
      endif
*
*
*-----------------------------------------------------------------------
      call subend ()
      return
*.end
      end subroutine shtci_kin
