def parse_margins(text):
    lines = [line.strip() for line in text.split("\n") if line.strip()]

    data = []

    # Skip header (first 4 lines)
    i = 4

    while i < len(lines):
        date = lines[i]
        revenue = lines[i+1]
        net_income = lines[i+2]
        margin = lines[i+3]

        # Clean margin → float
        margin_value = float(margin.replace("%", ""))

        data.append({
            "date": date,
            "margin": margin_value
        })

        i += 4

    return data

def score_margins(data):
    margins = [entry["margin"] for entry in data]

    volatility = max(margins) - min(margins)

    improving = 0
    declining = 0

    for i in range(1, len(margins)):
        if margins[i] > margins[i-1]:
            improving += 1
        elif margins[i] < margins[i-1]:
            declining += 1

    avg_margin = sum(margins) / len(margins)

    print("\nMargins:", margins)
    print("Average margin:", round(avg_margin, 2))
    print("Margin volatility:", round(volatility, 2))

    # Scoring logic
    if volatility > 30:
        return "Yikes"
    if avg_margin > 20 and improving > declining:
        return "Good"
    elif avg_margin < 5 and declining > improving:
        return "Yikes"
    else:
        return "Neutral"

def margins_interpreter(text):
    data = parse_margins(text)
    score = score_margins(data)

    print("\nParsed Margin Data:")
    print(data[:3], "...")

    print("\nMargin Score:", score)

    return score