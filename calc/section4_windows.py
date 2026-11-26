"""Section 4: window decomposition, lattice vs data-driven, and where in energy the gap sits.

Part A (published numbers, 1e-10):
  data-driven windows: Colangelo et al., arXiv:2205.12963 Table 1: SD 68.4(5), W 229.4(1.4), LD 395.1(2.4), total 693.0(3.9)
  lattice: WP25 (arXiv:2505.21476) SD avg 69.10(26) Eq. 3.22, W avg 236.58(43) Eq. 3.26, total 713.2(6.1) Eq. 3.31
  LD(lattice) is derived here as total - SD - W (inference, uncertainties treated as uncorrelated -> overestimate).
  Davier et al. arXiv:2312.02053 Fig. 12, W with each pi pi input: KLOE 227.3, BaBar 230.8, CMD-3 234.2, tau 232.4.
Part B (this repo's data): weight the CMD-3 - KLOE bin-by-bin difference (from pipi_by_experiment.py
  method) with the SD/W/LD fraction of each energy, computed from the time-momentum kernel in kernel.py.
Requires: python kernel.py (writes out/ktilde_table.csv) and data/kloe_combination_table1.csv.
Outputs: out/section4_windows.txt, out/section4_window_energy_map.csv
"""
import os
import numpy as np
from hvp_common import K, window_weights, HBARC

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
L = []
p = L.append

# ---------- Part A ----------
dd = {"SD": (68.4, 0.5), "W": (229.4, 1.4), "LD": (395.1, 2.4), "total": (693.0, 3.9)}
lat_tot = (713.2, 6.1)
lat = {"SD": (69.10, 0.26), "W": (236.58, 0.43)}
lat["LD"] = (lat_tot[0] - lat["SD"][0] - lat["W"][0], np.sqrt(lat_tot[1]**2 + 0.26**2 + 0.43**2))
lat["total"] = lat_tot
p("A. Lattice (WP25 averages) minus data-driven (Colangelo et al. 2022, WP20-era data), 1e-10")
p("   window  lattice        data-driven    diff      sigma   share of total diff   rel. diff")
dtot = lat_tot[0] - dd["total"][0]
for k in ["SD", "W", "LD", "total"]:
    d = lat[k][0] - dd[k][0]
    e = np.hypot(lat[k][1], dd[k][1])
    p(f"   {k:6s} {lat[k][0]:7.2f}({lat[k][1]:.2f})  {dd[k][0]:6.1f}({dd[k][1]})   {d:+6.2f}   {d/e:5.1f}   {100*d/dtot:6.1f}%            {100*d/dd[k][0]:+.1f}%")
p("   (LD lattice = total - SD - W; its uncertainty here ignores correlations, so it is conservative.)")
p("")
p("   Davier et al. 2023, intermediate window with each pi pi dataset (1e-10): KLOE 227.3, BaBar 230.8,")
p("   tau 232.4, CMD-3 234.2; lattice average quoted there 236.1(0.9).")
p(f"   CMD-3 - KLOE in W = {234.2-227.3:.1f};  lattice(WP25) - CMD-3-based W = {236.58-234.2:.1f}")
p("")

# ---------- Part B ----------
kt = np.loadtxt(os.path.join(HERE, "out", "ktilde_table.csv"), delimiter=",", skiprows=1)
t_fm, Kt = kt[:, 0], kt[:, 1]
t = t_fm / HBARC
sd_w, w_w, ld_w = window_weights(t_fm)


def fractions(E):
    e = np.exp(-E * t)
    tot = np.trapezoid(Kt * e, t)
    return [np.trapezoid(Kt * e * f, t) / tot for f in (sd_w, w_w, ld_w)]


kl = np.genfromtxt(os.path.join(ROOT, "data", "kloe_combination_table1.csv"), delimiter=",",
                   skip_header=2, names=True)
s_c, sig, F2k = kl["s_GeV2"], kl["sigma0_nb"], kl["F2"]
cm = np.loadtxt(os.path.join(ROOT, "data", "cmd3_fpi_2302.08834v3.dat"), comments="#")
o = np.argsort(cm[:, 0]); E_c, F2_c = cm[o, 0], cm[o, 1]
NB = 0.3893793721e6
rows = []
for sc, sg, f2 in zip(s_c, sig, F2k):
    lo, hi = sc - 0.005, sc + 0.005
    if np.sqrt(lo) < E_c[0] or np.sqrt(hi) > E_c[-1]:
        continue
    ss = np.linspace(lo, hi, 41)
    r = np.mean(np.interp(np.sqrt(ss), E_c, F2_c)) / f2
    a_k = np.trapezoid(K(ss), ss) * sg / NB / (4 * np.pi**3) * 1e10
    fr = fractions(np.sqrt(sc))
    rows.append([np.sqrt(sc), a_k, a_k * (r - 1), *fr])
rows = np.array(rows)
np.savetxt(os.path.join(HERE, "out", "section4_window_energy_map.csv"), rows, delimiter=",",
           header="sqrt_s_GeV,amu_KLOE_bin,amu_CMD3_minus_KLOE_bin,frac_SD,frac_W,frac_LD", comments="")
dk = rows[:, 2]
p("B. CMD-3 - KLOE pi pi difference (data in this repo, 0.32-0.975 GeV), split by window, 1e-10")
tot_d = dk.sum()
for i, k in enumerate(["SD", "W", "LD"]):
    v = (dk * rows[:, 3 + i]).sum()
    p(f"   {k:3s} {v:+6.2f}  ({100*v/tot_d:4.1f}% of the difference)")
p(f"   sum {tot_d:+6.2f}")
akl = rows[:, 1]
p("   For comparison, KLOE's own pi pi integral splits as: " + ", ".join(
    f"{k} {100*(akl*rows[:,3+i]).sum()/akl.sum():.1f}%" for i, k in enumerate(["SD", "W", "LD"])))
p("")
p("C. Ratio test (inference): if the whole lattice-data gap came from a pi pi normalisation offset")
p("   with the energy profile of CMD-3 - KLOE, the W:LD split of the gap would follow part B.")
fW = (dk * rows[:, 4]).sum() / tot_d
fLD = (dk * rows[:, 5]).sum() / tot_d
p(f"   Predicted share of gap in W = {100*fW:.0f}%, in LD = {100*fLD:.0f}%;  observed (part A): "
  f"W {100*(lat['W'][0]-dd['W'][0])/dtot:.0f}%, LD {100*(lat['LD'][0]-dd['LD'][0])/dtot:.0f}%")
p(f"   Gap scaled from part A W difference: {(lat['W'][0]-dd['W'][0])/fW:.1f}  vs actual total gap {dtot:.1f}")
open(os.path.join(HERE, "out", "section4_windows.txt"), "w").write("\n".join(L) + "\n")
print("\n".join(L))
