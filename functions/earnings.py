import re

def parse_earnings(text):
    data = {}

    lines = text.split("\n")

    pattern = re.compile(
        r"(\d{4}) annual EPS was \$(-?\d+\.\d+), a (\d+\.?\d*)% (increase|decline)"
    )

    for line in lines:
        if "annual EPS" not in line:
            continue

        match = pattern.search(line)
        if match:
            year = match.group(1)
            eps = float(match.group(2))
            growth = float(match.group(3))
            direction = match.group(4)

            # Convert decline to negative growth
            if direction == "decline":
                growth = -growth
            if growth > 100:
                growth = 100
            elif growth < -100:
                growth = -100
                
            data[year] = {
                "eps": eps,
                "growth": growth
            }

    return data

def score_earnings_quality(data):
    years = sorted(data.keys())
    
    eps_values = [data[y]["eps"] for y in years]
    growths = [data[y]["growth"] for y in years]

    improving_eps = 0

    for i in range(1, len(eps_values)):
        if eps_values[i] > eps_values[i-1]:
            improving_eps += 1

    avg_growth = sum(growths) / len(growths)

    print("\nEPS values:", eps_values)
    print("Growth values:", growths)
    print("Average growth:", round(avg_growth, 2))

    # Scoring logic
    if improving_eps >= 2 and avg_growth > 0:
        return "Good"
    elif improving_eps == 0 and avg_growth < 0:
        return "Yikes"
    else:
        return "Neutral"

def earnings_interpreter(text):

    data = parse_earnings(text)
    score = score_earnings_quality(data)

    print("\nParsed Earnings Data:")
    print(data)

    print("\nEarnings Score:", score)

    return score