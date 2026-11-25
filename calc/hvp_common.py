"""Shared constants and kernels for the dispersive HVP integral.

a_mu^HVP,LO = alpha^2/(3 pi^2) * Int ds K(s) R(s) / s       (s in GeV^2)
K(s) = Int_0^1 dx x^2 (1-x) / (x^2 + (1-x) s / m_mu^2)      (Brodsky-de Rafael form)

Time-momentum representation (Bernecker & Meyer, arXiv:1107.4388):
G(t) = 1/(12 pi^2) Int_0^inf dw w^2 R(w^2) exp(-w t)
a_mu = 4 alpha^2 Int_0^inf dt Ktil(t) G(t)
Window functions from RBC/UKQCD, arXiv:1801.07224 (t0=0.4 fm, t1=1.0 fm, Delta=0.15 fm).
"""
import numpy as np
from scipy import integrate

ALPHA = 1 / 137.035999084     # CODATA 2018
M_MU = 0.1056583755           # GeV, PDG
M_PI = 0.13957039             # GeV, charged pion, PDG
HBARC = 0.1973269804          # GeV fm


def K(s):
    """QED kernel K(s), s in GeV^2. Closed form checked against quadrature in kernel.py."""
    s = np.asarray(s, dtype=float)
    out = np.empty_like(s)
    for i, si in np.ndenumerate(s):
        r = si / M_MU**2
        out[i] = integrate.quad(lambda x: x * x * (1 - x) / (x * x + (1 - x) * r), 0, 1,
                                epsabs=0, epsrel=1e-11)[0]
    return out


def K_closed(s):
    """Closed form of K(s) (e.g. Jegerlehner & Nyffeler, Phys. Rept. 477 (2009) 1, eq. 4.?)
    with x = (1-beta)/(1+beta), beta = sqrt(1-4 m^2/s), valid for s > 4 m_mu^2."""
    s = np.asarray(s, dtype=float)
    beta = np.sqrt(1 - 4 * M_MU**2 / s)
    x = (1 - beta) / (1 + beta)
    return (x**2 / 2 * (2 - x**2)
            + (1 + x**2) * (1 + x)**2 / x**2 * (np.log(1 + x) - x + x**2 / 2)
            + (1 + x) / (1 - x) * x**2 * np.log(x))


def amu_from_R(sqrt_s, R, scale=1e10):
    """Trapezoid dispersion integral over a tabulated R(sqrt s). Returns a_mu * scale."""
    sqrt_s = np.asarray(sqrt_s, float)
    s = sqrt_s**2
    integrand = K(s) * np.asarray(R, float) / s
    return scale * ALPHA**2 / (3 * np.pi**2) * np.trapezoid(integrand, s)


def R_from_sigma_nb(sqrt_s, sigma_nb):
    """R(s) = sigma(e+e- -> X) / sigma_pt, sigma_pt = 4 pi alpha^2/(3 s) = 86.8 nb / s[GeV^2]."""
    s = np.asarray(sqrt_s, float)**2
    sigma_pt_nb = 4 * np.pi * ALPHA**2 / (3 * s) * 0.3893793721e6   # GeV^-2 -> nb
    return np.asarray(sigma_nb, float) / sigma_pt_nb


def R_pipi_from_F2(sqrt_s, F2):
    """R_pipi = beta_pi^3 |F_pi|^2 / 4 (no FSR)."""
    s = np.asarray(sqrt_s, float)**2
    beta = np.sqrt(np.clip(1 - 4 * M_PI**2 / s, 0, None))
    return beta**3 * np.asarray(F2, float) / 4


# ---------- time-momentum representation ----------

def _f_Q2(Q2):
    Z = -(Q2 - np.sqrt(Q2 * Q2 + 4 * M_MU**2 * Q2)) / (2 * M_MU**2 * Q2)
    return M_MU**2 * Q2 * Z**3 * (1 - Q2 * Z) / (1 + M_MU**2 * Q2 * Z * Z)


def Ktilde(t):
    """Time kernel Ktil(t) (t in GeV^-1), Bernecker-Meyer eq. with omega integral done numerically."""
    def integrand(lw):
        w = np.exp(lw)
        return 2 * _f_Q2(w * w) * (w * w * t * t - 4 * np.sin(w * t / 2)**2)
    return integrate.quad(integrand, np.log(1e-6), np.log(1e3), limit=800, epsrel=1e-10)[0]


def theta(t_fm, t0, delta):
    return 0.5 * (1 + np.tanh((t_fm - t0) / delta))


def window_weights(t_fm, t0=0.4, t1=1.0, delta=0.15):
    """Return (SD, W, LD) weights at Euclidean time t (fm)."""
    sd = 1 - theta(t_fm, t0, delta)
    w = theta(t_fm, t0, delta) - theta(t_fm, t1, delta)
    ld = theta(t_fm, t1, delta)
    return sd, w, ld
