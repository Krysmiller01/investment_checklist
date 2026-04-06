import re

def parse_earnings(text):
    data = {}

    lines = [line.strip() for line in text.split("\n") if line.strip()]

    for line in lines:
        parts = line.split()

        if len(parts) < 2:
            continue

        year = parts[0]
        eps_str = parts[1]

        eps = float(eps_str.replace("$", "").replace(",", ""))

        data[year] = {"eps": eps}

    return data

def add_earnings_growth(data):
    years = sorted(data.keys(), key=int)

    for i in range(1, len(years)):
        prev = data[years[i-1]]["eps"]
        curr = data[years[i]]["eps"]

        # 🔴 Handle negative / zero EPS (important)
        if prev <= 0:
            growth = 0
        else:
            growth = ((curr - prev) / prev) * 100

        data[years[i]]["growth"] = round(growth, 2)

    data[years[0]]["growth"] = 0

    return data

def score_earnings_quality(data):
    years = sorted(data.keys(), key=int)[-4:]
    
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
    if improving_eps >= 2 and avg_growth > 3:
        return "Good"
    elif improving_eps == 0 and avg_growth < 0:
        return "Yikes"
    else:
        return "Neutral"

def earnings_interpreter(text):

    data = parse_earnings(text)
    data = add_earnings_growth(data)
    score = score_earnings_quality(data)

    print("\nParsed Earnings Data:")
    print(data)

    print("\nEarnings Score:", score)

    return score