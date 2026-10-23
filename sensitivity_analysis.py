"""Sensitivity analysis for 'Mothers' Abuse Reports Under Uncertainty'.

All harms are expressed in units of the harm of separating a child from the
primary caregiver (sigma = 1). Parameter values are illustrative ranges, not
estimates. Run: python3 sensitivity_analysis.py
"""
import itertools

SIGMA = 1.0  # harm of separation from the primary caregiver (unit)

# Ranges for the illustrative grid
B = [0.02, 0.1, 0.2]           # burden of supervision on the contact relationship
H = [3, 10, 20]                # severity of abuse via the accused parent, in units of sigma
GAP_U = [0.1, 0.3, 0.5]        # e(U) - e(S): extra exposure under unsupervised vs supervised contact
GAP_T = [0.5, 0.8]             # e(T) - e(S): extra exposure under transfer vs supervised contact
P_F = [0.05, 0.2, 0.5]         # probability of abuse pathways running through the accused parent
H_M = [3, 10, 20]              # severity of the mother-risk pathway, in units of sigma
GAP_M = [0.5, 0.9]             # e_m(S) - e_m(T): reduction in mother-risk exposure from transfer


def threshold_U_over_S(b, h, gap):
    """Smallest father-side probability at which S beats U (S preferred if p > threshold)."""
    return b / (h * gap)


def threshold_mother_risk(b, h, gap_t, p_f, h_m, gap_m):
    """Probability of mother-risk pathway that T requires to beat S."""
    return ((SIGMA - b) + p_f * h * gap_t) / (h_m * gap_m)


def main():
    print("Result 1: with no mother-risk pathway, E[H|T] - E[H|S] = (sigma - b) + p*h*(e(T)-e(S)) > 0")
    worst = min((SIGMA - b) + p * h * g for b in B for p in P_F for h in H for g in GAP_T)
    print(f"  minimum difference over grid = {worst:.2f} (positive: T is worse everywhere)\n")

    print("Result 2: threshold probability above which S beats U")
    print("  b     h    gap   threshold")
    for b, h, g in itertools.product(B, H, GAP_U):
        print(f"  {b:<5} {h:<4} {g:<5} {threshold_U_over_S(b, h, g):.3f}")
    vals = [threshold_U_over_S(b, h, g) for b, h, g in itertools.product(B, H, GAP_U)]
    print(f"  range {min(vals):.3f} to {max(vals):.3f}; central (b=0.1,h=10,gap=0.3) "
          f"{threshold_U_over_S(0.1, 10, 0.3):.3f}\n")

    print("Result 3: probability of mother-risk pathway required for T to beat S (b=0.1, gap_t=0.8)")
    print("  p_f   h    h_m  gap_m  required")
    req = {}
    for p_f, h, h_m, g_m in itertools.product(P_F, H, H_M, GAP_M):
        r = threshold_mother_risk(0.1, h, 0.8, p_f, h_m, g_m)
        req[(p_f, h, h_m, g_m)] = r
        flag = "  (>1: never)" if r > 1 else ""
        print(f"  {p_f:<5} {h:<4} {h_m:<4} {g_m:<5}  {r:.3f}{flag}")
    return req


if __name__ == "__main__":
    main()
