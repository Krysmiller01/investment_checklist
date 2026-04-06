import re

def parse_pe(text):
    match = re.search(r"(\d+\.?\d*)", text)

    if not match:
        return None

    return float(match.group(1))


def score_pe(pe, earnings_score):
    print("\nP/E Ratio:", pe)

    # Context-aware scoring using earnings quality
    if earnings_score == "Good":
        if pe <= 30:
            return "Good"
        elif pe <= 50:
            return "Neutral"
        else:
            return "Yikes"

    elif earnings_score == "Neutral":
        if pe <= 20:
            return "Good"
        elif pe <= 35:
            return "Neutral"
        else:
            return "Yikes"

    else:  # earnings_score == "Yikes"
        if pe <= 15:
            return "Neutral"
        else:
            return "Yikes"


def pe_interpreter(text, earnings_score):
    pe = parse_pe(text)

    if pe is None:
        print("Could not parse P/E.")
        return "Neutral"

    score = score_pe(pe, earnings_score)

    print("P/E Score:", score)

    return score