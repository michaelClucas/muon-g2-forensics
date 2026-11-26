# muon-g2-forensics

Forensic reconstruction of where the 2020 Standard Model prediction of the muon anomalous magnetic moment a_mu = (g-2)/2 diverged from experiment, and what in the data-driven (e+e- -> hadrons) hadronic vacuum polarization (HVP) input produced the gap that lattice QCD later closed.

## Headline finding
The 2020 prediction was low because the measured e+e- -> pi+pi- cross section used for leading-order HVP was 3-5% too low across roughly 0.5-1.0 GeV (the rho region). Swapping the 2020 pi pi input for CMD-3's 2023 measurement moves HVP LO from 693.1 to 713.2 x 10^-10, exactly the lattice average adopted in 2025. That shift is 77% of the 262 x 10^-11 gap to the final 2025 experimental average; an upward revision of hadronic light-by-light supplies 9%, and the remaining 38(63) x 10^-11 is consistent with zero. QED, electroweak and the dispersive framework were never the problem. Why KLOE, CMD-2, SND and BESIII came out low (and CMD-3 high) is still unresolved; PHOKHARA-related radiative-correction effects are disputed and could cover at most about 40% of the KLOE-CMD-3 difference.

## Status
Complete through section 5 and adversarial review. See REPORT.md (answer), TIMELINE.md, SOURCES.md, REVIEW.md.

## Reproduce
Python 3 with numpy and scipy; `pdftotext` (poppler or xpdf) on PATH for the KLOE table.

```
python data/fetch_data.py         # downloads KLOE table (not redistributed) and checks the CMD-3 file
cd calc
python kernel.py                  # K(s), time kernel, window fractions
python section1_budget.py
python pipi_by_experiment.py
python section4_windows.py
python section5_attribution.py
```
Outputs land in `calc/out/`.
