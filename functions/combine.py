def combine_scores(revenue_score, earnings_score, margin_score):
    score_map = {
        "Good": 2,
        "Neutral": 1,
        "Yikes": 0
    }

    total = (
        score_map[revenue_score] +
        score_map[earnings_score] +
        score_map[margin_score]
    )

    print("\n--- SCORE BREAKDOWN ---")
    print("Revenue:", revenue_score)
    print("Earnings:", earnings_score)
    print("Margins:", margin_score)
    print("Total Score:", total)

    # Final classification
    if total >= 5:
        return "Strong"
    elif total >= 3:
        return "Watch"
    else:
        return "Avoid"