# Simil-kinetic sheath internal-ion-energy transmission coefficient

## Instructions

- See introduction of `shtci_kin.F` for theoretical details
- Modifications to original `b2stbc_phys.F` labeled "MMM" in the script
- Activated by setting `'b2stbc_bceni_03_style'` switch in b2mn.dat to `'1'`
- Diagnosed by setting `'b2stbc_diagno'` switch in b2mn.dat to `'2'`

## Current assumptions

- Pure hydrogenic plasma (no impurities)
- Unitary adiabatic coefficient in computing sound speed (`GAMMAI = 1`)
- `mompar(ismain,ib,2).lt.0.5_R8`
