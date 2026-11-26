# Where the 2020 muon g-2 Standard Model prediction went wrong

Units: a_mu contributions in units of 10^-11 unless stated (10^-10 where the source uses it). "[S:x]" points to an entry in SOURCES.md, "[calc:x]" to a script in `calc/` and its output in `calc/out/`.

Labels used throughout:
- **Established**: stated in a primary source and not contested in later primary literature.
- **Disputed**: primary sources disagree, or the source itself says the question is open.
- **Inference**: my own reasoning from the cited numbers.

## 1. The non-hadronic parts are not the problem

### Numbers

| Piece | WP2020 [S:WP20] | WP2025 [S:WP25] | Shift |
|---|---|---|---|
| QED | 116 584 718.931(104) | 116 584 718.8(2) | -0.13 |
| EW | 153.6(1.0) | 154.4(4) | +0.8 |
| HVP LO | 6931(40) (e+e- data) | 7132(61) (lattice average) | **+201** |
| HVP NLO | -98.3(7) | -99.6(1.3) | -1.3 |
| HVP NNLO | 12.4(1) | 12.4(1) | 0 |
| HLbL incl. NLO | 92(18) | 115.5(9.9) | +23.5 |
| **Total SM** | 116 591 810(43) | 116 592 033(62) | +223 |

Experiment (world averages):

| Average | Value | a_exp - a_SM(WP20) | Source |
|---|---|---|---|
| E821 alone (WP20-adjusted) | 116 592 089(63) | 279(76), 3.7 sigma | [S:WP20] Eq. 8.13-8.14 |
| + FNAL Run 1 (2021) | 116 592 061(41) | 251(59), 4.2 sigma | [S:FNAL21] |
| + FNAL Run 2/3 (2023) | 116 592 059(22) | 249(48), 5.2 sigma | [S:FNAL23]; sigma from [calc:section1_budget] |
| + FNAL Run 4-6 (2025, final) | 116 592 071.5(14.5) | 262(45), 5.8 sigma | [S:FNAL25]; sigma from [calc:section1_budget] |
| WP2025 vs 2025 average | | 38(63), 0.6 sigma | [S:WP25] Eq. 9.6 |

Corrections to the premise: the FNAL 2023 paper quotes 5.0 sigma, which is FNAL alone (116 592 055(24)) vs WP20; with the world average it is 5.2 sigma. The gap to the final 2025 world average is 262(45) x 10^-11, i.e. 2.6 x 10^-9, matching the prompt's "roughly 2.5 x 10^-9". E821's final paper (2006) quotes 116 592 080(63); WP20 shifts it to 089 for the updated muon-to-proton magnetic moment ratio [S:WP20 Eq. 8.13].

### QED (Established)
- WP20 QED uncertainty is 0.104 x 10^-11, about 0.04% of the gap. Two choices of alpha (Cs vs a_e) differ by 0.09 [S:WP20 Eqs. 6.30-6.31].
- The universal 5-loop coefficient A1(10) was for years computed only by Aoyama, Hayakawa, Kinoshita, Nio (AHKN): 6.737(159) as quoted in WP20 Eq. 6.9. Volkov's independent full calculation gives 5.891(61), a 5 sigma disagreement in the coefficient [S:Volkov24]. For the muon it does not matter: (alpha/pi)^5 x 0.846 = 0.006 x 10^-11, and the entire universal 5-loop term is 0.046 x 10^-11 [calc:section1_budget]. The muon-specific 5-loop term with electron loops, A2(10)(m_mu/m_e) = 742.32(86), contributes 5.0 x 10^-11 with an uncertainty of 0.006 [S:WP20 Eq. 6.21; calc:section1_budget].
- The Schwinger term alpha/2pi and the rest of the QED series were never in question. The disagreement that does exist (A1(10)) is relevant to the electron, where (alpha/pi)^5 is not suppressed relative to the experimental precision in the same way.

### Electroweak (Established)
- 153.6(1.0) in WP20, 154.4(4) in WP25 [S:WP20, S:WP25 Eq. 8.12]. Two-loop result from [S:GSS13]. The shift (+0.8) and uncertainty (1.0) are under 0.5% of the gap.

### Hadronic light-by-light (Established numbers; inference on the share)
- WP20: 92(18) including NLO; phenomenology 92(19) and the RBC/UKQCD lattice value 78.7(30.6)(17.7) were averaged [S:WP20 Eqs. 8.7-8.11].
- WP25: phenomenology 103.3(8.8), lattice 122.5(9.0), combined 112.6(9.6) with scale factor S=1.5; with NLO 115.5(9.9) [S:WP25 Table 33, Eqs. 9.2-9.3].
- The +23.5 HLbL shift moved the SM toward experiment and is 10.5% of the total WP20->WP25 upward shift [calc:section1_budget]. It is within 1.3 sigma of the WP20 HLbL uncertainty (18). So HLbL accounts for about 9% of the 262 gap (Inference from the cited numbers). Its own lattice-vs-phenomenology spread (122.5 vs 103.3, about 1.5 sigma) is still a live, but small, issue (Disputed, at the 20 x 10^-11 level).

### Conclusion of section 1
The WP20->WP25 shift is +223 x 10^-11, of which +201 (90%) is leading-order HVP and +23.5 (10%) is HLbL; QED, EW and higher-order HVP together move by -0.6 [calc:section1_budget]. Given the WP25 values for every other piece, experiment requires a_mu^HVP,LO = 7170 x 10^-11, vs 6931 from e+e- data in WP20 and 7132(61) from the WP25 lattice average [calc:section1_budget]. The gap lives in LO HVP, with a ~10% side contribution from the then-underestimated HLbL central value.

## 2. Reconstructing the data-driven HVP

### Kernel (Established math; numbers from [calc:kernel])
a_mu^HVP,LO = (alpha^2/3pi^2) Int ds K(s) R(s)/s, with K(s) = Int_0^1 dx x^2(1-x)/(x^2+(1-x)s/m_mu^2). `calc/kernel.py` evaluates K by quadrature and checks it against the closed form (agreement to 1e-9 or better below 3 GeV) and checks the large-s limit K -> m_mu^2/(3s). The weight K(s)/s relative to its value at the rho mass (0.775 GeV) is 42 at 0.28 GeV, 2.6 at 0.6 GeV, 0.38 at 1.0 GeV and 0.025 at 2.0 GeV. Together with the rho resonance in R(s), this puts most of the integral in the pi+pi- channel below 1 GeV.

Using the KLOE combination cross section [calc:pipi_by_experiment] the pi+pi- integral below 0.975 GeV splits as: 0.316-0.5 GeV 11.6%, 0.5-0.6 GeV 10.9%, 0.6-0.7 GeV 21.3%, 0.7-0.76 GeV 25.0%, 0.76-0.8 GeV 15.1%, 0.8-0.88 GeV 12.1%, 0.88-0.975 GeV 3.9%. The 0.6-0.88 GeV window alone is 360.6 x 10^-10 (KLOE) to 379.3 (CMD-3), i.e. 52-53% of the entire a_mu^HVP,LO (693-713 x 10^-10). The pi+pi- channel below 1.8 GeV is 504-526 x 10^-10, 73-74% of the total [S:WP25 Table 5]. Confirmed: pi+pi- in the rho region is the largest single contribution.

### Inputs to the 2020 combination (Established, [S:WP20 Sec. 2, Table 4-5])
- pi+pi- datasets: CMD-2 (2004-2007), SND (2004/2006), KLOE08, KLOE10, KLOE12 (and their 2018 combination [S:KLOE18]), BaBar 2009/2012 [S:BaBar12], BESIII 2016 [S:BESIII16], CLEO-c 2018 [S:CLEO18]; SND20 [S:SND20] arrived too late to be decisive. CMD-3 (2023) [S:CMD3-23] did not exist.
- Three evaluations: DHMZ19 [S:DHMZ19] 694.0(4.0), KNT19 [S:KNT19] 692.8(2.4) (and the analyticity-constrained CHHKS fits for pi pi and 3pi below 1 GeV). For pi+pi- below 1.8 GeV: DHMZ19 507.85(0.83)(3.23)(0.55) vs KNT19 504.23(1.90), difference 3.62 x 10^-10 [S:WP20 Table 5].
- DHMZ uses local (per fine bin) chi^2 averaging with uncertainties propagated by pseudo-experiments and adds a systematic for the BaBar-KLOE tension; KNT uses a global correlated chi^2 fit over the full mass range, which assumes the correlations are known exactly and yields a smaller uncertainty [S:WP20 Sec. 2.3.6].
- WP20 merging: central value = arithmetic mean of DHMZ and KNT (CHHKS included for pi pi below 1 GeV and 3pi); uncertainties = the larger of the two per channel; extra systematic = half the DHMZ-KNT difference, except in pi pi where the larger of that (1.8) and DHMZ's BaBar/KLOE term (2.8 x 10^-10, half the difference between evaluations without BaBar and without KLOE) is taken. Result 693.1(2.8)exp(2.8)sys(0.7)DV+QCD = 693.1(4.0) x 10^-10 [S:WP20 Eq. 2.33].

### Recomputing pi+pi- from individual datasets
`calc/pipi_by_experiment.py` integrates the KLOE combination table (85 bins in s) and reproduces KLOE's own numbers: 377.6 vs 377.5(2.2) for 0.35<s<0.85 GeV^2, 489.9 vs 489.8 for 0.10<s<0.95 GeV^2, and 360.6 vs CMD-3's quoted KLOE value 360.6(2.1) for 0.6<sqrt s<0.88 GeV. Mapping CMD-3's published |F_pi|^2 (arXiv ancillary file) onto the same bins via the form-factor ratio gives 379.3, identical to CMD-3's published 379.3(3.0).

Per-experiment integrals over 0.6<sqrt s<0.88 GeV (10^-10) [S:CMD3-23 Table 4]:

| Experiment | a_mu^pipi | minus KLOE |
|---|---|---|
| KLOE | 360.6(2.1) | 0 |
| BESIII | 361.8(3.6) | +1.2 |
| SND (VEPP-2M) | 364.7(4.9) | +4.1 |
| CMD-2 | 366.5(3.4) | +5.9 |
| SND2k (VEPP-2000) | 366.7(3.2) | +6.1 |
| CLEO-c | 370.0(6.2) | +9.4 |
| BaBar | 370.1(2.7) | +9.5 |
| CMD-3 | 379.3(3.0) | +18.7 |

Full pi+pi- below 1.8 GeV (DHMZ method, 10^-10) and the total a_mu^HVP,LO each implies when combined with WP20's non-pi pi offset 187.3(2.2) [S:WP25 Table 5 and caption; arithmetic in calc/out/pipi_by_experiment.txt]:

| Dataset | pi pi < 1.8 GeV | Implied HVP LO | minus lattice 713.2(6.1) |
|---|---|---|---|
| KLOE | 504.5(5.2) | 691.8 | -21.4 |
| SND06 | 505.3(6.7) | 692.6 | -20.6 |
| BESIII | 505.9(3.7) | 693.2 | -20.0 |
| CMD-2 | 508.1(3.9) | 695.4 | -17.8 |
| SND20 | 509.6(3.6) | 696.9 | -16.3 |
| BaBar | 514.1(3.8) | 701.4 | -11.8 |
| tau (Belle+CLEO+ALEPH+OPAL) | 517.2(5.8) | 704.5 | -8.7 |
| CMD-3 | 525.9(4.2) | 713.2 | 0.0 |

Each experiment's swing on the total: replacing the 2020-era pi pi input by KLOE alone moves HVP LO by about -1 x 10^-10 relative to 693.1; by BaBar alone, +8; by CMD-3 alone, +20 (Inference: arithmetic on the table above).
