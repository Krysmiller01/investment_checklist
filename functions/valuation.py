import re

def parse_pe(text):
    match = re.search(r"(\d+\.?\d*)", text)

    if not match:
        return None

    return float(match.group(1))

def score_pe(pe):
    print("\nP/E Ratio:", pe)

    if 10 <= pe <= 25:
        return "Good"
    elif 25 < pe <= 50:
        return "Neutral"
    else:
        return "Yikes"

def pe_interpreter(text):
    pe = parse_pe(text)

    if pe is None:
        print("Could not parse P/E.")
        return "Neutral"

    score = score_pe(pe)

    print("P/E Score:", score)

    return score