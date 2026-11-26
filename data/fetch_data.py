"""Download public pi+pi- inputs that are not redistributed in this repo.

KLOE combination (Table 1 of arXiv:1711.03085, JHEP 03 (2018) 173): the arXiv version carries the
arXiv non-exclusive licence, so the table is NOT committed. This script downloads the PDF, extracts
Table 1 with `pdftotext -raw` (poppler/xpdf, must be on PATH) and writes data/kloe_combination_table1.csv.

CMD-3 |F_pi|^2 (arXiv:2302.08834v3 ancillary file fpi_CMD3.dat) is CC-BY 4.0 and is committed as
data/cmd3_fpi_2302.08834v3.dat; this script can re-download it for checking.

Run: python data/fetch_data.py
"""
import os, re, subprocess, urllib.request, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
UA = {"User-Agent": "muon-g2-forensics data fetch"}


def get(url, path):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=120) as r, open(path, "wb") as f:
        f.write(r.read())


def kloe():
    tmp = tempfile.mkdtemp()
    pdf = os.path.join(tmp, "1711.03085v2.pdf")
    get("https://arxiv.org/pdf/1711.03085v2", pdf)
    txt = os.path.join(tmp, "k.txt")
    subprocess.run(["pdftotext", "-raw", pdf, txt], check=True)
    text = open(txt, encoding="utf-8", errors="replace").read()
    start = text.index("KLOE combination\ns (GeV2)")
    end = text.index("Table 1: The combined KLOE")
    num = r"([0-9.]+)\s*\S\s*([0-9.]+)"
    row = re.compile(r"^([0-9.]+) " + num + " " + num + r"(?: ([0-9.]+) " + num + " " + num + ")?", re.M)
    rows = []
    for m in row.finditer(text[start:end]):
        g = m.groups()
        rows.append(tuple(float(x) for x in g[:5]))
        if g[5]:
            rows.append(tuple(float(x) for x in g[5:]))
    rows.sort()
    out = os.path.join(HERE, "kloe_combination_table1.csv")
    with open(out, "w") as f:
        f.write("# KLOE combination, arXiv:1711.03085 Table 1. s bin centre (GeV^2), bin width 0.01 GeV^2\n")
        f.write("# sigma0_pipi(gamma) bare incl. FSR [nb] and |F_pi|^2, errors total (stat+syst, chi2-inflated)\n")
        f.write("s_GeV2,sigma0_nb,dsigma_nb,F2,dF2\n")
        for r in rows:
            f.write(",".join(f"{x:g}" for x in r) + "\n")
    print(f"KLOE: {len(rows)} bins -> {out}")
    assert len(rows) == 85, "expected 85 bins 0.105..0.945"


def cmd3_check():
    tmp = tempfile.mkdtemp()
    p = os.path.join(tmp, "fpi_CMD3.dat")
    get("https://arxiv.org/src/2302.08834v3/anc/fpi_CMD3.dat", p)
    same = open(p, "rb").read() == open(os.path.join(HERE, "cmd3_fpi_2302.08834v3.dat"), "rb").read()
    print("CMD-3 committed file identical to arXiv ancillary file:", same)


if __name__ == "__main__":
    kloe()
    cmd3_check()
