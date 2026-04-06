import re

def parse_revenue(text):
    data = {}

    lines = [line.strip() for line in text.split("\n") if line.strip()]

    for line in lines:
        parts = line.split()

        if len(parts) < 2:
            continue

        year = parts[0]
        revenue_str = parts[1]

        # Clean revenue: remove $, commas
        revenue = float(revenue_str.replace("$", "").replace(",", ""))

        data[year] = {"revenue": revenue}

    return data

def add_growth(data):
    years = sorted(data.keys(), key=int)

    for i in range(1, len(years)):
        prev = data[years[i-1]]["revenue"]
        curr = data[years[i]]["revenue"]
        

        growth = ((curr - prev) / prev) * 100
        data[years[i]]["growth"] = round(growth, 2)

    # First year has no growth
    data[years[0]]["growth"] = 0

    return data

def score_growth_quality(data):
    years = sorted(data.keys(), key=int)[-4:]
    
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
    data = add_growth(data)
    score = score_growth_quality(data)

    print("\nParsed Data:")
    print(data)

    print("\nGrowth Score:", score)
    
    return score