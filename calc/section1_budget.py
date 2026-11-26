"""Section 1: SM budget WP2020 vs WP2025 and where the gap lives.

All inputs in units of 1e-11, sources:
  WP20 = arXiv:2006.04822 Table 1 / Eqs. (8.3)-(8.14)
  WP25 = arXiv:2505.21476 Table 1 / Table 33 / Eqs. (7.27), (8.12), (9.1)-(9.6)
  EXP25 = arXiv:2506.03069 (world average incl. E821, E989 Runs 1-6)
  EXP23 = arXiv:2308.06230 (world average after Run 2/3)
  A1(10): AHKN value 6.737(159) as quoted in WP20 Eq. (6.9); Volkov 5.891(61), arXiv:2404.00649 abstract.
Run: python section1_budget.py   (writes out/section1_budget.txt)
"""
import math, os

WP20 = {"QED": (116584718.931, 0.104), "EW": (153.6, 1.0), "HVP_LO": (6931, 40),
        "HVP_NLO": (-98.3, 0.7), "HVP_NNLO": (12.4, 0.1), "HLbL_total": (92, 18)}
WP25 = {"QED": (116584718.8, 0.2), "EW": (154.4, 0.4), "HVP_LO": (7132, 61),
        "HVP_NLO": (-99.6, 1.3), "HVP_NNLO": (12.4, 0.1), "HLbL_total": (115.5, 9.9)}
SM20_quoted, SM25_quoted = (116591810, 43), (116592033, 62)
EXP = {"E821 (WP20-adjusted)": (116592089, 63), "avg 2021 (Run1)": (116592061, 41),
       "avg 2023 (Run1-3)": (116592059, 22), "avg 2025 (Run1-6)": (116592071.5, 14.5)}

ALPHA_PI = (1 / 137.035999084) / math.pi
out = []
p = out.append

def total(d):
    return sum(v for v, _ in d.values())

p("Sum of components (central): WP20 %.1f (quoted %d), WP25 %.1f (quoted %d)"
  % (total(WP20), SM20_quoted[0], total(WP25), SM25_quoted[0]))
p("")
p("Gap a_exp - a_SM(WP20), in 1e-11:")
for k, (v, e) in EXP.items():
    d, de = v - SM20_quoted[0], math.hypot(e, SM20_quoted[1])
    p(f"  {k:24s} {d:7.1f} +- {de:5.1f}  ({d/de:.1f} sigma)")
d25 = EXP["avg 2025 (Run1-6)"][0] - SM25_quoted[0]
p(f"  WP25 vs 2025 average      {d25:7.1f} +- {math.hypot(14.5, 62):5.1f}  ({d25/math.hypot(14.5,62):.1f} sigma)")
p("")
p("Component shifts WP20 -> WP25 (1e-11), and share of the total upward shift:")
shift_tot = total(WP25) - total(WP20)
for k in WP20:
    s = WP25[k][0] - WP20[k][0]
    p(f"  {k:11s} {s:8.2f}   {100*s/shift_tot:6.1f}%   (WP20 uncertainty {WP20[k][1]})")
p(f"  total       {shift_tot:8.2f}")
p("")
p("Precision of non-hadronic pieces vs the 2025 gap to WP20 (%.0f):" % (EXP['avg 2025 (Run1-6)'][0] - SM20_quoted[0]))
p("  QED uncertainty 0.104 (WP20), 0.2 (WP25); EW 1.0 (WP20), 0.4 (WP25)")
dA = 6.737 - 5.891
p(f"  AHKN vs Volkov A1(10) difference {dA:.3f} -> (alpha/pi)^5 * dA = {ALPHA_PI**5*dA*1e11:.4f} e-11")
p(f"  Whole universal 5-loop term (alpha/pi)^5*A1(10) = {ALPHA_PI**5*6.737*1e11:.4f} e-11")
p(f"  Mass-dependent A2(10)(m_mu/m_e)=742.32 term = {ALPHA_PI**5*742.32*1e11:.3f} e-11")
p("")
other25 = total(WP25) - WP25["HVP_LO"][0]
need = EXP["avg 2025 (Run1-6)"][0] - other25
p(f"HVP LO required by experiment given WP25 non-LO-HVP pieces: {need:.0f} (cf. WP20 e+e- 6931, WP25 lattice 7132)")
other20 = total(WP20) - WP20["HVP_LO"][0]
need20 = EXP["avg 2025 (Run1-6)"][0] - other20
p(f"HVP LO required given WP20 non-LO-HVP pieces:                {need20:.0f}")

os.makedirs(os.path.join(os.path.dirname(__file__), "out"), exist_ok=True)
with open(os.path.join(os.path.dirname(__file__), "out", "section1_budget.txt"), "w") as f:
    f.write("\n".join(out) + "\n")
print("\n".join(out))
