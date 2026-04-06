import re
from functions.revenue import *
from functions.earnings import *
from functions.margins import *
from functions.combine import *
from functions.cashflow import *
from functions.valuation import *
from functions.logger import *
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
    ticker = input("Enter ticker (e.g. DOCU): ").strip().upper()
    current_price = input("Enter current price: ")
    industry = input("Enter industry: ")
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

    cashflow_text = get_multiline_input(
    "\nPaste your cash flow data (press Enter twice when done):"
    )

    cashflow_score = cashflow_interpreter(cashflow_text)

    pe_text = get_multiline_input(
    "\nPaste P/E ratio (press Enter twice when done):"
)

    pe_score = pe_interpreter(pe_text, earn_score)

    final, total = combine_scores(rev_score, earn_score, margin_score, cashflow_score, pe_score)

    print("\nFINAL DECISION:", final)

    scores = {
    "revenue": rev_score,
    "earnings": earn_score,
    "margins": margin_score,
    "cashflow": cashflow_score,
    "pe": pe_score
}
    confirm_write = input("Do you want to save this into the csv? (y/n): ").strip().lower()

    if confirm_write == "y":
        log_result(ticker, current_price, industry, scores, final, total)
        print(f"Saved: {ticker} | {current_price} | {industry} | {final}")
        print("Saved successfully.")
    else:
        print("Not saved.")

if __name__ == "__main__":
    main()