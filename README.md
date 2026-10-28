# Mothers' Abuse Reports Under Uncertainty

Materials for the article **"Mothers' Abuse Reports Under Uncertainty: Why Custody Courts' Default Response Fails the Child"** by Vera Wilde (Technical University of Munich, TUM Campus Heilbronn).

The article treats a family court's response to a mother's abuse report as a decision under uncertainty. It shows that keeping the child with the primary caregiver under supervised contact dominates transfer to the accused parent for any probability of abuse, and that transfer can be preferred only on independent evidence that the mother herself endangers the child.

## Contents

| File | What it is |
|---|---|
| `10-23-26_Mothers_Abuse_Reports_Preprint.pdf` | Preprint of the manuscript (not yet peer reviewed) |
| `index.html` | Interactive decision calculator ([open it here](https://verawilde.github.io/custody-decisions-under-uncertainty/)) |
| `sensitivity_analysis.py` | Code for the sensitivity analysis (Tables 2 and 3) |
| `CITATION.cff` | Citation metadata |
| `LICENSE` | MIT license for the code; the preprint text is CC BY 4.0 |

## Decision calculator

[Supervise or Transfer?](https://verawilde.github.io/custody-decisions-under-uncertainty/) lets you set the probability of abuse, its severity, how much each option exposes the child, and the burden of supervision, and shows the expected harm of supervised contact, unsupervised contact and transfer across every probability of abuse. It uses the same model as the sensitivity analysis.

## Reproducing Tables 2 and 3

Requires Python 3 and no other packages.

```
python3 sensitivity_analysis.py
```

All harms are expressed in units of the harm of separating a child from the primary caregiver. The parameter values are illustrative ranges chosen to span mild to severe assumptions; they are not estimates.

## Status

Submitted for peer review. Preprint on PsyArXiv: link to follow.

## Citation

Wilde, V. (2026). *Mothers' abuse reports under uncertainty: Why custody courts' default response fails the child* [Preprint]. PsyArXiv.
