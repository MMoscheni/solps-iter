# Simil-kinetic sheath internal-ion-energy transmission coefficient

## Instructions

- See introduction of `shtci_kin.F` for theoretical details
- Modifications to original `b2stbc_phys.F` labeled "MMM" in the script
- Activated by setting `'b2stbc_bceni_03_style' '1'` in `b2mn.dat`
- Diagnosed by setting `'b2stbc_diagno' '2'` in `b2mn.dat`

## Current assumptions

- Pure hydrogenic plasma (no impurities)
- Unitary adiabatic coefficient in computing sound speed (`GAMMAI = 1`)
- `mompar(ismain,ib,2).lt.0.5_R8`
