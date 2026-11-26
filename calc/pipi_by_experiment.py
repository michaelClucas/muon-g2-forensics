"""Section 2b: pi+pi- contribution from individual datasets, KLOE combination vs CMD-3.

Inputs:
  data/kloe_combination_table1.csv  (make with: python data/fetch_data.py)  arXiv:1711.03085 Table 1
  data/cmd3_fpi_2302.08834v3.dat     CMD-3 |F_pi|^2, arXiv:2302.08834v3 ancillary file (CC-BY 4.0)
Method:
  a_mu = 1/(4 pi^3) Int ds K(s) sigma0(s)   with sigma0 the bare pi+pi-(gamma) cross section.
  KLOE: sigma0 given per 0.01 GeV^2 bin; integrate K exactly over each (partial) bin.
  CMD-3: published only |F_pi|^2 (VP-dressed, no FSR). To avoid needing a VP table and an FSR
  model, CMD-3 is mapped onto the KLOE bins as sigma0_KLOE * <|F|^2_CMD3>_bin / |F|^2_KLOE,bin.
  Both |F|^2 use the same convention (VP included, FSR excluded), so VP and FSR factors cancel
  in the ratio. Bin averages of CMD-3 use linear interpolation over all three CMD-3 data sets.
Outputs: out/pipi_by_experiment.txt, out/pipi_energy_breakdown.csv
"""
import os
import numpy as np
from scipy import integrate
from hvp_common import K

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
NB_PER_GEV2 = 0.3893793721e6   # 1 GeV^-2 in nb

kl = np.genfromtxt(os.path.join(ROOT, "data", "kloe_combination_table1.csv"), delimiter=",",
                   skip_header=2, names=True)
s_c, sig, dsig, F2k = kl["s_GeV2"], kl["sigma0_nb"], kl["dsigma_nb"], kl["F2"]
lo, hi = s_c - 0.005, s_c + 0.005

cm = np.loadtxt(os.path.join(ROOT, "data", "cmd3_fpi_2302.08834v3.dat"), comments="#")
order = np.argsort(cm[:, 0])
E_c, F2_c = cm[order, 0], cm[order, 1]


def F2_cmd3(E):
    return np.interp(E, E_c, F2_c)


def Kint(a, b):
    return integrate.quad(lambda s: K(np.array([s]))[0], a, b, epsrel=1e-9)[0]


def amu_kloe(smin, smax, ratio=None):
    tot = 0.0
    for i in range(len(s_c)):
        a, b = max(lo[i], smin), min(hi[i], smax)
        if b <= a:
            continue
        w = Kint(a, b) * sig[i] / NB_PER_GEV2
        if ratio is not None:
            w *= ratio[i]
        tot += w
    return tot / (4 * np.pi**3) * 1e10


# CMD-3 / KLOE form-factor ratio per KLOE bin (bin average of interpolated CMD-3 |F|^2)
ratio = np.full(len(s_c), np.nan)
for i in range(len(s_c)):
    if np.sqrt(lo[i]) < E_c[0] or np.sqrt(hi[i]) > E_c[-1]:
        continue
    ss = np.linspace(lo[i], hi[i], 41)
    ratio[i] = np.mean(F2_cmd3(np.sqrt(ss))) / F2k[i]

L = []
p = L.append
p("Validation of the KLOE combination integral against published numbers (1e-10):")
p(f"  0.35<s<0.85 GeV^2 : {amu_kloe(0.35, 0.85):.1f}   published 377.5(2.2) [1711.03085 Table 2]")
p(f"  0.10<s<0.95 GeV^2 : {amu_kloe(0.10, 0.95):.1f}   published 489.8(5.1) [1711.03085 Eq. 4.3]")
p(f"  0.60<sqrt s<0.88  : {amu_kloe(0.36, 0.88**2):.1f}   CMD-3's value for KLOE 360.6(2.1) [2302.08834 Table 4]")
p("")
ok = ~np.isnan(ratio)
smin_c, smax_c = 0.36, 0.88**2
k_ref = amu_kloe(smin_c, smax_c)
c_est = amu_kloe(smin_c, smax_c, ratio=np.where(ok, ratio, 1.0))
p("CMD-3 mapped onto KLOE bins, 0.60<sqrt s<0.88 GeV (1e-10):")
p(f"  KLOE {k_ref:.1f}  CMD-3 (this script) {c_est:.1f}  CMD-3 published 379.3(3.0)")
p(f"  difference CMD-3 - KLOE: {c_est-k_ref:.1f}  (published-number difference 379.3-360.6 = 18.7)")
p("")
# energy breakdown
edges = [0.316, 0.5, 0.6, 0.7, 0.76, 0.8, 0.88, 0.975]
rows = []
p("Breakdown by sqrt(s) [GeV] of a_mu^pipi (KLOE) and CMD-3 - KLOE (1e-10):")
p("  range          KLOE    share   CMD3-KLOE   rel.diff")
tot_k = amu_kloe(edges[0]**2, edges[-1]**2)
for a, b in zip(edges[:-1], edges[1:]):
    k = amu_kloe(a * a, b * b)
    c = amu_kloe(a * a, b * b, ratio=np.where(ok, ratio, 1.0))
    rows.append((a, b, k, c - k))
    p(f"  {a:.3f}-{b:.3f}  {k:7.2f}  {100*k/tot_k:5.1f}%   {c-k:+7.2f}    {100*(c-k)/k:+.2f}%")
p(f"  total {edges[0]}-{edges[-1]}: KLOE {tot_k:.1f}, CMD3-KLOE {sum(r[3] for r in rows):+.1f}")
np.savetxt(os.path.join(HERE, "out", "pipi_energy_breakdown.csv"), np.array(rows), delimiter=",",
           header="sqrt_s_lo,sqrt_s_hi,amu_KLOE_1e-10,amu_CMD3_minus_KLOE_1e-10", comments="")
np.savetxt(os.path.join(HERE, "out", "cmd3_over_kloe_F2_ratio.csv"),
           np.column_stack([np.sqrt(s_c[ok]), ratio[ok]]), delimiter=",",
           header="sqrt_s_bin_centre_GeV,F2_CMD3/F2_KLOE", comments="")
p("")
p("Published per-experiment numbers, 0.6<sqrt s<0.88 GeV, 1e-10 [2302.08834 Table 4]:")
for n, v in [("before CMD2", "368.8(10.3)"), ("CMD-2", "366.5(3.4)"), ("SND", "364.7(4.9)"),
             ("KLOE", "360.6(2.1)"), ("BaBar", "370.1(2.7)"), ("BESIII", "361.8(3.6)"),
             ("CLEO", "370.0(6.2)"), ("SND2k", "366.7(3.2)"), ("CMD-3", "379.3(3.0)")]:
    p(f"  {n:12s} {v}")
p("")
p("Published pi pi integrals below 1.8 GeV (DHMZ method), 1e-10 [2505.21476 Table 5], and the")
p("full a_mu^HVP,LO they imply with WP20's non-pipi offset 187.3(2.2):")
for n, v, e in [("SND06", 505.3, 6.7), ("CMD-2", 508.1, 3.9), ("BaBar", 514.1, 3.8), ("KLOE", 504.5, 5.2),
                ("BESIII", 505.9, 3.7), ("SND20", 509.6, 3.6), ("CMD-3", 525.9, 4.2), ("tau (Belle+CLEO+ALEPH+OPAL)", 517.2, 5.8)]:
    p(f"  {n:28s} {v:6.1f}({e})  -> HVP LO {v+187.3:6.1f}   vs lattice 713.2(6.1): {v+187.3-713.2:+6.1f}")
open(os.path.join(HERE, "out", "pipi_by_experiment.txt"), "w").write("\n".join(L) + "\n")
print("\n".join(L))
