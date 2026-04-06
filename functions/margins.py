def parse_margins(text):
    lines = [line.strip() for line in text.split("\n") if line.strip()]

    if not lines:
        return []

    data = []

    # Skip header if present
    if "Date" in lines[0]:
        lines = lines[1:]

    for line in lines:
        parts = line.split()

        if len(parts) < 4:
            continue

        date = parts[0]
        margin_str = parts[3]

        margin = float(margin_str.replace("%", ""))

        data.append({
            "date": date,
            "margin": margin
        })

    return data

def score_margins(data):
    # Sort by date (oldest → newest)
    data = sorted(data, key=lambda x: x["date"])

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

    # 🔥 Volatility penalty first
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

    if not data:
        print("No margin data.")
        return "Neutral"

    
    score = score_margins(data)

    print("\nParsed Margin Data:")
    print(data[:3], "...")

    print("\nMargin Score:", score)

    return score