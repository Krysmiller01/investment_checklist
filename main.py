import re
from functions.revenue import *
from functions.earnings import *
from functions.margins import *
from functions.combine import *
def get_multiline_input(prompt):
    print(prompt)
    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)
    return "\n".join(lines)


def main():
    revenue_text = get_multiline_input(
        "Paste your revenue data (press Enter twice when done):"
    )
    rev_score = revenue_interpreter(revenue_text)

    earnings_text = get_multiline_input(
        "\nPaste your earnings data (press Enter twice when done):"
    )
    earn_score = earnings_interpreter(earnings_text)

    margins_text = get_multiline_input(
        "\nPaste your margin data (press Enter twice when done):"
    )
    margin_score = margins_interpreter(margins_text)

    final = combine_scores(rev_score, earn_score, margin_score)

    print("\nFINAL DECISION:", final)

if __name__ == "__main__":
    main()