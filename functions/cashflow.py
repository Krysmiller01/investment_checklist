import re

def parse_cashflow(text):
    ocf_match = re.search(r"OCF\s*=\s*([-\d,]+)", text)
    capex_match = re.search(r"CapEx\s*=\s*([-\d,]+)", text)

    if not ocf_match or not capex_match:
        return None

    ocf = int(ocf_match.group(1).replace(",", ""))
    capex = int(capex_match.group(1).replace(",", ""))

    return ocf, capex

def calculate_fcf(ocf, capex):
    return ocf - capex

def cashflow_interpreter(text):
    parsed = parse_cashflow(text)

    if not parsed:
        print("Could not parse cash flow data.")
        return "Neutral"

    ocf, capex = parsed
    fcf = calculate_fcf(ocf, capex)

    print("\nOCF:", ocf)
    print("CapEx:", capex)
    print("FCF:", fcf)

    # Simple scoring
    if fcf > 0:
        return "Good"
    elif fcf < 0:
        return "Yikes"
    else:
        return "Neutral"