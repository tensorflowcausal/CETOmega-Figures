
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "output"
OUT.mkdir(parents=True, exist_ok=True)

# 1) Visibility decay: V(Δt, lc) = exp(-Δt/lc)
dt = np.linspace(0.0, 5.0, 600)
lc_values = [0.25, 0.5, 1.0, 2.0]

plt.figure(figsize=(5, 3.2))
for lc in lc_values:
    V = np.exp(-dt/lc)
    plt.plot(dt, V, label=fr"$\ell_c={lc}$")
plt.axhline(1e-3, linestyle="--", linewidth=1, label=r"threshold $10^{-3}$")
plt.xlabel(r"$\Delta t$ (arb. units)")
plt.ylabel(r"$V(\Delta t,\ell_c)$")
plt.yscale("log")
plt.ylim(1e-4, 1.1)
plt.xlim(0, dt.max())
plt.legend(frameon=False, ncol=2, fontsize=8)
plt.tight_layout()
plt.savefig(OUT / "visibility_decay.png", dpi=300)
plt.savefig(OUT / "visibility_decay.pdf")
plt.close()

# 2) Phase shift: Δφ(ω) = ω / M*
M_star_eV = 1e-1  # example
w = np.linspace(0.0, 5.0, 600)
phi = w / M_star_eV

plt.figure(figsize=(5, 3.2))
plt.plot(w, phi, label=rf"$M_*={M_star_eV}\,\mathrm{{eV}}$")
plt.fill_between(w, 1e-3, 1e-2, alpha=0.15, label=r"target $10^{-3}$–$10^{-2}$ rad")
plt.xlabel(r"$\omega$ (arb. units)")
plt.ylabel(r"$\Delta \phi(\omega)$ (rad)")
plt.xlim(0, w.max())
plt.ylim(0, max(phi.max(), 1e-2)*1.05)
plt.legend(frameon=False, fontsize=8)
plt.tight_layout()
plt.savefig(OUT / "phase_shift.png", dpi=300)
plt.savefig(OUT / "phase_shift.pdf")
plt.close()

print("Saved figures to:", OUT)
