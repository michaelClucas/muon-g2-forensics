# muon-g2-forensics

Forensic reconstruction of where the 2020 Standard Model prediction of the muon anomalous magnetic moment a_mu = (g-2)/2 diverged from experiment, and what in the data-driven (e+e- -> hadrons) hadronic vacuum polarization (HVP) input produced the gap that lattice QCD later closed.

## Headline finding
The 2020 prediction was low because the e+e- -> pi+pi- cross section used for leading-order HVP was too low in the rho region (about 0.5-1.0 GeV). Every pre-2023 pi pi dataset implies a total HVP below the lattice value; KLOE is the lowest, 3.7-5.7% below CMD-3 across 0.5-0.975 GeV. Swapping the 2020 pi pi input for CMD-3 moves HVP LO from 693.1 to 711-713 x 10^-10, the lattice average adopted in 2025. That shift is 77% of the 262 x 10^-11 gap to the final 2025 experimental average; an upward revision of hadronic light-by-light supplies 9%; the remaining 38(63) x 10^-11 is consistent with zero. QED, electroweak and the dispersive framework were never the problem. Why the older measurements came out low is unresolved. PHOKHARA-related radiative-correction effects are disputed and could cover at most about a fifth of the KLOE-CMD-3 difference. BaBar's November 2026 re-analysis is the first independent result near CMD-3's level.

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
