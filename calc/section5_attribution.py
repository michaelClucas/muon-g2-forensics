"""Section 5: attribution of the WP20 gap to experiment (2025 world average), 1e-11.

Inputs from section 1 sources (WP20 arXiv:2006.04822, WP25 arXiv:2505.21476, FNAL25 arXiv:2506.03069)
and section 2 (WP25 Table 5). Uncertainties on shifts treat WP20 and WP25 values as uncorrelated,
which overstates them (the non-pi pi HVP and much of HLbL input is shared).
"""
import math, os
gap = (116592071.5 - 116591810, math.hypot(14.5, 43))
pieces = {
    "HVP LO (e+e- 2020 -> lattice 2025)": (7132 - 6931, math.hypot(61, 40)),
    "HLbL incl. NLO": (115.5 - 92, math.hypot(9.9, 18)),
    "QED + EW + HVP NLO/NNLO": ((116584718.8 - 116584718.931) + (154.4 - 153.6) + (-99.6 + 98.3), math.hypot(1.0, 1.4)),
}
L = [f"Gap a_exp(2025) - a_SM(WP20) = {gap[0]:.1f} +- {gap[1]:.1f}"]
s = 0
for k, (v, e) in pieces.items():
    s += v
    L.append(f"  {k:38s} {v:+7.1f} +- {e:5.1f}   {100*v/gap[0]:5.1f}% of gap")
L.append(f"  {'remaining a_exp - a_SM(WP25)':38s} {gap[0]-s:+7.1f} +- 63.7    {100*(gap[0]-s)/gap[0]:5.1f}% of gap (quoted 38(63))")
L.append("")
L.append("Within LO HVP (1e-10): WP20 merged 693.1(4.0); single-dataset alternatives from WP25 Table 5 + 187.3 offset:")
for n, v in [("KLOE", 691.8), ("BaBar", 701.4), ("tau", 704.5), ("CMD-3", 713.2)]:
    L.append(f"  {n:6s} {v:6.1f}  shift vs WP20 {v-693.1:+5.1f}  remaining to lattice 713.2: {713.2-v:+5.1f}")
L.append("  Radiative-correction scenarios (DHLMZ arXiv:2312.02053 Sec. 5, disputed by WP25 Sec. 2.5.1):")
L.append("  upward KLOE08 correction +0.7% (scen. 2) to ~+1% (scen. 1 after NLO cancellation); WP25 generator tests limit")
L.append("  PHOKHARA to ~1%; KKMC would shift the other way. Applied to the whole KLOE combination (upper bound,")
L.append("  KLOE10/12 less affected), 0.6-0.88 GeV integral 360.6:")
# -0.3% is an illustrative KKMC-direction value chosen here, not a number from any source.
for f in (-0.003, 0.007, 0.01):
    L.append(f"    {100*f:+.1f}% -> {f*360.6:+.1f} of the 18.7 KLOE-CMD-3 difference ({100*f*360.6/18.7:+.0f}%)")
L.append(f"  (scenario-1 NNLO piece alone, +2%, would be {0.02*360.6:.1f}; DHLMZ say it is partly cancelled)")
os.makedirs(os.path.join(os.path.dirname(__file__), "out"), exist_ok=True)
open(os.path.join(os.path.dirname(__file__), "out", "section5_attribution.txt"), "w").write("\n".join(L) + "\n")
print("\n".join(L))
