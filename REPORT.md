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
