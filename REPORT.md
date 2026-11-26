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

## 3. Locating the failure

The question is which input made a_mu^HVP,LO(e+e-) come out about 20 x 10^-10 (2.9%) below the lattice average. Candidates are taken in turn. Section 4 adds the window evidence.

### 3.1 Lattice side: could lattice be wrong instead? (Established for W; Disputed at ~1% for the total)
- Intermediate window W (0.4-1.0 fm), full (all flavours, with isospin breaking), x10^-10 [S:RBC23, S:BMW20, S:Mainz22, S:ETMC22, S:FHM24, S:BMWDMZ24]: RBC/UKQCD 235.56(65)(50); BMW-20 236.7(0.4)(1.3); Mainz 237.30(79)(1.22); ETMC 236.3(1.3) (isospin breaking taken from BMW); FNAL/HPQCD/MILC 236.45(85); BMW/DMZ-24 236.29(57). WP25 average 236.58(43) [S:WP25 Eq. 3.26]. Data-driven with WP20-era e+e- data: 229.4(1.4) [S:CHKLST22 Table 1]. Six lattice groups with different actions, scale setting and finite-volume treatments agree within about 1.7 x 10^-10 of each other, and all sit 6-8 x 10^-10 above the e+e- value. This is the strongest single piece of evidence that the e+e- input, not lattice, was off.
- Full HVP is less uniform: BMW-20 707.5(5.5), BMW/DMZ-24 715.1(3.4) (lattice up to 2.8 fm plus a data-driven tail), Mainz-24 724.5(7.1), RBC/UKQCD as assembled by WP25 729.4(13.0); WP25 average 713.2(6.1) [S:BMW20, S:BMWDMZ24, S:Mainz24, S:WP25 Table 17, Eq. 3.31]. The long-distance region is harder on the lattice (signal-to-noise, finite volume), and the spread between groups (17 x 10^-10 between BMW-20 and Mainz-24) is comparable to the lattice-vs-data gap itself. So "lattice is right about the total to 1%" rests on fewer independent checks than the W result. **Disputed** at the 1% level, not in sign.
- Every lattice full-HVP result listed is above every pre-CMD-3 e+e- evaluation (691.8 to 701.4 in section 2). None points toward the e+e- central value.

### 3.2 Experimental normalization and systematics of specific pi+pi- measurements (Established: the data are mutually inconsistent. Disputed: which ones are wrong)
- In 0.6-0.88 GeV the measurements span 360.6 (KLOE) to 379.3 (CMD-3), 5.2%, while CMD-3 quotes a 0.7% systematic near the rho [S:CMD3-23 Table 4, S:CMD3-PRL]. Davier et al. quantify local discrepancies above 3 sigma (KLOE vs BaBar) and above 5 sigma (KLOE vs CMD-3), with BaBar vs CMD-3 at about 2 sigma [S:DHLMZ23 Sec. 8].
- The CMD-3 - KLOE difference is not localized at the rho peak or in the rho-omega interference region. It is +3.7% to +5.7% in every slice from 0.5 to 0.975 GeV and near zero below 0.5 GeV [calc:pipi_by_experiment, out/pipi_energy_breakdown.csv]. A near-constant fractional offset is what a normalization effect (luminosity, efficiency, acceptance, an overall radiative-correction factor) would produce, rather than a resonance-shape or energy-calibration effect (Inference).
- KLOE and BaBar were the two most precise inputs in 2020; the other pre-2023 data (CMD-2, SND, BESIII) cluster near KLOE. KLOE alone implies HVP LO 691.8, BaBar alone 701.4, CMD-3 alone 713.2 [S:WP25 Table 5].
- CMD-3 vs its predecessor CMD-2 differs by +12.8 x 10^-10 in 0.6-0.88 GeV (379.3 vs 366.5) [S:CMD3-23 Table 4]. CMD-3 says the reason for the discrepancies is unknown and suggests limited statistics in earlier experiments may have hidden some systematic effects [S:CMD3-23, discussion of Figs. 34-35]. No independent experiment had confirmed CMD-3's level as of WP25; new KLOE, BaBar, BESIII, SND, CMD-3 and Belle II analyses are in preparation [S:WP25 Sec. 2.12].
- Which experiments are wrong is not established. Lattice favours CMD-3's normalization (section 4); that is indirect evidence, not an identified experimental error.

### 3.3 Radiative corrections and Monte Carlo generators (Disputed. Current weight of evidence: not the main cause)
- The ISR experiments (KLOE, BaBar, BESIII) use PHOKHARA, an NLO generator. BaBar measured additional radiation in ISR events and found discrepancies in PHOKHARA's one-photon rates and angular distributions; the effect on BaBar's own pi pi cross section is negligible, "but could affect other measurements significantly" [S:BaBar23 abstract].
- DHLMZ estimated with fast simulation that missing NNLO radiation in PHOKHARA could change the KLOE08 cross section by -0.7% to -2.0% (two scenarios) and BESIII by about -3.2% in scenario 1, above the 0.5% radiative-correction uncertainties those experiments assigned. They call the studies approximate [S:DHLMZ23 Sec. 5, Sec. 8].
- WP25 records the response: BESIII showed the DHLMZ estimate did not account for corrections in the BESIII analysis; KLOE and BESIII showed 1%-level agreement between generators with different higher-order treatments; WP25 concludes scenario 1 "seems unlikely" and PHOKHARA's shortcomings "most likely do not explain" the differences [S:WP25 Sec. 2.12].
- Size check (Inference): 2% of KLOE's 0.6-0.88 GeV integral is 7.2 x 10^-10, 39% of the KLOE-CMD-3 gap there (18.7); 0.7% is 2.5 x 10^-10 (13%). Even the larger estimate cannot reconcile KLOE with CMD-3 by itself, and it does not touch CMD-2 or SND, which are energy-scan experiments with no ISR.
- Pion FSR: the standard treatment is scalar QED times the pion form factor. CMD-3 measured a forward-backward charge asymmetry that disagreed with it; Ignatov and Lee traced this to an oversimplified treatment of pion structure in two-photon exchange [S:IgnatovLee22], and Colangelo et al. confirmed significant corrections beyond scalar QED in a dispersive calculation [S:CHMR22]. These corrections are C-odd, so they largely cancel in the angle-integrated cross section if the detector acceptance is symmetric; their effect on a_mu^pipi is not quantified in the sources I read (**Unverified** magnitude). RadioMonteCarLow 2 identifies a class of resonance-enhanced virtual ISR corrections that could matter at the relevant level; generator improvements are still pending [S:RMCL2, as summarized in S:WP25 Sec. 2.12].
- Known incomplete at the time? The NLO-only nature of PHOKHARA and scalar-QED FSR were known approximations before 2020, and KLOE assigned 0.5% to radiative corrections. Whether 0.5% was too small is open.

### 3.4 The combination procedure (Established: the procedure could not have caught this)
- WP20 covered the BaBar/KLOE tension with a 2.8 x 10^-10 systematic (half the difference between evaluations without BaBar and without KLOE); total uncertainty 4.0 x 10^-10 [S:WP20 Eq. 2.33].
- The eventual shift, 693.1 -> 713.2, is +20.1 x 10^-10, five times the quoted uncertainty (Inference from S:WP20, S:WP25).
- The most favourable reading of the 2020 data (BaBar alone, 701.4) is 8 x 10^-10 above the merged value and still 12 x 10^-10 below lattice [S:WP25 Table 5]. No reweighting of the pre-2023 datasets reaches the lattice value, because apart from BaBar they agreed with each other and were all low. KNT19's global correlated fit, which takes quoted correlations as exact, came out 3.6 x 10^-10 below DHMZ19 in pi pi, i.e. further from lattice [S:WP20 Table 5].
- So the quoted uncertainty did underestimate the real spread, but the procedure was not the cause of the low central value. WP25 stopped averaging the pi pi channel because the differences exceed claimed systematics "by substantial factors" [S:WP25 Sec. 2.12].

### 3.5 Tau-decay data (Established numbers. IB corrections Disputed)
- tau -> pi pi nu gives the isovector spectral function; using it for e+e- needs isospin-breaking (IB) corrections. DHMZ's total IB correction to the pi pi contribution was -16.07(1.85) x 10^-10 in WP20 [S:WP20 Table 2], updated to -14.9(1.9) [S:DHLMZ23].
- WP20 did not use tau data because the estimable IB corrections did "not yet provide an understanding of the IB difference" between tau and e+e- [S:WP20 Sec. 2.2.6].
- Tau sits high: DHLMZ get a_mu^pipi(tau) = 517.3(1.9)(2.2)(1.9) x 10^-10 [S:DHLMZ23 Eq. 4]; WP25's tau estimate is 517.2(5.8), between BaBar (514.1) and CMD-3 (525.9), implying HVP LO 704.5, 8.7 below lattice [S:WP25 Table 5]. Tau-based W window 232.4 [S:DHLMZ23 Fig. 12]. Masjuan, Miranda and Roig find tau-based windows compatible with lattice [S:MMR23].
- Inference: excluding tau removed the one pre-2020 input that pointed upward. The reason for excluding it was defensible, but part of the tau-vs-e+e- disagreement was a symptom of the low e+e- data rather than only an IB problem. How much is not established; tau is still 8.7 x 10^-10 below lattice.

## 4. Windows and energy regions

Time-momentum representation: a_mu = 4 alpha^2 Int dt Ktil(t) G(t), with G(t) the Euclidean vector correlator. Windows: SD (t < 0.4 fm), W (0.4-1.0 fm), LD (t > 1.0 fm), smoothed with Delta = 0.15 fm [S:RBC18]. `calc/kernel.py` computes Ktil(t) numerically and checks that its Laplace transform reproduces 2K(omega^2)/omega^3 (relative error below 1e-6 from 0.3 GeV up). It then gives the share of each energy's contribution falling in each window: at 0.5 GeV SD/W/LD = 0.8/13.1/86.1%; at 0.775 GeV 3.6/34.8/61.6%; at 1.02 GeV 8.4/51.8/39.9%; at 2 GeV 39.3/57.2/3.6% [calc:kernel, out/window_fractions_vs_energy.csv].

### 4.1 Lattice minus data-driven, by window (x10^-10) [calc:section4_windows]

| Window | Lattice (WP25 avg) | e+e- (WP20-era data, CHKLST22) | Difference | sigma | Share of gap |
|---|---|---|---|---|---|
| SD | 69.10(26) | 68.4(5) | +0.7 | 1.2 | 3.5% |
| W | 236.58(43) | 229.4(1.4) | +7.2 | 4.9 | 35.5% |
| LD | 407.5(6.1) (total - SD - W) | 395.1(2.4) | +12.4 | 1.9 | 61.5% |
| Total | 713.2(6.1) | 693.0(3.9) | +20.2 | 2.8 | 100% |

LD for lattice is derived here by subtraction, and its uncertainty ignores correlations, so the 1.9 sigma is conservative (Inference). The relative excess is +1.0% in SD and +3.1% in both W and LD. SD is dominated by energies above ~1.5-2 GeV where R(s) is close to perturbative QCD; its near-agreement argues against a global lattice normalization problem such as scale setting (Inference). The gap is a uniform ~3% in the two windows that the rho region dominates.

### 4.2 Mapping the gap to energy
- The CMD-3 - KLOE pi pi difference reconstructed from the raw data (0.32-0.975 GeV) is +21.5 x 10^-10 in total. Weighted by window: SD +0.70, W +6.85, LD +13.91, i.e. 3% / 32% / 65% [calc:section4_windows].
- Independent check: DHLMZ computed the full W window with each pi pi dataset as input: KLOE 227.3, BaBar 230.8, tau 232.4, CMD-3 234.2 [S:DHLMZ23 Fig. 12]. Their CMD-3 - KLOE difference, 6.9, matches the 6.85 obtained here from the published tables.
- If the lattice-vs-data gap were caused by a pi pi normalization deficit with the energy profile of KLOE relative to CMD-3, 32% of it would appear in W and 65% in LD. Observed: 36% and 61%. Scaling the observed W difference (7.2) by 1/0.32 predicts a total gap of 22.5 vs the actual 20.2 [calc:section4_windows]. The window pattern is consistent with a 3-5% deficit in the pi pi cross section spread across roughly 0.5-1.0 GeV, centred on the rho (Inference). It is not consistent with a problem confined to high energies (that would show in SD) or to the threshold region below 0.5 GeV (that would put over 85% in LD).
- With CMD-3 as the pi pi input the W window becomes 234.2, 2.4 x 10^-10 below the lattice average 236.58(43); CMD-3 removes about 70% of the W discrepancy. With CMD-3 in the full HVP the total equals the lattice average (713.2) [S:WP25 Table 5]. I do not read anything into the 2.4 residual given the uncertainties of the non-pi pi channels in DHLMZ's W evaluation (Inference).
- Energy range holding the discrepancy: 0.5-0.975 GeV in pi+pi-, with 87% of the CMD-3 - KLOE difference (18.7 of 21.5 x 10^-10) between 0.6 and 0.88 GeV [calc:pipi_by_experiment, out/pipi_energy_breakdown.csv].
