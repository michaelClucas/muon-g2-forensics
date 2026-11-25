"""Section 2a: evaluate the QED kernel K(s) and the dispersive weight K(s)/s.

Outputs:
  out/kernel_table.csv      K(s), K(s)/s, normalised weight vs sqrt(s)
  out/kernel_checks.txt     closed form vs quadrature, time-kernel consistency check,
                            window fraction of each energy (used in section 4)
Run: python kernel.py
"""
import numpy as np
from scipy import integrate
from hvp_common import K, K_closed, Ktilde, window_weights, ALPHA, M_MU, HBARC
import os

OUT = os.path.join(os.path.dirname(__file__), "out")
os.makedirs(OUT, exist_ok=True)

roots = np.array([0.28, 0.3, 0.4, 0.5, 0.6, 0.7, 0.775, 0.8, 0.9, 1.0, 1.02, 1.5, 2.0, 3.0, 5.0, 10.0])
s = roots**2
Kq, Kc = K(s), K_closed(s)
lines = ["# K(s): quadrature vs closed form", "sqrt_s_GeV,K_quad,K_closed,rel_diff,K_over_s_GeV-2,(K/s)/(K/s at 0.775)"]
ref = K(np.array([0.775**2]))[0] / 0.775**2
for r, a, b in zip(roots, Kq, Kc):
    lines.append(f"{r:.3f},{a:.6e},{b:.6e},{(a-b)/a:.1e},{a/r**2:.6e},{a/r**2/ref:.4f}")

# K(s) -> m^2/(3s) at large s
lines.append("")
lines.append(f"large-s check: K(100 GeV^2)*3*100/m_mu^2 = {K(np.array([100.0]))[0]*300/M_MU**2:.4f} (-> 1)")

# Time-kernel consistency: Int dt Ktil(t) e^{-w t} must equal 2 K(w^2)/w^3
# build t grid in fm then convert to GeV^-1
t_fm = np.concatenate([np.linspace(0.0, 1.0, 401)[1:], np.linspace(1.0025, 14.0, 5200)])
t_gev = t_fm / HBARC
Kt = np.array([Ktilde(t) for t in t_gev])
np.savetxt(os.path.join(OUT, "ktilde_table.csv"), np.column_stack([t_fm, Kt]),
           delimiter=",", header="t_fm,Ktilde_t(GeV^-1 units)", comments="")

sd, w, ld = window_weights(t_fm)
lines.append("")
lines.append("# Time-momentum check and window fractions per energy")
lines.append("sqrt_s_GeV,LaplaceKtil,2K/w^3,rel_diff,frac_SD,frac_W,frac_LD")
win_rows = []
for r in [0.3, 0.4, 0.5, 0.6, 0.7, 0.775, 0.85, 0.95, 1.02, 1.2, 1.5, 2.0, 3.0]:
    e = np.exp(-r * t_gev)
    tot = np.trapezoid(Kt * e, t_gev)
    exact = 2 * K(np.array([r * r]))[0] / r**3
    fs = [np.trapezoid(Kt * e * wf, t_gev) / tot for wf in (sd, w, ld)]
    lines.append(f"{r:.3f},{tot:.6e},{exact:.6e},{(tot-exact)/exact:.1e},{fs[0]:.4f},{fs[1]:.4f},{fs[2]:.4f}")
    win_rows.append([r, *fs])
np.savetxt(os.path.join(OUT, "window_fractions_vs_energy.csv"), np.array(win_rows), delimiter=",",
           header="sqrt_s_GeV,frac_SD,frac_W,frac_LD", comments="")

# Dense table of the weight
dense = np.linspace(0.28, 2.0, 173)
Kd = K(dense**2)
np.savetxt(os.path.join(OUT, "kernel_table.csv"), np.column_stack([dense, Kd, Kd / dense**2]),
           delimiter=",", header="sqrt_s_GeV,K,K_over_s_GeV-2", comments="")

with open(os.path.join(OUT, "kernel_checks.txt"), "w") as f:
    f.write("\n".join(lines) + "\n")
print("\n".join(lines))
