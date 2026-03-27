import re

def parse_revenue(text):
    data = {}

    lines = text.split("\n")

    pattern = re.compile(
        r"annual revenue for (\d{4}) was \$(\d+\.\d+)B, a (\d+\.?\d*)% increase"
    )

    for line in lines:
        if "annual revenue" not in line:
            continue

        match = pattern.search(line)
        if match:
            year = match.group(1)
            revenue = float(match.group(2))
            growth = float(match.group(3))

            data[year] = {
                "revenue": revenue,
                "growth": growth
            }

    return data


def score_growth_quality(data):
    years = sorted(data.keys())
    
    growths = [data[year]["growth"] for year in years]

    improving = 0
    declining = 0

    for i in range(1, len(growths)):
        if growths[i] > growths[i-1]:
            improving += 1
        elif growths[i] < growths[i-1]:
            declining += 1

    avg_growth = sum(growths) / len(growths)

    print("\nGrowth values:", growths)
    print("Average growth:", round(avg_growth, 2))

    # Scoring logic
    if improving >= 2 and avg_growth > 10:
        return "Good"
    elif declining >= 2 and avg_growth < 10:
        return "Yikes"
    else:
        return "Neutral"

def revenue_interpreter(text): 
    
    data = parse_revenue(text)
    score = score_growth_quality(data)

    print("\nParsed Data:")
    print(data)

    print("\nGrowth Score:", score)
    
    return score