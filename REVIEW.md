# Adversarial review

Two reviewer subagents were given only REPORT.md, SOURCES.md and calc/ (not the author's reasoning, README or TIMELINE). Reviewer A checked numbers and calculations; reviewer B checked causal attributions and citations. Both reviewed the version at commit d5653c6. Their findings and the responses follow. Facts a reviewer introduced were re-checked against the primary source before use (noted per item).

## Reviewer A: numbers and calculations

Re-ran all six scripts from a clean copy; all 11 output files were byte-identical. Independently derived the time-kernel Laplace check, the a_mu = 1/(4 pi^3) Int K sigma conversion and the window method. Cross-check: CHKLST22 Table 1 splits pi pi below 1 GeV as SD/W/LD = 2.8/28.0/69.2%; calc gives 2.8/27.9/69.3% for KLOE. Spot-checked about 40 numbers against WP20, WP25, CMD-3, CHKLST22, FNAL23, FNAL25, DHLMZ23, KLOE18, BMW/DMZ abstracts; all matched.

| # | Finding | Severity | Response |
|---|---|---|---|
| A-F2 | Report said the AHKN vs Volkov A1(10) disagreement still exists. WP25 Eqs. 7.14-7.19: AHKN re-evaluated to 5.870(128); average 5.887(55). | Error | Fixed in Secs. 1 and 5.4. Verified in WP25 text (Eq. 7.19). Muon impact unchanged (0.006e-11). |
| A-F5 | Radiative-correction bound "0-7.2 (39%)" overstated: -2% is the NNLO piece alone, partly cancelled by NLO excess (~-1% at rho peak in scenario 1), scenario 2 -0.7%; only KLOE08 config; KLOE10/12 less affected. Sign inconsistent between Sec. 3.3 text and script. | Misleading | Fixed. Sec. 3.3 now states the upward-correction direction, the cancellation, KLOE10/12 protection. Bound revised to roughly -1 to +3.6 (up to ~19%) in Secs. 3.3, 5.2 and calc/section5_attribution.py. Verified against DHLMZ Sec. 5.2-5.4 text. |
| A-F6 | "Five times the quoted uncertainty" ignores lattice +-6.1; combined it is 2.8 sigma. | Misleading | Fixed in Secs. 3.4 and 5.2 (both numbers given). |
| A-F7 | Section 2 / 3.2 / 5.2 use only the DHMZ column of WP25 Table 5; CHKLS gives 688.6 / 699.5 / 711.4; "X alone" is filled in with other data outside X's range. | Misleading | Fixed: caveat paragraph under the Sec. 2 table; CHKLS numbers added in Secs. 2, 4.2, 5.2. Verified against WP25 Table 5. |
| A-F8 | SD agreement is a weak argument against scale-setting errors (sensitivity grows with t). | Misleading | Fixed in Sec. 4.1; W cross-group agreement named as the better argument. |
| A-F9 | Lattice LD by subtraction mixes averages over different collaborations; no lattice IB for pure LD; the 36/61 vs 32/65 share test has little power. Proposed W-only argument instead. | Minor | Fixed in Secs. 4.1 and 4.2; W-only argument added. |
| A-F3 | "Six independent lattice groups" is five collaborations; ETMC uses BMW IB. | Minor | Fixed in Secs. 3.1, 5.1, 5.2. |
| A-F4 | WP25 Table 9 lists BMW/DMZ-24 W as 235.94(29)(63). | Rejected as stated | Checked WP25 text: 235.94(29)(63) is in the BMW-20 row (corrected value), not BMW/DMZ-24. Added to Sec. 3.1 as BMW-20's corrected W. |
| A-F1 | Closed-form agreement claim too strong above 1 GeV. | Minor | Fixed in Sec. 2. |
| A-F10 | "Below 0.975 GeV" split starts at 0.316 GeV. | Minor | Fixed in Sec. 2. |
| A-F11 | Sec. 5.2 label "e+e- data input" describes a method switch and presupposes lattice is right. | Minor | Fixed: label and status column rewritten. |
| A (unverified) | DHLMZ Fig. 12 window values only in a figure; BMW-20 v1 712.4(4.5). | Note | DHLMZ's own text gives significances consistent with the figure values (1.1 sigma CMD-3, 5.4 KLOE) and the average 232.0(1.1); 712.4 was taken by the lattice research subagent from BMW's SI footnote and is left as is. |

## Reviewer B: claims and citations

Confirmed verbatim: WP25 "seems unlikely", "most likely do not explain", "by substantial factors", the BESIII rebuttal; WP20 tau-exclusion quote; BaBar23 abstract quote; Ignatov & Lee; CMD-3 Table 4 and "reason unknown" sentences; DHLMZ authors, >3 and >5 sigma, tau 517.3, IB -14.9(1.9).

| # | Finding | Severity | Response |
|---|---|---|---|
| B-1 | Sign error in Sec. 3.3: DHLMZ percentages are efficiency changes implying upward cross-section corrections. | Error | Fixed (same edit as A-F5). |
| B-2 | DHLMZ caveats omitted: estimates "cannot be taken at face value", NLO excess could cancel, KKMC predicts a downward shift. | Error | Fixed in Sec. 3.3; KKMC sentence verified in DHLMZ text. Range now extends below zero. |
| B-3 | "CMD-2, SND, BESIII cluster near KLOE" and "apart from BaBar all low" contradict WP20 Sec. 2.2.4 and WP25 Sec. 2.5.1; CMD-2 and SND2k are closer to BaBar than to KLOE. | Misleading | Accepted and fixed in Secs. 3.2, 3.4, 5.1. Both quotes verified. The report now says KLOE is the low end, scan experiments in the middle, and that what all pre-2023 sets share is an implied total below lattice. |
| B-4 | "Near-constant offset, so normalization" contradicts the report's own breakdown (-0.4% below 0.5 GeV, rising 3.7 to 5.7%); KLOE08 vs 10/12 slopes 2.5-3 sigma. | Misleading | Accepted. Sec. 3.2 rewritten: broad but energy-dependent, not a single luminosity factor. Slope statement verified in WP25 Sec. 2.5.1. |
| B-5 | IB is a shared input (3.4 of 6.1 lattice uncertainty, WP25 Eq. 3.30), not mentioned. | Misleading | Fixed in Sec. 3.1; Eq. 3.30 value 0.1(3.4) verified. |
| B-6 | "True cross section is close to CMD-3" unlabelled inference in 5.1. | Misleading | Fixed: labelled inference with the evidence listed. |
| B-7 | "Essentially all of it" assumes lattice total exact. | Misleading | Fixed in Sec. 5.2. |
| B-8 | 5.4 called HLbL "experimental input"; flat "No" sits awkwardly with Disputed items. | Misleading | Fixed: HLbL described as a theory evaluation; caveats added. The answer "No" is kept, because neither caveat concerns QED, EW or the dispersive framework. |
| B-9 | Tau: DHLMZ text has tau 2.5 sigma below lattice in W. | Misleading | Fixed in Sec. 3.5; verified in DHLMZ text. |
| B-10 | PHOKHARA mechanism "does not touch CMD-2 or SND" true only for PHOKHARA; scan experiments have their own generators. | Minor | Fixed in Sec. 3.3. |
| B-11 | "KLOE assigned 0.5%" unsourced. | Minor | Fixed: 0.5% PHOKHARA (WP25 Sec. 2.5.1) and FSR 0.3% / 0.5-0.6% (WP25 Sec. 2.2.3), both verified. |
| B-12 | Merging procedure is WP20 Sec. 2.3.7, not 2.3.6. | Minor | Partly accepted: Sec. 2.3.6 is correct for the local-vs-global method discussion; Sec. 2.3.7 added for the merging rule. |
| B-13 | SOURCES missing locations and journal refs. | Minor | Added. Journal refs for BaBar23, CMD3-PRL, CHMR22, MMR23 taken from the reviewer (INSPIRE) and flagged as such. |
| B-14 | "CMD-3 removes 70% of W" mixes DHLMZ and CHKLST22 baselines. | Minor | Fixed in Sec. 4.2: uses DHLMZ's own 1.1 sigma. |
| B-15 | WP25 already showed preliminary unblinded SND data (0.6-0.8% syst.). | Minor | Added to Sec. 3.2; verified in WP25 Sec. 2.2.2. |
| B-16 | Post-June-2025 literature: BaBar 2026 (arXiv:2611.04621) lands near CMD-3; ETMC 2026 full HVP 714.9(8.1); Allen et al. 2026 tau vs lattice agree; Narison 2026 dissent; arXiv:2509.08115 on IB (few x 10^-10 at most). | Important | All four main items verified via the arXiv API and, for BaBar-26, the paper body (Fig. 69 values, 520.7 vs 520.3, "typically below 2.5" sigma). Reviewer gave BaBar-26 as 525.8; the abstract says 525.9, which is used. Added to Secs. 2, 3.1, 3.2, 3.5, 5.2, 5.3, TIMELINE. arXiv:2509.08115 was not checked and is not used. |
| B (not checked) | Whether SND20 fails dispersive consistency checks. | Note | WP25 Sec. 2.12 says it does ("tensions with the dispersive constraints in the case of SND20"); seen in the WP25 text but not added to the report's argument. |

## Effect on conclusions
No finding changed the headline: the 2020 gap was in LO HVP, in the pi+pi- data between 0.5 and 1 GeV, with HLbL supplying ~9%, and QED/EW/framework not involved. The review did change three things materially: KLOE, not the whole pre-2023 data set, is the low outlier in the rho region; the radiative-correction upper bound fell from 39% to about 19% of the KLOE-CMD-3 difference; and the 2026 BaBar re-analysis is now the first independent result near CMD-3's level.
