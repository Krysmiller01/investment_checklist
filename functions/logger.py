import csv
from datetime import datetime
import os

def log_result(company, price, industry, scores, final_score, weighted_score):
    file_exists = os.path.isfile("results.csv")

    with open("results.csv", mode="a", newline="") as file:
        writer = csv.writer(file)

        # Write header if file doesn't exist
        if not file_exists:
            writer.writerow([
                "Date",
                "Ticker",
                "Price",
                "Industry",
                "Revenue",
                "Earnings",
                "Margins",
                "CashFlow",
                "PE",
                "FinalScore",
                "WeightedScore"
            ])

        writer.writerow([
            datetime.now().strftime("%Y-%m-%d"),
            company,
            price,
            industry,
            scores["revenue"],
            scores["earnings"],
            scores["margins"],
            scores["cashflow"],
            scores["pe"],
            final_score,
            round(weighted_score, 2)
        ])