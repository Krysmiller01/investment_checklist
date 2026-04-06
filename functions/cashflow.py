import re

def parse_fcf(text):
    lines = [line.strip() for line in text.split("\n") if line.strip()]

    try:
        values = [float(line.replace(",", "")) for line in lines]
    except:
        return None

    return values

def score_fcf(values):
    if not values or len(values) < 4:
        print("Not enough FCF data.")
        return "Neutral"

    # Ignore TTM → use last 4 annual values
    fcf_values = values[1:5]  # [2025, 2024, 2023, 2022]

    # Reverse so oldest → newest
    fcf_values = list(reversed(fcf_values))  # [2022 → 2025]

    improving = 0

    for i in range(1, len(fcf_values)):
        if fcf_values[i] > fcf_values[i-1]:
            improving += 1

    avg_fcf = sum(fcf_values) / len(fcf_values)

    print("\nFCF values:", fcf_values)
    print("Average FCF:", round(avg_fcf, 2))

    if all(f > 0 for f in fcf_values) and improving >= 2:
        return "Good"
    elif any(f < 0 for f in fcf_values):
        return "Yikes"
    else:
        return "Neutral"
    
def cashflow_interpreter(text):
    values = parse_fcf(text)

    if not values:
        print("Could not parse FCF data.")
        return "Neutral"

    score = score_fcf(values)

    print("\nFCF Score:", score)

    return score