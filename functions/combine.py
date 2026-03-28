def combine_scores(revenue_score, earnings_score, margin_score, cashflow_score, pe_score):
    score_map = {
        "Good": 2,
        "Neutral": 1,
        "Yikes": 0
    }

    total = (
        1.0 * score_map[revenue_score] +
        1.5 * score_map[earnings_score] +
        2.0 * score_map[margin_score] +
        2.5 * score_map[cashflow_score] +
        0.5 * score_map[pe_score]
    )

    print("\n--- SCORE BREAKDOWN ---")
    print("Revenue:", revenue_score)
    print("Earnings:", earnings_score)
    print("Margins:", margin_score)
    print("Cash Flow:", cashflow_score)
    print("P/E:", pe_score)
    if pe_score == "Yikes":
        print("⚠️ Warning: High valuation (P/E) - Too Expensive to go forward")
    print("Weighted Score (goal:>11):", round(total, 2))

    # Final classification
    if total >= 11:
        return "Strong"
    elif total >= 7:
        return "Watch"
    else:
        return "Avoid"