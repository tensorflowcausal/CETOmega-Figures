
# CET Ω — Supplementary Figures

This repository generates two publication-quality figures used in the CET Ω supplementary material:

1) **Visibility decay**:  V(Δt, ℓ_c) = exp(-Δt / ℓ_c) for several ℓ_c.
2) **Causal phase shift**:  Δφ(ω) = ω / M_*.

## Quick start

```bash
python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python src/generate_figures.py   # outputs to ./output/
```

## LaTeX include example (RevTeX)

```latex
\begin{figure}[t]
  \centering
  \includegraphics[width=0.45\textwidth]{output/visibility_decay.pdf}
  \caption{Visibility law V(\Delta t,\ell_c) for several \ell_c.}
  \label{fig:visibility-law}
\end{figure}

\begin{figure}[t]
  \centering
  \includegraphics[width=0.45\textwidth]{output/phase_shift.pdf}
  \caption{Causal phase shift \(\Delta\phi(\omega)=\omega/M_*\) with target band.}
  \label{fig:phase-shift}
\end{figure}
```
